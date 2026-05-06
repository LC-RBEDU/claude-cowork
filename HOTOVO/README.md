# HOTOVO — uzavřené tvary

> "Otevřené smyčky tě vyčerpávají. Hotové věci jsou pryč z aktivního zorného pole, ale nejsou ztracené — jen archivované."

## Struktura

```
HOTOVO/
├── 2026-Q2/         (uzavřené úkoly v daném kvartálu, jeden soubor per téma)
├── 2026-Q3/
└── processed/       (originály z INBOXu po triage — audit trail)
    └── 2026/
        └── 04/
            └── 28-sembly-strategy-mtg.md
```

## Co kam

- **`<rok>-Q<kvartál>/<slug>.md`** — dotažené úkoly z `AGENDA/<slug>.md`. Každý kvartál vlastní soubor per téma. Skill `agenda-co-ted` na konci kvartálu (nebo na vyžádání) odsune všechny ✅ úkoly z aktivních témat sem.
- **`processed/<rok>/<měsíc>/...`** — originály z INBOXu po zpracování (Sembly transkripty, Slack zprávy, screenshoty). Slouží jako audit trail "odkud co přišlo".

## Pravidlo "completionistu"

Po review (ad-hoc) volej `agenda-co-ted clean` — Claude ti ukáže, co je hotové a navrhne přesun do HOTOVO. Ty potvrdíš.
