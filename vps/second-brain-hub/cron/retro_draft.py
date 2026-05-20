#!/usr/bin/env python3
"""Sunday evening (+10 min): meta retro draft → 00-System/Memory/retro-YYYY-Www-draft.md"""
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
MEMORY_DIR = VAULT / "00-System/Memory"
WEEKLY_DIR = VAULT / "00-System/weekly"
TRIAGE_APPLIED = VAULT / "00-System/Triage-Applied"
TZ = ZoneInfo(os.environ.get("TZ", "Europe/Prague"))


def _today() -> date:
    return datetime.now(TZ).date()


def iso_week_label(d: date | None = None) -> str:
    d = d or _today()
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def count_recent_applied(cutoff: float) -> int:
    if not TRIAGE_APPLIED.is_dir():
        return 0
    n = 0
    for p in TRIAGE_APPLIED.glob("*.json"):
        if p.stat().st_mtime >= cutoff:
            n += 1
    for p in TRIAGE_APPLIED.glob("*.md"):
        if p.stat().st_mtime >= cutoff:
            n += 1
    return n


def weekly_draft_excerpt(week: str, max_lines: int = 25) -> str:
    draft = WEEKLY_DIR / f"{week}-draft.md"
    if not draft.is_file():
        return "_(weekly draft zatím neexistuje — spusť weekly_summary_draft.py)_"
    lines = draft.read_text(encoding="utf-8").splitlines()
    return "\n".join(lines[:max_lines]) + ("\n..." if len(lines) > max_lines else "")


def build_draft() -> Path:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    week = iso_week_label()
    out = MEMORY_DIR / f"retro-{week}-draft.md"
    today = _today()
    cutoff_ts = (datetime.now(TZ) - timedelta(days=7)).timestamp()
    applied = count_recent_applied(cutoff_ts)

    body = f"""# Retro spolupráce — draft {week}

**Vygenerováno:** {datetime.now(TZ).strftime("%Y-%m-%d %H:%M")} (Europe/Prague)  
**Schválení:** skill `agenda-retro` → finální `retro-{week}.md`

---

## Fakta z týdne

- Triage-Applied záznamů (7 dní): **{applied}**
- Weekly draft: `00-System/weekly/{week}-draft.md`

### Výňatek weekly draftu

```
{weekly_draft_excerpt(week)}
```

---

## Keep (co nechat — doplň v chatu)

- 

## Problem (co bolí)

- 

## Try next week (1 experiment)

- 

---

_Meta: vault, dashboard, triáž, skills, cron — ne obsah obchodních projektů._
"""
    out.write_text(body, encoding="utf-8")
    return out


def main() -> None:
    path = build_draft()
    print("wrote", path)


if __name__ == "__main__":
    main()
