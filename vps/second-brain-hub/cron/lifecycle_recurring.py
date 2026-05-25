#!/usr/bin/env python3
"""F7.2: Recurring task rotation — when a recurring task hits status: Done,
archive current instance and create the next one with reset body + new deadline.

Recurring tasks live as `02-PROJEKTY/<slug>/tasks/<ID>.md` (no slugify suffix —
fixed filename per recurring task ID).

Frontmatter:
    recurring:
      frequency: weekly | monthly | every-n-days | weekday
      interval: 42                     # for every-n-days
      weekday: thursday                # for weekly
      reset_body_sections: ["## Operativní kroky", "## Poznámky / log"]
      preserve_body_sections: ["## Kontext"]
    extra_module: edu_news             # optional, calls lifecycle_extra_<module>.py clear

Workflow per Done recurring task:
1. Move current `<ID>.md` to `07-ARCHIV/tasks-done/<slug>/<ID>-<YYYY-MM-DD>.md`
   (keeps history of past instances)
2. Compute next deadline from frequency rule
3. Create new `<ID>.md` with:
   - status: Waiting (or ASAP if waitUntil already passed)
   - waitUntil = next_deadline - 1 day
   - deadline = next_deadline
   - reset body sections (Operativní kroky, Poznámky / log) cleared, preserved sections kept
   - frontmatter `created` updated, `updated` = today
4. If `extra_module: <name>` present, post-call `lifecycle_extra_<name>.py --reset`
   (out of scope here — handled by separate scripts wired in crontab)

Idempotent — re-running on Already-rotated task does nothing (status no longer Done).
"""
from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

_LIB = Path(__file__).resolve().parents[1] / "lib"
if str(_LIB) not in sys.path:
    sys.path.insert(0, str(_LIB))

from drive_io import DriveVault, DriveNotFoundError, credentials_from_env  # noqa: E402
from task_io import (  # noqa: E402
    iter_active_tasks,
    parse_task_text,
    serialize_task,
    parse_iso_date,
    ARCHIV_DIR,
)

TZ = ZoneInfo(os.environ.get("TZ", "Europe/Prague"))

WEEKDAY_MAP = {
    "monday": 0, "mon": 0,
    "tuesday": 1, "tue": 1,
    "wednesday": 2, "wed": 2,
    "thursday": 3, "thu": 3,
    "friday": 4, "fri": 4,
    "saturday": 5, "sat": 5,
    "sunday": 6, "sun": 6,
}


