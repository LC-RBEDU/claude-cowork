# Téma: Vibe coding

**Slug**: `vibe-coding`
**Vznik**: 2026-05-03
**Posledně aktualizováno**: 2026-05-05
**Owner**: Lukáš

## Kontext

Rychlé AI-asistované prototypování a vývoj — prompt-to-code přístup, kdy výstupem je funkční MVP bez klasického software developmentu. Vlastní projekty, experimenty, inspirace a sledování toho, co dělají ostatní v tomto prostoru.

Sem patří: vlastní vibe-coding projekty, tooling, inspirační zdroje, lidi ze sítě kteří to dělají zajímavě, a případné propojení s interními projekty (RB Universe, PM feature atd.).

**Hranice**:
- vůči `rb-universe-development.md` — tam je konkrétní development RB Universe; tady jsou broader vibe-coding aktivity a inspirace
- vůči `strategy.md` — pokud se vibe-coding stane strategickou sázkou firmy, patří tam; tady je praktická/osobní rovina

---

## Aktivní úkoly

### V2 — Fix n8n: extrakce obsahu Google Doc z emailu
**Q3**
Pipeline pro automatické stahování obsahu Google Docs z přeposlaných emailů selhává. Chyba: `helpers.httpRequestWithAuthentication` není podporováno v Code Node.
- [ ] Zkontrolovat OAuth scope Google Drive credential v n8n
- [ ] Ověřit, zda je dokument sdílený se stejným Google účtem jako drive credential v n8n
- [ ] Nahradit Code Node za nativní n8n Google Drive node nebo HTTP Request node
_Zdroj: INBOX/email 5. 5. 2026_

---

## Backlog (nápady, ještě ne aktivní)

### V1 — Karpathy vibe coding guidelines pro Cursor
Prostudovat repo forrestchang/andrej-karpathy-skills, soubor `.cursor/rules/karpathy-guidelines.mdc` — vytáhnout principy.
- [GitHub — karpathy-guidelines.mdc](https://github.com/forrestchang/andrej-karpathy-skills/blob/main/.cursor/rules/karpathy-guidelines.mdc)
_Zdroj: Slack capture 3.5._

---

## Otevřené otázky / čeká na data

_(žádné)_

---

## Materiály a poznámky

_(žádné)_

---

## Recently moved to HOTOVO

_(žádné)_
