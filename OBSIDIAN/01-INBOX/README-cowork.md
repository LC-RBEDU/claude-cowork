# INBOX — capture zóna

Sem padá vše neroztříděné. Pravidlo: do INBOXu nikdy nečteš *retro* ručně, vždycky to projedeme přes skill `agenda-triage` (viz `00-System/Memory/agenda-skill-cheatsheet.md`).

## Podsložky

- **`sembly/`** — automatický import transkriptů z Sembly (n8n workflow)
- **`slack/`** — zprávy z **jednoho Slack capture kanálu** (n8n: nová zpráva → `.md`)
- **`email/`** — e-maily přeposlané na `lukas.cypra+cowork@gmail.com` (n8n Gmail trigger)
- **`daily/`** — ruční zápisky, mobilní capture (iOS Shortcut), paste uložený přes `agenda-capture`

## Naming convention

`YYYY-MM-DD-<typ>-<kratky-popis>.md` — datum kdy přišlo, ne kdy se to stalo.

Příklady:
- `2026-04-28-sembly-strategy-mtg.md`
- `2026-04-28-slack-finance-fakturace.md`
- `2026-05-20-daily-napad-rb-universe.md`

## Životní cyklus položky

1. **Přistane v INBOXu** (z libovolného zdroje)
2. **Triage** — `agenda-triage` skill ji roztřídí do `02-PROJEKTY/<téma>.md` s metadaty
3. **Originál** → `07-ARCHIV/inbox-processed/YYYY/MM/<typ>/` (audit trail)
