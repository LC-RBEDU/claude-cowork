#!/usr/bin/env python3
"""Sunday evening (+10 min): meta retro draft → 00-System/Memory/retro-YYYY-Www-draft.md

Phase 2 migrace — vault I/O přes lib/drive_io.DriveVault.
"""
from __future__ import annotations

import os
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

_LIB = Path(__file__).resolve().parents[1] / "lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from drive_io import DriveVault, DriveNotFoundError, credentials_from_env  # noqa: E402

TZ = ZoneInfo(os.environ.get("TZ", "Europe/Prague"))
TRIAGE_APPLIED_REL = "00-System/Triage-Applied"
WEEKLY_DIR_REL = "00-System/weekly"
MEMORY_DIR_REL = "00-System/Memory"

_VAULT_SINGLETON: DriveVault | None = None


def get_vault() -> DriveVault:
    global _VAULT_SINGLETON
    if _VAULT_SINGLETON is None:
        root_id = (os.environ.get("VAULT_DRIVE_ID") or "").strip()
        if not root_id:
            raise RuntimeError(
                "VAULT_DRIVE_ID env not set — Drive vault folder ID is required."
            )
        creds, _mode = credentials_from_env()
        _VAULT_SINGLETON = DriveVault(root_id, credentials=creds)
    return _VAULT_SINGLETON


def _today() -> date:
    return datetime.now(TZ).date()


def iso_week_label(d: date | None = None) -> str:
    d = d or _today()
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def count_recent_applied(cutoff: datetime) -> int:
    """Count applied entries (.json + .md) modified at or after `cutoff` (UTC)."""
    vault = get_vault()
    cutoff_utc = cutoff.astimezone(timezone.utc)
    n = 0
    for pattern in ("*.json", "*.md"):
        try:
            files = vault.list_dir(TRIAGE_APPLIED_REL, pattern=pattern)
        except DriveNotFoundError:
            continue
        for meta in files:
            if meta.modified_time >= cutoff_utc:
                n += 1
    return n


def weekly_draft_excerpt(week: str, max_lines: int = 25) -> str:
    rel = f"{WEEKLY_DIR_REL}/{week}-draft.md"
    try:
        text, _ = get_vault().read_text(rel)
    except DriveNotFoundError:
        return "_(weekly draft zatím neexistuje — spusť weekly_summary_draft.py)_"
    lines = text.splitlines()
    return "\n".join(lines[:max_lines]) + ("\n..." if len(lines) > max_lines else "")


def build_draft() -> str:
    week = iso_week_label()
    rel = f"{MEMORY_DIR_REL}/retro-{week}-draft.md"
    cutoff = datetime.now(TZ) - timedelta(days=7)
    applied = count_recent_applied(cutoff)

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
    get_vault().write_text(rel, body)
    return rel


def main() -> None:
    rel = build_draft()
    print("wrote drive://", rel)


if __name__ == "__main__":
    main()
