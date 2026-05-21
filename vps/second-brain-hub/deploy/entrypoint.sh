#!/bin/sh
set -eu

mkdir -p /var/log/second-brain

# Initial dashboard build on container start. Stateless — reads from Drive,
# writes to Drive. Tolerated to fail (e.g. if Drive creds aren't yet plumbed)
# so cron keeps running and the next scheduled build retries.
python3 /app/cron/build_dashboard.py >> /var/log/second-brain/build.log 2>&1 || true

echo "second-brain-hub: supercronic only (no public HTTP)"
exec /usr/local/bin/supercronic -passthrough-logs /app/crontab
