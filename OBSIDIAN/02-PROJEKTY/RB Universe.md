# Téma: RB Universe development

**Slug**: `rb-universe-development`
**Vznik**: 2026-04-29
**Posledně aktualizováno**: 2026-05-20
**Owner**: Lukáš

## Kontext

**Vibe-coding RB Universe** — vývoj a rozšiřování interní platformy "Centrální mozek RB EDU". Nové features, integrace, ReBeL chatbot (Text-to-SQL), AI shrnutí přes RAG, datová vrstva, reporting moduly (P&C, Finance, Marketing, EDUtéka).

Stack: FastAPI + PostgreSQL (pgvector) + Redis + Celery, React 18 + Vite + Tailwind, Coolify deploy.

**Hranice**: tady je **development** (nové features, vývoj, technický dluh, architektura). Pokud někdy přibude téma `rb-universe-provoz.md` (incident response, support, deployment ops), oddělíme to. Zatím to není potřeba.

> _TODO: doplň aktuální roadmapu / klíčové iniciativy v RB Universe._

---

## Aktivní úkoly

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]8 — Připravit finanční přehled pro RBL
**ASAP | Deadline 2026-05-22 | ICE I8 C7 E5 = 11.2**
Konkretní výstup z cashflow dashboardu ([[02-PROJEKTY/RB Universe#RBU10 — Cashflow dashboard pro produkty]]) — finanční přehled pro RBL: příjmy, náklady, marže, projekce. Pro management decision-making.
- [ ] Definovat strukturu výstupu (které metriky, jaký horizont)
- [ ] Naplnit data z Alfréd / Fakturoid
- [ ] Předat managementu
_Zdroj: navazuje na [[02-PROJEKTY/RB Universe#RBU10 — Cashflow dashboard pro produkty]] (cashflow dashboard pro produkty)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]9 — Připravit finanční přehled celkových nákladů
**ASAP | Deadline 2026-05-22 | ICE I9 C7 E5 = 12.6**
Komplexní přehled celkových nákladů firmy z dat v RB Universe / Alfréd / Fakturoid — pro strategické rozhodování o cashflow buffer (návazné na [[02-PROJEKTY/Finance#F17 — Podat žádost o kontokorent u FIO Banky]] kontokorent + [[02-PROJEKTY/Strategy#S2 — Hierarchie cílů: obrat vs. ziskovost vs. dopad]] hierarchie cílů).
- [ ] Definovat scope nákladů (fixní vs. variabilní, per produkt vs. firemní)
- [ ] Naplnit data z účetních systémů
- [ ] Předat managementu
_Zdroj: navazuje na [[02-PROJEKTY/RB Universe#RBU10 — Cashflow dashboard pro produkty]], [[02-PROJEKTY/Finance#F17 — Podat žádost o kontokorent u FIO Banky]], [[02-PROJEKTY/Strategy#S2 — Hierarchie cílů: obrat vs. ziskovost vs. dopad]]_

### RBU4 — Dovolené/volno tracking v Univerzu
**Q1 | ICE I8 C8 E7 = 9.1**
Káťa potřebuje evidenci dovolené v RB Universe, odkud se to propíše do infokalendáře (ne opačně). Lukáš přislíbil prioritně. Pozor: citlivé téma u přetížených lidí (Sandra) — schválení vs. evidence je potřeba procesně ošetřit (viz firemni-procesy).

**Dohodnutý spec (7. 5. 2026, Lukáš + Kateřina Bayerová):**
- FY od 1.3. → nárok 5 týdnů full-time, alikvotní pro zkrácené úvazky i pozdější nástup
- Zpětný import od 1.3.2026 (ne od 1.1.) — Káťa/Léňa pošlou data, Lukáš importuje
- Forma žádosti: "žádost o nedodávání služeb" (název vyřeší People&Culture), bez schvalování manažerem — pouze informování
- Integrace s infokalendářem: Univerz vytvoří event jako info@ se jménem zaměstnance v předmětu
- Na profilu zaměstnance: nárok / plánováno / zrealizováno + možnost zrušit nebo upravit
- Oznámení o změně procesu připraví Káťa/Léňa, Lukáš dodá technický popis + screenshot
- Spuštění cíl: červen (5 týdnů) nebo červenec (2,5 týdne) — závisí na kapacitě

- [ ] ↗ Sembly nahrávka (follow-up k appce, 7. 5. 2026):
- [ ] ↗ Sembly nahrávka (sync RB Universe, 30. 4.):
- [ ] Navrhnout datový model (nárok, čerpání, kategorie volna)
- [ ] Formulář žádosti o volno v Univerzu
- [ ] Propojení Univerz → infokalendář (Univerz vytvoří event jako info@ se jménem zaměstnance)
- [ ] Domluvit s Káťou mechanismus importu dat od 1.3.2026
- [ ] Profil uživatele: sekce nárok/plánováno/zrealizováno + editace/zrušení
- [ ] Notifikace (email nebo push) při podání žádosti
- [ ] Připravit technický popis změny + screenshot pro People&Culture
- [ ] Koordinovat s Káťou/Léňou text oznámení zaměstnancům před spuštěním
_Zdroj: sembly/sync-rb-universe 30.4., sembly/follow-up-k-appce 7.5.2026_

> **Poznámka (migrace 20. 5. 2026):** Plný Sembly transkript follow-up 7. 5. v archivu chybí — obnovit z Sembly exportu, pokud existuje. Odkaz: [[07-Archiv/inbox-processed/2026/05/sembly/2026-05-07-1241-follow-up-k-appce|archivní stub]].

### RBU5 — Self-service profil: co vidí a co může měnit každý uživatel
**Q2 | ICE I7 C7 E6 = 8.2**
Káťa + Leňa navrhují: každý zaměstnanec/kontraktor si sám aktualizuje údaje v Univerzu. Propíše se do Alfreda. Pozor: změna čísla účtu má dopad na platby — nutný review. Jméno zůstává přes Google Workspace (Indra).
_Zdroj: sembly/sync-rb-universe 30.4._

**Co uživatel VIDÍ na svém profilu:**
- [x] Historie plateb (z Alfrédu) ✓
- [x] Dokumenty / smlouvy (podepsané PDF, rámcová smlouva) ✓
- [x] Narozeniny + datum nástupu s reminderem 14 dní dopředu ✓
- [ ] Dovolená / volno — přehled nároku a čerpání **→ čeká na [[02-PROJEKTY/RB Universe#RBU4 — Dovolené/volno tracking v Univerzu]]**
- [x] Faktury (pro uživatele propojené s Alfrédem) ✓
- [x] Tým, role, organigramm, kontakty ✓

**Co uživatel může SÁM MĚNIT (self-service):**
- [x] Mobil ✓ (funguje)
- [x] Fotka ✓ (funguje)
- [x] Název pozice ✓ (funguje, nepropisuje se do Alfréda)
- [x] Adresa ✓ (s review — propisuje se do Alfréda)
- [x] Číslo účtu ✓ (s review — propisuje se do Alfréda)
- [x] Fakturační údaje ✓
- [x] Zadání dovolené → Univerz → infokalendář ✓ (vázáno na [[02-PROJEKTY/RB Universe#RBU4 — Dovolené/volno tracking v Univerzu]])

**Co self-service NENÍ:**
- Jméno — spravuje Google Workspace (Indra)

- Čeká na: [[02-PROJEKTY/RB Universe#RBU6 — Signi integrace s RB Universe]] (smlouvy/Signi), [[02-PROJEKTY/RB Universe#RBU4 — Dovolené/volno tracking v Univerzu]] (dovolené), [[02-PROJEKTY/RB Universe#RBU8 — Bug: uživatel nevidí historii plateb ✅]] (bug platby)

### RBU6 — Signi integrace s RB Universe
**Q2 | ICE I7 C6 E5 = 8.4**
Signi půjde propojit — Lukáš to potvrdil. Workflow: data v Univerzu → generovat smlouvu ze šablony → Signi k podpisu → RB Universe si stáhne podepsané PDF. Ale čeká na Kátu: nejdřív musí být šablony smluv v pořádku (2–3 měsíce).
- Čeká na: Káťa dá do pořádku šablony smluv + revizi stávajících smluv
_Zdroj: sembly/sync-rb-universe 30.4._


### RBU1 — RB Universe MCP: data integrity & rozšíření
**Q2 | ICE I9 C7 E6 = 10.5**
MCP nad RB Universe funguje (základ ukázán na čAI 28.4.) — propojení s Claudem i ChatGPT ověřeno. Bloker: Alfréd API má bugy → data nejsou čistá → odpovědi MCPčka jsou nespolehlivé. Až budou data v pořádku, MCP umožní "konverzaci nad daty" (projektové reporty, analýzy, grafy).
- [ ] Sledovat opravy Alfréd API (aktivně bug-trackovány)
- [ ] Po opravě: ověřit kvalitu dat v RB Universe přes MCP
- [ ] Řešit přístupová práva na sdíleném ChatGPT účtu (nyní vidí každý vše)
_Zdroj: sembly/ai-session, google-meet 28.4._

---

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]0 — Cashflow dashboard pro produkty
**Q2 | ICE I8 C6 E4**
Připravit v RB Universe možnost sledovat cashflow per produkt (EDUtéka, RBL a další) — aby bylo jasné, jak na tom daný produkt finančně je.
- [x] Upřesnit scope: RBL a EDUtéka
- [x] Navrhnout datový model (příjmy / náklady per produkt) — vč. Sales open projektů (výnosy i náklady)
- [x] Napojit na existující finanční data (Alfréd / Fakturoid)
- [x] Připravit wireframe / mockup cashflow grafu v Univerzu
_Zdroj: Slack capture 6. 5. 2026, 7. 5. 2026_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]5 — Filtrace pohledů v RB Universe
**Next**
Modal okno pro tvorbu filtrů (nested filters, a la HubSpot) + výběr polí pro filtrování, uložené a sdílené filtry.
- [ ] Modal okno s tvorbou filtrů (nested filters)
- [ ] Výběr polí pro filtrování v každém zdroji dat
- [ ] Uložené filtry
- [ ] Sdílení filtrů
_Zdroj: Slack capture 7. 5. 2026_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]1 — Enrichment profilu lidí: účast na akcích + LinkedIn data
**Q2 | Next · ICE I7 C6 E4 = 10.5**
Michal Šrajer navrhl, aby RB Universe uměl zobrazit komplexní profil lidí z daného workshopu/akce — účast, LinkedIn data, výstupy pro future reference. Stejná logika se hodí i pro Exponential Circles (Verčin Google Sheet na follow-ups). Otevřená otázka: legálnost a skladování LinkedIn dat (GDPR, rate limity Firecrawlu).

- [ ] Zmapovat, která data chceme u lidí sbírat (účast na akci, LinkedIn URL, výstupy z workshopu)
- [ ] Prozkoumat Firecrawl + LinkedIn scraping: legálnost, rate limity, GDPR
- [ ] Navrhnout datový model v RB Universe (relationship: person ↔ event/akce)
- [ ] Propojit s Verčiným Google Sheetem pro Exponential Circles ([tabulka](https://docs.google.com/spreadsheets/d/1FzQ0GIj8p1bNcKEPf1-v9PgwGYLN2Yh0WbpovyY3fJQ/edit?gid=0#gid=0)) — import nebo přímá integrace PD
- [ ] Zvážit MCP endpoint „dej mi vše o lidech z akce X" (navazuje na [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]])
_Zdroj: [Slack Šrajer 13:19](https://rb-edu.slack.com/archives/C061VU31TUY/p1778678341179429?thread_ts=1778675908.926539&cid=C061VU31TUY) + [Slack Šrajer 14:42](https://rb-edu.slack.com/archives/C061VU31TUY/p1778683349126929?thread_ts=1778675908.926539&cid=C061VU31TUY)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]3 — MVP karet externistů v RB Universe
**Waiting | Čekat do: 2026-05-23 | ICE I7 C7 E5 = 9.8**
Lukáš navrhl na sync meetingu 15. 5.: mapovat externisty jako karty v RB Universe (podobně jako interní parťáci) — témata, typ řemesla, kapacita, fakturace, projekty. Čeká na tabulku od Martina Rumana (IČO + LinkedIn profily).

- [ ] Počkat na tabulku externistů od Martina R. (IČO + LinkedIn profily)
- [ ] Navrhnout datový model karet externistů (témata, typ — lektor/facilitátor/coach, kapacita, fakturace)
- [ ] Zpracovat MVP v RB Universe: karta per externista s napojením na projekty + fakturace
- [ ] Sekce organigram: "delivery externisti" pod Martin Ruman
- [ ] Medailonek jako veřejné view (jen vybrané fieldy, bez interních dat)
_Zdroj: sembly/sync-delivery-package-externisti-na-universe 15.5.2026_

### RBU9 — Procesní architect
**Next | Deadline 2026-05-29 | ICE I7 C7 E8 = 6.1**
Feature v RB Universe pro generování procesních map z popisů/videí. První testovací proces vybrán — pokračujeme detailem.
- [x] Projít, zda někdo po Huddle reagoval s návrhem procesu
- [x] Vybrat jednoduchý, ohraničený proces (ideálně Sales/Delivery nebo HR)
- [x] Předat jako vstup do Projekt architekt feature
- [ ] Zpracovat konkrétní části sales procesu do detailu
_Zdroj: sembly/rb-edu-huddle 4.5.2026_

### RBU26 — Česká spořitelna Upgrade: chybí v Delivery projektech
**Next | Q2 | ICE I7 C8 E4 = 14.0**
Projekt aktivní v Allfredu, v Universe Delivery neviditelný (API/filtr bez invoicing plánu + expenses?). Prověřit a opravit zobrazení + finanční přehled.
- [ ] Reprodukovat: projekt v Alfredu vs. chybějící v Universe Delivery
- [ ] Zjistit root cause (API, filtr, chybějící invoicing plan)
- [ ] Opravit zobrazení; ověřit finanční přehled
_Zdroj: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-1443-google-meet-5-20-2026|Sembly Google Meet 20. 5.]]

---

## Backlog (nápady, ještě ne aktivní)

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]6 — Tabulka alokací PM dle mentální zátěže
**Backlog | Pavel**
Přehledová tabulka alokací project managerů s ohledem na mentální zátěž. Poptáváno Pavlem.
_Zdroj: Slack capture 7. 5. 2026_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]9 — Vytváření osob v PD / Universe z e-mail konverzací
**Backlog**
Automatické zakládání kontaktů v Pipedrive / RB Universe na základě e-mailových konverzací.
_Zdroj: Slack capture 7. 5. 2026_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]7 — Scoring pro time-sensitive projekty
**Backlog**
Feature pro automatické zvýraznění / prioritizaci projektů, u kterých se blíží deadline nebo jsou časově citlivé.
- [ ] Upřesnit definici "time-sensitive projekt" (kritéria, prahy)
- [ ] Navrhnout scoring model
- [ ] Implementovat v RB Universe
_Zdroj: Slack capture 7. 5. 2026_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]8 — Načítání mobilních čísel, pozic a dalších info z e-mailů do PD
**Backlog**
Automatická extrakce kontaktních údajů z e-mailových konverzací a zápis do Pipedrive.
- [ ] Zmapovat zdroje dat (e-mailové signatury, konverzace)
- [ ] Navrhnout mechanismus extrakce → zápis do Pipedrive
- [ ] Otestovat a nasadit
_Zdroj: Slack capture 7. 5. 2026_

### RBU7 — Project management feature (Pavel Kroupa MVP)
**Backlog | ICE I7 C5 E5 = 7.0**
Pavel Kroupa vibe-codoval rychlý prompt-kód-MVP front-end pro projekťáky (Solidpixels, live na redbuttonedu.cz/test). Taky připravil ChatGPT prompt na data model pro sběr dat napříč akademiemi. O víkendu 2.–4.5. chystá "project brief" — co chceme, k čemu, proč, jak. Sháňka po PM nástroji existuje — alternativa k ClickUp / Notion / tabulkám.
- [ ] Přečíst project brief od Pavla Kroupy (přijde po víkendu 2.–4.5.)
- [ ] Vyhodnotit: integrovat do RB Universe vs. standalone nástroj
_Zdroj: Slack capture 30.4. (1534)_

---

## Otevřené otázky / čeká na data

- **Onboarding sync — Pavla Kurník-Šopa**: Jindra udělal e-mail, Lukáš musí spustit sync z Google Workspace → přidat do Univerzu. Quick fix. _(30.4.)_

---

## Materiály a poznámky

- **Leadspicker handover (Veronika, 20. 5.):** přístup ke všem projektům ✅; září EC kampaň klon; export `reply` / Pipedrive; připomenout Honzovi RB Universe LinkedIn inbox plugin (nečíst inbox před odpovědí). _Zdroj: [[07-ARCHIV/inbox-processed/2026/05/sembly/2026-05-20-0905-ver-ak-luk-c-leadspicker-p-ed-n|Sembly Leadspicker 20. 5.]]_
- **Scoring firem:** nasazeno 20. 5. (RBU20 ✅); feedback Strategy tým příští týden.

---

## Recently moved to HOTOVO

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]3 — Přidat onboarding checklist pro Pavlu do RB Universe ✅
Onboarding checklist pro Pavlu přidán v RB Universe (leader: Mišo). _(2026-05-20)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]7 — Fix: duplicitní e-mail drafty při přesunu kandidáta ✅
Bug s vícenásobným e-mail draftem při přesunu kandidáta v ATS opraven a otestován. _(2026-05-20)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]5 — Fix: scoring pipeline zaseknutá + entity_summary 32 chybějících ✅
Celery scoring pipeline opravena, entity_summary doběhlo na všech 32 entit. _(2026-05-20)_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]1 — E-mailové remindery: narozeniny + výročí (14 dní dopředu) ✅
Reminder workflow pro narozeniny a datum nástupu nasazen. _(2026-05-20)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]4 — Upravit KAM sekci v RB Universe ✅
Nové segmenty dle skóre (firmy nad 80 / 70 / 50 bodů) a podsekce info, lidé, organigram. Nasazeno. _(2026-05-20)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]0 — Upravit scoring firem a lidí v RB Universe ✅
Nový scoring model (max. 100 bodů: 70 firma + 30 nejlepší člověk). Upraveno a nasazeno. _(2026-05-20)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]2 — Fix: odměna zmizela z karet + nefungující hromadný přesun ✅
_(2026-05-16)_

### [[02-PROJEKTY/RB Universe#RBU2 — ATS (hiring tracking) v RB Universe ✅]]6 — Osobní sekce Universe ✅
_(2026-05-16)_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]2 — Fix: buddy task — nelze změnit odpovědnou osobu ani datum ✅
Barča a další nemohou na buddy-generovaných úkolech editovat odpovědnou osobu ani datum. Opraveno. _(2026-05-07)_

### [[02-PROJEKTY/RB Universe#RBU1 — RB Universe MCP: data integrity & rozšíření]]4 — Zpřístupnit Alfréd pro Kateřinu Bayerovou ✅
Kateřina neměla přístup do Alfrédu. Lukáš ověřil uživatele a poslal přihlašovací odkaz. _(2026-05-07)_

### RBU8 — Bug: uživatel nevidí historii plateb ✅
Káťa Bayerová reportovala: v Univerzu viděla sekci "Alfred kontraktor", ale historii plateb ne. Opraveno. _(2026-05-06)_

### RBU2 — ATS (hiring tracking) v RB Universe ✅
Káťa ukazovala na strategické schůzce 28.4. — funguje, přehled kandidátů, komunikace, štítky, šablony e-mailů, databáze. Tým nadšený. Plán: napojit na onboarding + reporting. _(2026-04-30)_
