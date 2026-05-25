#!/usr/bin/env python3
"""F6.3: Append OVERDUE log line for tasks where deadline < today && status != Done.

Does NOT flip status (user decides whether to escalate). Only appends log line
to `## Poznámky / log` section, idempotent (skip if today's overdue line already there).

Bases dashboard already shows overdue list (`Overdue` view in `All-tasks.base`)
without this script. This is a supplementary log for the user.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

_LIB = Path(__file__).resolve().parents[1] / "lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from drive_io import DriveVault, credentials_from_env  # noqa: E402
from task_io import iter_active_tasks, update_task, parse_iso_date  # noqa: E402

TZ = ZoneInfo(os.environ.get("TZ", "Europe/Prague"))

OVERDUE_MARKER = "[lifecycle_overdue_flag]"


def main() -> None:
    root_id = (os.environ.get("VAULT_DRIVE_ID") or "").strip()
    if not root_id:
        raise RuntimeError("VAULT_DRIVE_ID env not set")
    creds, _ = credentials_from_env()
    vault = DriveVault(root_id, credentials=creds)

    today = datetime.now(TZ).date()
    today_str = today.isoformat()
    flagged = 0
    skipped = 0

    for task in iter_active_tasks(vault):
        if task.is_done:
            continue
        dl = parse_iso_date(task.frontmatter.get("deadline"))
        if dl is None or dl >= today:
            continue
        # Idempotency: skip if today's overdue line already in body
        today_marker = f"- {today_str}: OVERDUE"
        if today_marker in task.body:
            continue

        log = (
            f"- {today_str}: OVERDUE — deadline {dl.isoformat()} prošel. "
            f"{OVERDUE_MARKER}\n"
        )
        ok = update_task(
            vault,
            task,
            today_str=today_str,
            body_append=log,
        )
        if ok:
            flagged += 1
            print(f"  ✓ {task.rel_path} OVERDUE (deadline {dl.isoformat()})")
        else:
            skipped += 1

    print(f"lifecycle_overdue_flag: flagged={flagged}, conflicts/skipped={skipped}")


if __name__ == "__main__":
    main()
