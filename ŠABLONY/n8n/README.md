# n8n workflows pro Agenda systém

4 workflows. Každý je samostatný JSON, importovatelný do n8n.

## Google Drive — MrLUC INBOX

| | |
|--|--|
| **INBOX root** | [01-INBOX](https://drive.google.com/drive/u/0/folders/1ZaWrGl9DktNsu4K8KQZzqo2JWPtb7-ur) |
| **Folder ID (root)** | `1ZaWrGl9DktNsu4K8KQZzqo2JWPtb7-ur` |
| **Podsložky** | `slack/`, `sembly/`, `email/`, `uploads/`, `manual/` — každá má **vlastní** folder ID v URL |

Po přesunu INBOXu na Drive zkopíruj ID z URL každé podsložky do příslušného workflow (node „Save to Drive“ → `folderId`).  
Šablony používají placeholdery `REPLACE_WITH_INBOX_*_FOLDER_ID` — v produkční n8n instanci už máš nastaveno v UI.

## Workflows

| Soubor | Co dělá | Čeká na |
|--------|---------|---------|
| `sembly-to-cowork.json` | **Webhook** z Sembly → `.md` do `01-INBOX/sembly/` | Veřejná n8n URL, Drive credential, folder ID sembly |
| `slack-reaction-capture.json` | Nová zpráva v capture kanálu → `.md` → `01-INBOX/slack/` | Slack + Drive; viz `slack-app-setup-checklist.md` |
| `email-to-cowork.json` | Gmail `to:lukas.cypra+cowork@gmail.com` → `01-INBOX/email/` | Gmail + Drive; přílohy do stejné nebo `email-attachments` podsložky |
| `mobile-capture-to-cowork.json` | Webhook iOS → `01-INBOX/manual/` | Drive folder ID pro `manual/` |

## Společné předpoklady

- n8n self-hosted
- **Google Drive credential** — cíl = `MrLUC/01-INBOX/<podsložka>/` na Drive (sync s iCloud vaultem; SSOT Obsidian MrLUC)
- Slack: jen inbound capture

## Postup importu

1. n8n → Workflows → Import from File
2. Nastav credentials na triggerech a Drive nodech
3. U každého „Save to Drive“ ověř `folderId` = konkrétní podsložka pod root `1ZaWrGl9DktNsu4K8KQZzqo2JWPtb7-ur`
4. Activate workflow

## VPS triage

Cron na **coolify-dev** čte `/data/mrluc/01-INBOX/{slack,sembly,email,uploads,manual}/` — sync vaultu viz `vps/second-brain-hub/README.md`.
