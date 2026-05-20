# Téma: Firemní procesy

**Slug**: `firemni-procesy`
**Vznik**: 2026-04-29
**Posledně aktualizováno**: 2026-05-20
**Owner**: Lukáš

## Kontext

Obecné interní procesy a pravidla napříč firmou — jejich nastavení, popis, úpravy. Typicky:

- evidence dokladů a nákladů
- fakturace (výstupní)
- platby kartami
- cestovní náklady (cesťáky)
- schvalovací toky
- nákupy a interní pravidla pro výdaje

**Hranice**:
- vůči obchodním podmínkám RB EDU (projekt `obchodni-podminky-rb-edu`) — OP jsou smluvní rámec ven (B2B kontrakty), tady jsou interní procesy
- vůči [[02-PROJEKTY/Finance]] — tady jsou procesy (pracovní toky), tam je tým (lidé, role, fungování). Procesy mohou tým provozovat, ale popisují se tady.
- vůči [[02-PROJEKTY/Allfred]] — implementace a provoz nástroje Allfred; tady obecné procesy, kde Allfred není hlavní předmět úkolu

> _TODO: doplň aktuální bolesti / co se právě řeší._

## Výstupy

- [[Procesní inventář|procesní inventář]] *(doplň další odkazy)*

## Kanban

→ [[02-PROJEKTY/firemni-procesy/kanban|Board v Obsidianu]]

---

## Aktivní úkoly

