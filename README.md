# SECOND_BRAIN — repo (automatizace)

Git + tooling kolem Obsidian vaultu. **Vault (poznámky) není v kořeni repa.**

## Obsidian vault (SSOT)

```
/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN
```

| Složka | Účel |
|--------|------|
| `Home.md`, `01-INBOX/`, `02-PROJEKTY/`, … | Second Brain v Obsidianu |
| `vps/`, `scripts/`, `ŠABLONY/`, `.cursor/` | Jen v **kořeni repa** — neotevírat ve vaultu |

Migrace / n8n: `OBSIDIAN/00-System/Memory/vault-gdrive-migration.md`

**Mimo vault (repo kořen):** `ŠABLONY/` (n8n, skills). Kontext pro agenty: `OBSIDIAN/00-System/Memory/`.

## Příkazy

```bash
export VAULT_PATH="/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/OBSIDIAN"
unset LEGACY_TASKS
cd "/Users/lukascypra/My Drive - PRV/# WORK/SECOND_BRAIN/vps/second-brain-hub"
python3 cron/sync_tasks_from_projekty.py --force && python3 cron/build_dashboard.py
```

Dashboard: `OBSIDIAN/00-System/Dashboard.html`

## Git

Viz `.gitignore` — generované soubory pod `OBSIDIAN/00-System/`.
