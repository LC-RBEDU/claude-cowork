# MrLUC — procesy a rytmy

**SSOT:** markdown v `02-PROJEKTY/<slug>.md` (úkoly, kontext, materiály). JSON/dashboard jen odvozený pohled.

## Denně

| Co | Jak |
|----|-----|
| Capture | `01-INBOX/` (Slack, Sembly, email, daily) |
| Triáž | Cron `triage_run.py` → `Triage-Pending/` → schválení v Cursoru (`agenda-triage`) |
| Co teď | Skill `agenda-co-ted` nebo dashboard |
| Práce na projektu | Skill `agenda-work` — hub + složka výstupů |

## Neděle večer (cron 20:00 Europe/Prague)

| Krok | Výstup |
|------|--------|
| 1. Cron `weekly_summary_draft.py` | `00-System/weekly/YYYY-Www-draft.md` |
| 2. Cron `retro_draft.py` (+10 min) | `00-System/Memory/retro-YYYY-Www-draft.md` |
| 3. Ty v chatu | `agenda-weekly-review` → finální `YYYY-Www.md` |
| 4. Ty v chatu | `agenda-retro` → finální `retro-YYYY-Www.md` |
| 5. Volitelně | 1–2 věty do `## Progress` u dotčených hubů |

Draft = návrh k schválení. Finální soubory zapisuje skill až po „schval“.

## Ad-hoc

| Co | Skill | Poznámka |
|----|-------|----------|
| Revize priorit | `agenda-priority-review` | ICE, ASAP/Next, Waiting, duplicity — vždy preview |
| Capture / inbox | `agenda-capture` | Nové položky do hubů |

## Co není SSOT

- `dashboard-tasks-source.json` — sync z markdownu
- `Triage-Pending/*.json` — návrhy, ne pravda
- `*-draft.md` — skeleton z cronu, ne finální text

## Sekce v project hubu

| Sekce | Účel |
|-------|------|
| Kontext | Proč téma existuje |
| Progress | Týdenní posun (aktualizuje weekly review) |
| Materiály | Odkazy `- [název](url) — popis` |
| Otevřené otázky | Tagy `[watch]` `[blocked]` `[decision]` |
| Aktivní úkoly | `### ID` + ICE + checklist |
