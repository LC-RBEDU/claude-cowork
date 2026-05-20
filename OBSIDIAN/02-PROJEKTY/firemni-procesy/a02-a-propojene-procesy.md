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


| Jednatel | Subjekty                |
| -------- | ----------------------- |
| Luboš    | Rainfellows + další     |
| Jan      | Neurazitelny.cz, Cocuma |
| Lukáš    | Odyssey, Alviso, Pixley |


### Aktuální tok procesu

1. Jednatel vynaloží náklad v rámci svého vlastního IČO
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


| Co chybí                                 | Priorita | Blocker                      |
| ---------------------------------------- | -------- | ---------------------------- |
| Popis toku — jak jednatel zadává alokaci | ❓        | —                            |
| Allfred souhrnný doklad per jednatel     | ❓        | Allfred feature / workaround |
| Definice hranice A 02 vs. 06A            | ❓        | rozhodnutí Lukáš             |


---

## 06A — Soukromé náklady hrazené firmou → odečtení z odměn

**Owner**: Dominik (Jan, Luboš) + individuálně (Lukáš, Michal Šrajer)  
**Nástroje**: Google Sheets (přechodně) → Allfred (cílový stav)  
**Stav**: 🔧 návrh řešení zpracován, čeká na implementaci  
**Scope**: aktuálně pouze jednatelé RB Associates s.r.o. a Happiness at Work s.r.o.  
**Referenční dokument**: [Proces zúčtování odměn a soukromých výdajů v Allfredu](https://docs.google.com/document/d/1uF9AlTqPZK9mHW_rwB1xCthLoLuSwuXS2R9JsopPY5s/edit?usp=drive_link)

### Aktuální tok procesu (přechodný stav)

1. Firma platí kartou nebo na fakturu soukromou věc jednatele/parťáka
2. Dominik (nebo individuálně) eviduje v Google Sheetu:
  - [Jan — Google Sheet](https://docs.google.com/spreadsheets/d/1bGWlUV2oDWCz7o4tM6FaIjn5HZQXJ_RQun04YuJN760/edit?gid=0#gid=0)
  - [Luboš — Google Sheet](https://docs.google.com/spreadsheets/d/1xA713P06sDYk65wRQX7HBMcJiHmUfZpnJpvEBNtvUB0/edit?gid=0#gid=0)
  - [Lukáš + Michal Šrajer — finanční kapsičky](https://docs.google.com/spreadsheets/d/1z_J9rvkDV4xlR7hp8vpeZjvbzIV93xXx5nfN5vwTyj8/edit?gid=918938741#gid=918938741)
3. Odečet z odměny probíhá nepravidelně (ad hoc)

### Navrhovaný proces: Clearingový projekt + Zúčtovací Mock doklad

*(Příklad: parťák s odměnou 100 000 Kč, 10 soukromých plateb firemní kartou za 10 000 Kč)*

**Krok 1 — Průběžný sběr účtenek z firemní karty**
- Účtenky za soukromé výdaje přijdou do Alfrédu
- Dominik je zařadí na **Vyrovnávací projekt** daného parťáka (existující projekty, např. Lukáš Cypra – H1/FY2026)
- Doklady se spárují s reálnými pohyby na bankovním účtu
- Účetní v Money S4 vidí, že doklady patří pod vyrovnávací projekt → pohledávka za parťákem, ne firemní náklad

**Krok 2 — Zpracování ponížené faktury od parťáka (konec měsíce)**
- Parťák pošle fakturu na **90 000 Kč** (ponížena o 10 000 Kč za útraty)
- Dominik fakturu rozpadne procentuálně na reálné projekty (např. 60 % Projekt A, 40 % Projekt B)
- Položka v rozpočtu: vždy **Interní alokace**
- Výsledek: projekty nesou náklad 54 000 Kč a 36 000 Kč

**Krok 3 — Vytvoření Zúčtovacího Mock dokladu**
- Dominik vytvoří v Alfrédu manuálně (*New → Expense*) Mock doklad na **10 000 Kč** (součet soukromých výdajů na vyrovnávacím projektu za měsíc)
- Rozpadne ho ve stejném poměru jako fakturu z Kroku 2 (60 % / 40 %) na položku **Interní alokace**
- Označí statusem **Already paid** → doklad nevisí jako neuhrazený, nepletu cashflow
- Přiřadí štítek **„Zúčtování odměny parťáka"** → účetní v Money S4 pozná, že jde o vnitřní přeúčtování (zápočet), ne klasickou přijatou fakturu

> ⚠️ **Klíčový detail pro Money S4**: Z Alfrédu odchází celkem 110 000 Kč (10k účtenky + 90k faktura + 10k Mock doklad). Bez štítku by hrozilo zdvojení nákladů v účetnictví. Štítek „Zúčtování odměny parťáka" je **povinný** u každého Mock dokladu.

### Benefity řešení

- Dominik dělá alokaci jen 2× (faktura + Mock doklad) — jednotlivé účtenky nerozpadá
- Projekty mají přesné náklady (100 % odvedené práce)
- Banka sedí — každá útrata má spárovaný doklad
- Účetnictví má čistá data — vyrovnávací projekt + štítek dávají účetní jasný podklad k zaúčtování

### Gap — co zbývá k implementaci

| Co chybí | Priorita | Blocker |
| -------- | -------- | ------- |
| Nastavit Vyrovnávací projekty v Alfrédu pro všechny dotčené osoby | ❓ | Dominik |
| Zavést štítek „Zúčtování odměny parťáka" v Alfrédu | ❓ | Dominik |
| Instruovat účetní (Martina) k zacházení se štítkem v Money S4 | ❓ | Lukáš / Dominik |
| Definovat interval zúčtování (měsíčně?) a kdo spouští Krok 3 | ❓ | rozhodnutí Lukáš |
| Definice hranice 06A vs. A 02 | ❓ | rozhodnutí Lukáš |
| Zrušení dočasných Google Sheets po zaběhnutí Alfrédu | ❓ | po stabilizaci procesu |


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


| Co chybí                     | Priorita | Blocker             |
| ---------------------------- | -------- | ------------------- |
| Procesní popis toku mezd     | ❓        | Lenka T. jako autor |
| Definice návaznosti 08 → 06A | ❓        | po sepsání 08       |


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


| Co chybí                                  | Priorita | Blocker                           |
| ----------------------------------------- | -------- | --------------------------------- |
| Pravidla záloh — sepsat (kdo, kolik, kdy) | ❓        | —                                 |
| Oddělení / sjednocení evidence s 06A      | ❓        | rozhodnutí Lukáš                  |
| Migrace do Alfrédu / RB Universe          | ❓        | Allfred feature / RB Universe dev |


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

- Jak jednatel zadává alokaci nákladů na projekty? (e-mail? formulář? Allfred?)
- Jaký je interval odečtu soukromých nákladů z odměn? (měsíčně? při výplatě?)
- Kdo a jak kontroluje, že odečet proběhl?
- Jak v Alfrédu vyřešit souhrnný doklad per jednatel? (workaround nebo nová feature?)
- Kdo sepíše procesní popis mezd (08)? (Lenka T.?)

---

*Dokument je pracovní verze — doplňovat dle diskuse s týmem. Cílová podoba: import do Procesního architekta RB Universe.*