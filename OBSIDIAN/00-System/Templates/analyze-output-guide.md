# Analyze — příručka tvarů výstupu

> **Není to fixní šablona.** Skill `agenda-analyze` podle typu materiálu skládá strukturu z bloků níže. Cíl: rychlá orientace, bullets, tabulky/mermaid kde pomůžou — ne dlouhý esej.

## Společné jádro (každý soubor)

```markdown
---
datum: YYYY-MM-DD
typ: <clanek|smlouva|schuzka|technicky|data|slack|mix>
projekt: "[[02-PROJEKTY/<Hub>]]"
úkol: F22
zdroje: [...]
---

# <Krátký název analýzy>

## TL;DR
- …
- …

… typové sekce …

## Co s tím
- [ ] …

## Otevřené otázky
- …
```

## Příklad: schůzka (mermaid + tabulka akcí)

- Tabulka akcí: sloupce Kdo | Co | Do kdy
- Diagram: mermaid `flowchart LR` (Návrh → Finance → Odeslání), max 12 uzlů

## Příklad: smlouva (tabulka rizik)

```markdown
## Rizika

| Riziko | Závažnost | Mitigace |
|--------|-----------|----------|
| Automatické prodloužení | vysoká | Kalendář výpovědi |
```

## Příklad: technický (varianty)

```markdown
## Možnosti

| Varianta | Pro | Proti | Effort |
|----------|-----|-------|--------|
| A — oprava API | rychlé | křehké | S |
| B — workaround v hubu | hned | manuální | M |
```

## Pravidla délky

- TL;DR: max 5 bulletů
- Jedna sekce: max ~8 bulletů nebo jedna tabulka
- Celý soubor: cca 80–150 řádků markdown (výjimka u `mix` s mnoha zdroji)

Viz skill: `ŠABLONY/skills/agenda-analyze/SKILL.md`
