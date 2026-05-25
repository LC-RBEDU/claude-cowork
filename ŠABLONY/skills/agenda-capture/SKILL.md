---
name: agenda-capture
description: "Capture into MrLUC Second Brain v2 vault: paste, files, or new files in OBSIDIAN/01-INBOX/. Creates task files in 02-PROJEKTY/<slug>/tasks/<ID>-<slug>.md (file-per-task + frontmatter), archives source to 07-ARCHIV/inbox-processed/. Triggers: capture, zapiš si, INBOX. ALWAYS preview before write. Preserve subtask checklisty + source links."
---

# agenda-capture (v2)

> Bere libovolný střípek a integruje ho do živého systému jako **soubor-per-task** v `02-PROJEKTY/<slug>/tasks/`.

**Vault (SSOT):** `OBSIDIAN/` v repo `SECOND_BRAIN` (Google Drive).
Cesta: `/Users/lukascypra/My Drive (lukas@redbuttonedu.cz)/SECOND_BRAIN/OBSIDIAN`

## Architektura v2 (povinný kontext)

- **TASK** = vlastní `.md` v `02-PROJEKTY/<slug>/tasks/<ID>-<slugify(title)>.md` se YAML frontmatterem (SSOT) a body s checkboxy.
- **PROJECT HUB** = `02-PROJEKTY/<HubName>.md` s charter sekcemi a embedy `![[All-tasks.base#ProjectKanban]]` (Bases plugin).
- **MATERIAL** = `02-PROJEKTY/<slug>/materials/<title>.md` (project-specific) nebo `05-RESOURCES/<kategorie>/<title>.md` (cross-project), s frontmatter `projects:` array (M:N).
- Konvence: `OBSIDIAN/00-System/Templates/konvence-a-slovnik.md`, `task-convention.md`, `task-template.md`, `material-template.md`, `id-generation-spec.md`, `filename-normalization.md`.

## Kdy spouštět

- Uživatel paste-ne text do chatu
- V chatu se objeví soubor (PDF, .docx, .xlsx, .png, audio)
- Nové soubory v `01-INBOX/{slack,sembly,email,email/sent,daily}/` (n8n → Drive)
- "zapiš si", "hoď to k tématu X", "rozhoď to", "máš tam něco v inboxu?"

## Workflow

### 1. Načti kontext

1. Přečti `OBSIDIAN/00-System/Memory/about-me.md` (1× per session)
2. Přečti `OBSIDIAN/00-System/Index.md` (existující projekty)
3. Při čtení INBOXu: `01-INBOX/*/` soubory novější než archiv v `07-ARCHIV/inbox-processed/`

### 2. Vytěž obsah podle zdroje

- **Text v chatu** → ber jak je
- **PDF / .docx / .xlsx** → extrakce textu
- **Obrázek** → vision + OCR
- **Audio** → transkripce; jinak požádej o text
- **INBOX/sembly/** → markdown ze Sembly
- **INBOX/slack/** → markdown z n8n
- **INBOX/email/** → markdown z n8n (forward); přílohy vedle .md otevři zvlášť
- **INBOX/email/sent/** → odeslané z Workspace (`source: sent`); hledej Lukášovy sliby/úkoly

### 3. Rozsekej na položky

- Akční bod → **task soubor** v `02-PROJEKTY/<slug>/tasks/`
- Nápad bez akce → task se status `Backlog`
- Otázka / čeká na odpověď → projektový hub `## Otevřené otázky`
- Kontext bez akce → **material soubor** v `02-PROJEKTY/<slug>/materials/` nebo `05-RESOURCES/`

### 4. Navrhni projekt (slug)

- Projdi `02-PROJEKTY/*.md` (frontmatter `slug` + `aliases`)
- Sembly `Suggested topic:` jako default

### 5. Generuj ID a filename

- **ID:** scanuj `02-PROJEKTY/<slug>/tasks/*` + `07-ARCHIV/tasks-done/<slug>/*`, najdi max ID s prefixem (S, AF, F, RBU, …), použij `+1`. Algoritmus: `00-System/Templates/id-generation-spec.md`.
- **Filename:** `<ID>-<slugify(title)>.md` (max 50 chars, latin-only, kebab-case dle `filename-normalization.md`).

### 6. Frontmatter (povinný)

```yaml
---
id: <ID>
type: task
project: "[[<slug>]]"
slug: <slug>
status: Next | ASAP | Backlog | Waiting | Doing | Done
ice_i: <1-10>
ice_c: <1-10>
ice_e: <1-10>
deadline: <YYYY-MM-DD or empty>
waitUntil: <YYYY-MM-DD or empty>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
materials:
  - "[[<material-slug-or-filename>]]"
source: "<zdroj — Slack/Sembly/email/manual>"
blocked_by: []
---
```

### 7. Body šablony

```markdown
# <ID> — <Title>

**Z:** <zdroj s link>
**Detail:** <kontext z capture>

## Operativní kroky
- [ ] <subtask 1>
- [ ] <subtask 2>

## Poznámky / log
- <YYYY-MM-DD>: <poznámka>
```

### 8. Preview PŘED zápisem

```
## Návrh capture (X položek z [zdroj])

### → 02-PROJEKTY/rb-universe-development/tasks/RBU30-...md (NEW)
- Status: Next | ICE I8 C7 E4 (Score 14.0)
- Detail: ...

### → 02-PROJEKTY/<slug>/materials/<title>.md (NEW material)
- ...

OK? (ano / uprav / vyhoď)
```

### 9. Zapiš a archivuj

- Vytvoř task soubor v `02-PROJEKTY/<slug>/tasks/`
- Vytvoř material soubor v `02-PROJEKTY/<slug>/materials/` nebo `05-RESOURCES/<kategorie>/`
- Po vytvoření **inkrementuj** `open_tasks_count` v hub `.md` frontmatteru
- Originál z INBOX → `07-ARCHIV/inbox-processed/YYYY/MM/<den>-<filename>`
- V hubu odkaz na archiv v Materiálech (nebo nech projít přes triage)
- **Bases dashboard** se sám zaktualizuje při dalším otevření `Dashboard.md` — žádný cron build potřeba.

### 10. Refresh agent context (povinné)

Po každém zápisu spusť:
```bash
python3 scripts/build_agent_context.py
```

Aktualizuje `00-System/agent-context.json` — Cursor agent (s always-applied bootstrap rule) ho čte při dalších promptech.

### 11. Hláška

Krátká, akční: kolik task souborů, do kterých projektů, top ASAP/Q1 pokud je.

## Speciální případy

- Nejasný obsah → jedna cílená otázka
- ASAP s deadline today → explicitně v hlášce
- Smalltalk → neukládat
- Citlivá data → potvrzení před zápisem

## Tone

`OBSIDIAN/00-System/Memory/anti-ai-writing-tools.md`
