# Téma: Allfred

**Slug**: `allfred`
**Vznik**: 2026-05-20
**Posledně aktualizováno**: 2026-05-20
**Owner**: Lukáš

## Kontext

Implementace, nastavení, onboarding a provoz nástroje **Allfred** (ERP/finance stack RB EDU): práva, fakturace, API, bug reporty.

**Hranice**:
- vůči [[02-PROJEKTY/Firemní procesy]] — obecné procesy napříč firmou; sem jen úkoly, kde je **core** práce v Allfredu
- vůči [[02-PROJEKTY/Finance]] — finanční tým a role; sem funkce a nastavení Allfredu (ne šuplíčky jako celý proces)
- vůči [[pipedrive-a-dalsi-nastroje]] — CRM; integrace Allfred ↔ Pipedrive

## Výstupy

→ [[02-PROJEKTY/allfred/|složka výstupů]]

## Kanban

→ [[02-PROJEKTY/allfred/kanban|Board v Obsidianu]]

---

## Aktivní úkoly

### AF1 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)
**Q2 | ICE I7 C7 E8 = 6.1**
Martin Ruman upravil fakturu v Alfrédu (Arval invoice — text, popis položek, rozdělení), ale přes "uložit" to nepustilo. Přitom editovat mu to šlo. Otevřená otázka: co PM v Alfrédu může editovat a co ne? Kdo co dotahuje? Lukáš: "Potřebujeme otestovat proces Request for Invoicing a ověřit, co / kdy / jak může zadávat PM a co pak dotáhnou finance."
- [ ] Reprodukovat Martinův případ: [Arval invoice v Alfrédu](https://redbuttonedu.allfred.io/invoices/outgoing-invoices/edit/?id=310) — editovat jako PM, zkusit uložit
- [ ] Zmapovat co PM může vs. nemůže (editovat / uložit / schválit)
- [ ] Sepsat pravidla "kdo co zadává a kdy"
- [ ] Komunikovat pravidla týmu (PM + finance)
_Zdroj: [Slack thread Martin Ruman](https://rb-edu.slack.com/archives/C0ADUR4R8UR/p1778102516812999), Slack #_claude-capture 6. 5. 2026_

### AF2 — Alfred eurofakturace: proklikat krok 2 s Domčou
**Q1 | ICE I6 C8 E7**
Při fakturaci EUR projektů musí být druhý statistický krok (výběr položek z budgetu) přepočítán manuálně na správný kurz ČNB/ECB — Alfred to neumí automaticky. Nutno ověřit postup, a pokud systém blokuje, zadat bug report.
- [ ] S Domčou projít druhý statistický krok fakturace v Alfrédu u EUR projektů (kurz budgetu vs. kurz faktury)
- [ ] Ověřit, zda jde manuálně přepsat korunové částky, nebo to systém blokuje
- [ ] Pokud to nejde → zadat bug report Alfrédu s konkrétním příkladem (odkaz na fakturu)
_Archiv transkriptu: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-12-1332-finance-sync|Finance Sync 12. 5. 2026]]_

### AF3 — Otestovat Allfred write API: brands + clients + billing entities
**Next | ICE I8 C9 E8 = 9.0 | deadline 2026-05-22**
Allfred potvrdil dostupnost write endpointů: createBrand, updateBrand, createClient, updateClient, createBillingEntity, updateBillingEntity. Lukáš přislíbil v emailu Sašce Gallisové (15. 5.): „otestujeme na pár příkladech příští týden".

- [ ] Připravit testovací volání: createBrand, updateBrand, createClient, updateClient, createBillingEntity, updateBillingEntity
- [ ] Otestovat na pár příkladech v dev/stage prostředí RB Universe
- [ ] Zaznamenat výsledky — co funguje, co ne, jaká jsou omezení
- [ ] Navrhnout next steps pro integraci do RB Universe sync procesu
_Zdroj: Odeslaný email Re: Dotaz - API pro zápis (15. 5. 2026), odpověď od Alexandra Gallisová (Allfred)_

