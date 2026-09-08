# Getting started — your first week

*For students and new members of SEAR Labs. Written 2026-09-08.*

**This page is not the rules, and it does not summarise them.** It is a list of actions for your
first week. The rules are [`CLAUDE.md`](CLAUDE.md) in this repository, and it governs.

Read **Part 1** (nine short items) and the **table at the top of Part 2**. That is the whole
reading assignment for now. Everything else in that document exists because somebody got it
wrong once; you will be sent to the relevant Part when you reach it.

---

## Four things to do this week

### 1. Name the repository before you create it

A name freezes into every link anyone copies out of the repo. Renaming later redirects the
repo and redirects nothing that has already been copied.

    research code     subject-method          lithium-optsc
    course material   method-application      advopt-lithiumsc

Lowercase, hyphens, American spelling, numbers zero-padded. The two forms are inverted on
purpose — Part 1, *Repository names lead with what the searcher already knows*, says why.
**If you are unsure which form you are in, ask before creating it, not after.**

### 2. Create it in the organisation, private

```bash
gh repo create sear-labs/<name> --private --clone
```

Not on your personal account. `sear-labs` is where it lives so that it survives you
graduating, and so Jones can read it without being added to anything.

**Private is the starting state, not a permanent one.** See *How a repo grows up* below.

### 2b. You are Archetype A. Make these directories on day one.

Every project starting now is **Archetype A — batch analysis pipeline**. You will read the
Part 2 table eventually; you do not need it today. Make this shape before you write code:

    config.yaml              parameters, paths, thresholds - never hardcoded in a module
    data/raw/                what came from outside. READ-ONLY. Nothing writes back to it.
    data/interim/            partly processed
    data/processed/          what analysis reads
    src/<pkg>/               importable functions - the model lives here, not in __main__
    scripts/run_all.py       the one command that reproduces everything
    notebooks/               exploration and narration
    results/figures/         generated
    results/tables/          generated
    tests/                   at minimum: does it run, and are the outputs sane
    pyproject.toml           so `pip install -e .` works

**One exception, and it is the person collecting physical data.** If your project *captures*
measurements from equipment, you are **Archetype F**, not A, and the difference starts on day
one: every raw file needs a sidecar recording instrument, operator, calibration, conditions and
software version. That cannot be added later — nobody remembers a calibration three months on,
and a run cannot be re-collected. Everyone else: Archetype A.

**Three data tiers, one direction, never one merged `output/` folder.** This is the item that
cannot be retrofitted: if everything lands in one folder for six months, what derived from what
is gone, and no amount of later tidying recovers it.

### 3. Write `.gitignore` before the first commit — and verify it

This is the one mistake in the standard that cannot be undone. Git history is permanent: a
key or a dataset committed once is in the repository forever, and deleting it in a later
commit does not remove it.

```bash
# write .gitignore FIRST — data/, .env, *.csv, whatever your project produces
git check-ignore -v data/raw/something.csv     # must print the matching rule
git add . && git commit
```

`check-ignore` is not optional. Do not assume the pattern matched — make it say so.

### 4. Push every week, even when it is broken

A repo that appears the week before a deadline is not a record of the work. Weekly pushes
are how the work becomes reviewable, and how a wrong turn gets caught in week three instead
of month four.

---

## How a repo grows up

Private and rough is the correct state for a new project. It becomes public when it is
finished, not before. What changes in between:

| Stage | What must be true |
|---|---|
| **Day one** | The name is right. `.gitignore` is verified. `LICENSE` is present (MIT unless Jones says otherwise). The folder shape matches your archetype. |
| **Working** | One command runs the whole thing. Parameters live in a config file, not in the code. Nothing writes back to raw input. |
| **Shareable** | A stranger can follow the README and run it. There is a test that fails when the output is wrong. Dependencies are pinned. |
| **Public** | It runs from a clean clone on a machine that is not yours. Tagged. Citable. |

**The day-one items are the ones that are expensive later.** The rest are cheap to add when
you get there, and pretending to have them early is worse than not having them.

**Say where you are, in the README, in one line.** `Status: working — not yet reproducible
from a clean clone.` A half-finished repo with no status line is indistinguishable from a
finished repo that is broken, and the second is what a reader will assume.

---

## If you are using Claude Code — paste this

Open a session **in the empty folder you just cloned**, and paste this as the first message.
Do not paste it into a chat rooted somewhere else; the folder you open decides where everything
lands.

> Read <https://github.com/sear-labs/code-standard>. Read **Part 1** and **Part 2** only —
> skip Parts 3, 4 and 5, which are about teaching material, and skip Archetype P, which is
> about reimplementing a published model. I am **Archetype A**.
>
> Then, in this folder, and in this order:
>
> 1. Write `.gitignore` first, before anything is committed. It must ignore the *contents* of
>    `data/` while still tracking a `.gitkeep` in each tier, so the shape survives a clone —
>    `data/**`, then `!data/**/`, then `!data/**/.gitkeep`. It must also cover `.env`, virtual
>    environments and notebook checkpoints. Then run `git check-ignore -v` against a real data
>    file and show me the output. Do not proceed until it prints a match.
> 2. Create the Archetype A directory shape, with a `.gitkeep` in each empty directory.
> 3. Write `pyproject.toml` so `pip install -e .` works. Pin every dependency with an upper
>    bound, e.g. `pandas>=2.0,<4`.
> 4. Write `config.yaml` holding my parameters and paths. Nothing hardcoded in a module.
> 5. Write `scripts/run_all.py` as the single entry point, even if it currently does nothing.
> 6. Write `tests/test_smoke.py` asserting whatever must be true of any correct output of my
>    project — totals that balance, quantities that cannot go negative. Ask me what those are
>    rather than guessing.
> 7. Write `README.md` with a `Status:` line saying the project is in progress, and how to run
>    it.
> 8. Write `CLAUDE.md` in the root: one line pointing at the standard's URL, one line naming
>    Archetype A, and one line saying what the project is.
>
> Show me the diff before committing. Do not commit anything you have not shown me.

**Check the diff yourself before it commits.** The assistant will follow a shape it can see and
invent one it cannot. "The AI put it there" is not a reason a file is in the right place, and
this is your repository.

## If you are not using an AI assistant

Same eight steps, by hand, in the same order. Order 1 is the one that matters — `.gitignore`
before the first commit is the only item on this page that cannot be fixed later.

```bash
gh repo create sear-labs/<name> --private --clone
cd <name>
cat > .gitignore <<'EOF'
data/**
!data/**/
!data/**/.gitkeep
.env
.venv/
__pycache__/
.ipynb_checkpoints/
EOF
mkdir -p data/{raw,interim,processed} src scripts notebooks results/{figures,tables} tests
find data results -type d -exec touch {}/.gitkeep \;
git check-ignore -v data/raw/<a real data file>   # must print a rule; if it prints nothing, STOP
git add . && git commit -m "Initial structure"
git push
```

Then write `pyproject.toml`, `config.yaml`, `scripts/run_all.py`, `tests/test_smoke.py` and
`README.md` as you go. They can be nearly empty on day one — they cannot be absent on day sixty.

---

## What to bring to the next meeting

1. The repo URL.
2. Which archetype you picked, and one sentence on why.
3. The single command that runs your project — even if it currently fails.
