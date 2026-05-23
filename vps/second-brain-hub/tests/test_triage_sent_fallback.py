"""Tests for sent-email fallback proposals (no Drive I/O)."""
from __future__ import annotations

import sys
from pathlib import Path

_CRON = Path(__file__).resolve().parents[1] / "cron"
if str(_CRON) not in sys.path:
    sys.path.insert(0, str(_CRON))

import triage_commitments as mod  # noqa: E402


def _guess_proj(text: str, rel_path: str) -> str:
    if "pipedrive" in text.lower() or "ninjabot" in text.lower():
        return "pipedrive-a-dalsi-nastroje"
    return "finance"


NINJABOT_SENT = """---
source: sent
subject: Re: Check využívání služeb Ninjabot
---

# Email: Re: Check

**Source**: sent

## Tělo

Dobrý den, využívat nechceme nic z toho, takže bych to ukončil.
Děkuji.
"""

NEUTRAL_SENT = """---
source: sent
subject: Díky
---

## Tělo

Děkuji za schůzku, bylo to fajn. Hezký den.
"""


def test_sent_business_action_ninjabot():
    rel = "01-INBOX/email/sent/2026-05-23-ninjabot.md"
    pr = mod.sent_business_action_proposal(
        rel, NINJABOT_SENT, guess_proj=_guess_proj
    )
    assert pr is not None
    assert pr["proposalType"] == "add_task"
    assert pr["suggestedProj"] == "pipedrive-a-dalsi-nastroje"
    assert "Ninjabot" in pr["title"]
    assert pr.get("archiveAfterApply") is True


def test_sent_archive_only_when_no_action():
    rel = "01-INBOX/email/sent/thanks.md"
    assert mod.sent_business_action_proposal(rel, NEUTRAL_SENT, guess_proj=_guess_proj) is None
    arch = mod.sent_archive_only_proposal(rel, NEUTRAL_SENT)
    assert arch["proposalType"] == "archive_only"
    assert arch["action"] == "archive_only"
    assert arch.get("archiveAfterApply") is True


def test_normalize_maps_note_to_update_task():
    pr = mod.normalize_proposal({"action": "add_note_to_task", "title": "x"})
    assert pr["proposalType"] == "update_task"
