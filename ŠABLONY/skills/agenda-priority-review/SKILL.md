---
name: agenda-priority-review
description: "Use when user asks revize priorit, přehodnotit ICE, srovnat ASAP/Next/Waiting, or re-prioritize projects. Ad-hoc only. Scans all 02-PROJEKTY/*.md open tasks, proposes priority/ICE/waitUntil changes. ALWAYS preview before write. Optional export to Triage-Pending/priority-review-*.json."
---

# agenda-priority-review

> Ad-hoc srovnání priorit napříč vaultem. Ne cron — spouštíš, když cítíš chaos v prioritách.

## Kdy spouštět

- "Revize priorit" / "přehodnotit priority" / "srovnat ICE"
- Po velké změně v projektech (reorganizace, nové ASAP vlny)
- **Ne** místo týdenního shrnutí — to je `agenda-weekly-review`

## Načti data

1. Všechny `02-PROJEKTY/*.md` — aktivní `### ID` bloky (ne HOTOVO)
2. Volitelně `00-System/dashboard-data.json` — `topPriority`, `waiting`, overdue `dl`
3. `00-System/Memory/procesy-mrluc.md` — pravidla Waiting / SSOT

## Scoring (stejná logika jako dashboard)

Pro návrhy TOP vs podhodnocené použij:

- Skóre ≈ `(I×C)/E` + 50 pokud ASAP + 30 overdue deadline + 15 deadline do 2 dnů
- **Waiting** — nepatří do TOP 3; zkontroluj `waitUntil` a smysl
- **Blokováno** — pokud v bloku je `**Blokováno:**` kromě „nic“, označ v preview

## Preview formát

```
REVIZE PRIORIT — YYYY-MM-DD

Navrhované změny (N):
  [finance/F17] Q2 → ASAP, ICE I7→I10 (důvod: cashflow)
  [strategy/S8] ASAP → Waiting do 2026-05-31 (důvod: čeká na Lenku)
  ...

Beze změny (TOP 5 podle skóre):
  1. ...
```

## Zápis

- Jen po explicitním „schval" / „apply"
- Uprav **priority řádek** a **ICE** v markdownu (`**ASAP | ICE I…**`)
- Volitelně: ulož batch do `00-System/Triage-Pending/priority-review-YYYY-MM-DD.json` pro audit
- Po zápisu: připomeň `sync_tasks_from_projekty.py` + rebuild dashboard (nebo uživatel má watch)

## Pravidla

- Nikdy neměň text úkolů / subtasků bez explicitního požadavku
- Duplicitní ID napříč projekty — flagni, nespojuj automaticky
- Propojené úkoly (F13↔F19) — navrhni stejný wait/deadline jen pokud dává smysl
