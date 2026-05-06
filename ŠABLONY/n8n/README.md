# n8n workflows pro Agenda systém

4 workflows. Každý je samostatný JSON, importovatelný do n8n.

## Workflows

| Soubor | Co dělá | Čeká na |
|--------|---------|---------|
| `sembly-to-cowork.json` | **Webhook** z Sembly Custom Automation → .md na Drive (POST, path `sembly-cowork-transcript`) | Veřejná n8n URL, Google Drive credential |
| `slack-reaction-capture.json` | **Nová zpráva** v jednom kanálu (typicky private capture) → `.md` na Drive → po uložení **✅** k původní zprávě | Slack credential + ID kanálu + `message.groups`/`message.channels` + scope `reactions:write` (viz `slack-app-setup-checklist.md`) |
| `email-to-cowork.json` | Pollne Gmail s filtrem `to:lukas.cypra+cowork@gmail.com`, ukládá jako .md + **vloží text exportu** z odkazů Google Docs/Sheets/Slides (Drive API); paralelně **nahraje přílohy** (PDF atd.) přes „Drive: Upload příloh“ | Gmail OAuth + **stejný Drive OAuth i na Code nodu** „Format → Markdown“; **Gmail trigger: Simplify OFF**; druhá Drive složka `REPLACE_WITH_FOLDER_ID_OF_INBOX_EMAIL_ATTACHMENTS` (nebo stejné ID jako u .md) |
| `mobile-capture-to-cowork.json` | **Webhook** z iOS Shortcutů (POST, path `cowork-mobile-capture`) → .md do `INBOX/mobile/` | Google Drive credential + ID složky `INBOX/mobile/`. Setup viz `ŠABLONY/ios-shortcut-setup.md` |

## Společné předpoklady

- n8n self-hosted (potvrzeno v O MNĚ/about-me.md)
- **Google Drive credential** v n8n s přístupem do Cowork složky (servisní účet nebo OAuth na `lukas@redbuttonedu.cz`)
- Cílová Drive cesta = `CLAUDE COWORK/INBOX/<podsložka>/`

## Postup importu

1. V n8n → Workflows → Import from File → vyber JSON
2. Otevři workflow → klikni na první ikonku (input/trigger) → nastav credentials
3. Otevři "Google Drive" / "Save to Drive" node → ověř, že parent folder = Cowork `INBOX/<podsložka>/` (folder ID najdeš v Drive URL)
4. Activate workflow

## Tipy

- Začni se Sembly (nejjednodušší, nejméně závislostí)
- Slack potřebuje vytvořenou appku (postupuj podle `slack-app-setup-checklist.md`)
- Email potřebuje jen Gmail OAuth, nicméně **filter** musíš ověřit, ať to nesype úplně všechno
- Mobile capture: po Activate zkopíruj Production URL z Webhook nodu do iOS Shortcutů (návod v `ios-shortcut-setup.md`); zvaž basic auth, je to veřejný endpoint
