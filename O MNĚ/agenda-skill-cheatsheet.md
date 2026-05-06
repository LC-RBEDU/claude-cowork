# Agenda — skill cheatsheet

> Quick reference: kdy co zavolat. Detaily v `ŠABLONY/skills/<skill>/SKILL.md`.

## Triggery (co Lukáš může napsat → co se má spustit)

| Lukáš napíše | Spusť |
|--------------|-------|
| "Hoď to do agendy: …" | `agenda-capture` |
| "Zapiš si nápad: …" | `agenda-capture` |
| (drop souboru do chatu) | `agenda-capture` |
| "Co teď?" / "Co dnes?" | `agenda-co-ted` |
| "Ukaž mi dashboard" | `agenda-co-ted` |
| "Co je urgent?" | `agenda-co-ted` |
| "Projeď inbox" | `agenda-triage` |
| "Co tam mám nasbíráno?" | `agenda-triage` |
| "Re-priority" / "přepočítej Eisenhower" | `agenda-triage` (re-priority mode) |
| "Ukliď hotové" | `agenda-co-ted` (clean) |
| "Detail rb-universe" | `agenda-co-ted` (detail) |
| "Odlož ten Mixpanel" | `agenda-co-ted` (defer) |
| "Jdeme na <slug>" / "Pracujeme na <slug>" | `agenda-work` |
| "Otevři <slug>" / "Pokračujeme v <slug>" | `agenda-work` |
| "Udělej mi dokument / mindmapu pro <téma>" | `agenda-work` |
| "Aktualizuj výstupy <slug>" | `agenda-work` |
| "Přidej task" / "Uzavři task" / "Co zbývá v <slug>" | `agenda-work` |

## Klíčová pravidla

- **Capture** = ukládá rychle, ale vždycky preview
- **Triage** = pročistí, refresh `_index.md`
- **Co teď** = jen čte (kromě subcommands `ukliď`/`urgent`/`odlož`)

## Defaulty

- Triage mód: **Batch** (rychlé)
- Pokud uživatel neřekne kdy se vrátit → default **+7 dní**
- Pokud ICE odhad nejistý → použij C=5 a flagni v hlášce

## Anti-patterns (co nedělat)

- Nepiš úkoly bez metadat (kvadrant + ICE jsou minimum)
- Nepřesouvej do HOTOVO bez explicitního "ukliď"
- Necpi vše do `manual/` — třiď podle skutečného zdroje
- Neslučuj témata na vlastní pěst — ptej se
