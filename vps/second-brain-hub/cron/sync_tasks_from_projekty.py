#!/usr/bin/env python3
"""Merge task fields from 02-Projekty/*.md into dashboard-tasks-source.json (preserve ICE/ch)."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

import os

VAULT = Path(os.environ.get("VAULT_PATH", Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/MrLUC"))
TASKS_JSON = Path(
    os.environ.get("LEGACY_TASKS", VAULT / "00-System/dashboard-tasks-source.json")
)

ACC_MAP = {
    "strategy": "r",
    "firemni-procesy": "r",
    "rb-universe-development": "r",
    "financni-tym": "te",
    "ma-odyssey": "am",
    "operations": "gr",
    "pipedrive-a-dalsi-nastroje": "gr",
    "obecna-inspirace": "gr",
    "exponential-summit": "am",
    "kratky-potlesk": "gr",
    "vibe-coding": "te",
    "rb-network": "gr",
    "obchodni-podminky-rb-edu": "r",
    "owners": "r",
}

PRIORITY_RE = re.compile(r"\b(ASAP|Q1|Q2|Next|Backlog)\b", re.I)
DATE_RE = re.compile(r"\*\*Vrátit se\*\*:\s*(\d{4}-\d{2}-\d{2})")
TASK_HEAD_RE = re.compile(
    r"^###\s+(~~)?([A-Z]+\d+[a-z]?)\s*[—–-]\s*(.+?)(?:~~)?\s*(✅|HOTOVO)?\s*$",
    re.MULTILINE,
)
INLINE_TASK_RE = re.compile(
    r"^-\s+\[([ x])\]\s+\*\*([A-Z]+\d+[a-z]?)(?:\s+\[([^\]]+)\])?\*\*\s*(.+)$",
    re.MULTILINE,
)
CHECK_RE = re.compile(r"^-\s+\[([ x])\]\s+(.+)$", re.MULTILINE)
SLUG_RE = re.compile(r"^\*\*Slug\*\*:\s*`([^`]+)`", re.MULTILINE)
TITLE_RE = re.compile(r"^#\s+Téma:\s*(.+)$", re.MULTILINE)


def _priority_from(text: str) -> str:
    m = PRIORITY_RE.search(text)
    if not m:
        return "Next"
    p = m.group(1)
    if p.upper() == "ASAP":
        return "ASAP"
    if p.upper() == "Q1":
        return "ASAP"
    if p.upper() == "Q2":
        return "Next"
    return p


def _deadline_from(block: str) -> str | None:
    m = DATE_RE.search(block)
    return m.group(1) if m else None


def _parse_checklist(block: str) -> list[dict]:
    out = []
    for m in CHECK_RE.finditer(block):
        line = m.group(2).strip()
        if line.startswith("**") and "—" in line[:20]:
            continue
        out.append({"t": line, "d": m.group(1).lower() == "x"})
    return out


def _parse_file(path: Path) -> tuple[str, str, list[dict]]:
    text = path.read_text(encoding="utf-8")
    slug_m = SLUG_RE.search(text)
    slug = slug_m.group(1) if slug_m else path.stem
    title_m = TITLE_RE.search(text)
    title = title_m.group(1).strip() if title_m else slug
    tasks: list[dict] = []

    for m in TASK_HEAD_RE.finditer(text):
        tid, name = m.group(2), m.group(3).strip()
        if m.group(1) or m.group(4):
            st = "dn"
        else:
            st = "wt"
        start = m.end()
        nxt = TASK_HEAD_RE.search(text, start)
        block = text[start : nxt.start() if nxt else len(text)]
        ch = _parse_checklist(block)
        if ch and all(c["d"] for c in ch):
            st = "dn"
        tasks.append(
            {
                "id": tid,
                "name": name,
                "p": _priority_from(m.group(0) + "\n" + block[:400]),
                "dl": _deadline_from(block),
                "st": st,
                "ch": ch,
            }
        )

    for m in INLINE_TASK_RE.finditer(text):
        done = m.group(1).lower() == "x"
        tid, name = m.group(2), m.group(4).strip()
        p = _priority_from(m.group(3) or "")
        tasks.append(
            {
                "id": tid,
                "name": name,
                "p": p,
                "dl": None,
                "st": "dn" if done else "wt",
                "ch": [],
            }
        )

    return slug, title, tasks


def _newest_projekty_mtime() -> float:
    proj = VAULT / "02-Projekty"
    if not proj.is_dir():
        return 0.0
    return max((p.stat().st_mtime for p in proj.glob("*.md")), default=0.0)


def needs_sync() -> bool:
    if not TASKS_JSON.exists():
        return True
    return _newest_projekty_mtime() > TASKS_JSON.stat().st_mtime


def sync(force: bool = False) -> bool:
    if not force and not needs_sync():
        return False
    data = (
        json.loads(TASKS_JSON.read_text(encoding="utf-8"))
        if TASKS_JSON.exists()
        else {"version": 1, "proj_order": [], "projects": {}, "tasks": []}
    )
    by_id = {(t.get("proj"), t.get("id")): t for t in data.get("tasks", [])}
    proj_order: list[str] = list(data.get("proj_order", []))

    for md in sorted((VAULT / "02-Projekty").glob("*.md")):
        if md.name.startswith("_"):
            continue
        slug, title, parsed = _parse_file(md)
        if slug not in proj_order:
            proj_order.append(slug)
        proj = data.setdefault("projects", {}).setdefault(
            slug,
            {
                "name": title,
                "acc": ACC_MAP.get(slug, "gr"),
                "watch": [],
                "materials": [],
                "done": [],
            },
        )
        proj["name"] = title
        for pt in parsed:
            key = (slug, pt["id"])
            existing = by_id.get(key)
            if existing:
                existing["name"] = pt["name"]
                existing["p"] = pt["p"]
                existing["st"] = pt["st"]
                if pt["dl"]:
                    existing["dl"] = pt["dl"]
                if pt["ch"]:
                    existing["ch"] = pt["ch"]
            else:
                new_t = {
                    "p": pt["p"],
                    "id": pt["id"],
                    "st": pt["st"],
                    "proj": slug,
                    "dl": pt["dl"],
                    "ice": {"i": 5, "c": 5, "e": 5},
                    "name": pt["name"],
                    "ch": pt["ch"],
                }
                data.setdefault("tasks", []).append(new_t)
                by_id[key] = new_t

    data["proj_order"] = proj_order
    data["updated"] = str(date.today())
    TASKS_JSON.parent.mkdir(parents=True, exist_ok=True)
    TASKS_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return True


def main() -> None:
    if sync(force="--force" in __import__("sys").argv):
        print("synced", TASKS_JSON)
    else:
        print("skip (projekty not newer than json)")


if __name__ == "__main__":
    main()
