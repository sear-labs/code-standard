# New machine? Paste this into Claude Code.

You found this on GitHub, which means you already have the only thing you need: the URL.

Open Claude Code on the new machine, in any folder, and paste the block below. It sets the
machine up in four steps and changes nothing else.

**What it will do:** set git's default branch to `main`; clone this repository somewhere you
choose; append a pointer to `~/.claude/CLAUDE.md` without overwriting what is already there;
and read Part 0. It will not copy the standard into your projects — that is the one thing this
standard asks you not to do, and Part 0 explains why.

---

```
You are setting up a NEW MACHINE to follow the SEAR Lab code and teaching standard.

The standard is ONE document, public, and is POINTED AT — never copied:

    https://github.com/sear-labs/code-standard

Do these four things. Verify each by its RESULT, not by the command exiting cleanly.

1. Read the WHOLE standard, once, now — all of it, not only the parts named here:
   https://raw.githubusercontent.com/sear-labs/code-standard/main/CLAUDE.md

   It is one document on purpose and its halves contradict each other on purpose, so
   reading a section in isolation is how people confidently do the wrong thing.

   Two parts matter most on a first read. **Part 0** governs steps 2-4 below and explains
   why nothing is copied. **Part 4** is the one the standard itself says to read if you
   read nothing else. After today, "read it first and last" applies every time you work
   in a project folder — not just at setup.

2. Make git agree with every convention around it:
       git config --global init.defaultBranch main
   Verify: `git config --global init.defaultBranch` returns `main`. Without this, git
   creates `master` while every badge, tool and URL assumes `main`.

3. Clone the standard for speed and offline reading. The clone is a convenience, never
   the address:
       git clone https://github.com/sear-labs/code-standard.git
   Ask me where to put it. Prefer a path OUTSIDE a syncing folder (OneDrive, Dropbox,
   Google Drive) — a .git tree under a second syncing system causes churn and conflicts.

4. Add a pointer to `~/.claude/CLAUDE.md`, the file that loads in every session in every
   folder. **APPEND — do not overwrite.** That file may already hold facts about this
   machine (interpreter paths, tool versions, which credentials are set) and all of it
   must survive. If a pointer to sear-labs/code-standard is already present, change
   nothing and say so.

   The block to add:

       # THE RULES ARE NOT IN THIS FILE
       # This file holds facts about THIS MACHINE. It holds no portable rules,
       # deliberately.
       #
       # Every rule lives in one document:
       #   https://github.com/sear-labs/code-standard  canonical, public - no auth
       #   <path to your local clone>                  faster, optional
       #
       # Read it first and last. Do not restate it here or anywhere else.

Then tell me what you changed and what was already correct.

DO NOT copy the standard's CLAUDE.md into project folders. A project's CLAUDE.md names
the URL and adds only what is true of that project, under `Part 11 - This project
specifically`. Copying is what this standard replaced; Part 0 says why.

If you find something the standard gets wrong or fails to cover, do NOT edit it. See
Governance in Part 0: write the proposed text out in full and petition. A pull request
is the petition from outside; it does not merge itself.
```
