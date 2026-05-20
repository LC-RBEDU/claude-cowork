# Agenda systém — referenční dokument

> Living document. Task & idea management nad **Obsidian vault** `OBSIDIAN/` na Google Drive. Repo `SECOND_BRAIN/` = tooling (`vps/`, `ŠABLONY/`, `scripts/`).

**Vznik**: 2026-04-28 · **Migrace MrLUC + Drive**: 2026-05-20

---

## Proč

Z [[about-me]]: slabá střední vrstva, otevřené smyčky. Systém: **Capture → Třídění → Strukturování → Prioritizace → Návrat**.

---

## Architektura (aktuální)

```
SECOND_BRAIN/                          ← git repo (mimo Obsidian)
├── OBSIDIAN/                          ← Obsidian vault root (SSOT poznámky)
│   ├── Home.md
│   ├── 01-INBOX/{slack,sembly,email,daily}/
│   ├── 02-PROJEKTY/<slug>.md + <slug>/
│   ├── 00-System/{Index, Triage-Pending, weekly, Memory/}
│   └── 07-ARCHIV/inbox-processed/
├── ŠABLONY/{skills,n8n}/             ← zdroj skills + workflow JSON
└── vps/second-brain-hub/              ← cron, dashboard build
```

Detail cest: [[vault-gdrive-migration]], [[Jak čtu vault MrLUC]].

---

## Capture

| Zdroj | Jak | Kam |
|-------|-----|-----|
| Slack capture kanál | n8n `SECOND BRAIN: Slack -> INBOX` | `01-INBOX/slack/` |
| Sembly | n8n webhook | `01-INBOX/sembly/` |
| E-mail `lukas.cypra+cowork@gmail.com` | n8n Gmail | `01-INBOX/email/` |
| Paste / chat / mobil později | `agenda-capture` skill | `01-INBOX/daily/` nebo přímo do `02-PROJEKTY` po preview |

n8n cíl na Drive: `SECOND_BRAIN/OBSIDIAN/01-INBOX/<podsložka>/`.

---

## Projekty a úkoly

- Hub: `02-PROJEKTY/<slug>.md` — aktivní `### ID`, backlog, HOTOVO sekce
- Výstupy: `02-PROJEKTY/<slug>/`
- Přehled: [[00-System/Index]]
- Konvence: [[00-System/Templates/task-hybrid-convention]]

---

## Prioritizace

**Eisenhower** — celý název kvadrantu (ne Q1–Q4): Urgentní+Důležité → **ASAP**; Důležité ne urgentní → **Next** + ICE; backlog → **Backlog**; **Waiting** s `Čekat do: YYYY-MM-DD`.

**ICE**: Score = (I × C) / E (E 10 = málo práce).

---

## Triáž a dashboard

| Krok | Kdo |
|------|-----|
| Capture | n8n → `01-INBOX/` |
| Návrh batch | VPS `triage_run.py` → `00-System/Triage-Pending/*.json` |
| Schválení | **Cursor** — `schval pending triáž` (`agenda-triage` PENDING) |
| Přehled | `00-System/Dashboard.html` (build: `build_dashboard.py`) |

Po zpracování capture → [[07-ARCHIV/inbox-processed]] (ne mazat bez archivace).

---

## Skills

Zdroj: `ŠABLONY/skills/` → instalace `scripts/sync-agenda-skills.sh` → `~/.cursor/skills/`, `~/.claude/skills/`.

| Skill | Účel |
|-------|------|
| `agenda-capture` | Capture → preview → `02-PROJEKTY` |
| `agenda-triage` | INBOX, pending batch, re-priority |
| `agenda-co-ted` | Co teď, dashboard, ukliď |
| `agenda-work` | Práce na `<slug>`, výstupy, úkoly |
| `agenda-weekly-review` | Weekly draft → final |
| `agenda-retro` | Meta retro systému |
| `agenda-priority-review` | Revize ICE / Waiting |

Cheatsheet: [[agenda-skill-cheatsheet]].

---

## Pravidla pro agenty

1. Před capture/triage přečti [[about-me]] + [[00-System/Index]]
2. **Nikdy nezapisuj bez preview** (kromě explicitního „apply“ / schválení batch)
3. Tone: [[anti-ai-writing-tools]]
4. Triggery: viz [[agenda-skill-cheatsheet]] — nespouštěj skill bez důvodu

---

## Změnový log

- **2026-04-28**: Cowork struktura, skills, n8n
- **2026-04-30**: n8n rozběh (Sembly, Slack, email); `agenda-work`
- **2026-05-04**: Zrušen iOS Shortcut capture; diktát → Slack
- **2026-05-20**: Migrace na Drive vault `OBSIDIAN/`; SSOT mimo iCloud; `O MNĚ/` sloučeno do `00-System/Memory/`
