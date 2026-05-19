# second-brain-hub (MrLUC dashboard + triage cron)

HTML dashboard + **supercronic** (cron v kontejneru) pro Obsidian vault **MrLUC**.

## Git → Coolify Auto Deploy

| Položka | Hodnota |
|---------|---------|
| Repozitář | `https://github.com/LC-RBEDU/claude-cowork` |
| Větev | **`main`** (Auto Deploy po push) |
| Base directory | `vps/second-brain-hub` |
| Build pack | Dockerfile (`/Dockerfile`) |
| Host | **coolify-dev** |

```bash
# Lokální změna → deploy
git add vps/second-brain-hub/
git commit -m "second-brain: …"
git push origin main
```

Coolify na dev po pushu automaticky rebuildne image a restartuje kontejner (včetně **nového crontabu** z `deploy/crontab`).

## URL (dev)

**Dashboard:** `https://second-brain.dev.redbuttonedu.cz`  
(pokud DNS ještě není — Coolify ukáže sslip URL v UI)

## Env (runtime, Coolify)

| Proměnná | Význam |
|----------|--------|
| `VAULT_PATH` | `/data/mrluc` — **volume mimo git** |
| `TZ` | `Europe/Prague` |
| `DASHBOARD_JSON` | `/var/www/html/dashboard-data.json` |
| `LEGACY_TASKS` | `/data/mrluc/00-System/dashboard-tasks-source.json` |

## Vault na serveru (odděleně od gitu)

MrLUC **není** v repozitáři. Na hostu:

```bash
# Jednorázově na coolify-dev
sudo mkdir -p /data/mrluc-second-brain
sudo chown 1000:1000 /data/mrluc-second-brain   # uprav dle UID kontejneru

# Sync z Macu (příklad)
rsync -avz --delete \
  "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/MrLUC/" \
  coolify-dev:/data/mrluc-second-brain/
```

Kontejner mount: `/data/mrluc-second-brain` → `/data/mrluc`

## Cron (v image, Europe/Prague)

| Job | Po–Pá | So–Ne |
|-----|-------|-------|
| `triage_run.py` | 7:00, 14:00, 20:00 | 7:00 |
| `build_dashboard.py` | +5 min | 7:05 |
| `edu_news_refresh.py` | 7:10 | 7:10 |

Logy: `/var/log/second-brain/*.log` v kontejneru.

## Schvalování triáže

Pouze **Cursor**: `schval pending triáž`. Slack = jen inbound capture.

## Lokální build test

```bash
cd vps/second-brain-hub
docker build -t second-brain-hub:test .
docker run --rm -p 8080:80 -v /path/to/MrLUC:/data/mrluc second-brain-hub:test
open http://localhost:8080
```

## Coolify bootstrap (jednorázově)

Na `coolify-dev`:

```bash
bash deploy/setup-coolify.sh
```

Vytvoří projekt **Second Brain**, aplikaci, env, Auto Deploy, frontu deploye.
