#!/bin/sh
set -eu

mkdir -p /data/mrluc/01-INBOX/slack \
  /data/mrluc/01-INBOX/sembly \
  /data/mrluc/01-INBOX/email \
  /data/mrluc/00-System/Triage-Pending \
  /data/mrluc/00-System/Triage-Applied \
  /data/mrluc/02-Projekty \
  /var/log/second-brain

# Initial dashboard build if vault has data
if [ -f "${LEGACY_TASKS}" ] || [ -d "${VAULT_PATH}/02-Projekty" ]; then
  python3 /app/cron/build_dashboard.py >> /var/log/second-brain/build.log 2>&1 || true
fi

nginx

echo "second-brain-hub: nginx + supercronic (Europe/Prague)"
exec supercronic -passthrough-logs /etc/cron.d/second-brain
