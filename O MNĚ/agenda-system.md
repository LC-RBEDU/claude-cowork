# Agenda systém — referenční dokument

> Living document. Popisuje, jak funguje **Lukášův task & idea management systém** postavený nad Cowork složkou. Pro Claude: čti vždy, když se v session řeší cokoli kolem úkolů, nápadů, INBOXu, AGENDY, capture nebo priorit.

**Vznik**: 2026-04-28
**Status**: aktivní

---

## Proč

Z `about-me.md`: slabá střední/projektová vrstva, žádné review, otevřené smyčky vyčerpávají. Apple Reminders nestačí — chybělo místo, kam zachytit **rozdělané věci, nápady, požadavky** s kontextem (zdroj, blokátory, kdy se vrátit).

Systém řeší pětiboj: **Capture → Třídění → Strukturování → Prioritizace → Návrat**.

---

## Architektura

```
CLAUDE COWORK/
├── O MNĚ/                      ← memory (Claude čte před každým úkolem)
│   ├── about-me.md
│   ├── anti-ai-writing-tools.md
│   ├── agenda-system.md        ← TENTO SOUBOR
│   └── agenda-skill-cheatsheet.md
│
├── ŠABLONY/
│   ├── lukas-writing-style.mdc
│   ├── skills/                 ← agenda-capture, -triage, -co-ted (instalují se do ~/.claude/skills/)
│   ├── n8n/                    ← workflow JSONy pro Sembly + Slack
│   ├── slack-app-setup-checklist.md
│   ├── ios-shortcut-setup.md
│   └── sembly-md-template.md
│
├── INBOX/                      ← capture zóna
│   ├── sembly/   slack/   cowork-uploads/   email/   manual/
│
├── AGENDA/                     ← strukturovaná, živá témata
│   ├── _index.md
│   ├── _ŠABLONA.md
│   └── <slug>.md               ← roste organicky
│
├── HOTOVO/                     ← uzavřené tvary
│   ├── 2026-Q2/    └── processed/
│
└── VÝSTUPY/                    ← klasické deliverables (nesouvisí přímo s agendou)
```

---

## Capture zdroje

| Zdroj | Jak to padá | Kam |
|-------|-------------|-----|
| Paste do Cowork chatu | Claude rozpozná "tohle je capture" → `agenda-capture` skill | `INBOX/manual/` (nepřímo, přes skill rovnou do AGENDY) |
| Drop souboru/screenshotu do chatu | Claude vytěží obsah (vision/text) → `agenda-capture` | `INBOX/cowork-uploads/` (originál archivován) |
| Sembly transkript | n8n workflow `sembly-to-cowork` (cron / webhook) | `INBOX/sembly/YYYY-MM-DD-HHMM-title.md` |
| Zpráva v **Slack capture kanálu** (forward / nový příspěvek) | n8n workflow `slack-reaction-capture` (Socket Mode, trigger „nová zpráva“) | `INBOX/slack/YYYY-MM-DD-channel-snippet.md` |
| Forward e-mailu na `lukas.cypra+cowork@gmail.com` | n8n Gmail trigger | `INBOX/email/YYYY-MM-DD-HHMM-from-subject.md` |
| Manuál | ručně hozený soubor / paste přes chat | `INBOX/manual/...` |

---

## Témata v AGENDA/

- Vznikají **organicky** podle toho, co padá do INBOXu
- **Slug** = kebab-case bez diakritiky (`rb-universe`, `ceo-reporting`, `interni-pravidla-vydaje`)
- Každé téma má vlastní soubor `AGENDA/<slug>.md` podle `AGENDA/_ŠABLONA.md`
- Sekce v souboru:
  - **Kontext** — proč téma existuje, cíl
  - **Aktivní úkoly** — s metadaty (kvadrant, ICE, vrátit se, blokováno)
  - **Backlog** — nápady, ne aktivní
  - **Otevřené otázky / čeká na data** — typicky věci od CEO
  - **Materiály a poznámky** — kontext, screenshoty, citace
  - **Recently moved to HOTOVO** — co se nedávno dotáhlo

---

## Prioritizace

