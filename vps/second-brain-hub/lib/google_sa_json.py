"""Parse Service Account JSON from env (same logic as RB Universe backend)."""

import ast
import json
import re
from typing import Optional


def parse_service_account_json(raw: str) -> dict:
    if not raw or not raw.strip():
        raise ValueError("Empty value")
    s = raw.strip().lstrip("\ufeff")
    s = s.replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'")

    def try_parse(t: str) -> Optional[dict]:
        try:
            out = json.loads(t)
            return out if isinstance(out, dict) else None
        except (json.JSONDecodeError, ValueError, TypeError):
            return None

    data = try_parse(s)
    if data is not None:
        return _fix_private_key(data)
    if '\\"' in s:
        data = try_parse(s.replace('\\"', '"'))
    if data is None and len(s) >= 2 and s.startswith('"') and s.endswith('"'):
        data = try_parse(s[1:-1].replace('\\"', '"').replace("\\\\", "\\"))
    if data is None:
        data = try_parse(s.replace("\\n", "\n"))
    if data is None and s.strip().startswith("{"):
        fixed = re.sub(r'([{,]\s*)([a-zA-Z_][a-zA-Z0-9_]*)(\s*:)', r'\1"\2"\3', s)
        data = try_parse(fixed)
    if data is None:
        try:
            parsed = ast.literal_eval(s)
            data = parsed if isinstance(parsed, dict) else None
        except (SyntaxError, ValueError, TypeError):
            pass
    if data is None:
        raise ValueError("Could not parse Service Account JSON")
    return _fix_private_key(data)


def _fix_private_key(data: dict) -> dict:
    pk = data.get("private_key")
    if isinstance(pk, str):
        data = {**data, "private_key": pk.replace("\\n", "\n")}
    return data