### FP14 — Projít handover procesní mapu a doplnit finance kroky v Alfredovi
**ASAP | ICE I8 C8 E7 = 9.1 | deadline 2026-05-22**
Martin Ruman poslal živou verzi procesní mapy handoveru v Miru. Lukáš má projít mapu detailně a doplnit konkrétní kroky, které se týkají financí / Alfrédu — zejména v místech, kde přechod zakázky prochází finančním procesem.
- [ ] Otevřít procesní mapu v Miru: [https://miro.com/app/board/uXjVGsmebuo=/?moveToWidget=3458764664976764250&cot=14](https://miro.com/app/board/uXjVGsmebuo=/?moveToWidget=3458764664976764250&cot=14)
- [ ] Viz také sekce Allfred info při handoveru: [https://miro.com/app/board/uXjVGsmebuo=/?moveToWidget=3458764665102045684&cot=14](https://miro.com/app/board/uXjVGsmebuo=/?moveToWidget=3458764665102045684&cot=14)
- [ ] Projít mapu — identifikovat kroky, kde chybí finance / Allfred kontext
- [ ] Doplnit konkrétní kroky v Alfredovi (co, kdy, kdo, jak)
- [ ] Výsledek sdílet s Martinem Rumanem
_Zdroj: [Slack #_claude-capture 18. 5. 2026](https://slack.com/archives/C0B0LJ86MKN/p1779096223657129); [Slack DM Martin Ruman](https://rb-edu.slack.com/archives/D014V2PJWHK/p1779094226849839)_

### FP1 — Sales/Delivery handover zakotven a spuštěn
**Q1 | ICE I9 C7 E7 = 9.0 | 📌 TOP**
Kickoff meeting proběhl (~29.4.). Výstup: mapa procesu pro akademie i jednorázovky, focus na resourceovou část a handover body na začátku/konci projektu. Dalším krokem je **official rollout do týmu** — procesní mapa na jedno místo, komunikace "od teď jedeme takhle".
- [ ] Ověřit výstupy ze středečního meetingu (Martin R.)
- [ ] Rozeslat mapu procesu do týmu (Martin R. + Verča)
- [ ] Domluvit se, kde mapa "bydlí" (Notion / RB Universe / GDrive)
_Zdroj: sembly/delivery-sales-handover, strategická schůzka 28.4._

### F8 — Pravidla pro náhrady za cestovné (use-case list)
**Q2 | ICE I6 C8 E8 = 6.0**
Sazba 7 CZK/km je potvrzena. Záměr: nastavit plošně pro všechny, kdo používají soukromá vozidla pro firemní účely (aktuálně jen pár lidí ad hoc). Km náhrada nahrazuje +15 % přirážku na benzínku — je jednodušší pro obě strany. Týká se 06B parťáků i zaměstnanců/owners s vlastním autem.
- [ ] Definovat use-cases, na které se 7 CZK/km vztahuje (klienti, teambuilding, školení…)
- [ ] Definovat výjimky — co náhradu nezakládá
- [ ] Zmapovat kdo aktuálně soukromé vozidlo na firemní účely používá
- [ ] Ověřit, kdo pravidla schválí (Strategy / Lukáš?)
- [ ] Uložit na kanonické místo + komunikovat do týmu
_Zdroj: Slack #_claude-capture 4.5.2026, hovor Lenka 5.5., chat 5.5._

### P8 — Neurazitelný: stav podpisu smlouvy + náklady Káťa Gaillard
**Waiting | Čekat do: 2026-05-22**
Ověřit stav smlouvy u projektu Neurazitelný a vyjasnit, jak jsou náklady na Káťu Gaillard zařazeny — jestli jsou součástí naší standardní podpory, nebo jdou nad rámec (8%).
- [x] Zjistit aktuální stav podpisu smlouvy
- [x] Ověřit: jsou náklady na Káťu Gaillard součástí 8% režie, nebo jsou fakturovány nad rámec?
- [x] Výsledek zapsat zpět do příslušného projektu
_Zdroj: Slack capture 6. 5. 2026_

### P9 — Otestovat Request for Invoicing proces v Alfrédu (PM vs. finance práva)
**Q2 | ICE I7 C7 E8 = 6.1**
Martin Ruman upravil fakturu v Alfrédu (Arval invoice — text, popis položek, rozdělení), ale přes "uložit" to nepustilo. Přitom editovat mu to šlo. Otevřená otázka: co PM v Alfrédu může editovat a co ne? Kdo co dotahuje? Lukáš: "Potřebujeme otestovat proces Request for Invoicing a ověřit, co / kdy / jak může zadávat PM a co pak dotáhnou finance."
- [ ] Reprodukovat Martinův případ: [Arval invoice v Alfrédu](https://redbuttonedu.allfred.io/invoices/outgoing-invoices/edit/?id=310) — editovat jako PM, zkusit uložit
- [ ] Zmapovat co PM může vs. nemůže (editovat / uložit / schválit)
- [ ] Sepsat pravidla "kdo co zadává a kdy"
- [ ] Komunikovat pravidla týmu (PM + finance)
_Zdroj: [Slack thread Martin Ruman](https://rb-edu.slack.com/archives/C0ADUR4R8UR/p1778102516812999), Slack #_claude-capture 6. 5. 2026_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]0 — Rozhodnout: alokace nákladů na dovolenou zaměstnanců
**Urgentní + Důležité**
Otevřená procesní otázka: mají se náklady na dovolenou zaměstnanců alokovat do režie, nebo na středisko/projekt zaměstnance?
- [ ] Konzultovat s Lenkou Turečkovou — jaký je správný účetní/daňový přístup
- [ ] Zapsat jako pravidlo (interní dokumentace / Allfred)
- [ ] Komunikovat do týmu (Dominik, Martina)
_Zdroj: [Slack capture 11. 5. 2026](https://slack.com/archives/C0B0LJ86MKN/p1778504046207849)_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]1 — Alfred eurofakturace: proklikat krok 2 s Domčou
**Q1**
Při fakturaci EUR projektů musí být druhý statistický krok (výběr položek z budgetu) přepočítán manuálně na správný kurz ČNB/ECB — Alfred to neumí automaticky. Nutno ověřit postup, a pokud systém blokuje, zadat bug report.
- [ ] S Domčou projít druhý statistický krok fakturace v Alfrédu u EUR projektů (kurz budgetu vs. kurz faktury)
- [ ] Ověřit, zda jde manuálně přepsat korunové částky, nebo to systém blokuje
- [ ] Pokud to nejde → zadat bug report Alfrédu s konkrétním příkladem (odkaz na fakturu)
_Archiv transkriptu: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-12-1332-finance-sync|Finance Sync 12. 5. 2026]]_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]2 — Přefakturace klientům: sepsat parametry a pokyny
**Q2**
Domluvená preferovaná varianta: jedna položka "přefakturace nákladů" + 21% DPH. Pokud klient chce rozpad → po položkách. Případná 15% marže za administraci musí být podložena smluvním rámcem. Obchodníci a PM potřebují jasné pokyny, co musejí domluvit.
- [ ] Rozhodnout a zapsat preferovanou variantu (jedna položka s 21% DPH)
- [ ] Definovat, kdy a jak se přidává 15% marže (vyžaduje smluvní základ s klientem)
- [ ] Sepsat stručné pokyny pro Sales a PM — "co musíte dodat/domluvit, aby bylo možné přefakturovat"
- [ ] Ukázat příště na finance meetingu (pondělí 18. 5.)
_Zdroj: [Finance Sync transkript 12.5.2026]_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]7 — Otestovat Allfred write API: brands + clients + billing entities
**Next | ICE I8 C9 E8 = 9.0 | deadline 2026-05-22**
Allfred potvrdil dostupnost write endpointů: createBrand, updateBrand, createClient, updateClient, createBillingEntity, updateBillingEntity. Lukáš přislíbil v emailu Sašce Gallisové (15. 5.): „otestujeme na pár příkladech příští týden".

- [ ] Připravit testovací volání: createBrand, updateBrand, createClient, updateClient, createBillingEntity, updateBillingEntity
- [ ] Otestovat na pár příkladech v dev/stage prostředí RB Universe
- [ ] Zaznamenat výsledky — co funguje, co ne, jaká jsou omezení
- [ ] Navrhnout next steps pro integraci do RB Universe sync procesu
_Zdroj: Odeslaný email Re: Dotaz - API pro zápis (15. 5. 2026), odpověď od Alexandra Gallisová (Allfred)_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]3 — Nahlásit Alfrédu bug: DUZP chybí u Card Payment
**Next | ICE I6 C9 E9 = 6.0**
U Card Payment chybí v Alfrédu pole DUZP (datum uskutečnění zdanitelného plnění) — doklady se pak nezobrazují správně ve filtrech po měsících. Na rozdíl od Invoice, kde DUZP standardně je.
- [ ] Napsat na support Alfrédu (Saša / support)
- [ ] Popsat bug: Card Payment → pole DUZP chybí → dokumenty nejdou filtrovat dle měsíce
- [ ] Přiložit screenshot příkladu
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — Lukáš: „zkusím odreportovat tohle"_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]4 — Ověřit/nahlásit Alfrédu bug: IBAN párování
**Next | ICE I7 C8 E8 = 7.0**
Bug: do IBAN pole se plní číslo účtu místo IBAN → automatické párování bankovních pohybů s doklady nefunguje. Řešeno dříve, stav opravy nejasný.
- [ ] Ověřit v Alfrédu, zda bug stále trvá
- [ ] Pokud ano → nahlásit s konkrétním příkladem
- [ ] Pokud opraveno → ověřit zlepšení párování v praxi
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — Lukáš: „prozměnuju zase od reportů, jestli už to mají nějak vyřešený"_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]5 — Fakturační proces (varianta 2 dle Saše): rozpadnout do konkrétních kroků
**Next | ICE I8 C8 E6 = 10.7**
Na pondělní schůzce (11. 5.) domluvena varianta 2 procesu zpracování faktur. Lukáš přislíbil zapsat jako konkrétní kroky a přidat do procesního workflow.
- [ ] Zapsat kroky schváleného procesu — ext. faktury (příjde → Alfred → schválení → platba)
- [ ] Zahrnout oblasti: šuplíčky, cestovné, interní expense handling
- [ ] Přidat krok se 4 očima od určité částky (Dominik + Lukáš nebo dle dostupnosti)
- [ ] Hodit do workflow (procesní diagram v RB Universe Procesní architect)
- [ ] Rozšíření o schvalování project ownery → jako krok 2 po ustálení základního procesu
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — Lukáš: „zkusím fakt rozpadnout do konkrétních kroků... tak jak to říkala ta Saša"_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]8 — Podepsat NDA — AI Readiness projekt (Mejzlík)
**ASAP | ICE I7 C8 E8 = 7.0 | st: wt**
Michal a Luboš dělají 3. 6. strategy workshop pro vedení firmy Mejzlík na téma AI Readiness. Lukáš prošel NDA, doplnil hlavičku za RBE a odeslal Jirkovi Bukvaldovi — zjistil, že Klára není jednatelka v rejstříku, požádal o plnou moc jako přílohu. Čeká na odpověď.
- [ ] Počkat na odpověď Jirky/Kláry z Mejzlíku (plná moc + funkce Kláry)
- [ ] Zkontrolovat přiloženou plnou moc
- [ ] Podepsat NDA za RBE a doplnit přílohu
- [ ] Odeslat podepsanou smlouvu zpět na bukvald@mejzlik.eu + cc Michal, Martin
_Zdroj: Odeslaný email "NDA pro AI Readiness projekt" (17. 5. 2026)_

### P20 — Platby vs. expenses v Alfredovi: sjednotit postup
**Q2 | ICE I8 C7 E6 = 9.3**
Na Finance Syncu 12. 5. otevřená otázka, jak v Alfredovi rozlišovat a zpracovávat platby vs. expenses — domluvit offline s Dominikem a zapsat do procesní mapy.
- [ ] S Dominikem projít aktuální praxi (kdo co zadává, kde se to láme)
- [ ] Zapsat jednotný postup do procesní dokumentace / workflow v RB Universe
- [ ] Sladit s účetní (Marta/Lenka), pokud to ovlivňuje reporting
_Zdroj: [Finance Sync 12. 5. 2026](07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-12-1332-finance-sync.md) — deep triage 20. 5. 2026_

### P21 — Příprava faktur v Alfredovi: doplnit kroky s Dominikem
**Q2 | ICE I7 C8 E7 = 8.0**
Doplňuje [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]5 — konkrétní kroky přípravy faktury v UI Alfreda (ne jen schválený proces „varianta 2“).
- [ ] S Dominikem projít end-to-end přípravu faktury v Alfredovi (včetně EUR kroků)
- [ ] Výstup sloučit do [[02-PROJEKTY/Firemní procesy#P15 — Fakturační proces (varianta 2 dle Saše): rozpadnout do konkrétních kroků]] / procesního diagramu
_Zdroj: Finance Sync 12. 5. 2026 — deep triage 20. 5. 2026_

### P22 — Kurzová politika faktur: ECB vs. ČNB (interní směrnice)
**Q2 | ICE I6 C7 E8 = 5.3**
Po proklikání eurofakturace rozhodnout, zda firma fakturuje dle ECB nebo ČNB, a případně sepsat krátkou interní směrnici pro finance + PM.
- [ ] Konzultace s Lenkou T. / Martou (účetní dopad)
- [ ] Rozhodnutí a zápis do interní dokumentace
- [ ] Komunikace do týmu (Sales/PM), pokud ovlivňuje klientské faktury
_Zdroj: Finance Sync 12. 5. 2026 — deep triage 20. 5. 2026_

### P23 — Komentáře Jardy Fulneka k procesnímu dokumentu
**Next | ICE I6 C8 E9 = 5.3**
Jarda slíbil offline komentáře k procesnímu dokumentu — projít, zapracovat nebo odmítnout s důvodem.
- [ ] Získat komentáře od Jardy (Slack/e-mail)
- [ ] Projít bod po bodu a zapracovat do dokumentu / Miro mapy
- [ ] Potvrdit Jardovi uzavření
_Zdroj: Finance Sync 12. 5. 2026 — deep triage 20. 5. 2026_

---

## Backlog (nápady, ještě ne aktivní)

### P1 — Project closing process v Alfrédu
**Q2 | ICE I8 C6 E6 = 8.0**
V Alfrédu neexistuje formální uzavření projektu → Lukáš neví, jestli projekt čeká na náklady nebo je hotov. Potřeba: PM na konci projektu projde budget, invoicing plan, expense plan a klikne "uzavřít" → vyběhne hodnocení a marže.
- Teď to dělá ad hoc Dominik nebo Lukáš
- Závisí na PM onboardingu do Alfrédu (fáze 3)
_Zdroj: sembly/google-meet 28.4._

### P15 — PM progress: milníky vs. finance tracking (4 pohledy)
**Backlog | Q2 | ICE I7 C6 E5 = 8.4**
Čtyři pohledy progresu projektu (fakturace, expense forecast, time, milníky/úkoly). Alfred tasky technicky možné; **do léta nenasazovat** (dohoda s Martinem; status quo ClickUp/Trello). Riziko: prepayment vs. budget gap u ČS — propojit s [[02-PROJEKTY/Allfred#AF6 — Proforma bez projektu: Imprompt a obecně]] / [[02-PROJEKTY/RB Universe#RBU26 — Česká spořitelna Upgrade: chybí v Delivery projektech]].
_Zdroj: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-1443-google-meet-5-20-2026|Sembly Google Meet 20. 5.]]

### F6 — Firemní karty: pravidla co proplácet přes firmu
**Q2 | ICE I6 C8 E8 = 6.0**
Pravidlo daňové/nedaňové je popsáno v interním dokumentu (5. 5. 2026). Chybí: kdo konkrétně kartu dostane, kdo si bere kartu ad-hoc od držitele, a evidence soukromých nákupů hrazených firmou.
- [ ] Sepsat seznam držitelů karet (jméno, karta na jméno)
- [ ] Sepsat pravidla ad-hoc výpůjčky karty
- [ ] Nastavit evidenci soukromých nákupů hrazených firmou (06A)
- [ ] Nastavit způsob alokace na projekt v Alfrédu
_Zdroj: mobile dict 29.4., strategická schůzka 28.4., interní doc 5. 5. 2026_

### P5 — Pravidla evidence dovolené a volna
**Q2 | ICE I7 C6 E7 = 6.0**
Káťa otevřela téma: neexistují jasná pravidla co se eviduje, kdo schvaluje, jak se to počítá u různých typů úvazků. Konkrétní otázky:
- Schvaluje šéf, nebo je evidence bez schvalování (Lukáš preferuje volnější přístup — evidenci, ne kontrolu)?
- Jak se počítá dovolená u částečných úvazků?
- Náhradní volno pro přetížené (Sandra a pod.) — jak do systému?
- Výstup tohoto tématu je vstupem pro T4 (Univerz dovolené tracking).
_Zdroj: sembly/sync-rb-universe 30.4._

### P3 — Smlouvy s kontraktory / švárc
**Q2 | ICE I7 C5 E4 = 8.75**
Stávající nastavení je jako "bezpečnější varianta" (nedáváme vše do nákladů). Potřebujeme vyřešit formální rámec: smlouvy, podmínky, pravidla pro jednotlivé kontraktory. Vyžaduje Lenku — bez ní se nepohneme.
- Čeká na Lenčinu dostupnost
- Lokajíček disponuje šablonou smlouvy ze 30.1.2024 řešící švárc systém — připraveni pomoci
_Zdroj: strategická schůzka 28.4., Slack capture 30.4. (1354)_

### [[02-PROJEKTY/Firemní procesy#P1 — Project closing process v Alfrédu]]6 — Alfred API: ověřit možnost stažení příloh → automatizace na Google Drive
**Backlog | ICE I5 C5 E7 = 3.6**
Explorativní nápad: pokud Alfred API umí vrátit soubory příloh (expenses, invoices), dala by se postavit automatizace, která je pushuje na Google Drive + přidá link do tabulky → Martina by nemusela nic stahovat ručně.
- [ ] Projít Alfred API dokumentaci — přílohy k expenses/invoices
- [ ] Pokud API existuje → navrhnout automatizaci (n8n nebo RB Universe)
- [ ] Domluvit jmennou konvenci souborů a folder strukturu s Martinou
_Zdroj: Hovor Dominik & Lukáš 14. 5. 2026 — nápad, ne příslib_

### P6 — AI-based procesní řízení: inspirace a směr
**Q3 | ICE I6 C4 E6 = 4.0**
RB Universe má základ procesního architekta — potřeba dát to do souladu s tím, kam chceme procesy dotáhnout. Inspirace: businessascode.ai/architecture + umělaintelligence.cz. Zatím jen orientační — ujasnit si vizi a možnosti.
- Referenční materiál: https://businessascode.ai/architecture
_Zdroj: Slack capture 30.4. (1135), mobile dict 30.4._

---

## Otevřené otázky / čeká na data

- **Martin Ruman (OB reference — QED Group)**: Honza zmínil kontakt přes Martina R. na QED Group jako potenciální OB referenci. Sledovat — zatím jen střípek, bez konkrétní akce. _(Zdroj: Slack 29.4.)_

---

## Materiály a poznámky

- **Fakturace, typy nákladů a firemní karty** — interní dokument (PDF, 5. 5. 2026). Pokrývá: pravidla firemních karet (05), fakturace nedaňových nákladů parťáků +15 % (06B), ubytování a hotely, seznam daňových vs. nedaňových nákladů. _Nepokrývá: 06A (soukromé náklady hrazené firmou), 07 (km náhrady), přiřazení karet konkrétním lidem._

## Poznámky k budoucí práci

- **Procesní architect v RB Universe** — až přijde čas na tvorbu formálních procesních popisů (04–07 a další), Lukáš dá přesné zadání formátu pro import do tohoto nástroje. Nepředbíhat.

---

## Recently moved to HOTOVO

### P7 — Napsat aktualizovaný medailonek pro web ✅
_(2026-05-20)_

### F1 — Alokace nákladů na projekty (utilizace) ✅
Pokyn k utilizaci rozestán; Dominik nastavil v Alfrédu. _(2026-05-20)_
