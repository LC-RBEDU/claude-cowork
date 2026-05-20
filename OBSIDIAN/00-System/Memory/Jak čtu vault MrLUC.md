# Jak čtu MrLUC

> Jednostránkový návod — kam ukládat, kde číst, čemu se vyhnout. SSOT = tato složka **OBSIDIAN** na Google Drive (repo `SECOND_BRAIN` je jen tooling mimo vault).

## Kam něco uložit

| Co | Kam |
|----|-----|
| Capture ze Slack / Sembly / e-mail | `01-INBOX/{slack,sembly,email,daily}/` (automaticky n8n) |
| Rychlý nápad z mobilu | `01-INBOX/daily/` nebo Backlog v hubu projektu |
| Strategický úkol (ICE, Q1/Q2, Waiting) | `02-PROJEKTY/<název hubu>.md` — sekce **Aktivní úkoly**; **Slug** v hlavičce = ID pro sync |
| Podúkol s termínem | Checkbox `- [ ]` v hubu, ideálně s `📅 YYYY-MM-DD` |
| Dokument / výstup práce | `02-PROJEKTY/<slug>/` (složka výstupů podle **Slug**, ne podle názvu hub souboru) |
| Inspirace mimo projekt | `05-RESOURCES/` (markdown reference) |
| Obrázek / PDF (příloha) | `05-RESOURCES/attachments/_paste/` → po zpracování vedle zdroje nebo v `02-PROJEKTY/<slug>/` — viz [[05-RESOURCES/attachments/README]] |
| Trvalá oblast (role) | `03-AREAS/` |
| Zpracovaný INBOX | `07-ARCHIV/inbox-processed/YYYY/MM/…` |

## Kde co číst

| Situace | Kde |
|---------|-----|
| Planning u PC (TOP 3, kanban, Waiting) | [[00-System/Dashboard.html]] v prohlížeči |
| „Co dnes“ v chatu | Cursor: `co teď` / skill agenda-co-ted |
| Úkoly na cestách (podúkoly s due) | [[Home]] — Tasks dotazy |
| Práce na jednom tématu | Hub `02-PROJEKTY/<slug>.md` + složka výstupů |
| Operativní board v Obsidianu | `02-PROJEKTY/<slug>/kanban.md` |
| Přehled projektů | [[00-System/Index]] |

## Ikony v exploreru (Iconize)

Hub = soubor `02-PROJEKTY/<název>.md` s diakritikou OK (ikona layout-dashboard). Výstupy = složka `02-PROJEKTY/<slug>/` podle pole **Slug** (ikona package). Finance hub = landmark. Po úpravě konfigurace: reload vault. Viz [[Ikony ve vaultu]].

## Stav úkolu (kdo co přepisuje)

| Vrstva | Směr | Poznámka |
|--------|------|----------|
| `02-PROJEKTY/<slug>.md` | **SSOT** | Checkboxy, Waiting, ASAP, HOTOVO — jediné místo ruční změny |
| `dashboard-tasks-source.json` | md → JSON | `sync_tasks_from_projekty.py` při buildu; **nezpět do md** |
| Dashboard HTML | jen čtení | Kliky nic neukládají |
| `Triage-Pending/*.json` | návrh | `waiting_expired` / triáž — platí až po schválení v Cursoru |

Automatika **sama nevrací** odškrtnutý subtask ani Waiting → ASAP. Změna „zpět“ vzniká jen úpravou hub `.md` (ty, skill, skript) nebo schváleným pending batch.

**Cesta projektů:** vždy `02-PROJEKTY/` (velká P).

Viz [[00-System/Memory/vault-gdrive-migration]] po migraci z iCloud.

## Co nedělat

- Needitovat ručně `00-System/dashboard-tasks-source.json` — generuje sync + `build_dashboard.py`.
- Needitovat živé úkoly ve starém Cowork `AGENDA/` nebo `SECOND_BRAIN_INBOX` — SSOT je `OBSIDIAN/02-PROJEKTY/`.
- Nedávat výstupy do samostatného `02-PROJEKTY/` — patří pod projekt.

## Konvence úkolů

Viz [[00-System/Templates/task-hybrid-convention]].

## Schválení triáže

Po VPS cronu: v Cursoru `schval pending triáž` nebo `co čeká na schválení`.
