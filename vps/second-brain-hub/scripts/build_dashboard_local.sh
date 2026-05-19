#!/usr/bin/env bash
# Mac: build dashboard-data.json from iCloud MrLUC vault and serve web/ locally.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
VAULT_PATH="${VAULT_PATH:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/MrLUC}"
WEB="$REPO/web"
PORT="${PORT:-8765}"

export VAULT_PATH
export DASHBOARD_JSON="$WEB/dashboard-data.json"
export LEGACY_TASKS="${LEGACY_TASKS:-$VAULT_PATH/00-System/dashboard-tasks-source.json}"

python3 "$REPO/cron/build_dashboard.py"

echo "Dashboard: http://127.0.0.1:${PORT}/"
echo "Vault: $VAULT_PATH"
cd "$WEB"
exec python3 -m http.server "$PORT"
