#!/usr/bin/env python3
"""Build dashboard-data.json from vault 02-Projekty + optional legacy _tasks.json."""
from __future__ import annotations

import json
import os
import re
from datetime import date, datetime
from pathlib import Path

VAULT = Path(os.environ.get("VAULT_PATH", Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/MrLUC"))
_DEFAULT_OUT = Path(__file__).resolve().parents[1] / "web/dashboard-data.json"
OUT_JSON = Path(os.environ.get("DASHBOARD_JSON", _DEFAULT_OUT))
LEGACY_TASKS = Path(os.environ.get("LEGACY_TASKS", ""))


def count_inbox() -> int:
    inbox = VAULT / "01-INBOX"
    if not inbox.exists():
        return 0
    return len(list(inbox.rglob("*.md"))) - len(list(inbox.rglob("README*.md")))


def count_pending() -> int:
    pending = VAULT / "00-System/Triage-Pending"
    if not pending.exists():
        return 0
    n = 0
    for f in pending.glob("*.json"):
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
            if b.get("status", "open") == "open":
                n += 1
        except json.JSONDecodeError:
            pass
    return n


def load_tasks() -> dict:
    legacy = LEGACY_TASKS or (VAULT / "00-System/dashboard-tasks-source.json")
    if Path(legacy).exists():
        return json.loads(Path(legacy).read_text(encoding="utf-8"))
    # Minimal fallback
    return {"version": 1, "updated": str(date.today()), "proj_order": [], "projects": {}, "tasks": []}


def top_priority(tasks: list, limit: int = 5) -> list:
    today = date.today()

    def score(t: dict) -> float:
        ice = t.get("ice") or {}
        i, c, e = ice.get("i", 5), ice.get("c", 5), max(ice.get("e", 5), 1)
        s = (i * c) / e
        if t.get("p") == "ASAP":
            s += 50
        dl = t.get("dl")
        if dl:
            try:
                d = date.fromisoformat(dl[:10])
                if d <= today:
                    s += 30
                elif (d - today).days <= 2:
                    s += 15
            except ValueError:
                pass
        if t.get("st") == "dn":
            return -1
        return s

    ranked = sorted([t for t in tasks if t.get("st") != "dn"], key=score, reverse=True)
    return ranked[:limit]


def main() -> None:
    src = load_tasks()
    payload = {
        "version": 2,
        "generated": datetime.now().isoformat(timespec="seconds"),
        "inboxCount": count_inbox(),
        "pendingCount": count_pending(),
        "proj_order": src.get("proj_order", []),
        "projects": src.get("projects", {}),
        "tasks": src.get("tasks", []),
        "topPriority": top_priority(src.get("tasks", [])),
        "eduNews": src.get("eduNews", []),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", OUT_JSON, "inbox=", payload["inboxCount"], "pending=", payload["pendingCount"])


if __name__ == "__main__":
    main()
