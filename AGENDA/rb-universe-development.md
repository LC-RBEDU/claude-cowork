# Téma: RB Universe development

**Slug**: `rb-universe-development`
**Vznik**: 2026-04-29
**Posledně aktualizováno**: 2026-04-29
**Owner**: Lukáš

## Kontext

**Vibe-coding RB Universe** — vývoj a rozšiřování interní platformy "Centrální mozek RB EDU". Nové features, integrace, ReBeL chatbot (Text-to-SQL), AI shrnutí přes RAG, datová vrstva, reporting moduly (P&C, Finance, Marketing, EDUtéka).

Stack: FastAPI + PostgreSQL (pgvector) + Redis + Celery, React 18 + Vite + Tailwind, Coolify deploy.

**Hranice**: tady je **development** (nové features, vývoj, technický dluh, architektura). Pokud někdy přibude téma `rb-universe-provoz.md` (incident response, support, deployment ops), oddělíme to. Zatím to není potřeba.

> _TODO: doplň aktuální roadmapu / klíčové iniciativy v RB Universe._

---

## Aktivní úkoly

### T4 — Dovolené/volno tracking v Univerzu
**Q1 | ICE I8 C8 E7 = 9.1**
Káťa potřebuje evidenci dovolené v RB Universe, odkud se to propíše do infokalendáře (ne opačně). Lukáš přislíbil prioritně. Součást: propočet nároku (podle úvazku a data nástupu), zpětné doplnění od 1.1.2026 z infokalendáře. Pozor: citlivé téma u přetížených lidí (Sandra) — schválení vs. evidence je potřeba procesně ošetřit (viz firemni-procesy).
- [ ] Navrhnout datový model (nárok, čerpání, kategorie volna)
- [ ] Propojení Univerz → infokalendář (task in Univerz → event v info)
- [ ] Vyřešit zpětný import od 1.1.2026 z infokalendáře
- [ ] Domluvit s Káťou pravidla (co se eviduje, co ne)
_Zdroj: sembly/sync-rb-universe 30.4._

### T5 — Self-service profil: co vidí a co může měnit každý uživatel
**Q2 | ICE I7 C7 E6 = 8.2**
Káťa + Leňa navrhují: každý zaměstnanec/kontraktor si sám aktualizuje údaje v Univerzu. Propíše se do Alfreda. Pozor: změna čísla účtu má dopad na platby — nutný review. Jméno zůstává přes Google Workspace (Indra).
_Zdroj: sembly/sync-rb-universe 30.4._

**Co uživatel VIDÍ na svém profilu:**
- [ ] Historie plateb (z Alfrédu) — aktuálně nefunguje → viz T8
- [ ] Dokumenty / smlouvy (podepsané PDF, rámcová smlouva) — po T6 Signi integraci
- [ ] Narozeniny + datum nástupu s reminderem 14 dní dopředu
- [ ] Dovolená / volno — přehled nároku a čerpání → po T4
- [ ] Faktury (pro uživatele propojené s Alfrédem)
- [ ] Tým, role, organigramm, kontakty

**Co uživatel může SÁM MĚNIT (self-service):**
- [x] Mobil ✓ (funguje)
- [x] Fotka ✓ (funguje)
- [x] Název pozice ✓ (funguje, nepropisuje se do Alfréda)
- [ ] Adresa (s review — propisuje se do Alfréda)
- [ ] Číslo účtu (s review — propisuje se do Alfréda, dopad na platby)
- [ ] Fakturační údaje
- [ ] Zadání dovolené → Univerz → infokalendář (trust-based, bez schvalování) → T4

**Co self-service NENÍ:**
- Jméno — spravuje Google Workspace (Indra)

- Čeká na: T6 (smlouvy/Signi), T4 (dovolené), T8 (bug platby)

### T6 — Signi integrace s RB Universe
**Q2 | ICE I7 C6 E5 = 8.4**
Signi půjde propojit — Lukáš to potvrdil. Workflow: data v Univerzu → generovat smlouvu ze šablony → Signi k podpisu → RB Universe si stáhne podepsané PDF. Ale čeká na Kátu: nejdřív musí být šablony smluv v pořádku (2–3 měsíce).
- Čeká na: Káťa dá do pořádku šablony smluv + revizi stávajících smluv
_Zdroj: sembly/sync-rb-universe 30.4._


