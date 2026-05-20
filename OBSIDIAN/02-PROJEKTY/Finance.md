# Téma: Finance

**Slug**: `finance`
**Vznik**: 2026-04-29
**Posledně aktualizováno**: 2026-05-20
**Owner**: Lukáš

## Kontext

Téma pokrývá fungování a rozvoj finančního týmu: role a odpovědnosti, onboarding / handover, rozvoj členů, migrace GSheets/GAS → Allfred, reporting na Strategy tým.

**Hranice vůči [[02-PROJEKTY/Firemní procesy]]**: Finance = lidi (organizační jednotka). Firemní procesy = pracovní toky. Pokud se mění proces → [[02-PROJEKTY/Firemní procesy]]. Pokud se řeší kdo to dělá / jak tým funguje → sem.

**Hranice vůči [[02-PROJEKTY/Allfred]]**: nastavení, testování a bugy samotného Allfredu → [[02-PROJEKTY/Allfred]]. Tady zůstávají úkoly týmu a procesy, kde je Allfred jen jeden z kanálů (např. remindery, šuplíčky).

## Výstupy

- [[02-PROJEKTY/finance/bankovni-ramce-fio/|Bankovní rámce Fio]]
- [[02-PROJEKTY/finance/cfo/|CFO]]

## Kanban

→ [[02-PROJEKTY/finance/kanban|Board v Obsidianu]]

---

## Tým — složení a zodpovědnosti

### Lukáš Cypra — spolumajitel, Finance & Data (vedení týmu)

- Rozvoj **RB Universe** a implementace **Alfrédu** z pohledu funkčnosti a použitelnosti (finance, PM a další týmy)
- Komunikační linka na **Strategy tým** — slaďování strategických cílů a business vývoje s aktivitami finančního týmu
- Zastřešení **mezitýmových procesních návrhů a dohod**
- **People témata** v rámci týmu
- Nastavování **priorit týmu**
- Zpracovávání návrhů smluv, **revize klientských návrhů**, podpisy smluv
- Komunikace s **bankami** — úvěrový rámec, dodatečné služby

### Dominik Holíček — finanční specialista (~50 % úvazek)