**Eisenhower (1. průchod)**:
- Q1 = Urgentní + Důležité → dělej teď
- Q2 = Důležité, ne urgentní → naplánuj (zde dává smysl ICE)
- Q3 = Urgentní, ne důležité → deleguj nebo škrtni
- Q4 = Ani urgentní, ani důležité → backlog / drop

**ICE (2. průchod, hlavně Q2)**:
- Impact 1–10
- Confidence 1–10
- Effort 1–10 (pozor: 10 = málo práce, 1 = hodně — aby šla jednotka nahoru)
- **Score** = (I × C) / E

Položka v AGENDA souboru:
```
- [ ] **[Q2, ICE 8/7/4, S=14]** Krátký akční titulek
  - Z: Sembly 28/4
  - Vrátit se: 2026-05-05
  - Blokováno: nic
  - Detail: 1–3 věty
```

---

## Skills (popis)

4 skills v `ŠABLONY/skills/`, instalují se do `~/.claude/skills/` (viz `ŠABLONY/skills/README.md`):

- **`agenda-capture`** — bere střípky odkudkoli, vytěží, navrhne téma + metadata, ukládá. Vždy preview před zápisem.
- **`agenda-triage`** — projetí INBOXu, batch nebo deep mód. Refresh `_index.md`.
- **`agenda-co-ted`** — dashboard "co dnes". Subcommands: `ukliď`, `detail <slug>`, `urgent <slug>`, `odlož <slug>`.
- **`agenda-work`** — work session nad konkrétním tématem. Čte AGENDA/<slug>.md + VÝSTUPY/<slug>/, tvoří nebo aktualizuje výstupy (dokumenty, mindmapy, kalkulace, skripty, MCPs), aktualizuje úkoly v tématu. Vždy preview před zápisem.

Detail viz `O MNĚ/agenda-skill-cheatsheet.md`.

---

## Externí automatizace

- **n8n self-hosted** — pohání Sembly + Slack capture
- Workflow JSONy v `ŠABLONY/n8n/` — naimportuj + nastav credentials
- Setup checklist:
  - `ŠABLONY/slack-app-setup-checklist.md` (vytvoření Slack appky)
  - `ŠABLONY/ios-shortcut-setup.md` (iOS Shortcut do Google Drive)
  - `ŠABLONY/sembly-md-template.md` (formát MD souboru z Sembly)

---

## Pravidla pro Claude (DŮLEŽITÉ)

1. **Před capture/triage vždy přečti `O MNĚ/about-me.md` + `AGENDA/_index.md`** — znát kontext + existující témata
2. **Nikdy neukládej do AGENDA bez preview** — uživatel musí mít možnost upravit/škrtnout
3. **Originály po zpracování přesunout do `HOTOVO/processed/`** — ne smazat
4. **Při vzniku nového tématu update i `AGENDA/_index.md`**
5. **Tone**: viz `O MNĚ/anti-ai-writing-tools.md` — informálně, bullet-points, konkrétně, žádné AI fráze
6. **Když uživatel řekne "dej to do agendy" / "zapiš si" / "co teď?" / "projeď inbox"** — automaticky spusť odpovídající skill, nečekej na explicitní instrukci

---

## Změnový log

- **2026-04-28**: vznik systému (struktura, šablony, 3 skills, memory). Phase 2 (n8n + iOS) připravena, čeká na tokeny a setup.
- **2026-04-29**: Slack capture přepnut z reakce `:cowork:` na **nové zprávy v jednom capture kanálu** (jednotný postup s forwardem z DM).
- **2026-04-30**: n8n workflows rozběhány (Sembly, Slack, email, iOS). Přidán 4. skill `agenda-work` — work session pro tvorbu a aktualizaci výstupů (dokumenty, mindmapy, kalkulace, skripty, MCPs) a správu úkolů v tématu.
- **2026-05-04**: Zrušen mobile capture (iOS Shortcut). Diktování přesunuto přímo do Slack capture kanálu. Smazat ručně: `INBOX/mobile/`, `ŠABLONY/n8n/mobile-capture-to-cowork.json`, `ŠABLONY/ios-shortcut-setup.md` a n8n workflow z instance.
