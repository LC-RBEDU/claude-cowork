#!/usr/bin/env python3
"""F7.3: Refresh EDU news topic suggestions for OPS2 recurring task (file-per-task v2).

Reads:
- 02-PROJEKTY/<slug>/tasks/*.md (active in-progress signals)
- 07-ARCHIV/tasks-done/<slug>/*.md (recently archived, completed in last 7 days)

Patches body of `02-PROJEKTY/operations/tasks/OPS2.md` between
`<!-- edu-news-topics:start -->` and `<!-- edu-news-topics:end -->` markers.

Usage:
    python3 lifecycle_extra_edu_news.py             # refresh (default cron)
    python3 lifecycle_extra_edu_news.py --reset     # clear topics (after recording)
    python3 lifecycle_extra_edu_news.py --dry-run   # preview only
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import json
import urllib.error
import urllib.request
from datetime import datetime, timedelta, date
from pathlib import Path
from zoneinfo import ZoneInfo

_LIB = Path(__file__).resolve().parents[1] / "lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from drive_io import DriveVault, DriveNotFoundError, DriveConflictError, credentials_from_env  # noqa: E402
from task_io import iter_active_tasks, iter_archive_tasks, parse_iso_date  # noqa: E402

TZ = ZoneInfo(os.environ.get("TZ", "Europe/Prague"))

OPS2_PATH = "02-PROJEKTY/operations/tasks/OPS2.md"
TOPICS_STATE_PATH = "00-System/edu-news-topics.json"

MAX_TOPICS = int(os.environ.get("EDU_NEWS_MAX", "5"))
LOOKBACK_DAYS = int(os.environ.get("EDU_NEWS_LOOKBACK_DAYS", "7"))

EXCLUDE_SLUGS = frozenset(
    s.strip()
    for s in os.environ.get("EDU_NEWS_EXCLUDE_SLUGS", "osobni,owners").split(",")
    if s.strip()
)

EXCLUDE_NAME_RE = re.compile(
    r"\b(osobní|soukrom|daňové přiznání|přiznání fy|manžel|rodin)\b",
    re.I,
)

MARKER_RE = re.compile(
    r"<!-- edu-news-topics:start -->.*?<!-- edu-news-topics:end -->",
    re.DOTALL,
)


def collect_recently_done(vault: DriveVault, cutoff: date) -> list[dict]:
    """Return archived tasks completed (updated) >= cutoff."""
    out: list[dict] = []
    for task in iter_archive_tasks(vault):
        slug = task.slug
        if slug in EXCLUDE_SLUGS:
            continue
        title = task.frontmatter.get("id", "") + " — " + (task.body.split("\n", 2)[0] if task.body else "")
        title = re.sub(r"^#+\s*", "", title).strip()
        if EXCLUDE_NAME_RE.search(title):
            continue
        updated = parse_iso_date(task.frontmatter.get("updated"))
        if updated is None or updated < cutoff:
            continue
        out.append({
            "task_id": task.task_id,
            "slug": slug,
            "title": title[:200],
            "updated": updated.isoformat(),
            "kind": "done",
            "score": _score(task.frontmatter, kind="done", today=cutoff + timedelta(days=LOOKBACK_DAYS)),
        })
    return out


def collect_progress(vault: DriveVault) -> list[dict]:
    """Active tasks with checkbox progress >= 50% — in-progress signal."""
    out: list[dict] = []
    for task in iter_active_tasks(vault):
        if task.is_done:
            continue
        if task.status in ("Waiting", "Backlog"):
            continue
        slug = task.slug
        if slug in EXCLUDE_SLUGS:
            continue
        body = task.body or ""
        boxes = re.findall(r"^-\s+\[([ xX])\]", body, re.MULTILINE)
        if len(boxes) < 2:
            continue
        done_n = sum(1 for b in boxes if b.lower() == "x")
        ratio = done_n / len(boxes) if boxes else 0
        if ratio < 0.5:
            continue
        title = (re.search(r"^#+\s+(.+)$", body, re.MULTILINE) or [None, ""]).__getitem__(1).strip()
        if EXCLUDE_NAME_RE.search(title):
            continue
        out.append({
            "task_id": task.task_id,
            "slug": slug,
            "title": title[:200],
            "ratio": f"{done_n}/{len(boxes)}",
            "kind": "progress",
            "score": _score(task.frontmatter, kind="progress", today=datetime.now(TZ).date()),
        })
    return out


def _score(fm: dict, *, kind: str, today: date) -> float:
    i, c, e = (
        int(fm.get("ice_i") or 5),
        int(fm.get("ice_c") or 5),
        max(int(fm.get("ice_e") or 5), 1),
    )
    s = (i * c) / e
    if kind == "done":
        s += 8.0
    elif kind == "progress":
        s += 2.0
    slug = fm.get("slug") or ""
    if slug in ("rb-universe-development", "firemni-procesy", "strategy"):
        s += 1.5
    return round(s, 2)


def rank_and_dedup(candidates: list[dict]) -> list[dict]:
    by_key: dict[str, dict] = {}
    for c in candidates:
        key = f"{c['slug']}:{c['task_id']}"
        if key not in by_key:
            by_key[key] = c
    items = list(by_key.values())
    items.sort(key=lambda x: -x.get("score", 0))
    return items[:MAX_TOPICS]


def llm_rerank(candidates: list[dict]) -> list[dict] | None:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key or len(candidates) <= MAX_TOPICS:
        return None
    model = os.environ.get("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")
    brief = [
        {"key": f"{c['slug']}:{c['task_id']}", "title": c["title"], "kind": c["kind"]}
        for c in candidates[:20]
    ]
    prompt = (
        f"Vyber max {MAX_TOPICS} témat pro 30s firemní EDU news video. "
        f"Kritéria: zajímavé pro celou firmu, raději hotové/viditelný posun než plány, "
        f"ne osobní finance. Vrať POUZE JSON pole klíčů `key` seřazených.\n\n"
        f"Kandidáti:\n{json.dumps(brief, ensure_ascii=False, indent=2)}"
    )
    body_data = json.dumps({
        "model": model, "max_tokens": 400,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    try:
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=body_data,
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"edu_news: LLM skip: {e}", file=sys.stderr)
        return None
    content = ""
    for block in data.get("content", []):
        if block.get("type") == "text":
            content += block.get("text", "")
    m = re.search(r"\[[\s\S]*?\]", content)
    if not m:
        return None
    try:
        keys = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    by_key = {f"{c['slug']}:{c['task_id']}": c for c in candidates}
    ordered = [by_key[k] for k in keys if k in by_key]
    return ordered[:MAX_TOPICS]


def patch_ops2(vault: DriveVault, topics: list[dict]) -> bool:
    """Update OPS2.md marker block. CAS-aware. Returns True if changed."""
    try:
        text, meta = vault.read_text(OPS2_PATH)
    except DriveNotFoundError:
        print(f"edu_news: {OPS2_PATH} not found — skipping (F7.4 still pending?)")
        return False
    now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M")
    if topics:
        lines = [f"**Návrhy témat** _(auto {now})_:"]
        for t in topics:
            tid = t.get("task_id") or "—"
            slug = t.get("slug") or ""
            line = t.get("title") or ""
            lines.append(f"- [ ] **{tid}** ({slug}) — {line}")
    else:
        lines = [
            f"**Návrhy témat** _(vyčištěno {now})_:",
            "- _(sbírám témata pro příští EDU news)_",
        ]
    block = (
        "<!-- edu-news-topics:start -->\n"
        + "\n".join(lines)
        + "\n<!-- edu-news-topics:end -->"
    )
    if MARKER_RE.search(text):
        new_text = MARKER_RE.sub(block, text)
    else:
        # Append at end if no marker
        if text and not text.endswith("\n"):
            text += "\n"
        new_text = text + "\n" + block + "\n"
    if new_text == text:
        return False
    try:
        vault.write_text(OPS2_PATH, new_text, expect_mtime=meta.modified_time)
        return True
    except DriveConflictError as e:
        print(f"edu_news: OPS2 changed externally — skipping ({e})", file=sys.stderr)
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Clear topics (po nahrání EDU news)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root_id = (os.environ.get("VAULT_DRIVE_ID") or "").strip()
    if not root_id:
        raise RuntimeError("VAULT_DRIVE_ID env not set")
    creds, _ = credentials_from_env()
    vault = DriveVault(root_id, credentials=creds)

    if args.reset:
        print("edu_news: --reset (clearing topics)")
        if not args.dry_run:
            patch_ops2(vault, [])
        return

    today = datetime.now(TZ).date()
    cutoff = today - timedelta(days=LOOKBACK_DAYS)

    done = collect_recently_done(vault, cutoff)
    progress = collect_progress(vault)

    print(f"edu_news: {len(done)} done signals, {len(progress)} progress signals")

    candidates = done + progress
    ranked = rank_and_dedup(candidates)
    llm_ordered = llm_rerank(candidates)
    if llm_ordered is not None:
        ranked = llm_ordered

    for t in ranked:
        print(f"  [{t.get('score')}] {t['task_id']} ({t['slug']}) — {t['title'][:60]}")

    if args.dry_run:
        return

    if patch_ops2(vault, ranked):
        print(f"edu_news: patched drive://{OPS2_PATH}")


if __name__ == "__main__":
    main()
