# Agenda systém — build log

**Projekt**: vybudování systému pro sběr, třídění, strukturování a prioritizaci úkolů z různých zdrojů
**Datum**: 2026-04-28
**Status**: Fáze 1 hotová, Fáze 2 čeká na tokeny + setup

---

## Co bylo postaveno (Fáze 1 — done)

### Struktura složek

- ✅ `INBOX/` (sembly, slack, email, cowork-uploads, mobile, manual) + README
- ✅ `AGENDA/` + `_index.md` + `_ŠABLONA.md`
- ✅ `HOTOVO/2026-Q2/` + `HOTOVO/processed/` + README

### Skills (v `ŠABLONY/skills/`, instalace do `~/.claude/skills/`)

- ✅ `agenda-capture/SKILL.md`
- ✅ `agenda-triage/SKILL.md`
- ✅ `agenda-co-ted/SKILL.md`
- ✅ `ŠABLONY/skills/README.md` (instalace + test)

### Memory updates

- ✅ `O MNĚ/agenda-system.md` (referenční dokument)
- ✅ `O MNĚ/agenda-skill-cheatsheet.md` (quick reference)
- ✅ `O MNĚ/about-me.md` (drobný update v sekci Slabé stránky)

### Capture zdroje (pro rychlé použití hned)

- ✅ Cowork chat (paste / drop souboru) — funguje hned přes capture skill
- ✅ Manuální drop do `INBOX/manual/` — funguje hned

## Co je připravené pro Fázi 2 (čeká na tebe)

### n8n workflows v `ŠABLONY/n8n/`

- ✅ `sembly-to-cowork.json` (cron 30min poll, REST API, MD format, Drive save)
- ✅ `slack-reaction-capture.json` (Socket Mode, reakce :cowork:, Drive save)
- ✅ `email-to-cowork.json` (Gmail trigger na lukas.cypra+cowork@gmail.com)
- ✅ `README.md` (postup importu)

### Setup checklisty v `ŠABLONY/`

- ✅ `slack-app-setup-checklist.md` (vytvoření Slack appky, 9 kroků)
- ✅ `ios-shortcut-setup.md` (3 shortcuts: text, clipboard, voice)
- ✅ `email-forward-setup.md` (Gmail OAuth + plus-addressing)
- ✅ `sembly-md-template.md` (referenční šablona)

## Co potřebuji od tebe pro spuštění Fáze 2

| Co | K čemu |
|----|---------|
| Sembly API token | Workflow `sembly-to-cowork.json` |
| Info o Sembly webhoocích (umí to tvůj plán?) | Volba: cron vs webhook |
| Slack workspace URL + admin práva | Vytvoření Slack appky |
| Vytvoření Slack appky podle checklistu | Tokeny pro `slack-reaction-capture.json` |
| Custom emoji `:cowork:` ve Slacku | Reakce-trigger |
| Gmail OAuth pro n8n | `email-to-cowork.json` |
| Google Drive OAuth pro n8n | Všechny 3 workflows (Drive Save) |
| Folder IDs pro `INBOX/sembly/`, `INBOX/slack/`, `INBOX/email/` | n8n Drive nodes |

## Co dál

### Hned po dnešní session (5 min)

1. Nainstalovat skills do `~/.claude/skills/` podle `ŠABLONY/skills/README.md`
2. Restart Cowork session
3. Zkusit: *"Co teď?"* (mělo by spustit `agenda-co-ted`, hláška: "agenda prázdná")
4. Zkusit: *"Hoď do agendy: nápad — ReBeL přes Slack"* (mělo by spustit `agenda-capture`)

### Tento týden

1. n8n: importovat 3 workflows
2. Slack: postavit appku podle checklistu (≈ 15 min)
3. Sembly: vygenerovat API token, ověřit webhooks
4. Email: vyzkoušet plus-addressing
5. iOS: postavit 3 shortcuty (≈ 10 min)

### Až systém poběží 2–3 týdny

1. Re-evaluace: jaká témata vznikla organicky? Jsou rozumně velká, nebo příliš obecná/granulární?
2. Update `TOPIC_KEYWORDS` v Sembly + Email workflows podle reálných témat
3. Případně mind map view — Claude umí render mermaid; mohl by ti pravidelně generovat mind map agendy

## Otevřené body / nice-to-have (nezahrnuté ve Fázi 1+2)

- Whisper transkripce voice memo z mobilu (řešitelné dalším n8n workflow)
- Stahování e-mail příloh jako binárek vedle .md (rozšíření email workflow)
- Slack endpoint na "stáhni mi tenhle thread podle linku" (jde to, ale není priorita 1)
- Pravidelný mind map render agendy (ad-hoc na vyžádání zatím stačí)

---

**Soubory upravené v této session**: 24 (vč. update `about-me.md`)

**Pravidla, která jsem dodržel**:
- Před jakoukoli prací jsem přečetl `O MNĚ/about-me.md` a `O MNĚ/anti-ai-writing-tools.md`
- Nečetl jsem `ŠABLONY/lukas-writing-style.mdc` ani existující `VÝSTUPY/` (ledaže by user řekl)
- Tone podle anti-ai-writing-tools.md (informálně, bullet-points, žádné AI fráze)
- Výstupy do `VÝSTUPY/agenda-system-setup/` (tento log) podle podsložky pojmenované podle projektu
