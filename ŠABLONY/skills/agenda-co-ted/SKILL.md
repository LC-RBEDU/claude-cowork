---
name: agenda-co-ted
description: "Use when user asks 'co teď', 'co dnes', 'na co se mám zaměřit', 'co je urgentní', 'ukaž mi dashboard', 'co mám rozdělaného' v MrLUC Second Brain v2. Reads 02-PROJEKTY/<slug>/tasks/*.md frontmatter (file-per-task) or 00-System/agent-context.json (po F8). ICE scoring (I*C)/E sjednocený s Bases formula. Optional 'ukliď' archivuje Done tasky do 07-ARCHIV/tasks-done/. Never modifies files unless user says ukliď/clean/urgent/odlož."
---

# agenda-co-ted (v2)

> "Sednu si, jednou se podívám, vím co dělat." Ad-hoc prioritní kapka — bez týdenního review.

**Vault:** `OBSIDIAN/` — `/Users/lukascypra/My Drive (lukas@redbuttonedu.cz)/SECOND_BRAIN/OBSIDIAN`

## Kdy spouštět

- "Co teď?" / "Co dnes?" / "Na co se mám zaměřit?"
- "Co je v agendě?" / "Ukaž mi dashboard"
- Začátek pracovního dne

## Načti data

V2 priority pořadí:

1. **`OBSIDIAN/00-System/agent-context.json`** (PRIMARY) — pre-rendered `top_priority` (top 15), `recently_done`, `upcoming_deadlines`, `recurring_pending`, `blocked_by_graph`. Pokud `generated_at` je starší než 24 h, spusť `python3 scripts/build_agent_context.py` před analýzou.
2. Fallback: parsuj všechny `OBSIDIAN/02-PROJEKTY/<slug>/tasks/*.md` frontmattery (file-per-task)
3. Backup: `OBSIDIAN/00-System/Dashboard.md` Bases embedy ukazují totéž — agent může otevřít

## Klasifikuj (z frontmatter status + deadline + waitUntil + ice)

- **PO TERMÍNU**: `deadline` < dnes && `status != Done`
- **DNES**: `deadline` = dnes
- **ASAP / Doing**: `status` = ASAP nebo Doing
- **TOP podle ICE**: `priority_score = (ice_i * ice_c) / ice_e` + bonusy:
  - +50 pokud `status` = ASAP
  - +30 pokud overdue
  - +15 pokud `deadline <= dnes + 2 dnů`
  - **bez Waiting**
- **WAITING**: `status = Waiting` && `waitUntil >= dnes` — zobraz zvlášť
- **BLOKOVANÉ**: `blocked_by != []` — kromě "nic"

## Vrať dashboard

```
═══════════════════════════════════════════════
CO TEĎ — DD/MM/YYYY
═══════════════════════════════════════════════

🔥 TOP 3 (z agent-context / ICE)
  • [slug/ID] název — status=ASAP deadline=…
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

- **`ukliď` / `clean`**:
  - Najdi task soubory v `02-PROJEKTY/<slug>/tasks/` se `status: Done`
  - Preview seznam → potvrzení
  - Přesuň do `07-ARCHIV/tasks-done/<slug>/<filename>` (cron `archive_done_tasks.py` to dělá automaticky, ale tady manuální verze)
  - Update `open_tasks_count` v hub `.md` frontmatteru
  - Po batchi spusť `python3 scripts/build_agent_context.py`
- **`detail <slug>`** → otevři `02-PROJEKTY/<HubName>.md` + briefing (Cíl, Scope, Kontext, Otevřené otázky, Aktivní úkoly)
- **`revize priorit`** → deleguj na skill `agenda-priority-review`

## Pravidla

- Nikdy neukládej bez explicitního příkazu
- Waiting nikdy v TOP 3
- Cesty: `02-PROJEKTY/<slug>/tasks/` (ne `AGENDA/`, ne H3 v hubu)
- Bases dashboard (`Dashboard.md`) je pro user oko, agent ho čte přes frontmatter parser
