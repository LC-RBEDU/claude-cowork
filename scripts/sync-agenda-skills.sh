#!/usr/bin/env bash
# Sync MrLUC agenda skills from ŠABLONY → Cursor, Claude, project .cursor/skills
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$REPO_ROOT/ŠABLONY/skills"
SKILLS=(
  agenda-capture
  agenda-triage
  agenda-co-ted
  agenda-work
  agenda-status-update
  agenda-analyze
  agenda-weekly-review
  agenda-priority-review
  agenda-retro
  agenda-proces
)
DESTS=(
  "$HOME/.cursor/skills"
  "$HOME/.claude/skills"
  "$REPO_ROOT/.cursor/skills"
)
for dest in "${DESTS[@]}"; do
  mkdir -p "$dest"
  for s in "${SKILLS[@]}"; do
    mkdir -p "$dest/$s"
    cp "$SRC/$s/SKILL.md" "$dest/$s/SKILL.md"
    echo "  $dest/$s/SKILL.md"
  done
done
echo "Synced ${#SKILLS[@]} skills to ${#DESTS[@]} destinations."
