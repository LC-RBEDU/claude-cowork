# Agenda skills — instalace

3 skills, které pohánějí Agenda systém:

- **`agenda-capture`** — bere střípky odkudkoli, navrhuje téma + metadata, ukládá do AGENDA
- **`agenda-triage`** — projetí INBOXu, batch nebo deep mód
- **`agenda-co-ted`** — ad-hoc dashboard "co dnes řešit"

## Jak je nainstalovat

Cowork bere skills z `~/.claude/skills/` na hostiteli (Mac). Pro každý skill:

```bash
# Vytvoř adresář pro skill
mkdir -p ~/.claude/skills/agenda-capture

# Zkopíruj SKILL.md ze ŠABLONY do skill složky
cp "/Users/lukascypra/Library/CloudStorage/GoogleDrive-lukas@redbuttonedu.cz/.shortcut-targets-by-id/12xJBQTYKiG9t9zmnexRWocfkB5PCKkxi/CLAUDE COWORK/ŠABLONY/skills/agenda-capture/SKILL.md" ~/.claude/skills/agenda-capture/SKILL.md

# Stejně pro triage a co-ted
mkdir -p ~/.claude/skills/agenda-triage
cp "/Users/lukascypra/Library/CloudStorage/GoogleDrive-lukas@redbuttonedu.cz/.shortcut-targets-by-id/12xJBQTYKiG9t9zmnexRWocfkB5PCKkxi/CLAUDE COWORK/ŠABLONY/skills/agenda-triage/SKILL.md" ~/.claude/skills/agenda-triage/SKILL.md

mkdir -p ~/.claude/skills/agenda-co-ted
cp "/Users/lukascypra/Library/CloudStorage/GoogleDrive-lukas@redbuttonedu.cz/.shortcut-targets-by-id/12xJBQTYKiG9t9zmnexRWocfkB5PCKkxi/CLAUDE COWORK/ŠABLONY/skills/agenda-co-ted/SKILL.md" ~/.claude/skills/agenda-co-ted/SKILL.md
```

Pak restart Cowork session — skills se načtou a začnou triggerovat na popis (`description` ve frontmatteru).

## Jak otestovat

V chatu:
- *"Co teď?"* → měl by se spustit `agenda-co-ted`
- *"Hoď do agendy: nápad — ReBeL by mohl mít integraci se Slackem"* → měl by se spustit `agenda-capture`
- *"Projeď inbox"* → měl by se spustit `agenda-triage`

Pokud se skill nespustí, řekni explicit: *"použij skill agenda-capture"* a sleduj, kde to nedotáhlo.

## Update skills

Když cokoli upravím v ŠABLONY/skills/`<skill>`/SKILL.md, znovu spusť `cp` výše. Případně si na to udělej alias:

```bash
alias agenda-skills-sync='for s in agenda-capture agenda-triage agenda-co-ted; do cp "/Users/lukascypra/Library/CloudStorage/GoogleDrive-lukas@redbuttonedu.cz/.shortcut-targets-by-id/12xJBQTYKiG9t9zmnexRWocfkB5PCKkxi/CLAUDE COWORK/ŠABLONY/skills/$s/SKILL.md" ~/.claude/skills/$s/SKILL.md; done'
```
