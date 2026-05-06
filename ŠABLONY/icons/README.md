# Cowork ikony pro Slack

3 varianty, všechny 128×128 PNG, warm clay barva (`#D97757`).

## Volby

| Soubor | Vzhled | Sémantika |
|--------|--------|-----------|
| `cowork-inbox.png` | Šipka dolů + inbox tray | "Pošli to do Cowork inboxu" — doslovný význam reakce |
| `cowork-c.png` | Bold "C" lettermark | Cowork = první písmeno, čisté, dobře čitelné v 32×32 |
| `cowork-bookmark.png` | Bookmark/flag | "Uloženo, vrátím se k tomu" — abstraktnější |

SVG zdroje vedle PNG (kdybys chtěl upravit).

## Instalace do Slacku

1. Slack → workspace name (vlevo nahoře) → **Customize > Customize Workspace**
2. Záložka **Emoji** → **Add Custom Emoji**
3. Upload PNG, **Name**: `cowork`
4. Save

## Doporučení

- Začni s **`cowork-inbox.png`** — je sémanticky nejjasnější (šipka do inboxu = "ulož to")
- Pokud chceš diskrétnější vzhled, **`cowork-bookmark.png`**
- Pokud preferuješ wordmark, **`cowork-c.png`**

Můžeš mít i víc reakcí naráz (např. `:cowork:` pro běžné capture a `:cowork-urgent:` pro Q1 — n8n workflow by se rozšířil o filter podle emoji name a přidal by kvadrant Q1 rovnou do hlavičky .md souboru).
