# Téma: Pipedrive a další nástroje

**Slug**: `pipedrive-a-dalsi-nastroje`
**Vznik**: 2026-05-13
**Posledně aktualizováno**: 2026-05-21
**Owner**: Lukáš

## Kontext

> CRM a obchodní nástroje firmy — Pipedrive jako hlavní systém, webové formuláře pro lead capture, reporty a dashboardy pro business review. Téma pokrývá údržbu a rozvoj těchto nástrojů, napojení na web a správu produktového portfolia v reportech (nově včetně modulů z Allfreda).

## Výstupy

- [[02-PROJEKTY/pipedrive-a-dalsi-nastroje/2026-05-20-analyza-ninjabot-smlouvy|Ninjabot — inventář 6 dokumentů + rozhodovací flow (PD4)]]
- [[02-PROJEKTY/pipedrive-a-dalsi-nastroje/2026-05-21-analyza-ninjabot-mesicni-fakturace|Ninjabot — měsíční fakturace (2298, doc 3–6)]]
- **Materiály Ninjabot (PDF):** `02-PROJEKTY/pipedrive-a-dalsi-nastroje/ninjabot/` — 6× objednávky (1498 implementace + 2298 automatizace)

---

## Aktivní úkoly

### PD2 — Vyčistit a aktualizovat reporty pro Lukáše D.
**Next | ICE I6 C8 E7 = 6.9**
Sada reportů pro business review — aktuální stav, Order Entry pro aktuální FY, dashboardy per produkt/stream. Produktové portfolio je potřeba vyčistit, nově obsahuje moduly z Allfreda.
- **Z**: Slack #_claude-capture, 12. 5. 2026
- **Vrátit se**: tento sprint
- [ ] Report: Aktuální stav (dle streamů)
- [ ] Report: Order Entry pro aktuální FY (dle streamů)
- [ ] Dashboardy pro jednotlivé produkty / streamy
- [ ] Vyčistit produktové portfolio — doplnit / restrukturovat moduly z Allfreda

### PD3 — Navrhnout komplexní proces aktualizace dat v Pipedrive přes RB Universe
**Next | ICE I8 C7 E5 = 11.2**
Komplexní workflow pro aktualizaci dat v Pipedrive skrze RB Universe — bizmachine aktualizace, meeting prep / sales feed, řešení přechodů kontaktních osob mezi firmami (zachovat historii ex-pozice, dealů, ale mít aktuální info o nové firmě).
- **Z**: Slack #_claude-capture, 14. 5. 2026 (Lukáš)
- ↗ Původní Slack zpráva: https://slack.com/archives/C0B0LJ86MKN/p1778749020429839
- [ ] Zmapovat aktuální stav — co dnes teče do Pipedrive odkud
- [ ] Navrhnout flow pro bizmachine aktualizace
- [ ] Navrhnout meeting prep / sales feed info modul
- [ ] Řešit historii kontaktních osob při přechodech mezi firmami
- [ ] Implementovat v RB Universe
- [ ] Otestovat a nasadit

### PD4 — Ninjabot: projít smlouvy / služby, rozhodnout vypověď
**Next | Q2 | ICE I6 C7 E5 = 8.4**
Projít 6 dokumentů z Pipedrive Ninjabot; zmapovat co platíme; rozhodnout vypověď vs. ponechat.
_Analýza: [[02-PROJEKTY/pipedrive-a-dalsi-nastroje/2026-05-21-analyza-ninjabot-mesicni-fakturace|měsíční fakturace]] · [[02-PROJEKTY/pipedrive-a-dalsi-nastroje/2026-05-20-analyza-ninjabot-smlouvy|inventář]] · PDF: `ninjabot/`_
- [x] **1.** Inventář 6 dokumentů + měsíční platba (PDF, analýza, Allfred 3 650 Kč/měs) — 2026-05-21
- [x] **2.** Sync s Pavlem Kroupou — které závazky jsou aktivní — 2026-05-21
- [x] Stáhnout 6 PDF do `ninjabot/` (2026-05-20)
- [x] Analýza měsíční fakturace (doc 3–6) — 2026-05-21
- [x] Ověřit měsíční částku v RB Universe / Allfred — **3 650 Kč/měs** (mix tarifů, 2026-05-21)
- [ ] Rozhodnutí: vypovědět / ponechat / přejít — zapsat výsledek sem
- [ ] Pokud vypověď → notice period + komunikace s Ninjabotem
_Zdroj: [[07-ARCHIV/inbox-processed/2026/05/slack/2026-05-20-1257-_claude-capture-do-projektu-pipedrive-ovit-sluby-od-ninjabotu-a-pp|Slack capture 20. 5.]]

## Recently moved to HOTOVO

- **PD1** — Implementovat formulář pro medailonky (varianta 2) ✅ _(2026-05-20)_

