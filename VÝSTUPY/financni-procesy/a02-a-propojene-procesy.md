# Procesní popis: A 02 a propojené procesy

**Verze**: 0.1 — pracovní  
**Datum**: 2026-05-07  
**Owner**: Lukáš Cypra  
**Scope**: A 02 + procesy 06A, 08, 10 (přímé závislosti)  
**Vstup**: `procesni-inventar.md` v1.0 (5. 5. 2026)

---

## Jak číst tento dokument

Každý proces je popsán ve třech vrstvách:
- **Aktuální stav** — jak to funguje dnes (tok kroků, nástroje, zodpovědnosti)
- **Problémy / rizika** — co nefunguje nebo chybí
- **Cílový stav + gap** — kde chceme být a co k tomu chybí

Flagy:
- ✅ funguje
- ⚠️ neformálně / nepodchyceno
- ❌ chybí
- 🔧 probíhá / v řešení
- ❓ k doplnění / otevřená otázka

---

## A 02 — Přefakturace nákladů jednatelů (přes jiné subjekty)

**Owner**: každý jednatel individuálně; přehled má Dominik + Martina  
**Nástroje**: Allfred  
**Stav**: ⚠️ funguje, ale bez systematického popisu  

### Aktuální nastavení — kdo fakturuje přes jaký subjekt

| Jednatel | Subjekty |
|----------|----------|
| Luboš | Rainfellows + další |
| Jan | Neurazitelny.cz, Cocuma |
| Lukáš | Odyssey, Alviso, Pixley |

### Aktuální tok procesu

1. Jednatel vynaloží náklad v rámci svého vedlejšího subjektu (nebo na vlastní IČO)
2. Tento náklad je přefakturován na RB EDU (resp. příslušnou entitu)
3. Faktura přijde do Alfrédu → zpracovává Dominik nebo Martina
4. ❓ Rozpad na projekty: **není popsáno** — kdo zadává alokaci, kdy, v jakém formátu

### Problémy / rizika

- **Neexistuje procesní popis** — každý jednatel to řeší jinak, tok závisí na neformální dohodě
- **Hlavní problém — Allfred konsolidace nákladů jednatelů:**
  - Každý jednatel může mít soukromé náklady hrazené firmou v řádu desítek tisíc Kč
  - Rozpadat každý doklad zvlášť na 10+ projektů (jako u parťáků) je neúnosné
  - Potřebujeme způsob, jak konsolidovat veškeré náklady jednoho jednatele na jeden souhrnný doklad per jednatel — a ten pak rozpadnout na projekty
- **Propojení s 06A**: pokud jednatel platí soukromou věc firemní kartou, vstupuje to do evidence 06A (odečet z odměn) — hranice mezi A 02 a 06A není jasně definována

### Cílový stav

- Popsaný tok: jak jednatel zadává alokaci (e-mail Dominikovi? formulář? přímo v Alfrédu?)
- V Alfrédu existuje mechanismus souhrnného dokladu per jednatel s rozpadem na projekty
- Jasná hranice: co jde do A 02 (firemní výdaj přefakturovaný přes subjekt jednatele) vs. co jde do 06A (soukromý výdaj odečtený z odměny)

### Gap

| Co chybí | Priorita | Blocker |
|----------|----------|---------|
| Popis toku — jak jednatel zadává alokaci | ❓ | — |
| Allfred souhrnný doklad per jednatel | ❓ | Allfred feature / workaround |
| Definice hranice A 02 vs. 06A | ❓ | rozhodnutí Lukáš |

---

## 06A — Soukromé náklady hrazené firmou → odečtení z odměn

**Owner**: Dominik (Jan, Luboš) + individuálně (Lukáš, Michal Šrajer)  
**Nástroje**: Google Sheets (přechodně)  
**Stav**: ⚠️ neformálně funguje; není popsáno, kontrolováno ani systematicky evidováno  
**Scope**: aktuálně pouze jednatelé RB Associates s.r.o. a Happiness at Work s.r.o.

### Aktuální tok procesu

