# Code Standard — a drop-in kit

Copy this folder's contents into any new project. Nothing here depends on
anything outside this folder.

## What's here

| File | What to do with it |
|---|---|
| `CLAUDE.md` | The standard. Copy it to a repo root **as `CLAUDE.md`** — that filename is what Claude Code reads automatically every session. |
| `gitignore-starter` | Rename to `.gitignore` and commit it **first**, before any other file. |
| `README.md` | This. Don't copy it. |

## Three ways to use the standard

1. **A code repo** — copy `CLAUDE.md` to the repo root. Append a final
   "This project specifically" section for the things that are true only there:
   credentials that must never be committed, licence or runtime limits, which
   file is the template to copy, known open defects. Everything above that
   section stays generic, so it can be replaced wholesale when this is updated.
2. **Every repo on the machine** — put it at `~/.claude/CLAUDE.md`. Note it is
   ~511 lines; if you already keep environment notes there, keep those separate
   and reference this instead.
3. **A non-code chat** — paste it into a Claude Project's custom instructions.
   For a one-off chat, Part 10's prompt block is the short version.

## Starting a new project

> *"Scaffold this as a [archetype] per CLAUDE.md."*

Pick the archetype from Part 2's table. For a teaching notebook:

> *"Teaching-code style per CLAUDE.md Part 3."*

## The order that matters

Do these in this sequence, because one of them cannot be undone:

1. `git init`
2. `cp gitignore-starter .gitignore`, add anything project-specific
3. **`git check-ignore -v <each secret file>`** — verify, don't assume the
   pattern matched
4. `git add . && git status` — read the list before committing
5. First commit

A credential in git history means rotating the credential, not amending the
commit. Everything else in the standard is a preference you can revisit later;
this one isn't.

## If you read only one section

**Part 4.** It is the boundary between the engineering half (Parts 1–2) and the
teaching half (Part 3), which contradict each other on purpose. Someone who reads
only one half will confidently refactor the other half in the wrong direction.
