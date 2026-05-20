# Wikilinks — konvence

1. **Projekt hub:** `[[02-PROJEKTY/<název souboru hubu>]]` (bez `.md` — Obsidian doplní). Příklad: `[[02-PROJEKTY/Finance]]`, `[[02-PROJEKTY/RB Universe]]`.
2. **Složka výstupů:** podle pole **Slug** v hubu — `[[02-PROJEKTY/finance/kanban]]`, ne podle názvu hub souboru.
3. **Úkol v hubu:** `[[02-PROJEKTY/Finance#F17 — Podat žádost o kontokorent u FIO Banky]]` — celý text nadpisu `###` za `#`.
4. **Výstup / analýza:** `[[02-PROJEKTY/<slug>/YYYY-MM-DD-analyza-tema|popisek]]` + zápis v sekci **Výstupy** hubu.
5. **Archiv INBOX:** `[[07-ARCHIV/inbox-processed/YYYY/MM/<typ>/soubor|popisek]]` u `_Zdroj:` u úkolu.
6. **Resources:** `[[05-RESOURCES/...]]` pro cross-projekt materiály (markdown).
7. **Přílohy (binárky):** vedle zdrojového `.md` v archivu nebo `02-PROJEKTY/<slug>/`; pasty → `05-RESOURCES/attachments/_paste/`. Viz [[05-RESOURCES/attachments/README]].
8. **Areas:** `[[03-AREAS/...]]` pro trvalé oblasti.
9. **Memory / System:** `[[00-System/Memory/agenda-system]]`, `[[00-System/Index]]`.

## Externí odkazy

Pro URL **nepoužívat** `[[ ]]`. Použít markdown:

```markdown
[popisek](https://example.com/path)
```

V Obsidianu jde na ně kliknout a otevřou se v prohlížeči.

## Nepoužívat

Staré cesty: `07-Archiv`, `04-Vystupy`, `02-Projekty`, `AGENDA/`, `O MNĚ/`.

## Analýzy materiálů

Skill `agenda-analyze` — výstup `YYYY-MM-DD-analyza-<tema>.md` ve `02-PROJEKTY/<slug>/`, tvar podle typu dokumentu (bullets, tabulky, mermaid). Příručka: [[00-System/Templates/analyze-output-guide]].
