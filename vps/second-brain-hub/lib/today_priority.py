"""TOP priority dnes — eligibility + today_score (SSOT for agent-context.json).

Rules:
- Never: Waiting, Backlog, Done
- ASAP always eligible when status == ASAP
- Next eligible only when no open ASAP exists in vault
- Sort: today_score DESC (ICE base + urgency bonuses)

Urgency bonuses (on top of priority_score = (I*C)/E):
- overdue (deadline < today): +35
- deadline today: +30
- deadline tomorrow: +15
"""
from __future__ import annotations

from datetime import date, timedelta
from typing import Any

URGENCY_BONUS_OVERDUE = 35
URGENCY_BONUS_TODAY = 30
URGENCY_BONUS_TOMORROW = 15

TOP_PRIORITY_TODAY_LIMIT = 3
TOP_PRIORITY_LIMIT = 15

EXCLUDED_STATUSES = frozenset({"Done", "Waiting", "Backlog"})


def _task_get(task: Any, key: str, default=None):
    if isinstance(task, dict):
        return task.get(key, default)
    return getattr(task, key, default)


def parse_deadline(deadline: str | None, today: date) -> date | None:
    if not deadline:
        return None
    try:
        return date.fromisoformat(str(deadline)[:10])
    except ValueError:
        return None


def urgency_bonus(deadline: str | None, today: date) -> float:
    dl = parse_deadline(deadline, today)
    if dl is None:
        return 0.0
    if dl < today:
        return float(URGENCY_BONUS_OVERDUE)
    if dl == today:
        return float(URGENCY_BONUS_TODAY)
    if dl == today + timedelta(days=1):
        return float(URGENCY_BONUS_TOMORROW)
    return 0.0


def today_score(priority_score: float, deadline: str | None, today: date) -> float:
    return round(float(priority_score) + urgency_bonus(deadline, today), 2)


def has_any_asap(open_tasks: list[Any]) -> bool:
    return any(_task_get(t, "status") == "ASAP" for t in open_tasks)


def is_top_eligible(status: str, any_asap: bool) -> bool:
    if status in EXCLUDED_STATUSES:
        return False
    if status == "ASAP":
        return True
    if status == "Next":
        return not any_asap
    return False


def enrich_task_dict(task_dict: dict, today: date) -> dict:
    ps = float(task_dict.get("priority_score") or 0)
    dl = task_dict.get("deadline")
    ub = urgency_bonus(dl, today)
    ts = today_score(ps, dl, today)
    out = dict(task_dict)
    out["urgency_bonus"] = ub
    out["today_score"] = ts
    return out


def select_top_priority(
    open_tasks: list[Any],
    today: date,
    *,
    today_limit: int = TOP_PRIORITY_TODAY_LIMIT,
    general_limit: int = TOP_PRIORITY_LIMIT,
) -> tuple[list[dict], list[dict]]:
    """Return (top_priority_today, top_priority) as enriched dicts."""
    any_asap = has_any_asap(open_tasks)
    eligible = [t for t in open_tasks if is_top_eligible(_task_get(t, "status"), any_asap)]

    scored: list[tuple[Any, float]] = []
    for t in eligible:
        ps = _task_get(t, "priority_score")
        if ps is None:
            ice_i = _task_get(t, "ice_i", 5)
            ice_c = _task_get(t, "ice_c", 5)
            ice_e = max(_task_get(t, "ice_e", 5) or 1, 1)
            ps = round((ice_i * ice_c) / ice_e, 2)
        dl = _task_get(t, "deadline")
        scored.append((t, today_score(ps, dl, today)))

    scored.sort(key=lambda pair: -pair[1])

    def to_enriched(task: Any, ts: float) -> dict:
        if isinstance(task, dict):
            base = dict(task)
            if "priority_score" not in base:
                base["priority_score"] = round(
                    (_task_get(task, "ice_i", 5) * _task_get(task, "ice_c", 5))
                    / max(_task_get(task, "ice_e", 5) or 1, 1),
                    2,
                )
        else:
            base = task.to_dict()
        base["today_score"] = ts
        base["urgency_bonus"] = urgency_bonus(base.get("deadline"), today)
        return base

    top_today = [to_enriched(t, ts) for t, ts in scored[:today_limit]]
    top_general = [to_enriched(t, ts) for t, ts in scored[:general_limit]]
    return top_today, top_general
