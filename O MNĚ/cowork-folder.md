# Cowork „second brain" — kanonická cesta

Tato složka (`CLAUDE COWORK`) je Lukášův hlavní pracovní hub a paměť. Pokud čteš tento soubor, nejspíš už ji máš připojenou — ale pro jistotu si zapamatuj absolutní cestu, abys ji v budoucích sessions uměl/a vyžádat hned na začátku.

## Absolutní cesta (macOS, lokálně)

```
/Users/lukascypra/Library/CloudStorage/GoogleDrive-lukas@redbuttonedu.cz/.shortcut-targets-by-id/12xJBQTYKiG9t9zmnexRWocfkB5PCKkxi/CLAUDE COWORK
```

> Cesta vede přes Google Drive shortcut — ID `12xJBQTYKiG9t9zmnexRWocfkB5PCKkxi`. Složka je sdílená, takže shortcut ID je stabilní.

## Postup na startu každé nové session

1. Pokud složka `CLAUDE COWORK` ještě není připojená, vyžádej ji přes nástroj `request_cowork_directory` s **přesně touto cestou**.
2. Přečti všechny soubory v `O MNĚ/` (včetně tohoto).
3. **Nečti** `VÝSTUPY/` ani `ŠABLONY/`, dokud o to Lukáš nepožádá.
4. Výstupy ukládej do `VÝSTUPY/<projekt>/`.
5. Když si nejsi jistý/á zadáním, ptej se. Nevymýšlej si.

## Struktura složky

- `O MNĚ/` — informace o Lukášovi a jeho systémech (about-me, agenda, anti-AI tooling cheat-sheet…)
- `INBOX/` — vstupy / nezpracované materiály
- `AGENDA/` — live projektová agenda
- `HOTOVO/` — uzavřené projekty
- `VÝSTUPY/` — finální výstupy v podsložkách podle projektu
- `ŠABLONY/` — šablony
- `Cursor/`, `.cursor/` — IDE artefakty, ignoruj
- `io.rbedu.claude-cowork-push.plist`, `push-artifacts.sh` — synchronizační skripty (neřeš, pokud o to není požádáno)