### T1 — RB Universe MCP: data integrity & rozšíření
**Q2 | ICE I9 C7 E6 = 10.5**
MCP nad RB Universe funguje (základ ukázán na čAI 28.4.) — propojení s Claudem i ChatGPT ověřeno. Bloker: Alfréd API má bugy → data nejsou čistá → odpovědi MCPčka jsou nespolehlivé. Až budou data v pořádku, MCP umožní "konverzaci nad daty" (projektové reporty, analýzy, grafy).
- [ ] Sledovat opravy Alfréd API (aktivně bug-trackovány)
- [ ] Po opravě: ověřit kvalitu dat v RB Universe přes MCP
- [ ] Řešit přístupová práva na sdíleném ChatGPT účtu (nyní vidí každý vše)
_Zdroj: sembly/ai-session, google-meet 28.4._

---

### T10 — Cashflow dashboard pro produkty
**Q2**
Připravit v RB Universe možnost sledovat cashflow per produkt (EDUtéka, RBL a další) — aby bylo jasné, jak na tom daný produkt finančně je.
- [x] Upřesnit scope: RBL a EDUtéka
- [ ] Navrhnout datový model (příjmy / náklady per produkt)
- [ ] Napojit na existující finanční data (Alfréd / Fakturoid)
- [ ] Připravit wireframe / mockup pohledu v Univerzu
_Zdroj: Slack capture 6. 5. 2026_

---

## Backlog (nápady, ještě ne aktivní)

### T9 — Projekt architekt: najít první testovací proces
**Q2 | ICE I7 C7 E8 = 6.1**
Feature v RB Universe pro generování procesních map z popisů/videí je v progresu. Lukáš na Huddle (4.5.) veřejně požádal o návrhy — hledá jednoduchý, ohraničený proces jako první testovací případ.
- [ ] Projít, zda někdo po Huddle reagoval s návrhem procesu
- [ ] Vybrat jednoduchý, ohraničený proces (ideálně Sales/Delivery nebo HR)
- [ ] Předat jako vstup do Projekt architekt feature
_Zdroj: sembly/rb-edu-huddle 4.5.2026_

### T7 — Project management feature (Pavel Kroupa MVP)
**Q2 | ICE I7 C5 E5 = 7.0**
Pavel Kroupa vibe-codoval rychlý prompt-kód-MVP front-end pro projekťáky (Solidpixels, live na redbuttonedu.cz/test). Taky připravil ChatGPT prompt na data model pro sběr dat napříč akademiemi. O víkendu 2.–4.5. chystá "project brief" — co chceme, k čemu, proč, jak. Sháňka po PM nástroji existuje — alternativa k ClickUp / Notion / tabulkám.
- [ ] Přečíst project brief od Pavla Kroupy (přijde po víkendu 2.–4.5.)
- [ ] Vyhodnotit: integrovat do RB Universe vs. standalone nástroj
_Zdroj: Slack capture 30.4. (1534)_

### T3 — Sales summary e-mail přes "husku"
**Q3 | ICE I5 C6 E7 = 4.3**
Lukáš posílá obchodníkům přes husku souhrnný e-mail s daty podobnými jako appka. Honza chce verzi jako podcast (text-to-speech). Zatím jen nápad — nízká priorita.
_Zdroj: strategická schůzka 28.4._

---

## Otevřené otázky / čeká na data

- **Onboarding sync — Pavla Kurník-Šopa**: Jindra udělal e-mail, Lukáš musí spustit sync z Google Workspace → přidat do Univerzu. Quick fix. _(30.4.)_

---

## Materiály a poznámky

_(žádné)_

---

## Recently moved to HOTOVO

### T8 — Bug: uživatel nevidí historii plateb ✅
Káťa Bayerová reportovala: v Univerzu viděla sekci "Alfred kontraktor", ale historii plateb ne. Opraveno. _(2026-05-06)_

### T2 — ATS (hiring tracking) v RB Universe ✅
Káťa ukazovala na strategické schůzce 28.4. — funguje, přehled kandidátů, komunikace, štítky, šablony e-mailů, databáze. Tým nadšený. Plán: napojit na onboarding + reporting. _(2026-04-30)_
