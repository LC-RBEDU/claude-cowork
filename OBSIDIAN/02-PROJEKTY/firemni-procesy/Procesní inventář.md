# Procesní inventář — Finance & správa RB EDU

**Verze**: 1.0  
**Datum**: 5. 5. 2026  
**Owner**: Lukáš Cypra  
**Status**: pracovní verze — základ pro tvorbu formálních procesních popisů (import do RB Universe / Procesní architect)

---

## Jak číst tento dokument

Každý proces má:
- **Owner** — kdo je primárně zodpovědný
- **Nástroje** — kde se to dělá
- **Stav** — funguje / částečně / chybí / probíhá
- **Poznámky / otevřené otázky** — co není dořešeno nebo kde je riziko

Flagy:
- ✅ funguje
- ⚠️ částečně / neformálně
- ❌ chybí nebo nepodchyceno
- 🔧 probíhá / v řešení

---

## Cluster A — Fakturace a příjmy

### 01 — Vystavování výstupních faktur klientům
**Owner**: Dominik + PM  
**Nástroje**: Allfred  
**Stav**: ✅ funguje

---

### 02 — Přefakturace nákladů jednatelů (přes jiné subjekty)
**Owner**: každý jednatel si řeší individuálně; přehled má Dominik + Martina  
**Nástroje**: Allfred  
**Stav**: ⚠️ funguje, ale bez systematického popisu

Aktuální nastavení:
- Luboš → Rainfellows + další
- Jan → Neurazitelny.cz, Cocuma
- Lukáš → Odyssey, Alviso, Pixley

**Otevřený problém — Allfred konsolidace nákladů jednatelů:**  
Každý jednatel může mít soukromé náklady hrazené firmou v řádu desítek tisíc Kč. Rozpadat každý doklad zvlášť na 10+ projektů (jako u parťáků) je neúnosné. Potřebujeme najít způsob, jak v Alfrédu konsolidovat veškeré takové náklady na jednoho jednatele a dostat je do nákladů firmy jedním souhrnným dokladem per jednatel — a ten pak rozpadnout na projekty.  
_Souvisí s procesem 06A a 10._

---

### 03 — Sledování splatností a upomínky
**Owner**: Dominik  
**Nástroje**: Allfred (automatické upomínky)  
**Stav**: ⚠️ funguje, ale bez pozornosti — automatické upomínky v Alfrédu neověřeny

---

## Cluster B — Evidence nákladů a výdajů

> **Strategický směr**: celý cluster (04–10) cílí na konsolidaci v Alfrédu / RB Universe. Veškerá aktuální dočasná řešení (Google Sheets, ad hoc evidence, ruční odečty) jsou přechodná.

### 04 — Příjem a účtování dokladů (hlavní proces)
**Owner**: Dominik (operativně) + Martina (účetně)  
**Nástroje**: Allfred  
**Stav**: ✅ běží; čeká na nové funkce Alfrédu (forecast nákladů)

Procesy 05–07 a 06A/B jsou speciální případy uvnitř tohoto procesu.

---

### 05 — Firemní karty — přiřazení a pravidla použití
**Owner**: Lukáš (nastavení pravidel), Dominik (operativně)  
**Nástroje**: —  
**Stav**: ⚠️ pravidlo daňové/nedaňové popsáno (viz dok. 5. 5. 2026); přiřazení karet osobám nepodchyceno

Zdokumentováno (dok. 5. 5. 2026):
- Daňové náklady → platí firemní karta
- Nedaňové náklady → platí soukromá karta → faktura firmě +15 %
- Karty jsou vždy na jméno držitele (na IČO nelze)
- Ad-hoc uživatelé si půjčí kartu od držitele

Chybí:
- Seznam držitelů karet (jméno, typ)
- Pravidla ad-hoc výpůjčky
- Evidence soukromých nákupů hrazených firmou (→ proces 06A)

---

### 06A — Soukromé náklady hrazené firmou → odečtení z odměn
**Owner**: Dominik (Jan, Luboš), individuálně (Lukáš, Michal Šrajer)  
**Stav**: ⚠️ neformálně funguje; není popsáno, kontrolováno ani systematicky evidováno  
**Scope**: aktuálně pouze jednatelé RB Associates s.r.o. a Happiness at Work s.r.o. Výhledově potenciálně použitelné šířeji.

Tok: firma platí kartou nebo na fakturu soukromou věc jednatele → eviduje se → odečte se z odměny, na kterou má daný člověk nárok.

