---
name: agenda-triage
description: "INBOX triage in MrLUC Second Brain v2 vault, pending batch approval from cron, or re-priority. Triggers: projeď inbox, schval pending triáž, apply batch, udělejme triage. Modes: BATCH, DEEP, PENDING (read 00-System/Triage-Pending/*.json with v2 schema). Creates task files in 02-PROJEKTY/<slug>/tasks/<ID> — <Title>.md (human-readable filename, em-dash U+2014; subtasks číslované **<ID>-N**), archives to 07-ARCHIV/inbox-processed/. ALWAYS preview before write."
---

# agenda-triage (v2)

> Pravidelný průchod nasbíraného. Capture ukládá rychle, triage pročistí. **V2:** vytváří `task .md` soubory v `02-PROJEKTY/<slug>/tasks/` (file-per-task), Bases dashboard se aktualizuje sám.

**Vault:** `OBSIDIAN/` — `/Users/lukascypra/My Drive (lukas@redbuttonedu.cz)/SECOND_BRAIN/OBSIDIAN`

## Kdy spouštět

- "Projeď inbox" / "udělejme triage" / "co tam mám nasbíráno"
- V `01-INBOX/*` je >5 nezpracovaných položek
- "Schval pending triáž" / "apply batch" → mód **PENDING**

## Módy

```
Mám N položek v INBOXu.
  [B]atch — rychlý souhrn, potvrzení najednou
  [D]eep — položka po položce
  [P]ending — schválení 00-System/Triage-Pending/*.json (cron návrh)
  [R]e-priority — delegace na agenda-priority-review

Default: B (nebo P pokud uživatel žádá pending).
```

## Auto-routing „komplexních" zdrojů

V BATCH i PENDING módu skill **automaticky** detekuje komplexní materiál a routuje ho do DEEP, místo aby ho mlel přes default add_task flow.

**Komplexní materiál** = ten, ze kterého se zákonitě bude rozsekávat víc tasků nebo se z něj stane samostatný materiál. Sdílená heuristika `vps/second-brain-hub/lib/triage_complexity.py` (volá ji i cron `triage_run.py`); pravidla v OR:

- Subdir `01-INBOX/sembly/` → **vždy** DEEP (přepisy meetingů).
- Subdir `01-INBOX/email/sent/` → **nikdy** DEEP (commitment fast-path).
- `word_count > 800` nebo `line_count > 100`.
- 3+ H2/H3 headingů v těle.
- 5+ otevřených checkboxů `- [ ]`.
- Signální fráze: „Action items", „Akční kroky", „Úkoly", „Závěry", „Decision points", „Rozhodnutí", „Next steps", „Další kroky".
- Override v souboru: `<!-- triage:deep -->` nebo `<!-- triage:simple -->` má precedenci přede vším ostatním.

Cron označuje takový návrh `requires_deep_analysis: true`, `kind: "deep"`, `proposalType: "deep_analysis"`, `target_path: null`, `frontmatter: null`, `body: "DEEP analysis required..."` a v summary `…-summary.md` přidává sekci **DEEP candidates** s důvody.

## Batch

1. Načti `01-INBOX/*/`
2. Pro každou položku zavolej **`is_complex_source(rel, body)`** (`vps/second-brain-hub/lib/triage_complexity.py`).
3. Komplexní zdroj → automaticky DEEP flow pro ten jeden zdroj (viz níže), zbytek dál v BATCH.
4. Pro non-DEEP položku: extrahuj, navrhni projekt + ICE + status (Next/ASAP/Backlog/Waiting)
5. Generuj ID (scan `02-PROJEKTY/<slug>/tasks/` + `07-ARCHIV/tasks-done/<slug>/`)
6. Preview všech BATCH položek najednou + výpis DEEP candidates (skill agenda-capture struktura)
7. Po OK: zápis task `.md` souborů, archiv source → `07-ARCHIV/inbox-processed/YYYY/MM/`

### Odeslané e-maily (`01-INBOX/email/sent/`)

- Capture: n8n `workspace-sent-to-inbox.json` (Workspace `lukas@redbuttonedu.cz`, frontmatter `source: sent`)
- Cron `triage_run.py` + `triage_commitments.py`: závazky (`kind: commitment`) nebo fallback u mailu bez závazku
- Každý návrh v batchi má **`proposalType`**:
  - `add_task` — vytvoří `02-PROJEKTY/<slug>/tasks/<ID> — <Title>.md` (em-dash U+2014, sanitized title) + frontmatter `aliases: [<ID>]` + očíslované subtasky `**<ID>-N**`
  - `update_task` — patchne frontmatter / body existujícího task souboru
  - `archive_only` — jen přesune source do archivu
