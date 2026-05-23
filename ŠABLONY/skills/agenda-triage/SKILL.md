---
name: agenda-triage
description: "INBOX triage in MrLUC vault, pending batch approval from cron, or re-priority. Triggers: projeď inbox, schval pending triáž, apply batch, udělejme triage. Modes: BATCH, DEEP, PENDING (read 00-System/Triage-Pending/*.json). Updates 02-PROJEKTY/<slug>.md, 00-System/Index.md, archives to 07-ARCHIV/inbox-processed/. ALWAYS preview before write."
---

# agenda-triage

> Pravidelný průchod nasbíraného. Capture ukládá rychle, triage pročistí.

**Vault:** `OBSIDIAN/` — `/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN`

## Kdy spouštět

- „Projeď inbox“ / „udělejme triage“ / „co tam mám nasbíráno“
- V `01-INBOX/*` je >5 nezpracovaných položek
- „Schval pending triáž“ / „apply batch“ → mód **PENDING**

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
2. Extrahuj, navrhni téma + ICE + kvadrant
3. Preview jako v `agenda-capture`
4. Po OK: zápis do `02-PROJEKTY/`, archiv, Index

### Odeslané e-maily (`01-INBOX/email/sent/`)

- Capture: n8n `workspace-sent-to-inbox.json` (Workspace `lukas@redbuttonedu.cz`, frontmatter `source: sent`)
- Cron `triage_run.py` + `triage_commitments.py`: závazky (`kind: commitment`) nebo fallback u mailu bez závazku
- Každý návrh v batchi má **`proposalType`**: `add_task` (vytažení úkolu) | `update_task` (změna stavu) | `archive_only` (jen HOTOVO)
- Souhrn: `00-System/Triage-Pending/YYYY-MM-DD-HHMM-summary.md` — české odrážky po souborech (typ, projekt, archiv po schválení)
- **`archiveAfterApply`**: default `true` u INBOX položek — po schválení `add_task` z odeslaného mailu přesuň zdroj do `07-ARCHIV/inbox-processed/` + `**ZPRACOVÁNO**` v hlavičce
- Bez závazku: `archive_only` (informační/uzavírací mail) **nebo** `add_task` při heuristice ukončení smlouvy/služby (např. Ninjabot → `pipedrive-a-dalsi-nastroje`)
- PENDING: u commitmentů zkontroluj `notes` (citace) a `confidence`; u `archive_only` stačí schválit archiv

## Deep

Pro každou položku: shrnutí, návrh tématu/metadata, OK/uprav/přeskoč/drop.

## PENDING (cron)

1. Načti nejnovější `00-System/Triage-Pending/*-batch.json` + `*-summary.md`
2. Ukaž změny podle `proposalType` (Vytažení úkolu / Změna stavu / Přesun do HOTOVO). U commitmentů: `confidence` + citace v `notes`. Vypršené **Waiting** → `build_dashboard.py` (hub **ASAP**); staré `waiting_expired` batch jen archivuj.
3. **Nikdy neaplikuj bez explicitního „ano“ / „apply“**
4. Po schválení: hub `.md` pro `add_task`/`update_task`; u položek s `archiveAfterApply` archivuj `sourceFile` do `07-ARCHIV/inbox-processed/`; batch → `Triage-Applied/`; volitelně rebuild dashboard

## Refresh Index

Po triage: pro každý `02-PROJEKTY/<slug>.md` aktivní úkoly, top Score, last update → tabulka v `00-System/Index.md`.

## Re-prioritizace

„Eisenhower přepočítej“ → skill `agenda-priority-review` nebo projdi aktivní úkoly (po termínu, Q1 dnes, Q2 top 3).

## Kontext před startem

- `00-System/Memory/about-me.md`
- `00-System/Index.md`
