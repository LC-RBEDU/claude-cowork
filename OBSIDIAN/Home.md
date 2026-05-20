# Second Brain — Home

> SSOT: tento vault na Google Drive (`SECOND_BRAIN`). Dashboard: [[00-System/Dashboard.html]].

## Rychlé odkazy

- [[00-System/Index|Index projektů]]
- [[01-INBOX/README|INBOX]]
- **Dashboard (prohlížeč):** [[00-System/Dashboard.html]]
- Auto-refresh: `SECOND_BRAIN/scripts/install-dashboard-watch.sh` (launchd) nebo `python3 SECOND_BRAIN/scripts/watch_dashboard.py`
- Návod ke struktuře: [[Jak čtu vault MrLUC]]
- Ikony: [[Ikony ve vaultu]]

## Schválení triáže (Cursor)

Po cron běhu: `schval pending triáž` nebo `co čeká na schválení` v Cursor chatu.

## Tasks — dnes (ASAP + po termínu)

```tasks
not done
path includes 02-PROJEKTY
(tags include #asap) OR (due before tomorrow)
sort by due
limit 20
```

> Strategické úkoly (`### [[02-PROJEKTY/Finance#F4 — Cashflow forecast v Alfrédu]]`, ICE, Waiting) jsou v hubu projektu a v Dashboard.html — ne v Tasks dotazech níže.

## Tasks — tento týden (podúkoly)

```tasks
not done
path includes 02-PROJEKTY
due after yesterday
due before in 7 days
sort by due
limit 30
```

## INBOX capture

Nové položky: `01-INBOX/` (Slack, Sembly, email, daily).
