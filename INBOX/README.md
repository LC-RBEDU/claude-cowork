# INBOX — capture zóna

Sem padá vše neroztříděné. Pravidlo: do INBOXu nikdy nečteš *retro* ručně, vždycky to projedeme přes skill `agenda-triage` (viz O MNĚ/agenda-skill-cheatsheet.md).

## Podsložky

- **`sembly/`** — automatický import transkriptů z Sembly (n8n workflow)
- **`slack/`** — zprávy z **jednoho Slack capture kanálu** (n8n: nová zpráva → `.md`; typicky forward z DM / jiných míst)
- **`email/`** — e-maily přeposlané na `lukas.cypra+cowork@gmail.com` (n8n Gmail trigger)
- **`cowork-uploads/`** — soubory/obrázky/screenshoty hozené do Cowork chatu
- **`mobile/`** — položky z mobilu (iOS Shortcut do Google Drive)
- **`manual/`** — vše, co sem hodíš ručně (nebo paste do chatu, který Claude uloží sem)

## Naming convention

`YYYY-MM-DD-<typ>-<kratky-popis>.md` — datum kdy přišlo, ne kdy se to stalo.

Příklady:
- `2026-04-28-sembly-strategy-mtg.md`
- `2026-04-28-slack-finance-fakturace.md`
- `2026-04-28-cowork-screenshot-pipedrive-bug.md`

## Životní cyklus položky

1. **Přistane v INBOXu** (z libovolného zdroje)
2. **Triage** — `agenda-triage` skill ji roztřídí do `AGENDA/<téma>.md` s metadaty (kvadrant, ICE, návrat)
3. **Originál** se po zpracování přesune do `HOTOVO/processed/<rok>/` (audit trail), v INBOXu nezůstává
