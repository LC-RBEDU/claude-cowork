#!/bin/bash
# push-artifacts.sh
# Automaticky pushne změny v Cowork artefaktech na GitHub Pages
# Repo: https://github.com/LC-RBEDU/claude-cowork
# Spouštěno launchd demonem při každé změně v ~/Documents/Claude/Artifacts

ARTIFACTS_DIR="$HOME/Documents/Claude/Artifacts"
LOG="$HOME/Library/Logs/claude-cowork-push.log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG"
}

cd "$ARTIFACTS_DIR" || { log "❌ Složka nenalezena: $ARTIFACTS_DIR"; exit 1; }

git add -A

if git diff --cached --quiet; then
  log "✅ Žádné změny"
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
git commit -m "Auto-push — $TIMESTAMP"

if git push origin gh-pages >> "$LOG" 2>&1; then
  log "✅ Push OK → https://lc-rbedu.github.io/claude-cowork/"
else
  log "❌ Push selhal — viz výše"
fi
