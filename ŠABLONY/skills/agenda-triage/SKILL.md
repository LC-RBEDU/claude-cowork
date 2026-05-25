---
name: agenda-triage
description: "INBOX triage in MrLUC Second Brain v2 vault, pending batch approval from cron, or re-priority. Triggers: projeď inbox, schval pending triáž, apply batch, udělejme triage. Modes: BATCH, DEEP, PENDING (read 00-System/Triage-Pending/*.json with v2 schema). Creates task files in 02-PROJEKTY/<slug>/tasks/, archives to 07-ARCHIV/inbox-processed/. ALWAYS preview before write."
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

## Batch

1. Načti `01-INBOX/*/`
2. Pro každou položku: extrahuj, navrhni projekt + ICE + status (Next/ASAP/Backlog/Waiting)
3. Generuj ID (scan `02-PROJEKTY/<slug>/tasks/` + `07-ARCHIV/tasks-done/<slug>/`)
4. Preview všech položek najednou (skill agenda-capture struktura)
5. Po OK: zápis task `.md` souborů, archiv source → `07-ARCHIV/inbox-processed/YYYY/MM/`

### Odeslané e-maily (`01-INBOX/email/sent/`)

- Capture: n8n `workspace-sent-to-inbox.json` (Workspace `lukas@redbuttonedu.cz`, frontmatter `source: sent`)
- Cron `triage_run.py` + `triage_commitments.py`: závazky (`kind: commitment`) nebo fallback u mailu bez závazku
- Každý návrh v batchi má **`proposalType`**:
  - `add_task` — vytvoří `02-PROJEKTY/<slug>/tasks/<ID>-<slug>.md`
  - `update_task` — patchne frontmatter / body existujícího task souboru
  - `archive_only` — jen přesune source do archivu
- Souhrn: `00-System/Triage-Pending/YYYY-MM-DD-HHMM-summary.md` — české odrážky po souborech (typ, projekt, archiv po schválení)
- **`archiveAfterApply`**: default `true` — po schválení `add_task` z odeslaného mailu přesuň zdroj do `07-ARCHIV/inbox-processed/` + `**ZPRACOVÁNO**` v hlavičce
- PENDING: u commitmentů zkontroluj `notes` (citace) a `confidence`

## Deep

Pro každou položku: shrnutí, návrh projekta + frontmatter, OK/uprav/přeskoč/drop. Pak zápis a archiv.

## PENDING (cron)

1. Načti nejnovější `00-System/Triage-Pending/*-batch.json`
2. JSON v2 schema (každý návrh):

```json
{
  "proposalType": "add_task" | "update_task" | "archive_only",
  "target_path": "02-PROJEKTY/<slug>/tasks/<ID>-<slug>.md",
  "frontmatter": {
    "id": "RBU30",
    "type": "task",
    "project": "[[rb-universe-development]]",
    "slug": "rb-universe-development",
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
  "notes": "..."
}
```

3. Ukaž změny podle `proposalType`. **Nikdy neaplikuj bez explicitního "ano" / "apply"**
4. Po schválení:
   - `add_task` → vytvoř `target_path` se YAML frontmatterem + body
   - `update_task` → patchne frontmatter + append do body (CAS-aware)
   - `archive_only` → přesun source
   - Archiv batch: `00-System/Triage-Applied/`

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
