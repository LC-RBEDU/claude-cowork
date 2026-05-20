#!/usr/bin/env python3
"""Sunday evening: factual weekly summary draft → 00-System/weekly/YYYY-Www-draft.md"""
from __future__ import annotations

import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

VAULT = Path(
    os.environ.get(
        "VAULT_PATH",
        Path("/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN"),
    )
)
TASKS_JSON = Path(
    os.environ.get("LEGACY_TASKS", VAULT / "00-System/dashboard-tasks-source.json")
)
WEEKLY_DIR = VAULT / "00-System/weekly"
INBOX_SUBDIRS = ("slack", "sembly", "email", "daily")
TZ = ZoneInfo(os.environ.get("TZ", "Europe/Prague"))


def _today() -> date:
    return datetime.now(TZ).date()


def iso_week_label(d: date | None = None) -> str:
    d = d or _today()
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def count_inbox() -> int:
    inbox = VAULT / "01-INBOX"
    n = 0
    for sub in INBOX_SUBDIRS:
        d = inbox / sub
        if not d.is_dir():
            continue
        for p in d.glob("*.md"):
            if p.name.startswith("README") or p.name.startswith("._"):
                continue
            head = p.read_text(encoding="utf-8", errors="replace")[:400]
            if "ZPRACOVÁNO" in head.upper():
                continue
            n += 1
    return n


def count_pending() -> int:
    pending = VAULT / "00-System/Triage-Pending"
    if not pending.is_dir():
        return 0
    return len(list(pending.glob("*.json")))


def ice_score(t: dict, today: date) -> float:
    ice = t.get("ice") or {}
    i, c, e = ice.get("i", 5), ice.get("c", 5), max(ice.get("e", 5), 1)
    s = (i * c) / e
    if t.get("p") == "ASAP":
        s += 50
    dl = t.get("dl")
    if dl:
        try:
            d = date.fromisoformat(str(dl)[:10])
            if d <= today:
                s += 30
            elif (d - today).days <= 2:
                s += 15
        except ValueError:
            pass
    return s


def build_draft() -> Path:
    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    week = iso_week_label()
    out = WEEKLY_DIR / f"{week}-draft.md"
    today = _today()
    week_start = today - timedelta(days=7)

    src = json.loads(TASKS_JSON.read_text(encoding="utf-8")) if TASKS_JSON.exists() else {}
    tasks = src.get("tasks", [])
    projects = src.get("projects", {})
    proj_order = src.get("proj_order", [])

    done_lines: list[str] = []
    for slug in proj_order:
        p = projects.get(slug) or {}
        dw = (p.get("stats") or {}).get("doneWeek", 0)
        if dw:
            done_lines.append(f"- **{p.get('name', slug)}** — {dw} položek v HOTOVO tento týden")

    open_tasks = [t for t in tasks if t.get("st") != "dn" and t.get("p") != "Waiting"]
    ranked = sorted(open_tasks, key=lambda t: ice_score(t, today), reverse=True)[:8]
    top_lines = [
        f"- `{t.get('proj')}/{t.get('id')}` {t.get('p')} dl={t.get('dl') or '—'} — {t.get('name', '')[:70]}"
        for t in ranked
    ]

    waiting = [t for t in tasks if t.get("p") == "Waiting" and t.get("st") != "dn"]
    wait_lines = [
        f"- `{t.get('proj')}/{t.get('id')}` do {t.get('waitUntil', '?')} — {t.get('name', '')[:60]}"
        for t in waiting[:12]
    ]

    overdue = []
    for t in open_tasks:
        dl = t.get("dl")
        if not dl:
            continue
        try:
            if date.fromisoformat(str(dl)[:10]) < today:
                overdue.append(t)
        except ValueError:
            pass
    overdue_lines = [
        f"- `{t.get('proj')}/{t.get('id')}` deadline {t.get('dl')} — {t.get('name', '')[:60]}"
        for t in overdue[:10]
    ]

    progress_bits = []
    for slug in proj_order:
        prog = (projects.get(slug) or {}).get("progress") or []
        if prog:
            progress_bits.append(f"### {projects.get(slug, {}).get('name', slug)}")
            for line in prog[:3]:
                progress_bits.append(f"- {line}")

    body = f"""# Týdenní shrnutí — draft {week}

**Vygenerováno:** {datetime.now(TZ).strftime("%Y-%m-%d %H:%M")} (Europe/Prague)  
**Období:** {week_start.isoformat()} – {today.isoformat()}  
**Schválení:** skill `agenda-weekly-review` → finální `{week}.md`

---

## Metriky

- INBOX nezpracovaných: **{count_inbox()}**
- Triage-Pending batchů: **{count_pending()}**
- Otevřených úkolů (bez Waiting): **{len(open_tasks)}**
- Waiting: **{len(waiting)}**
- Po termínu: **{len(overdue)}**

---

## Hotovo tento týden (z HOTOVO sekcí hubů)

{chr(10).join(done_lines) if done_lines else "- _(žádné datované HOTOVO v hubech)_"}

---

## Progress v hubech

{chr(10).join(progress_bits) if progress_bits else "- _(sekce ## Progress prázdná — doplň po schválení)_"}

---

## TOP úkoly podle skóre (návrh fokusu)

{chr(10).join(top_lines) if top_lines else "- —"}

---

## Waiting

{chr(10).join(wait_lines) if wait_lines else "- —"}

---

## Po termínu

{chr(10).join(overdue_lines) if overdue_lines else "- —"}

---

## Co povedlo / kam to posunulo / priorita příští týden

_(doplň v chatu při schvalování — tento draft je jen fakta)_

### Co se povedlo
- 

### Kam se posunulo
- 

### Priorita příští týden
1. 
2. 
3. 

---

_Viz `00-System/Memory/procesy-mrluc.md`_
"""
    out.write_text(body, encoding="utf-8")
    return out


def main() -> None:
    path = build_draft()
    print("wrote", path)


if __name__ == "__main__":
    main()