def compute_next_deadline(rec: dict, last_deadline: Optional[date], today: date) -> date:
    """Compute next deadline based on recurring rule."""
    freq = (rec.get("frequency") or "").lower().strip()
    base = last_deadline or today

    if freq == "monthly":
        # Same day-of-month, next month
        d = base
        if d.month == 12:
            return d.replace(year=d.year + 1, month=1)
        try:
            return d.replace(month=d.month + 1)
        except ValueError:
            # e.g. Jan 31 → Feb 28
            for day in range(28, 32):
                try:
                    return d.replace(month=d.month + 1, day=min(day, 28))
                except ValueError:
                    continue
            return d.replace(month=d.month + 1, day=28)

    if freq == "weekly":
        wd_name = (rec.get("weekday") or "").lower().strip()
        wd = WEEKDAY_MAP.get(wd_name)
        if wd is None:
            return base + timedelta(days=7)
        # Next occurrence of weekday after today
        days_ahead = (wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    if freq == "every-n-days":
        try:
            interval = int(rec.get("interval") or 7)
        except (ValueError, TypeError):
            interval = 7
        return today + timedelta(days=interval)

    if freq == "weekday":
        wd_name = (rec.get("weekday") or "").lower().strip()
        wd = WEEKDAY_MAP.get(wd_name, 3)  # default thursday
        days_ahead = (wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    # Unknown frequency — fallback to +7 days
    return today + timedelta(days=7)


def reset_body(body: str, reset_sections: list[str], preserve_sections: list[str]) -> str:
    """Clear specified ## sections, keep preserved ones."""
    sections: dict[str, list[str]] = {}
    current = "_HEADER"
    sections[current] = []

    for line in body.splitlines():
        if line.startswith("## "):
            current = line.strip()
            sections[current] = [line]
        else:
            sections[current].append(line)

    out_lines: list[str] = []
    for sec, lines in sections.items():
        if sec == "_HEADER":
            out_lines.extend(lines)
            continue
        if sec in reset_sections:
            # Keep header, clear content
            out_lines.append(sec)
            if sec == "## Operativní kroky":
                out_lines.append("- [ ] (next instance — doplň operativní kroky)")
            elif sec == "## Poznámky / log":
                out_lines.append(f"- {datetime.now(TZ).date().isoformat()}: New recurring instance.")
            out_lines.append("")
        else:
            out_lines.extend(lines)

    return "\n".join(out_lines)


def main() -> None:
    root_id = (os.environ.get("VAULT_DRIVE_ID") or "").strip()
    if not root_id:
        raise RuntimeError("VAULT_DRIVE_ID env not set")
    creds, _ = credentials_from_env()
    vault = DriveVault(root_id, credentials=creds)

    today = datetime.now(TZ).date()
    today_str = today.isoformat()
    rotated = 0
    skipped = 0

    for task in iter_active_tasks(vault):
        if not task.is_done:
            continue
        rec = task.frontmatter.get("recurring")
        if not rec or not isinstance(rec, dict):
            continue

        slug = task.slug or "unknown"
        task_id = task.task_id
        if not task_id:
            print(f"  ! skipping recurring task without id: {task.rel_path}")
            continue

        # 1. Archive current instance
        archive_filename = f"{task_id}-{today_str}.md"
        archive_path = f"{ARCHIV_DIR}/{slug}/{archive_filename}"
        vault.mkdir_p(f"{ARCHIV_DIR}/{slug}")

        try:
            existing = vault.stat(archive_path)
            if existing:
                print(f"  - archive exists: {archive_path}")
        except DriveNotFoundError:
            pass

        # 2. Compute next deadline
        last_dl = parse_iso_date(task.frontmatter.get("deadline"))
        next_dl = compute_next_deadline(rec, last_dl, today)
        next_wu = next_dl - timedelta(days=1)

        # 3. Reset body
        reset_sections = rec.get("reset_body_sections") or [
            "## Operativní kroky",
            "## Poznámky / log",
        ]
        preserve_sections = rec.get("preserve_body_sections") or []
        new_body = reset_body(task.body, reset_sections, preserve_sections)

        # 4. Build new frontmatter
        new_fm = dict(task.frontmatter)
        new_fm["status"] = "Waiting" if next_wu > today else "ASAP"
        new_fm["deadline"] = next_dl.isoformat()
        new_fm["waitUntil"] = next_wu.isoformat() if new_fm["status"] == "Waiting" else None
        new_fm["updated"] = today_str
        new_fm["created"] = today_str
        new_text = serialize_task(new_fm, new_body)

        # 5. Move current → archive, then write new at original path
        try:
            vault.move(task.rel_path, archive_path)
        except Exception as e:
            print(f"  ! archive move failed: {e}")
            skipped += 1
            continue

        try:
            vault.write_text(task.rel_path, new_text)
        except Exception as e:
            print(f"  ! new instance write failed: {e}")
            skipped += 1
            continue

        rotated += 1
        print(
            f"  ↻ {task.rel_path}: archived {today_str}, next deadline {next_dl.isoformat()}, "
            f"status={new_fm['status']}"
        )

        extra = task.frontmatter.get("extra_module")
        if extra:
            print(f"    extra_module: {extra} (handled by lifecycle_extra_{extra}.py)")

    print(f"lifecycle_recurring: rotated={rotated}, skipped={skipped}")


if __name__ == "__main__":
    main()