Evidence per osoba:
- **Jan** → [Google Sheet — fakturace](https://docs.google.com/spreadsheets/d/1bGWlUV2oDWCz7o4tM6FaIjn5HZQXJ_RQun04YuJN760/edit?gid=0#gid=0) (řeší Dominik)
- **Luboš** → [Google Sheet — fakturace](https://docs.google.com/spreadsheets/d/1xA713P06sDYk65wRQX7HBMcJiHmUfZpnJpvEBNtvUB0/edit?gid=0#gid=0) (řeší Dominik)
- **Lukáš + Michal Šrajer** → [finanční kapsičky](https://docs.google.com/spreadsheets/d/1z_J9rvkDV4xlR7hp8vpeZjvbzIV93xXx5nfN5vwTyj8/edit?gid=918938741#gid=918938741) — odečet neprobíhá pravidelně, ale jednorázově jednou za čas

**Cílový stav**: celý tento mechanismus přesunout do Alfrédu / RB Universe — aktuální řešení je dočasné.  
_Souvisí s procesy 02, 08, 10._

---

### 06B — Firemní náklady hrazené soukromě → přefakturace +15 %
**Owner**: parťák (platba), Dominik (kontrola a zpracování)  
**Nástroje**: Allfred  
**Stav**: ✅ popsáno a funguje (dok. 5. 5. 2026)  
**Platí**: plošně pro všechny parťáky

Tok: parťák platí projektový náklad soukromě (karta nebo faktura) → přefakturuje firmě s přirážkou +15 % pod položkou „Organizační a technické zabezpečení" → přikládá doklady pro interní kontrolu.  
Rozpad nákladů na zakázky: parťák uvede v průvodním e-mailu → Dominik alokuje.

---

### 07 — Km náhrady za použití soukromého vozidla
**Owner**: Lukáš (nastavení pravidel)  
**Nástroje**: —  
**Stav**: ⚠️ sazba jasná (7 CZK/km), funguje u pár lidí ad hoc; plošné nastavení chybí

Kontext: 7 CZK/km je zjednodušení místo přefakturace benzínu +15 % — úspora času pro obě strany. Jde o specifický případ 06B.  
Záměr: nastavit plošně pro všechny, kdo používají soukromá vozidla pro firemní účely.  
Chybí: seznam use-casů, výjimky, seznam dotčených lidí, schválení.

---

## Cluster C — Odměny a mzdy

### 08 — Mzdy zaměstnanců (Honza, Luboš)
**Owner**: Lenka Turečková (procesně)  
**Nástroje**: —  
**Stav**: ⚠️ funguje neformálně; není sepsáno  
_Souvisí s procesy 02 a 06._

---

### 09 — Odměny kontraktorů (DPP / faktury)
**Owner**: Dominik  
**Nástroje**: Allfred (zpracování faktur), RB Universe (přehled)  
**Stav**: ✅ funguje

P&C tým a jednotliví parťáci vidí přehledy v RB Universe.

---

### 10 — Zálohy kontraktorům / šuplíčky + evidence smíšených nákladů
**Owner**: Dominik (zálohy), jednotlivci sami (evidence)  
**Nástroje**: Google Sheets (Lukáš + Michal): [Evidence smíšených nákladů](https://docs.google.com/spreadsheets/d/1z_J9rvkDV4xlR7hp8vpeZjvbzIV93xXx5nfN5vwTyj8/edit?gid=918938741#gid=918938741)  
**Stav**: ⚠️ ad hoc, není systematicky popsáno

Součást clusteru 05–07. Zahrnuje evidenci soukromých nákladů u firmy i firemních nákladů placených soukromě.  
_Viz také 06A, 02._

---

## Cluster D — Reporting a kontroling

### 11 — Měsíční P&L
**Owner**: Martina (sestavení), Dominik (vložení do RB Universe po kontrole)  
**Nástroje**: RB Universe  
**Stav**: ✅ funguje

---

### 12A — Cashflow sledování (aktuální stav)
**Owner**: Lukáš  
**Nástroje**: RB Universe (Finance dashboard, Strategy dashboard)  
**Stav**: ✅ funguje

Evidujeme:
- zůstatky na účtech
- plánované a vystavené faktury
- přijaté / nezaplacené faktury od dodavatelů

---

### 12B — Cashflow forecast (výhled)
**Owner**: Lukáš  
**Nástroje**: RB Universe (Finance dashboard, Strategy dashboard)  
**Stav**: ❌ nefunguje

Blocker: Allfred tuto funkci zatím neumí. Bez forecast expenses není možné runway sledování. Čeká na dodání featury od Alfrédu.

---

### 13 — Alokace nákladů na projekty (utilizace → marže na zakázce)
**Owner**: Dominik  
**Nástroje**: Allfred  
**Stav**: 🔧 částečně funguje

- Přijaté náklady: ✅ OK
- Vystavené faktury: ✅ OK
- Plánované faktury: ⚠️ závisí na aktuálnosti Invoicing plánů (aktuálně 60–80 %)
- Forecast nákladů: ❌ vůbec neřešen (viz 12)

---

### 14 — Uzavírání projektů (project closing)
**Owner**: nikdo aktuálně  
**Nástroje**: —  
**Stav**: ❌ chybí — žádné podmínky, timing, zodpovědnost, šablona

---

## Cluster E — Daně a účetnictví

### 15 — Rozhodování sporných daňových/účetních případů
**Owner**: Martina + Lenka Turečková (+ případně Lukáš)  
**Nástroje**: —  
**Stav**: ✅ nastaveno, funguje

---

### 16 — Roční daňové přiznání
**Owner**: Martina + Lenka Turečková  
**Stav**: ✅ pro FY2025 podáno (Network + RBJD)

---

### 17 — Optimalizace nákladů (daňové vs. nedaňové)
**Owner**: Martina + Lenka Turečková  
**Stav**: ⚠️ dříve ad hoc; nově systematičtěji s Lenkou

---

## Cluster F — Bankovní operace

### 18 — Odchozí platby
**Owner**: Martina  
**Nástroje**: S4 (platební příkazy přímo)  
**Stav**: ⚠️ funguje, ale bez kontroly / schvalování — potenciální riziko

---

### 19 — Sledování bankovních zůstatků
**Owner**: Lukáš  
**Nástroje**: RB Universe (Finance + Strategy dashboard)  
**Stav**: ⚠️ funguje, ale cíl (runway sledování) vyžaduje forecast nákladů (viz 12)

---

### 20 — Správa úvěrového rámce a bankovních produktů
**Owner**: Lukáš  
**Stav**: 🔧 probíhá

Účty a karty řeší Lukáš průběžně.

---

## Cluster G — Smlouvy a právní rámec

### 21 — Smlouvy s kontraktory (švárc systém)
**Owner**: aktuálně P&C tým  
**Nástroje**: RB Universe  
**Stav**: 🔧 velké téma přes léto 2026

Plán: Lenka Turečková (P&C) + Lenka (účto/daně) + případně Honza Lokajíček (právník).  
_Viz také AGENDA téma `firemni-procesy.md` → [[02-PROJEKTY/Firemní procesy#P3 — Smlouvy s kontraktory / švárc]]._

---

### 22 — Klientské smlouvy — revize a podpisy
**Owner**: Lukáš  
**Nástroje**: šablony, interim OP, Gemini Gem „Právník"  
**Stav**: ⚠️ funguje provizorně; potřeba komplexní revize

Potřeba revize:
- Obchodní podmínky obecné
- OP pro EDUtéku
- OP pro Delivery
- OP pro Eventy a Summit

---

### 23 — M&A a akvizice
**Owner**: Honza Lokajíček (právník, primárně)  
**Stav**: 🔧 aktuálně řešíme Odyssey

Podklady: příklady smluv z akvizice H@W.  
_Viz detaily v AGENDA `ma-odyssey.md`._

---

## Cluster H — Systémy a data

### 24 — Správa a rozvoj Alfrédu
**Owner**: Lukáš + Dominik  
**Nástroje**: Allfred  
**Stav**: 🔧 probíhá — bugy + nové features

Aktuální focus:
- forecast expenses
- rozšíření funkčnosti API
- možnost zápisů

---

### 25 — Migrace GSheets/GAS → Allfred
**Owner**: Lukáš + Dominik (+ Jarda při přechodu)  
**Stav**: 🔧 probíhá

Zbývající tabulky ke migraci:
- tabulky Středisek
- Reporty EDU
- Utilizační tabulka

---

### 26 — RB Universe — datové integrace
**Owner**: Lukáš  
**Nástroje**: RB Universe (FastAPI + pgvector + React)  
**Stav**: ✅ běží; plánováno rozšiřování

Aktuální blocker: omezení Allfred API:
- nenačítání všech projektů
- nemožnost zápisu (kromě projektů a tvorby faktur)
- chyby na straně Alfrédu

---

## Přehled statusů

| # | Proces | Stav |
|---|--------|------|
| 01 | Vystavování faktur klientům | ✅ |
| 02 | Přefakturace nákladů jednatelů | ⚠️ |
| 03 | Splatnosti a upomínky | ⚠️ |
| 04 | Příjem a účtování dokladů | ✅ |
| 05 | Firemní karty — přiřazení a pravidla | ⚠️ |
| 06A | Soukromé náklady hrazené firmou | ⚠️ |
| 06B | Firemní náklady hrazené soukromě (+15 %) | ✅ |
| 07 | Km náhrady | ⚠️ |
| 08 | Mzdy zaměstnanců | ⚠️ |
| 09 | Odměny kontraktorů | ✅ |
| 10 | Zálohy / šuplíčky + evidence smíšených nákladů | ⚠️ |
| 11 | Měsíční P&L | ✅ |
| 12A | Cashflow sledování (aktuální stav) | ✅ |
| 12B | Cashflow forecast (výhled) | ❌ |
| 13 | Alokace nákladů na projekty | 🔧 |
| 14 | Uzavírání projektů | ❌ |
| 15 | Sporné daňové/účetní případy | ✅ |
| 16 | Roční daňové přiznání | ✅ |
| 17 | Optimalizace nákladů | ⚠️ |
| 18 | Odchozí platby | ⚠️ |
| 19 | Sledování bankovních zůstatků | ⚠️ |
| 20 | Správa úvěrového rámce | 🔧 |
| 21 | Smlouvy s kontraktory | 🔧 |
| 22 | Klientské smlouvy | ⚠️ |
| 23 | M&A a akvizice | 🔧 |
| 24 | Správa a rozvoj Alfrédu | 🔧 |
| 25 | Migrace GSheets → Allfred | 🔧 |
| 26 | RB Universe datové integrace | ✅ |

_✅ funguje · ⚠️ neformálně / nepodchyceno · ❌ chybí · 🔧 probíhá_
