#!/usr/bin/env bash
# Mac: build dashboard-data.json from Drive SECOND_BRAIN vault and serve web/ locally.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
VAULT_PATH="${VAULT_PATH:-/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN}"
WEB="$REPO/web"
PORT="${PORT:-8765}"

export VAULT_PATH
export DASHBOARD_JSON="$WEB/dashboard-data.json"
export LEGACY_TASKS="${LEGACY_TASKS:-$VAULT_PATH/00-System/dashboard-tasks-source.json}"

export DASHBOARD_HTML="${DASHBOARD_HTML:-$VAULT_PATH/00-System/Dashboard.html}"
python3 "$REPO/cron/build_dashboard.py"

echo "Soubor (dvojklik): $DASHBOARD_HTML"
echo "Live refresh: $REPO/../../scripts/serve_dashboard.sh → http://127.0.0.1:8765/Dashboard.html"
echo "Dev web/: http://127.0.0.1:${PORT}/"
echo "Vault: $VAULT_PATH"
cd "$WEB"
exec python3 -m http.server "$PORT"