1. Firma platí kartou nebo na fakturu soukromou věc jednatele
2. Dominik (nebo individuálně) eviduje v Google Sheetu:
   - [Jan — Google Sheet](https://docs.google.com/spreadsheets/d/1bGWlUV2oDWCz7o4tM6FaIjn5HZQXJ_RQun04YuJN760/edit?gid=0#gid=0)
   - [Luboš — Google Sheet](https://docs.google.com/spreadsheets/d/1xA713P06sDYk65wRQX7HBMcJiHmUfZpnJpvEBNtvUB0/edit?gid=0#gid=0)
   - [Lukáš + Michal Šrajer — finanční kapsičky](https://docs.google.com/spreadsheets/d/1z_J9rvkDV4xlR7hp8vpeZjvbzIV93xXx5nfN5vwTyj8/edit?gid=918938741#gid=918938741)
3. Odečet z odměny:
   - Jan, Luboš: ❓ pravidelnost odečtu není popsána
   - Lukáš + Michal Šrajer: odečet **jednorázově jednou za čas** (ne pravidelně)
4. ❓ Jak se eviduje, že odečet proběhl? Kdo kontroluje?

### Problémy / rizika

- Není popsáno, **kdo a kdy** zadává nový soukromý výdaj do evidence
- Není jasné, jak se rozlišuje soukromý výdaj od firemního při platbě kartou (→ závisí na procesu 05)
- Odečty pro Lukáše a Michala Šrajera jsou nepravidelné — riziko narůstajícího salda
- Google Sheets = dočasné řešení bez auditní stopy v hlavním systému
- Hranice vůči A 02 není definována (viz výše)

### Cílový stav

- Evidence v Alfrédu nebo RB Universe (Google Sheets zrušeny)
- Pravidelný odečet per jednatel (měsíčně nebo při výplatě odměny)
- Jasný trigger: kdy se výdaj eviduje jako 06A vs. A 02

### Gap

| Co chybí | Priorita | Blocker |
|----------|----------|---------|
| Definice triggeru: kdy 06A vs. A 02 | ❓ | rozhodnutí Lukáš |
| Pravidelnost odečtu — stanovit interval | ❓ | — |
| Migrace evidence do Alfrédu / RB Universe | ❓ | Allfred feature / RB Universe dev |
| Popis kdo a kdy zadává nový výdaj do evidence | ❓ | — |

---

## 08 — Mzdy zaměstnanců (Honza, Luboš)

**Owner**: Lenka Turečková (procesně)  
**Nástroje**: ❓ neuvedeno  
**Stav**: ⚠️ funguje neformálně; není sepsáno  

### Propojení s A 02

- Honza a Luboš jsou zároveň jednatelé — jejich odměna (mzda) je vstupem pro výpočet odečtu v 06A
- Bez popsaného toku mezd není jasné, jak 06A odečet k mzdě správně navazuje

### Aktuální tok procesu

- ❓ Celý tok není zdokumentován — závisí na Lence Turečkové

### Cílový stav

- Sepsaný procesní popis (autor: Lenka T.)
- Jasná návaznost na 06A — kdy a jak se odečet promítá do výplaty

### Gap

| Co chybí | Priorita | Blocker |
|----------|----------|---------|
| Procesní popis toku mezd | ❓ | Lenka T. jako autor |
| Definice návaznosti 08 → 06A | ❓ | po sepsání 08 |

---

## 10 — Zálohy kontraktorům / šuplíčky + evidence smíšených nákladů

**Owner**: Dominik (zálohy), jednotlivci sami (evidence)  
**Nástroje**: Google Sheets — [Evidence smíšených nákladů Lukáš + Michal](https://docs.google.com/spreadsheets/d/1z_J9rvkDV4xlR7hp8vpeZjvbzIV93xXx5nfN5vwTyj8/edit?gid=918938741#gid=918938741)  
**Stav**: ⚠️ ad hoc, není systematicky popsáno  

### Propojení s A 02 a 06A

- Zálohy kontraktorům jsou součást toku nákladů, který se konsoliduje v A 02 (přefakturace přes subjekty)
- Evidence smíšených nákladů je sdílená s 06A (stejný Google Sheet pro Lukáše + Michala)

### Aktuální tok procesu

**Zálohy (šuplíčky):**
1. Kontraktor s hodinovkou dostane zálohu na začátku měsíce / období
2. Záloha je zpracována Dominikem v Alfrédu
3. Na konci období proběhne vypořádání: záloha vs. skutečně vykázané hodiny
4. ❓ Pravidla (kdo má nárok, výše zálohy, termín vypořádání) nejsou sepsána

**Evidence smíšených nákladů:**
- Sdílena s 06A (viz výše)
- Zahrnuje firemní náklady placené soukromě i soukromé náklady placené firmou

### Problémy / rizika

- Žádná pravidla pro zálohy — kdo má nárok, jak se počítá, kdy se vypořádá
- Evidence smíšených nákladů splývá s 06A — dvě věci v jednom nástroji
- Google Sheets = dočasné řešení

### Cílový stav

- Sepsaná pravidla záloh (šuplíčků): nárok, výše, vypořádání
- Oddělení evidence smíšených nákladů od 06A (nebo sjednocení do jednoho místa s rozlišením typů)
- Migrace do Alfrédu / RB Universe

### Gap

| Co chybí | Priorita | Blocker |
|----------|----------|---------|
| Pravidla záloh — sepsat (kdo, kolik, kdy) | ❓ | — |
| Oddělení / sjednocení evidence s 06A | ❓ | rozhodnutí Lukáš |
| Migrace do Alfrédu / RB Universe | ❓ | Allfred feature / RB Universe dev |

---

## Přehled závislostí

```
A 02 (přefakturace přes subjekty jednatelů)
 ├── 06A (soukromé náklady hrazené firmou → odečet z odměn)
 │    └── 08 (mzdy — základ pro odečet u Honzy a Luboše)
 └── 10 (zálohy + evidence smíšených nákladů)
      └── 06A (sdílená evidence smíšených nákladů)
```

**Klíčová hranice k definování**: A 02 vs. 06A  
→ Firemní výdaj fakturovaný přes subjekt jednatele (A 02) ≠ soukromý výdaj hrazený firmou s odečtem z odměny (06A)  
→ Tato hranice musí být jasně popsána, jinak vznikají chyby v klasifikaci nákladů.

---

## Otevřené otázky (k vyřešení)

- [ ] Jak jednatel zadává alokaci nákladů na projekty? (e-mail? formulář? Allfred?)
- [ ] Jaký je interval odečtu soukromých nákladů z odměn? (měsíčně? při výplatě?)
- [ ] Kdo a jak kontroluje, že odečet proběhl?
- [ ] Jak v Alfrédu vyřešit souhrnný doklad per jednatel? (workaround nebo nová feature?)
- [ ] Kdo sepíše procesní popis mezd (08)? (Lenka T.?)

---

*Dokument je pracovní verze — doplňovat dle diskuse s týmem. Cílová podoba: import do Procesního architekta RB Universe.*