Náplň viz [Google Doc](https://docs.google.com/document/d/1Nw2vPzH7FwtJvjI0DEhxDZR3GKLXi4MKoD0jKe3SblM/) _(doručeno 4. 5. 2026)_

### Martina — účetní

Náplň doručena e-mailem přes Lenku _(5. 5. 2026)_ — obsah bude zpracován v rámci [[02-PROJEKTY/Finance#F9 — Procesní mapa a mapa zodpovědností finančního týmu]].

### Lenka Turečková — externí finanční konzultant (Rainfellows, ad-hoc)

- **Úzká spolupráce s Martinou**: řešení nejasných účetních a daňových případů, rozhodování sporných situací
- **Ad-hoc konzultace** k systémovým řešením (např. fakturace za použití soukromých vozidel, optimalizace nákladů apod.)
- Účastní se pondělních finance meetingů (od 5. 5. 2026)

### Jarda — expertní konzultant (GS/GAS, odchází)

- Autor stávajícího Google Sheets / GAS řešení
- Postupně se odpojuje — účast jen při přechodu na Allfred

---

## Aktivní úkoly

### ~~F5 — Daňové přiznání FY2025~~ ✅ HOTOVO
Přiznání podáno Martinou + Lenkou pro Network i RBJD. Zjištěno z hovoru 5.5.2026.
_Přesunuto do HOTOVO 5. 5. 2026_

### F9 — Procesní mapa a mapa zodpovědností finančního týmu
**Q2 | ICE I8 C7 E7 = 8.0**
Cíl: sestavit procesní mapu a mapu zodpovědností finančního týmu jako základ pro onboarding, handovery a rozvoj. Dominikova pracovní náplň doručena 4. 5. — chybí náplně od zbývajících dvou členů.
- [x] Získat pracovní náplň od účetní _(Martina, via Lenka, 5. 5.)_
- [x] Získat pracovní náplň od Dominika _(Google Doc, 4. 5.)_
- [x] Zodpovědnosti Lukáše doplněny _(5. 5.)_
- [ ] Zpracovat náplně + role → procesní mapa (kdo dělá co)
- [ ] Sestavit mapu zodpovědností (RACI nebo podobné)
_Zdroj: email Dominik Holíček 4. 5. 2026, triage 5. 5. 2026_

### F13 — Kapsičky jednatelů: proklikat v Alfrédu + testovat na datech
**Q2**
Proces srážení soukromých nákladů jednatelů z jejich odměn — technicky přes Alféd, zobrazení v RB Universe. Otestovat na datech za březen a duben jako pilotní běh.
- [ ] S Domčou zkontrolovat kapsičky v Alfrédu pro sebe a Srakyiho
- [ ] Vytáhnout přehled nákladů za březen a duben (testovací data)
- [ ] Rozhodnout, zda se Q1 odečte v jedné splátce (v květnu), nebo rozloží
- [ ] Podklady poslat zbytku týmu před pondělním meetingem
_Zdroj: [Finance Sync transkript 12.5.2026]_

### F14 — Aktivovat Google účet Lenky Turečkové → přístup do RB Universe
**Q2**
Lenka T. potřebuje přístup do RB Universe pro sledování finančních přehledů. Přístup je možný jen přes doménový @redbuttonedu.cz účet.
- [x] Ověřit, zda má Lenka T. aktivní @redbuttonedu.cz účet — účet není aktivní _(12. 5. 2026)_
- [x] Požádat správce Google Workspace o aktivaci — odesláno _(12. 5. 2026)_
- [ ] Přidat Lenku do RB Universe po aktivaci účtu
_Zdroj: [Finance Sync transkript 12.5.2026]_

### F16 — Overdue faktury: zkontrolovat spárování + spustit remindery
**Next | ICE I8 C8 E6 = 10.7**
V Alfrédu je ~450k CZK overdue faktur (cca 20 položek). Automatické upomínky zřejmě nechodí pro faktury odeslané robotem. Dominik má zkontrolovat spárování (platby bez dokladu), Lukáš připraví remindery přes Universe.
- [x] Požádat Dominika, ať projde faktury kde přišla platba ale není spárovaná s dokladem
- [x] Ověřit, zda Alfred posílá automatické upomínky — a pokud ne, proč ne u robot-odeslaných faktur
- [ ] Připomenout se s fixem místo workaroundu 📅 2026-06-10
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — Lukáš: „podívám se na to, jak případně poslat nějaký reminder… je toho tam za 300 litrů"_

### F17 — Podat žádost o kontokorent u FIO Banky
**Waiting | Čekat do: 2026-05-23 | ICE I10 C8 E2 = 40.0**
Lukáš odeslal ~12. 5. dotaz bance na nezávaznou konzultaci ohledně úvěrového rámce / kontokorentu jako buffer pro firmu.
- [x] Podat online žádost o kontokorent na FIO (web / internet banking)
- [ ] Sledovat odpověď banky
- [ ] Po obdržení domluvit termín konzultace
- [ ] Připravit otázky: výše kontokorentu, podmínky zajištění, časový rámec
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — Lukáš: „poslal do banky dotaz... zatím reakci nemám"; Finance Sync 18. 5. 2026 — Lukáš: „podat online žádost o kontokorent"_

### F15 — Domluvit s Honzou Maškem finální nastavení odměn (soc./zdrav.)
**Q2**
Honza upozornil na historický nesoulad v nastavení odměn — srážky soc./zdrav. šly z jeho čisté mzdy, ne tak jako u ostatních owners. Rozdíl cca 100K CZK. Honza říká, že to ve firmě nechá, ale chce situaci finálně dohodnout. Není urgentní.
- [ ] Rozhodnout s Honzou: přejde na model jako ostatní (platí si sám), nebo zůstane jiný přístup?
- [ ] Dopad na historické vyúčtování — potvrdit, že Honza nároky nechává ve firmě
- [ ] Zapsat jako interní dohodu (příp. dodat Lence T. k posouzení)
_Zdroj: [Slack Jan Mašek 12.5.2026](https://rb-edu.slack.com/archives/C062T31FL82/p1778575465170089)_

### F19 — Šuplíčky Happiness: srovnání + mock doklady + procesní dokument
**ASAP | ICE I7 C7 E5 = 9.8 | deadline 2026-05-31**
Šuplíčky Happiness (soukromé výdaje Lukáše + Srakyiho hrazené přes firmu) je potřeba vypořádat: doplnit leden–únor (cutoff ke dni 1. 3.), přidat duben a květen. Zároveň přepsat procesní dokument pro mock doklady a koordinovat s Janou a Dominikem ohledně Allfred taguování.
- [ ] Srovnat šuplíčky za leden–únor s cutoffem 1. 3.
- [ ] Přidat výdaje za duben a květen
- [ ] Koordinovat s Janou (účetní) ohledně zpracování
- [ ] Koordinovat s Marketou (Happiness) — srovnat postup mock dokladů s RB
- [ ] Koordinovat s Dominikem ohledně taguování v Alfrédu
- [ ] Přepsat procesní dokument pro mock doklady
_Zdroj: Finance Sync 18. 5. 2026_

### F20 — Audit EUR faktur v Alfredovi (chybné kurzy / DPH)
**Q1 | ICE I8 C8 E6 = 10.7**
Dominik + Lenka mají projít EUR faktury namapované v Alfredovi a opravit nesprávné kurzy nebo DPH (navazuje na [[02-PROJEKTY/Firemní procesy#P11 — Alfred eurofakturace: proklikat krok 2 s Domčou]]).
- [ ] Vytáhnout seznam EUR faktur k revizi (Alfred / export)
- [ ] Dominik: opravit mapování; Lenka: review vzorku
- [ ] Zapsat typické chyby jako checklist pro PM/finance
_Zdroj: Finance Sync 12. 5. 2026 — deep triage 20. 5. 2026_

### F22 — Prověřit Národní záruku (NRBCZ) pro firmu
**Next | Q2 | ICE I7 C6 E4 = 10.5**
Ověřit podmínky Výzvy 04/2026 (leasingové společnosti, provozovna, expozice NRB >30M), vhodnost pro RB (ručení vs. leasing vs. investice). Navazuje na [[02-PROJEKTY/Finance#F17 — Podat žádost o kontokorent u FIO Banky]] a zmínku národní záruky v hovoru s Dominikem (Odyssey).
- [ ] Projít změny výzvy 04/2026 (NRBCZ / NRB podmínky)
- [ ] Ověřit vhodnost pro RB EDU / konkrétní use case (kontokorent, leasing, investice)
- [ ] Konzultace s bankou / Lenkou pokud potřeba
- **Vrátit se**: po FIO odpovědi
_Zdroj: [[07-ARCHIV/inbox-processed/2026/05/slack/2026-05-20-1452-_claude-capture-finance-task-provit-monost-nrodn-zruky-pes-nrbcz|Slack capture 20. 5.]]; [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-1413-dominik-luk|Sembly Dominik & Lukáš 20. 5.]]

---

## Backlog (nápady, ještě ne aktivní)

### F2 — Analýza uzavřených zakázek Q1 2026
**Q2 | ICE I9 C6 E7 = 7.7**
Cíl: porovnat nadcenění vs. realita (čas + peníze) u zakázek uzavřených od začátku roku. Data k dispozici: utilizace, PM záznamy, Looker (loňský rok). Výstup = vstup pro lepší nadcenění na podzim a pro strategický tým.
- [ ] Zeptat se Martina R.: které zakázky jsou uzavřené a co k nim máme
- [ ] Podívat se do Lookru za loňský rok (akademie s vlastním střediskem)
- [ ] Udělat přehled: plán vs. realita pro top 5–10 zakázek
_Zdroj: sembly/google-meet (Lukáš + Luboš) 28.4._

### F4 — Cashflow forecast v Alfrédu
**Q2 | ICE I9 C5 E5 = 9.0**
Alfréd teď aktivně vyvíjí expense plan + forecast funkce (Lukáš čeká na doplnění). Priorita č. 1 pro Alfréd roadmapu. Bez toho se letí "cashflow pod tmě".
- Čeká na dodání featury od Alfrédu
_Zdroj: sembly/google-meet 28.4._

### F7 — Nákladová struktura dashboard (pareto pro owners)
**Q3 | ICE I7 C6 E6 = 7.0**
Vizualizace: prodali jsme za 100 Kč → 94–96 jsou náklady → z toho 38–40 jsou režie → z těch 97% jsou mzdy → top 3 drivery. Jeden obrázek pro management. Podklad pro rozhodnutí "co si můžeme/nemůžeme dovolit".
_Zdroj: sembly/google-meet 28.4._

---

## Otevřené otázky / čeká na data

- **Přefakturace** — jak systematicky řešit přefakturaci (Honza, Luboš, Lukáš)? Zmíněno v JD Dominika bez rozhodnutí. _(Zdroj: email Dominik 4. 5.)_

---

## Materiály a poznámky

- **PNL březen 2026**: výsledek = **+367 000 Kč** (první měsíc nového fiskálu). Lukáš sdělil na Strategy meetingu 28.4. _(Zdroj: sembly/strategická schůzka 28.4.)_
- **Dominik Holíček — pracovní náplň**: [Google Doc](https://docs.google.com/document/d/1Nw2vPzH7FwtJvjI0DEhxDZR3GKLXi4MKoD0jKe3SblM/) sdílený 4. 5. 2026. Vstup pro [[02-PROJEKTY/Finance#F9 — Procesní mapa a mapa zodpovědností finančního týmu]].
- **Pozdní nákladové doklady po uzávěrce měsíce** (20. 5.): Dominik + Martina OK zařadit do správného měsíce; Lukáš apeluje ve Slacku na včasné dodávání. Daňový pohled → Lenka pokud sporné. _Zdroj: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-1413-dominik-luk|Sembly 20. 5.]]_

---

## Recently moved to HOTOVO

- **F10** — Pozvat Lenku Turečkovou na pondělní finance meeting ✅ _(5. 5. 2026)_
- **F11** — Formalizovat Lenčinu roli jako ad-hoc finanční konzultant ✅ _(5. 5. 2026)_
- **F12** — Wise.com: účet schválen a aktivován ✅ _(12. 5. 2026)_
- **F18** — Zahájit splácení půjček společníků (Luboš + Honza) ✅ _(20. 5. 2026)_
