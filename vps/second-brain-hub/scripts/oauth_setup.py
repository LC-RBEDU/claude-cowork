#!/usr/bin/env python3
"""One-shot OAuth consent flow for the MrLUC Drive integration.

Run this **once on your Mac** to obtain a long-lived `refresh_token` that
the cron container will use to act on Google Drive on your behalf.

Prereqs:
  1. Google Cloud project with a "Desktop app" OAuth client created.
     Download the credentials JSON and save it to:
         ~/.config/mrluc/oauth_client.json
     (Override with --client PATH.)
  2. pip install google-auth-oauthlib  (already in requirements.txt)

Usage:
    python3 scripts/oauth_setup.py
    python3 scripts/oauth_setup.py --client /path/to/client_secret.json
    python3 scripts/oauth_setup.py --out ~/.config/mrluc/oauth_creds.json

What it does:
    1. Reads the OAuth client JSON (client_id + client_secret).
    2. Opens your browser → Google sign-in.
       **Sign in as lukas@redbuttonedu.cz** (NOT a personal gmail account).
    3. Click "Allow" for Drive scope (full read+write).
    4. Local server on 127.0.0.1:<random> receives the auth code.
    5. Exchanges code for access_token + refresh_token.
    6. Writes a combined credentials JSON to:
         ~/.config/mrluc/oauth_creds.json
       containing: client_id, client_secret, refresh_token, token_uri.
    7. Prints the JSON content to stdout — paste this into Coolify env
       as GOOGLE_DRIVE_OAUTH_JSON.

The refresh_token does NOT expire (provided the OAuth consent screen
"Publishing status" is set to "In production" inside a Workspace org;
"Testing" mode also works but tokens issued there expire after 7 days,
so make sure the consent screen lives in the Workspace org).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

DEFAULT_CLIENT = Path.home() / ".config" / "mrluc" / "oauth_client.json"
DEFAULT_OUT = Path.home() / ".config" / "mrluc" / "oauth_creds.json"
DRIVE_SCOPE = "https://www.googleapis.com/auth/drive"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--client", type=Path, default=DEFAULT_CLIENT,
                   help=f"Path to OAuth client JSON (default: {DEFAULT_CLIENT})")
    p.add_argument("--out", type=Path, default=DEFAULT_OUT,
                   help=f"Where to write merged credentials JSON (default: {DEFAULT_OUT})")
    p.add_argument("--port", type=int, default=0,
                   help="Local server port (default: random free port)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not args.client.is_file():
        print(f"ERROR: OAuth client JSON not found at {args.client}", file=sys.stderr)
        print(f"  Save the file downloaded from Google Cloud Console as:", file=sys.stderr)
        print(f"  {args.client}", file=sys.stderr)
        return 2

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("ERROR: missing dependency 'google-auth-oauthlib'.", file=sys.stderr)
        print("       Run: pip install google-auth-oauthlib", file=sys.stderr)
        return 2

    client_raw = json.loads(args.client.read_text(encoding="utf-8"))
    # Desktop app JSON wraps the secrets under an "installed" key.
    inner = client_raw.get("installed") or client_raw.get("web") or client_raw
    if "client_id" not in inner or "client_secret" not in inner:
        print(f"ERROR: client JSON is missing client_id / client_secret keys: {args.client}", file=sys.stderr)
        return 2

    print("== OAuth consent flow ==")
    print(f"Using client_id: {inner['client_id']}")
    print("Opening browser. Sign in as **lukas@redbuttonedu.cz** and click Allow.")
    print()

    flow = InstalledAppFlow.from_client_config(
        {"installed": inner}, scopes=[DRIVE_SCOPE]
    )
    # `run_local_server` spins up a temporary HTTP server on 127.0.0.1:<port>
    # to receive the auth-code callback from Google. Browser opens automatically.
    creds = flow.run_local_server(
        host="127.0.0.1",
        port=args.port,
        prompt="consent",          # force consent so refresh_token is returned
        access_type="offline",     # offline → refresh_token included
        open_browser=True,
    )

    if not creds.refresh_token:
        print("ERROR: no refresh_token returned. Possible causes:", file=sys.stderr)
        print("  - You already consented before and Google reused an existing grant.", file=sys.stderr)
        print(
            "  - Revoke previous access at https://myaccount.google.com/permissions",
            file=sys.stderr,
        )
        print("    then re-run this script.", file=sys.stderr)
        return 3

    merged = {
        "client_id": inner["client_id"],
        "client_secret": inner["client_secret"],
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "scopes": list(creds.scopes or [DRIVE_SCOPE]),
        # Helpful debug context — not used by the runtime.
        "account_hint": creds.id_token.get("email") if getattr(creds, "id_token", None) else None,
    }
    # Remove None
    merged = {k: v for k, v in merged.items() if v is not None}

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(merged, indent=2), encoding="utf-8")
    os.chmod(args.out, 0o600)

    print(f"\n== Wrote merged credentials to {args.out} (mode 0600) ==\n")
    print("Copy this entire JSON value into Coolify env GOOGLE_DRIVE_OAUTH_JSON:\n")
    print(json.dumps(merged, indent=2))
    print("\nDone. Refresh tokens do NOT expire (until you revoke access).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
