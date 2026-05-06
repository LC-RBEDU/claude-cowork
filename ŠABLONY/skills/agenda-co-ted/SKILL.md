---
name: agenda-co-ted
description: "Use this skill when the user asks 'co teď', 'co dnes', 'na co se mám zaměřit', 'co je urgentní', 'co je dnes priorita', 'ukaž mi dashboard', 'co mám rozdělaného'. Ad-hoc dashboard pro rozhodnutí 'co dělám teď'. Reads all AGENDA/<topic>.md files, filters Q1 + top Q2 by ICE score + items due today/overdue + blocked items, and presents a tight, actionable summary. Optional 'clean' subcommand moves completed items to HOTOVO/. Never modifies files unless user explicitly says 'ukliď' or 'clean'."
---

# agenda-co-ted

> "Sednu si, jednou se podívám, vím co dělat." Žádný plán, žádné review — jen aktuální prioritní kapka.

## Kdy spouštět

- "Co teď?" / "Co dnes?" / "Na co se mám zaměřit?"
- "Co je v agendě?" / "Ukaž mi dashboard"
- Začátek pracovního dne (pokud uživatel řekne "vítej zpět" nebo podobně)

## Co dělá

### 1. Načti agendu

- Přečti všechny `AGENDA/*.md` (kromě `_index.md` a `_ŠABLONA.md`)
- Z každého vytáhni aktivní úkoly s metadaty

### 2. Klasifikuj

- **PO TERMÍNU**: `vrátit se < dnes` (datum v minulosti)
- **DNES**: `vrátit se = dnes` nebo `vrátit se = "tento týden"` v týdnu kde je dnes
- **Q1 (urgent + důležité)**: všechny aktivní Q1
- **Q2 TOP 5**: Q2 úkoly podle Score sestupně, prvních 5
- **BLOKOVANÉ**: položky se vyplněným polem `Blokováno: ...` (kromě "nic")

### 3. Vrať dashboard

Format (stručný, akční):

```
═══════════════════════════════════════════════
CO TEĎ — 28/4/2026 14:32
═══════════════════════════════════════════════

⚠️ PO TERMÍNU (2)
  • [ceo-reporting] Vrátit se k Mixpanel napojení (mělo být 25/4)
  • [finance-procesy] Schvalovací proces karet — návrh pro tým

🔥 Q1 — DĚLEJ TEĎ (3)
  • [rb-universe] FIO sync retry — ICE S=24
    └ vrátit se: dnes | nic neblokuje
  • [ceo-reporting] Sales dashboard pro CEO 1:1 zítra
    └ vrátit se: dnes večer | nic neblokuje
  • [interni-pravidla] Doupravit cesťák pravidla — Strategy mtg pátek
    └ vrátit se: čtvrtek | nic neblokuje

📌 Q2 TOP 5 (důležité, naplánuj)
  1. [rb-universe] ReBeL přes Slack — S=18
  2. [finance-procesy] Migrace GAS → Allfred plán — S=14
  3. [ceo-reporting] Konverzní trychtýř EDUtéky — S=12 (BLOKOVÁNO: data)
  4. [interni-pravidla] Karty + cesťáky sloučit do 1 dokumentu — S=10
  5. [rb-universe] pgvector tuning — S=9

🚧 BLOKOVANÉ (4) — popíchni zdroj odblokování
  • [ceo-reporting] Mixpanel data — čeká na CEO
  • [ceo-reporting] Konverzní trychtýř — chybí napojení Mixpanel
  • [finance-procesy] Allfred migrace — čeká na expertního konzultanta
  • [rb-universe] FIO 2FA — čeká na Davida

═══════════════════════════════════════════════
Příkazy: 'ukliď' | 'detail <slug>' | 'urgent <slug>' | 'odlož <slug>'
```

### 4. Subcommands

- **`ukliď` / `clean`** → projdi všechna témata, najdi položky s `[x]` (dokončené), ukaž preview, na potvrzení přesuň do `HOTOVO/<rok>-Q<kvartál>/<slug>.md`
- **`detail <slug>`** → vypiš celý obsah `AGENDA/<slug>.md` se zvýrazněním aktivních úkolů
- **`urgent <slug>` / `urgent <task>`** → přesuň do Q1, navrhni novou ICE
- **`odlož <slug>` / `defer <task>`** → posuň `vrátit se` o týden

## Pravidla

- Nikdy neukládej, dokud uživatel neřekne `ukliď` / `urgent` / `odlož`
- Pokud žádné položky neodpovídají Q1 a žádné nejsou po termínu → zobraz: "Žádné Q1 ani po termínu. Pojď na Q2 #1: ..."
- Při 0 aktivních úkolů ve všech tématech → "Inbox čistý, agenda prázdná. Hoď tam něco z hlavy nebo z inboxu."