### AF4 — Nahlásit Alfrédu bug: DUZP chybí u Card Payment
**Next | ICE I6 C9 E9 = 6.0**
U Card Payment chybí v Alfrédu pole DUZP (datum uskutečnění zdanitelného plnění) — doklady se pak nezobrazují správně ve filtrech po měsících. Na rozdíl od Invoice, kde DUZP standardně je.
- [ ] Napsat na support Alfrédu (Saša / support)
- [ ] Popsat bug: Card Payment → pole DUZP chybí → dokumenty nejdou filtrovat dle měsíce
- [ ] Přiložit screenshot příkladu
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — Lukáš: „zkusím odreportovat tohle"_

### AF5 — Ověřit/nahlásit Alfrédu bug: IBAN párování
**Next | ICE I7 C8 E8 = 7.0**
Bug: do IBAN pole se plní číslo účtu místo IBAN → automatické párování bankovních pohybů s doklady nefunguje. Řešeno dříve, stav opravy nejasný.
- [ ] Ověřit v Alfrédu, zda bug stále trvá
- [ ] Pokud ano → nahlásit s konkrétním příkladem
- [ ] Pokud opraveno → ověřit zlepšení párování v praxi
- **Triage 20. 5.:** Dominik — párování „jde do kopru“; eskalovat Sašovi / support urgentně.
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026; [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-1413-dominik-luk|Sembly 20. 5.]]

### AF6 — Proforma bez projektu: Imprompt a obecně
**Next | Q1 | ICE I8 C7 E5 = 11.2**
Zjistit, proč proforma z API není linknutá na projekt (případ Imprompt); workaround pro Dominika (ruční projekt + edit faktury); eskalace Allfred supportu pokud systémové.
- [ ] Prověřit v Allfredu / Fakturoidu tok proforma → faktura (API vs. ruční)
- [ ] Opravit / zdokumentovat workaround pro finance
- [ ] Ticket Allfred support pokud chyba systému
_Zdroj: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-1413-dominik-luk|Sembly Dominik & Lukáš 20. 5.]]

### AF7 — Platby vs. expenses v Alfredovi: sjednotit postup
**Q2 | ICE I8 C7 E6 = 9.3**
Na Finance Syncu 12. 5. otevřená otázka, jak v Alfredovi rozlišovat a zpracovávat platby vs. expenses — domluvit offline s Dominikem a zapsat do procesní mapy.
- [ ] S Dominikem projít aktuální praxi (kdo co zadává, kde se to láme)
- [ ] Zapsat jednotný postup do procesní dokumentace / workflow v RB Universe
- [ ] Sladit s účetní (Marta/Lenka), pokud to ovlivňuje reporting
_Zdroj: [Finance Sync 12. 5. 2026](07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-12-1332-finance-sync.md) — deep triage 20. 5. 2026_

### AF8 — Příprava faktur v Alfredovi: doplnit kroky s Dominikem
**Q2 | ICE I7 C8 E7 = 8.0**
Doplňuje FP11 — konkrétní kroky přípravy faktury v UI Alfreda (ne jen schválený proces „varianta 2“).
- [ ] S Dominikem projít end-to-end přípravu faktury v Alfredovi (včetně EUR kroků)
- [ ] Výstup sloučit do FP11 / procesního diagramu
_Zdroj: Finance Sync 12. 5. 2026 — deep triage 20. 5. 2026_

