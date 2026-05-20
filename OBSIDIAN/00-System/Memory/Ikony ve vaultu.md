# Ikony ve vaultu MrLUC (Iconize)

> Plugin v Obsidianu: **Iconize** (ID v souboru: `obsidian-icon-folder` — starý název složky, aktuální plugin je Iconize 2.x).

Konfigurace je v [`.obsidian/plugins/obsidian-icon-folder/data.json`](../../.obsidian/plugins/obsidian-icon-folder/data.json) a syncuje přes iCloud.

## Zapnutí

1. Settings → **Community plugins** → **Iconize** musí být **Enabled** (v `community-plugins.json` je `obsidian-icon-folder`).
2. Settings → **Iconize** → Icon packs: **Lucide (native)** — `lucideIconPackType: native` (už nastaveno).
3. Po změně `data.json`: **Reload vault** (Command palette → „Reload app without saving“) nebo restart Obsidianu — ikony se aplikují při načtení file exploreru.

## Co je nastaveno

### Složky top-level (přímá cesta)

| Cesta | Ikona | Význam |
|-------|-------|--------|
| `Home.md` | LiHouse | Vstupní bod vaultu |
| `00-System` | LiSettings | Systém, dashboard |
| `01-INBOX` | LiInbox | Capture |
| `02-PROJEKTY` | LiFolders | Projekty |
| `03-AREAS` | LiCompass | Oblasti (PARA) |
| `05-RESOURCES` | LiLibrary | Reference |
| `06-Canvas` | LiLayout | Canvas |
| `07-ARCHIV` | LiArchive | Archiv |

### Custom rules (hub vs. výstupy)

| Priorita | Pravidlo | Ikona | Platí pro |
|----------|----------|-------|-----------|
| 0 | [[02-PROJEKTY/Finance]] | LiLandmark | Hub Finance |
| 1 | `^02-PROJEKTY/[^/]+\.md$` | LiLayoutDashboard | **Hub** — `.md` přímo v `02-PROJEKTY/` |
| 2 | `^02-PROJEKTY/finance$` | LiWallet | Složka výstupů Finance |
| 3 | `^02-PROJEKTY/[^/]+$` | LiPackage | **Výstupy** — první úroveň podsložek projektu |
| 4 | `^02-PROJEKTY/finance/.+` | LiFolderOpen | Podsložky pod Finance (`cfo/`, `bankovni-ramce-fio/`) |

## Hub vs. složka se stejným slugem

- **`finance.md`** → LiLandmark (výjimka) nebo LiLayoutDashboard (ostatní projekty).
- **`finance/`** → LiWallet; podadresáře → LiFolderOpen.

## Ruční úprava ikony

Pravý klik na soubor/složku v exploreru → **Change icon** (Iconize). Uloží se do stejného `data.json` pod cestou souboru.

## Finder (Mac, volitelné)

Barevné tagy — jen lokální, nesyncuje do mobilu.

## Poznámka k „Icon Folder“

Community plugin se jmenuje **Iconize**; složka pluginu zůstává `obsidian-icon-folder`. Nepřidávej starý plugin „Icon Folder“ — není to samostatný produkt.

