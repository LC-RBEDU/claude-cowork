#!/usr/bin/env bash
# Mac → VPS: export dashboard JSON + optional vault snapshot (read-only on VPS)
set -euo pipefail

VAULT_PATH="${VAULT_PATH:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/MrLUC}"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
VPS_HOST="${VPS_HOST:-}"
VPS_WEB="${VPS_WEB:-/var/www/second-brain-hub/web}"

if [[ -z "$VPS_HOST" ]]; then
  echo "Set VPS_HOST=user@host"
  exit 1
fi

export VAULT_PATH
export LEGACY_TASKS="${LEGACY_TASKS:-$VAULT_PATH/00-System/dashboard-tasks-source.json}"
python3 "$REPO/cron/build_dashboard.py"

rsync -avz "$REPO/web/dashboard-data.json" "$VPS_HOST:$VPS_WEB/"
rsync -avz "$REPO/web/index.html" "$REPO/web/app.js" "$REPO/web/styles.css" "$VPS_HOST:$VPS_WEB/"

echo "Exported dashboard to $VPS_HOST:$VPS_WEB"
