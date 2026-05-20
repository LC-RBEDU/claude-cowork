# Vault na Google Drive (migrace 2026-05-20)

## SSOT — pouze složka OBSIDIAN

**Obsidian vault** (otevři jako root):

```
/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN
```

**Repo / automatizace** (mimo vault):

```
/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/
├── OBSIDIAN/     ← jediný Obsidian root
├── vps/
├── scripts/
└── ŠABLONY/
```

| V OBSIDIAN | Účel |
|------------|------|
| `Home.md` | Domovská stránka |
| `01-INBOX/{slack,sembly,email,daily}/` | Capture — cíl **n8n** |
| `02-PROJEKTY/` | Úkoly a projekty |
| `00-System/` | Dashboard, JSON, triage-pending |
| `07-ARCHIV/` | Zpracovaný INBOX |

## Co je potřeba od tebe

### 1. Obsidian

- **Open folder as vault** → cesta **`…/SECOND_BRAIN/OBSIDIAN`** (ne celý SECOND_BRAIN)
- Zavři starý iCloud MrLUC (záloha, nesmaž hned)
- **Obsidian Sync** — na složku `OBSIDIAN`

### 2. n8n (Slack, Sembly, E-mail)

Folder ID v Google Drive pro:

| Podsložka | Cesta |
|-----------|--------|
| slack | `SECOND_BRAIN/OBSIDIAN/01-INBOX/slack/` |
| sembly | `SECOND_BRAIN/OBSIDIAN/01-INBOX/sembly/` |
| email | `SECOND_BRAIN/OBSIDIAN/01-INBOX/email/` |

Staré cíle (`SECOND_BRAIN_INBOX`, kořenové `INBOX/` na jiném účtu) nepoužívat.

### 3. VPS

Po rclone: sync celé `OBSIDIAN/` → `/data/mrluc/` (layout stejné jako vault root).

### 4. Terminál

```bash
export VAULT_PATH="/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN"
unset LEGACY_TASKS
```