- Souhrn: `00-System/Triage-Pending/YYYY-MM-DD-HHMM-summary.md` — české odrážky po souborech (typ, projekt, archiv po schválení)
- **`archiveAfterApply`**: default `true` — po schválení `add_task` z odeslaného mailu přesuň zdroj do `07-ARCHIV/inbox-processed/` + `**ZPRACOVÁNO**` v hlavičce
- PENDING: u commitmentů zkontroluj `notes` (citace) a `confidence`

## Deep

Pro každou položku (přímo spuštěnou v DEEP módu **nebo** auto-routnutou z BATCH/PENDING):

1. Read sourceFile naplno (ne jen prvních pár řádků).
2. Shrnutí 3–5 bullety: o čem to je, klíčové entity, decision points.
3. Návrh **více tasků** + případných **materiálů** + cross-linků (`materials: [[...]]`).
4. Projdi s uživatelem po jednom: OK / uprav / přeskoč / drop.
5. Zápis task `.md` + materiál `.md` souborů; archiv source → `07-ARCHIV/inbox-processed/YYYY/MM/`.

## PENDING (cron)

1. Načti nejnovější `00-System/Triage-Pending/*-batch.json`.
2. Rozděl proposals na **2 fronty**:
   - `simple_queue` — `requires_deep_analysis != true` (default BATCH apply route).
   - `deep_queue` — `requires_deep_analysis == true` (`kind: "deep"`, `proposalType: "deep_analysis"`).
3. Pokud `deep_queue` není prázdná, řekni uživateli:
   > Nalezeno N návrhů (M simple, K DEEP). Začneme DEEP, protože vyžadují víc pozornosti. Pokračovat? [yes/skip-deep/simple-only]
4. **DEEP fronta**: pro každý zdroj projet DEEP analysis flow s pre-loaded `sourceFile` z Pending JSONu. Po schválení DEEP zápisu:
   - Smazat ten proposal z Pending JSONu (CAS write s `expect_mtime`).
   - Přesunout zdroj do `07-ARCHIV/inbox-processed/YYYY/MM/`.
5. **Simple fronta**: stávající BATCH apply (per-proposal `proposalType`).
6. JSON v2 schema (každý návrh):

```json
{
  "proposalType": "add_task" | "update_task" | "archive_only" | "deep_analysis",
  "target_path": "02-PROJEKTY/<slug>/tasks/<ID> — <Title>.md",
  "frontmatter": {
    "id": "RBU30",
    "type": "task",
    "title": "Titulek lidsky čitelný",
    "project": "[[RB Universe]]",
    "slug": "rb-universe-development",
    "aliases": ["RBU30"],
    "status": "Next",
    "ice_i": 7, "ice_c": 8, "ice_e": 5,
    "materials": ["[[some-material]]"],
    "source": "...",
    "deadline": null,
    "waitUntil": null
  },
  "body": "...",
  "sourceFile": "01-INBOX/...",
  "archiveAfterApply": true,
  "confidence": 0.85,
  "notes": "...",
  "requires_deep_analysis": false,
  "deep_reasons": []
}
```

Body návrhu musí mít subtasky se prefixem `**<ID>-N**` v `## Operativní kroky`.

7. Ukaž změny podle `proposalType`. **Nikdy neaplikuj bez explicitního „ano" / „apply"**.
8. Po schválení:
   - `add_task` → vytvoř `target_path` se YAML frontmatterem + body.
   - `update_task` → patchne frontmatter + append do body (CAS-aware).
   - `archive_only` → přesun source.
   - `deep_analysis` → **nikdy se neaplikuje automaticky**; přepni do DEEP flow (krok 4) pro daný `sourceFile`.
   - Archiv batch: `00-System/Triage-Applied/`.

## Refresh dashboard + agent context

V2 — žádný cron build pro dashboard nepotřebuje. **Bases dashboard** (`OBSIDIAN/00-System/Dashboard.md`) čte přímo z task `.md` frontmatterů.

**Po každém zápisu** (apply triage batch / commit task changes):

1. (Volitelně) update `open_tasks_count` v hub `.md` frontmatteru pro každý dotčený slug
2. **Vždy spusť** `python3 scripts/build_agent_context.py` (vault root) — refresh `00-System/agent-context.json` pro Cursor agenta
3. V chatu uveď výsledek: `tasks_created=N tasks_updated=M archived=K agent_context_refreshed=yes`

## Refresh Index

Po triage update `00-System/Index.md` — list aktivních projektů (Bases embed udělá většinu, manuální texty doplň pokud potřeba).

## Re-prioritizace

"Eisenhower přepočítej" → skill `agenda-priority-review` nebo projdi aktivní task soubory (po termínu, ASAP dnes, Next top 3).

## Kontext před startem

- `00-System/Memory/about-me.md`
- `00-System/Index.md`
- `00-System/Templates/konvence-a-slovnik.md`
- `00-System/Templates/task-convention.md`
