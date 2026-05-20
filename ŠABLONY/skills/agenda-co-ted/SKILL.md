---
name: agenda-co-ted
description: "Use when user asks 'co teď', 'co dnes', 'na co se mám zaměřit', 'co je urgentní', 'ukaž mi dashboard', 'co mám rozdělaného'. Reads 02-PROJEKTY/*.md or 00-System/dashboard-data.json. ICE scoring aligned with dashboard top_priority. Optional 'ukliď' moves done items to HOTOVO. Never modifies files unless user says ukliď/clean/urgent/odlož."
---

# agenda-co-ted

> "Sednu si, jednou se podívám, vím co dělat." Ad-hoc prioritní kapka — bez týdenního review.

## Kdy spouštět

- "Co teď?" / "Co dnes?" / "Na co se mám zaměřit?"
- "Co je v agendě?" / "Ukaž mi dashboard"
- Začátek pracovního dne

## Načti data

Preferuj (v pořadí):

1. `OBSIDIAN/00-System/dashboard-data.json` — `topPriority`, `waiting`, `tasks`
2. Jinak parsuj všechny `OBSIDIAN/02-PROJEKTY/*.md` (kromě `DEPRECATED.md`)

## Klasifikuj

- **PO TERMÍNU**: `dl` nebo `Vrátit se` < dnes
- **DNES**: deadline = dnes
- **ASAP / Q1**: priorita ASAP (Q1 v md → ASAP)
- **TOP podle ICE**: `(I×C)/E` + bonusy (+50 ASAP, +30 overdue, +15 do 2 dnů) — **bez Waiting**
- **WAITING**: aktivní s `waitUntil` ≥ dnes — zobraz zvlášť, ne v TOP
- **BLOKOVANÉ**: `**Blokováno:**` kromě „nic"

## Vrať dashboard

```
═══════════════════════════════════════════════
CO TEĎ — DD/MM/YYYY
═══════════════════════════════════════════════

🔥 TOP 3 (z dashboardu / ICE)
  • [slug/ID] název — p=ASAP dl=…
  ...

⏸ WAITING (N)
  • [slug/ID] do YYYY-MM-DD — název

⚠️ PO TERMÍNU (N)
  ...

🚧 BLOKOVANÉ (N)
  ...

═══════════════════════════════════════════════
Příkazy: ukliď | detail <slug> | revize priorit
```

## Subcommands

- **`ukliď` / `clean`** → `[x]` subtasky / hotové úkoly → preview → `## Recently moved to HOTOVO` v hub md
- **`detail <slug>`** → celý `02-PROJEKTY/<slug>.md` + briefing (Kontext, Progress, Materiály)
- **`revize priorit`** → deleguj na skill `agenda-priority-review`

## Pravidla

- Nikdy neukládej bez explicitního příkazu
- Waiting nikdy v TOP 3
- Cesty: `02-PROJEKTY/`, ne `AGENDA/`
