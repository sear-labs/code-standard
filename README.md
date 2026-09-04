# Code and Teaching Standard

The engineering and teaching conventions for the SEAR Lab (Erick C. Jones Jr., IMSE, UT Arlington).

> ### New machine?
> **[NEW-MACHINE.md](NEW-MACHINE.md)** — a prompt to paste into Claude Code. It sets git's default
> branch, clones this repo, and adds the pointer to your global `CLAUDE.md` without overwriting it.

**This document is pointed at, never copied.** A project's own `CLAUDE.md` names this repository and
then adds only what is true of that project, under a heading `Part 11 — This project specifically`:

```
# <Project> conventions

The portable standard governs this repo. Read it before working here:
  https://github.com/sear-labs/code-standard    canonical - the same from any machine
  a local clone, if you have one                faster

# Part 11 - This project specifically
...archetype, data layout, known defects, exemptions...
```

**Read it first and last.** First because it decides how the work is done; last because a change you
are about to make may be one it already settles.

## Why pointing rather than copying

Copying is the obvious mechanism — Claude Code loads `CLAUDE.md` automatically and does not load
this repository, so a drop-in copy guarantees the rules arrive. Measured across two days in
September 2026, that guarantee cost more than it bought: one project's copy ran 46 lines behind,
another 28 behind *while appearing stamped with a source version*, and four scaffolding templates
carried not a stale copy but this document's **predecessor**, a whole generation behind. Nothing
reported any of it.

A pointer costs one deliberate read, cannot drift, and cannot be edited into a competing authority.

> **A subordinate document may point at this one. It may never restate it** — not a summary, not a
> quick-reference table. A partial restatement reads as complete and stops the search.

## What is here

| File | |
|---|---|
| `CLAUDE.md` | The standard. Read it; do not copy it. |
| `gitignore-starter` | Rename to `.gitignore` and commit it **first**, before any other file. |

## The order that matters when starting a project

One of these cannot be undone, so the sequence is not cosmetic:

1. `git init`
2. `cp gitignore-starter .gitignore`, add anything project-specific
3. **`git check-ignore -v <each secret file>`** — verify the pattern matched; do not assume
4. `git add . && git status` — read the list before committing
5. First commit

**A credential in git history means rotating the credential, not amending the commit.** Everything
else in the standard is a preference you can revisit; this one is not.

## If you read only one section

**Part 4** — the boundary between the engineering half (Parts 1–2) and the teaching half (Part 3),
which contradict each other on purpose. Someone who reads only one half will confidently refactor
the other in the wrong direction.

## How to cite

```bibtex
@software{jones_code_teaching_standard,
  author  = {Jones, Jr., Erick C.},
  title   = {Code and Teaching Standard},
  url     = {https://github.com/sear-labs/code-standard},
  year    = {2026}
}
```

BibTeX reads a three-part name as `Last, Jr, First`, so the suffix goes in the middle field. Written
as `{Jones, Erick C., Jr.}` it parses the given name as the suffix.

MLA works-cited:

> Jones, Erick C., Jr. *Code and Teaching Standard*. 2026, github.com/sear-labs/code-standard.

See `CITATION.cff`. Licensed MIT — see `LICENSE`.