### [[02-PROJEKTY/Allfred#AF1 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)]]3 — Audit EUR faktur v Alfredovi (chybné kurzy / DPH)
**Q1 | ICE I8 C8 E6 = 10.7**
Dominik + Lenka mají projít EUR faktury namapované v Alfredovi a opravit nesprávné kurzy nebo DPH (navazuje na [[02-PROJEKTY/Allfred#AF2 — Alfred eurofakturace: proklikat krok 2 s Domčou]]).
- [ ] Vytáhnout seznam EUR faktur k revizi (Alfred / export)
- [ ] Dominik: opravit mapování; Lenka: review vzorku
- [ ] Zapsat typické chyby jako checklist pro PM/finance
_Zdroj: Finance Sync 12. 5. 2026 — deep triage 20. 5. 2026_

### [[02-PROJEKTY/Allfred#AF1 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)]]5 — Zjistit možnosti: LOST reason Allfred → Pipedrive
**Next | ICE I6 C8 E7 = 6.9**
Když v Allfred označím projekt jako LOST, Pipedrive ho taky označí jako ztracený — ale nepožaduje uvedení důvodu. Dlouhodobě tak přicházíme o data o důvodech ztráty obchodů.
- **Z**: Slack #_claude-capture, 15. 5. 2026 — Pavel Kroupa nahlásil
- ↗ Původní zpráva (Pavel Kroupa): https://rb-edu.slack.com/archives/C0ADUR4R8UR/p1778816268572789?thread_ts=1778816268.572789&cid=C0ADUR4R8UR
- ↗ Pipedrive deal #6856: https://redbuttoncz.pipedrive.com/deal/6856
- [ ] Prověřit, zda Allfred API umí při LOST eventu přenést reason code do PD
- [ ] Pokud ne → zjistit, zda jde nastavit webhook nebo workaround
- [ ] Rozhodnout: řešit nebo vědomě ignorovat (s odůvodněním)

---

## Backlog (nápady, ještě ne aktivní)

### AF9 — Project closing process v Alfrédu
**Q2 | ICE I8 C6 E6 = 8.0**
V Alfrédu neexistuje formální uzavření projektu → Lukáš neví, jestli projekt čeká na náklady nebo je hotov. Potřeba: PM na konci projektu projde budget, invoicing plan, expense plan a klikne "uzavřít" → vyběhne hodnocení a marže.
- Teď to dělá ad hoc Dominik nebo Lukáš
- Závisí na PM onboardingu do Alfrédu (fáze 3)
_Zdroj: sembly/google-meet 28.4._

### [[02-PROJEKTY/Allfred#AF1 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)]]0 — Reporting PM aktivit v Alfrédu (time tracking na zakázky)
**Q2 | ICE I8 C5 E5 = 8.0**
PM-ové zatím nevykazují čas v Alfrédu. Plán: dobrovolně od května, povinně přes léto. Lukáš je skeptický k oběma datům. Bez toho nemáme data pro nadcenění a analýzu zakázek.
_Zdroj: sembly/google-meet 28.4._

### [[02-PROJEKTY/Allfred#AF1 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)]]1 — Alfred API: ověřit možnost stažení příloh → automatizace na Google Drive
**Backlog | ICE I5 C5 E7 = 3.6**
Explorativní nápad: pokud Alfred API umí vrátit soubory příloh (expenses, invoices), dala by se postavit automatizace, která je pushuje na Google Drive + přidá link do tabulky → Martina by nemusela nic stahovat ručně.
- [ ] Projít Alfred API dokumentaci — přílohy k expenses/invoices
- [ ] Pokud API existuje → navrhnout automatizaci (n8n nebo RB Universe)
- [ ] Domluvit jmennou konvenci souborů a folder strukturu s Martinou
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — nápad, ne příslib_

### [[02-PROJEKTY/Allfred#AF1 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)]]4 — Cashflow forecast v Alfrédu
**Waiting | Čekat do: 2026-05-21 | ICE I10 C5 E5 = 10.0**
Vysoký impact na chod firmy: bez forecast featury letíme "cashflow pod tmě". Alfréd aktivně vyvíjí expense plan + forecast funkci. Po dodání featury (čekáme do čtvrtka 2026-05-21) — připravit konkrétní výstupy.
- [ ] Expense forecast k uzavřeným projektům
- [ ] Výnosy z otevřených Pipedrive dealů
- [ ] Externí náklady k otevřeným Pipedrive dealům
_Zdroj: sembly/google-meet 28.4._

---

## Otevřené otázky / čeká na data

_(žádné)_

---

## Materiály a poznámky

- [Procesní inventář — cluster Allfred](Procesní%20inventář.md)

---

## Recently moved to HOTOVO

_(žádné)_
