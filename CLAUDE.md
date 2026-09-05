# CODE AND TEACHING STANDARD

*Portable. Nothing below is specific to one course, language, library or project.*

**How to use this:**
- Drop it in a repo root as `CLAUDE.md` — Claude Code reads it automatically every session.
- Or put it at `~/.claude/CLAUDE.md` to apply to every repo on the machine.
- Or paste it into a Claude Project's custom instructions for non-code chats about the work.

When starting a new repo: *"Scaffold this as a [archetype] per CLAUDE.md."*
When starting a teaching notebook: *"Teaching-code style per CLAUDE.md Part 3."*

---

## Part 0 — What this document is, and why it is one document

This merges two standards that are each correct and that **contradict each other
in two specific places**:

- **Engineering conventions** (Parts 1–2): how to build something reproducible.
- **Teaching code standard** (Part 3): how to write code somebody learns from.

They were previously separate files. That was the mistake. An assistant — or a
person — reading only the engineering half will "clean up" a teaching notebook in
exactly the wrong direction, and reading only the teaching half will ship research
code with no tests and unpinned dependencies. **Part 4 is the boundary between
them and is the most important section here.** If you read nothing else, read
Part 4.

### How this document reaches a project: it is pointed at, never copied

**There is one of this file.** It lives at `sear-labs/code-standard` and nowhere else. A project
does not hold a copy of it; a project holds a `CLAUDE.md` that *names* it and then adds what is
true of that project alone:

    # <Project> conventions

    The portable standard governs this repo. Read it before working here:
      https://github.com/sear-labs/code-standard    canonical - same from any machine
      a local clone, if you have one                faster; e.g. C:\Users\<you>\repos\code-standard

    # Part 11 - This project specifically
    ...archetype, data layout, known defects, exemptions...

**Read it first and last.** First, because the rules here decide how the work is done. Last,
because a change you are about to make may be one this document already settles.

**Lead with the URL, not with a path.** An absolute path is true of one machine and silently wrong
on every other, so it must never be the only pointer. The repository URL is the reference that
travels — to a laptop, to a collaborator, to a session running somewhere else. Name a local clone
as a convenience underneath it, never as the address.

**Clone outside any syncing folder.** On Windows, Known Folder Move redirects `Documents` and
`Desktop` into OneDrive, so a path beginning `Documents\` **is** a synced path while reading as a
safe default. A `.git` tree under a second syncing system is the hazard, and the example above used
to model exactly what it warns against.

**A clone can be clean and still wrong.** A working copy sitting on a feature branch reads exactly
like this document — same filename, same path, no warning — while serving text nobody has approved.
Observed 2026-09-05: the maintainer's own working copy sat on a branch at 1,492 lines against
`main`'s 1,417, with a clean tree, presenting **75 lines of unadopted text as adopted.**

So the branch is part of the address, and this is the same defect as `owner/repo` reading as a whole
URL when it is two-thirds of one:

    owner / repo / branch / path

**Check the branch before you quote a clone**, and pull after. A convenience is only a convenience
while it matches; the moment it does not, it is an authority that disagrees with the authority.

#### Why a pointer and not a drop-in copy

Copying is the obvious mechanism — `CLAUDE.md` loads automatically and the standard does not, so a
copy guarantees the rules arrive. **Measured over two days, that guarantee cost more than it
bought.** One project's copy ran 46 lines behind; another ran 28 behind *while appearing stamped*;
four scaffolding templates carried not a stale copy but this document's **predecessor**, a whole
generation behind, and nothing reported any of it.

A pointer costs one deliberate read. It cannot drift, it cannot be edited into a competing
authority, and it needs no sync rule and no version stamp — both of which existed only to manage a
problem that copying creates.

> **A subordinate document may POINT at this one. It may never RESTATE it** — not a summary, not a
> quick-reference table, not “the short version for convenience.”

That rule is the load-bearing one. Every rule that went missing in two days went missing inside a
document that *summarised* this one instead of naming it, and **a partial restatement is worse than
no restatement, because it reads as complete and stops the search.**

### Merge policy across the organization

This document's own gate is the tightest in the org and **should not be copied everywhere by
reflex.** Gate on **how much depends on a repo**, not on what kind of thing it is.

Nobody is a bottleneck by virtue of having created a repo. GitHub permissions are role-based, and
the protection config is the only thing that decides who lands a change.

| | What a bad merge reaches | Who merges |
|---|---|---|
| This standard | every project, forever | Jones only |
| The teaching library | every course drawing on that topic, every year | Jones only |
| A published paper repo | one frozen release, plus errata | Jones **and the coauthors** |
| Active research | the work of everyone on that project | **the project team**, Jones included |

**Jones can merge anywhere** — he owns the organisation, and no table grants or removes that. The
column says who *else* can, which is the only part that is a decision. A research project with four
people on it is not gated to whoever ran `git init`.

**The teaching library sits beside this document, not below it.** It is organised by topic rather
than by course or semester, so one notebook serves several courses across several years and an
error in it propagates the way a bad rule here would. TAs and students who teach **propose**;
they do not merge.

**If it consolidates observations about student work it is education-record adjacent**, not merely
internal. Keep it private, keep names and rosters out of it, and let that decide visibility before
convenience does.

#### The published-paper case is looser than it looks, deliberately

The instinct is to lock a paper repo read-only. That is backwards. **A Zenodo DOI is minted against
a tagged release, not a branch**, so the artifact anyone cites is already frozen — locking the
branch buys nothing and costs the ability to publish errata.

    the release    frozen; this is what is cited
    the branch     stays open; corrections land here
    a correction   new tag -> new version DOI; the concept DOI follows it automatically

**A pull request is also the credit mechanism.** Someone who finds a mistake and opens one is
recorded permanently as the author of that change, which an email is not. Merge it, then credit
them in the release notes and `CITATION.cff`. **Locking the branch pushes them back to email, where
the credit evaporates.**

**When a paper repo is genuinely finished, archive it.** GitHub's archive makes the whole repo
read-only and is reversible. It says *this work is complete* rather than *this branch is defended*,
and it belongs after the errata window rather than instead of one.

#### Contributions from outside the organisation are safe by construction

**A fork is their copy. A pull request is a proposal against yours.** With `main` protected and the
author not a collaborator, nothing they do reaches the deployed repo until someone with merge rights
lands it. Public visibility therefore costs **triage, not safety** — and the asymmetry is heavily
one-sided: closing a junk PR takes seconds, while a good one is something you would never otherwise
have received.

So the question is never *“will they break it”*. It is whether the repository should be readable at
all, which is a separate decision with separate reasons.

#### Which is what actually decides the teaching library: split it

Two different things get called teaching material and they want opposite visibility:

    notebooks, code examples, topic material   public. Takes outside PRs; they cost nothing and
                                               occasionally find a real error.
    consolidated observations on student work  private. Education-record adjacent, so no outside
                                               contribution is wanted and none is possible.

**Keeping them in one repository forces the stricter rule onto both** — the whole library goes
private to protect the observations, and the notebooks lose every reader and every correction they
would have attracted. Splitting costs one extra repository and settles the visibility question
honestly instead of by compromise.

Merge rights do not change either way: Jones only, on both.

#### Blocking is access, not protection

Branch protection decides who **merges**. It does not decide who may push a branch at all — that is
repository access, and access is the control for keeping casual contributions out.

    not a collaborator   cannot push a branch. On a public repo may still fork and open a PR,
                         which you are free to close.
    write collaborator   may push a branch and open a PR; protection still decides the merge.
    private repo         not visible at all.

So *“regular students should not be committing here”* is answered by **not adding them as
collaborators**, never by tightening a branch rule.

#### On a free plan, protection is public-repo only

Private repositories cannot be branch-protected without a paid plan. That affects active research,
which is also the case that least needs gating — the people writing it own it. **Do not make a repo
public to gain protection it does not need.**


### Setting up a new machine

Two things, once per machine. Nothing is copied and nothing is cloned unless you want the speed.

**1. Make `git init` agree with everything else:**

    git config --global init.defaultBranch main

**2. Put the pointer in that machine's `~/.claude/CLAUDE.md`** — the file that loads in every
session in every folder, and so the only thing guaranteed to be read:

    # THE RULES ARE NOT IN THIS FILE
    # This file holds facts about THIS MACHINE. It holds no portable rules, deliberately.
    #
    # Every rule lives in one document:
    #     https://github.com/sear-labs/code-standard   canonical, public - no clone, no auth
    #
    # Read it first and last. Do not restate it here or anywhere else.

**Optionally** clone it for speed or offline use — a clone is a convenience, never the address:

    git clone https://github.com/sear-labs/code-standard.git

That machine's `~/.claude/CLAUDE.md` then holds **only facts about that machine**: interpreter
paths, tool versions, which credentials are set, connector state. None of that is portable, so none
of it belongs here — and no rule belongs there.

**Nothing else is brought down.** The repository is read, not distributed. If a machine has the URL
it has the standard.

### Governance: how this document changes

**It is the only document that binds.** Notes record reasoning, briefings stage text, project files
describe one project. None of them is authority, and none may override this file.

**To amend it, petition — do not edit locally.** A session that hits something this document gets
wrong or fails to cover writes the proposed text out in full and sends it to whoever holds
`Classes\Code Standard\`, who checks it against what is already recorded and commits it with
provenance in the message. **Sessions do not amend their own working copy of the standard.**

**The floor is two.** Petition once the same thing has been hit by two independent sessions, or
twice by one. Below that it is friction, not a pattern, and a standard that grows on first friction
grows by accretion. *(Set at two on 2026-09-04, to be revisited at three once the current rules
have settled.)*

**The floor governs new rules, not corrections.** Two sightings are the bar for *adding* something.
A document that contradicts itself, or states a rule incompletely, is a **defect** — fix it on one
sighting. Requiring a second is how a known contradiction survives to be found twice.

**Nothing is adopted without Jones's explicit approval.** A peer session cannot authorise an
amendment, and neither can this document's own reasoning.

**Read access is public; write access is not.** Anyone, on any machine, reads this without a clone
or a token. Pushing is restricted to named collaborators. **That asymmetry is the control** —
everyone works from the same document and nobody edits it in passing.

**From outside, a pull request is the petition** — same floor, same approval, and it does not merge
itself. A PR is a proposal with a diff attached, not a change.

**Never edit a clone to fix a problem.** The edit survives until the next `git pull` and then
vanishes with nothing reporting the loss — the same failure as the drop-in copies this document
replaced, one level up.

#### How this is enforced, not merely agreed

`main` is a protected branch:

    every change goes through a pull request      including Jones's own
    only Jones may merge to main                  others open PRs; they cannot land them
    force pushes and branch deletion              blocked

**The merge restriction is the gate — not the approval count.** GitHub lets anyone with read
access submit an approving review and that cannot be turned off, so approvals are set to zero and
made irrelevant. One collaborator approving another's pull request changes nothing, because
approval is not what lands it.

Approvals stay at zero for a second reason: **GitHub refuses to let anyone approve their own pull
request.** Requiring even one approval would permanently deadlock a sole maintainer on their own
amendments.

So the pull request is a **rate limiter and a record**, and the merge restriction is the
authorisation. The first is what stops a run of small changes going in one at a time, each one
quietly invalidating the last — which is how most of the errors in this document's own history were
made, and then found.

---

## Part 1 — The invariant core

These apply to **every** project. If a suggestion conflicts with one of these,
the rule wins unless overridden explicitly.

1. **One command reproduces everything.** `make all`, `pytest`,
   `python scripts/run_all.py` — one documented entry point. If a clean clone
   can't reproduce the outputs, the repo is broken. Highest-value property here.

2. **Configuration lives outside code.** Parameters, paths, thresholds and
   credentials never hardcoded in a module. A scenario change is a config edit,
   never a code edit or a copy-pasted script. *(Part 4 carves out the exception.)*

3. **Dependencies are pinned with upper bounds.** `pandas>=2.0,<4`, not `pandas`.
   An unpinned dependency will one day install a major version with a changed API
   and either break or — worse — silently alter results. Record the interpreter
   version too, and make it match what actually ran.

4. **Inputs are immutable.** Whatever comes from outside is read-only. No stage
   writes back to it. Fix the code and re-run; never lose the original.

5. **Generated files are gitignored — with deliberate, documented exceptions.**
   The exception worth making: commit final figures and results so a reader sees
   outputs without running anything. State it in the README so it reads as a
   choice, not an accident.

6. **Tests exist and CI runs them on a clean machine.** At minimum a smoke test:
   does it run end to end, are the outputs sane. The clean machine matters more
   than the test count — it catches "works on my laptop."

7. **The README says how to run it.** Install, run, expected inputs, expected
   outputs, what's deliberately committed. Written for a stranger, or for you in
   eighteen months.

8. **Commits are meaningful; releases are tagged.** Messages describe *why*. Tag
   anything cited externally or handed to students, so ongoing development never
   invalidates a published result or a link someone is using.

**Never:** commit secrets, credentials, API keys, or unpublishable data.

> **Git history is permanent.** Deleting a file in a later commit does not remove
> it. Add `.env`, `*.lic`, `*_key*`, and data directories to `.gitignore` **before
> the first commit**, and *verify* — `git check-ignore -v <file>` — rather than
> assuming the pattern matched. A credential in history means rotating the
> credential, not amending the commit. This is the one mistake in this document
> that cannot be undone.

### When the sort key and the readable label disagree, carry both

A name has two jobs: sort correctly for a machine, and read correctly for a person. Words rarely do
both. `Spring`, `Summer`, `Fall` sort alphabetically into `Fall, Spring, Summer` — which is not the
order they happen in, so every listing of a multi-term course is wrong and nothing says so.

**Number first for the machine, word second for the person:**

    2026_01_Spring_IE_5301_001
    2026_06_Summer_IE_5301_001
    2026_08_Fall_IE_5301_001

Use the **month the term starts**, not an ordinal 01/02/03. The month is real information: it
survives a term shifting, it matches how the registrar and Canvas already think, and it needs no
key to interpret. An ordinal is an index into a list somebody has to know.

Neither half is sufficient alone. `2026_01` does not read; `2026_Spring` does not sort.

**Research files take the number alone**, because there is no term and no name anyone uses:

    run045-rev01-leo          zero-padded sequence, where order is the point
    2026-09-03-slug           ISO date, where chronology is the point

Both sort natively and need no label. Adding a season to research output invents a discriminator
that does not exist.

**The general rule: use the discriminator that actually distinguishes, and make it sort.** For
course material that is the term. For runs it is the sequence. For records it is the date.

### Repository names lead with what the searcher already knows

    research     subject-method       sear-labs/lithium-optsc
    teaching     method-application   sear-labs/advopt-lithiumsc
    published    add journal + year   sear-labs/lithium-optsc-energies-2024
    websites     website-<name>       personal account
    grad school  gradschool-<name>    personal account

Lab-era research goes under the organization; personal work under the personal account.

**The first two are deliberately inverted, and the inversion is the rule — not the examples.** A
researcher searches by subject; a student searches by course. Each form leads with the half its
audience already has in mind, which is why `advopt-lithiumsc` reads backwards beside
`lithium-optsc` and is nonetheless correct: the student arriving has a course, not a commodity.

**Anyone who “fixes” the teaching form to match the research one has deleted the reason both
exist.** That is the failure this paragraph is here to prevent, and it is why the reason is written
down beside the forms rather than left to be inferred from a pair of examples.

**American spelling** — `optimization`, not `optimisation`. Lowercase, hyphen-separated, numbers
zero-padded. Not a style preference: see the cost below. A name freezes into every badge URL and
every install line in the repo, and those are not corrected by a rename.

### Refer to people by surname

**`Jones`, not `Erick`.** In anything another person reads — this standard, a README, a commit
message, a handoff — the surname is what identifies someone to a reader who does
not already know them, and it is what every citation format uses. A first name is internal
shorthand: it reads as familiarity to the people already in the room and as ambiguity to everyone
else, and a document written in shorthand does not survive being shared.

**In prose, surname alone — no suffix, no honorific, no first name.** `Jones`, not `Jones Jr.`,
not `Dr. Jones`, not `Erick`. Prose does not carry identity metadata.

**When surname alone does not identify one person, escalate — but only as far as it takes.** The
disambiguator differs by case, and reaching for the wrong one does not work:

1. **Surname alone.** `Conlin`. The default, and correct wherever only one person in the document
   carries that surname.
2. **Initial and surname** — two people sharing a surname but not a given name. `G. Conlin` and
   `J. Conlin`, never `Guillermo` and `John`. **If the initials collide too**, use the full given
   name — `John Conlin` and `Jane Conlin` — and only then.
3. **Surname and generational suffix** — two people sharing the surname *and* the given name, where
   an initial disambiguates nothing. `Jones Sr.` and `Jones Jr.` **Not** `E. C. Jones Jr.`: the
   suffix is doing the work, the initials are noise, and the combined form reads as a citation that
   has fallen into a sentence.
4. **The one name you have** — when only one is known. `Bryan`, if that is genuinely all the source
   carries. **Never invent the missing half:** a guessed surname is a misidentification that looks
   authoritative, which is worse than a name that is visibly partial. Say once that it is partial
   — *“Bryan (surname not recorded in the source documents)”* — so a bare first name among
   surnames reads as a limit of the record rather than as familiarity.

**Escalation is scoped to the document, not to the person.** A paper with one Conlin in it uses
`Conlin`; a roster listing both uses `G. Conlin` and `J. Conlin`. **The same person is written
differently in two documents, and that is correct** — the rule serves the reader in front of the
document, not a global registry.

**This governs prose only.** The citation rule below is unchanged.

**In a citation, the full form including the suffix**, because a citation *is* identity metadata and
a dropped suffix makes it the wrong person. Follow MLA: `Jones, Erick C., Jr.`

    CITATION.cff   family-names: Jones / given-names: Erick C. / name-suffix: Jr.
    BibTeX         author = {Jones, Jr., Erick C.}
    MLA            Jones, Erick C., Jr.

**BibTeX reads a three-part name as `Last, Jr, First`** — the suffix is the *middle* field. Written
in MLA order, `{Jones, Erick C., Jr.}`, it silently parses the given name as the suffix and the
suffix as the given name. This is the one place the two formats disagree, and it fails without an
error.

### Published work carries the journal and year

Research repos are named `subject-method` — `lithium-optsc`, `covid-optsc`. **When the work
accompanies a published paper, append the journal abbreviation and year:**

    lithium-optsc-energies-2024
    covid-optsc-ffutr-2021

The suffix does two jobs. It signals at a glance that the repo is a **frozen artifact behind a
publication** rather than active work, and it says **which** publication — which matters when one
project yields several papers.

**Never invent the abbreviation — look it up.** Two people inventing one for the same venue is the
failure this prevents, so every route below ends at an authority.

**1. The DOI stem, where the publisher encodes an alphabetic one.** Elsevier's `j.<code>` and
Frontiers' `f<code>` do:

    10.1016/j.scs.2020.102515     -> scs
    10.3389/ffutr.2021.652185     -> ffutr

**Springer, IEEE and Wiley encode a numeric journal id instead**, and the stem is unusable there:
`10.1007/s10669-021-09838-8` is Springer's journal **number** 10669, not an abbreviation. The rule's
original example happened to be a publisher where the stem works, which is why this gap stayed
invisible.

**2. Otherwise, Crossref's `short-container-title`, reduced to initials** — lowercased, dropping
articles and conjunctions:

    https://api.crossref.org/works/<doi>   ->  message.short-container-title

    "Environ Syst Decis"                  ->  esd
    "Sustainable Cities and Society"      ->  scs

**Reduce to initials rather than to the string itself, because Crossref returns whatever the
publisher deposited** — sometimes the ISO-4 abbreviation, sometimes the full title. The two examples
above are one of each. Initials give the same answer either way, and `scs` derived this way matches
Elsevier's own DOI stem, which is the check that the fallback agrees with rule 1.

**3. No DOI at all — use the venue's own acronym.** Conference proceedings are frequently not
DOI-registered, and a conference *is* known by its acronym, so the acronym is the authority rather
than something derived from it:

    IISE Annual Conference 2020   ->  der-decomp-iise-2020

**The discriminator is *published*, not *has a DOI*.** A DOI test has a false negative: a
peer-reviewed conference paper at a venue that does not register DOIs fails it for a reason that has
nothing to do with its status, and would be filed as coursework beside a homework assignment. Where
a published work has no DOI, rule 3 above carries the suffix.

**The suffix is only for published work.** Unpublished research keeps plain `subject-method`. A repo
with no paper takes no journal — **inventing one would assert a publication that does not exist.**
`houston-covid-gis` carries no suffix because the map was never written up, even though it sits
under the same award as `covid-optsc-ffutr-2021`.

This **composes with** the table above rather than replacing it — the suffix is appended to a name
already formed by those rules, and a teaching repo behind a paper takes it too.

#### Cost of getting it wrong

A repo name freezes **every hosted-notebook badge URL** and **every `pip install git+https://…`
line** in the repo. A rename redirects the repo URL; it does not redirect anything already copied
out of it.

**Count both substitutions before renaming, and count them again immediately before running the
replace.** There are two, and only one looks like a placeholder — `USERNAME` announces itself, while
the hardcoded repo name sits beside it reading like a real name. Measured in one repo on 2026-09-03:
62 and 64 occurrences across git-tracked files, against 78 and 80 including compiled bytecode, which
regenerates and must not be edited. **A replace run against the wrong figure leaves survivors, and
every survivor is a badge pointing at a repo that does not exist** — which presents as a hosting
fault, so the search starts in the wrong place.

---

## Part 2 — Archetypes

Pick one. Each lists only its **delta** from Part 1.

| The output is… | Archetype |
|---|---|
| Files: CSVs, figures, tables | **A** batch analysis pipeline |
| A thing people click through in a browser | **B** dashboard, on top of A |
| Something others import | **C** library |
| Something others call over a network | **D** web service |
| A trained model + metrics | **E** ML sweeps, A plus tracking |
| Measurements from physical equipment | **F** acquisition |
| **Something people learn from** | **T** — see Part 3 |
| **Nothing that runs** — proposals, deliverables, documents | **not a repo** — see Part 2b |

**Answer the last row first.** Most project folders are not repos and should not be given an
archetype at all; **Part 2b** covers their shape. Reaching for one because the table offers seven
is how a proposal folder of Word and Excel acquires a `src/` directory and a test suite nobody
runs.

**A — Batch analysis pipeline** *(default for research code)*
`config.yaml`, `scenarios/`, `data/{raw,interim,processed}/`, `src/<pkg>/`,
`scripts/run_all.py`, `notebooks/`, `results/{figures,tables}/`, `tests/`.
Three data tiers, one-way flow — never one merged `output/` folder, or you lose
track of what derives from what and a plot tweak forces a full recompute. Stages
are importable functions, not logic in `__main__`. `pyproject.toml` so
`pip install -e .` works — required for Colab, and it removes all `sys.path`
fragility. Smoke test asserts the domain invariants — whatever must be true of
any correct output, such as totals that have to balance or quantities that
cannot go negative.

**B — Dashboard.** Keep A underneath; the app is a presentation layer. **It must
not run the model on page load** — precompute into `data/processed/` and have the
app read it. Cache at the load boundary. GitHub Pages cannot host it (static files
only); use Streamlit Cloud, HF Spaces, Render or Fly.

**C — Library.** Drop the data tiers; there is no linear pipeline. Real coverage,
not a smoke test — the public API is a contract. SemVer + `CHANGELOG.md`. Test
across a Python version matrix.

**D — Web service.** Twelve-factor config (environment variables, not
`config.yaml`). Integration tests against real endpoints. Structured logging,
health check, graceful shutdown. Versioned migrations. Containerize.

**E — ML sweeps.** Experiment tracking is not optional: MLflow, W&B, or at minimum
`results/runs/<timestamp>/` holding config + metrics + git SHA. Weights don't
belong in git. Record every seed, and document the tolerance rather than
pretending GPU bit-exactness.

**F — Acquisition.** Raw immutability is critical, not merely good practice — you
cannot re-collect a run. Sidecar metadata per raw file: instrument, operator,
calibration, conditions, software version. `run_all.py` doesn't apply; the
*analysis* is a separate archetype-A project reading acquisition output as raw.

**Mixed projects are normal.** A + B is common. A + C should be *split* into a
library repo with real tests and an analysis repo that depends on it — don't make
one repo satisfy both rigor levels. **A + T is the subject of Part 4.**

## Part 2b — Folders that are not repos

Most project folders should never be repos. Proposal folders are Word, PDF and Excel; git stores
binaries badly and they bloat history permanently. They still need a shape.

### The organising rule

**Separate what ACCUMULATES from what PERSISTS.**

    00-ADMIN/           the folder's own metadata. Zero-prefixed so it sorts first.
    code/               PERSISTS  - scripts and models, subfoldered by variant
    reference/          PERSISTS  - source docs, specs, literature, mappings
    automation/         PERSISTS  - the things that run the above
    verification/       PERSISTS  - checks, and evidence they passed
    2025/  2026/        ACCUMULATES - runs, outputs and deliverables of that year
    design-history/     ACCUMULATES - superseded work, archived by year, not deleted

The test for any new item: **would you look for this by "when", or by "what"?** A 2025 simulation
run is found by when. The script that produced it is found by what. They go in different places even
though they were created the same afternoon.

### State where new work goes, or people will guess

A year folder and a function folder sitting at the same level is ambiguous the moment there is new
code: does it go in `code/` or in `2026/`? **Answer it in the folder's own README rather than leaving
it to instinct**, because two people will resolve it differently and both will be reasonable.

The Green Building answer, which generalises: **code lives in `code/`, with the year in the
subfolder name** — `code/ret-2025/`, `code/treed-opt/`. The year folders hold outputs, never sources.

### `00-ADMIN/` earns the zero

It sorts above everything and holds what governs the folder: the README, the naming standard, the
inventory, the decisions log. Somebody arriving cold reads that first because it is first.

### When a folder becomes a repo

The line is the same granularity rule as Part 2: **a repo is a unit that is versioned, released and
cloned together.** Ask whether anyone would ever want this *without the rest of it*.

    Has code that runs, and someone might clone it          -> repo, archetype A
    Finished outputs - papers, posters, reports             -> stays a folder; deposit to Zenodo
    Active working files                                    -> stays a folder
    Binaries over 100 MB                                    -> can never be a repo; GitHub rejects them

A folder can contain a repo — `code/treed-opt/` may be its own repo inside a working folder that is
not. That is normal, and better than promoting the whole tree to satisfy one subdirectory.

---

---

## Part 3 — Archetype T: code meant for instruction

### The rule

> **The top of a teaching notebook is step-by-step. The bottom may be
> streamlined.**

Good production code hides repetition; that is what it is for. But **abstraction
hides exactly the thing the student came to learn.** So: a chunk of code carrying
one step, with markdown above it saying what it does and why. The tidy version
with the functions and loops comes later, clearly labelled, after the reader
already knows what it contains.

### Why, in increasing order of importance

1. **A function is a promise that the details don't matter** — true for a working
   engineer, false for a learner. `results = run_model(config)` teaches one line.
   The eight decisions inside are invisible, and invisible decisions cannot be
   questioned, adapted or debugged.
2. **Students cannot debug what they have not seen assembled.** The common failure
   is not "my code broke," it is "my code ran and I don't know if the answer is
   right." Someone who typed each component knows where to look.
3. **The steps are the content.** In a modelling course the sequence *is* the
   syllabus. Wrapping it in `build()` does not compress the lesson, it deletes it.
   The student ends the term able to operate a tool and unable to build one.

### Do

- **One idea per cell.** If you can't write a one-sentence heading for a cell, it
  is doing two things — split it.
- **Markdown above every code cell**, saying what it does and, where there's a
  choice, why this choice.
- **Name the argument that matters.** When one keyword carries the concept, say so:
  *this one flag is the difference between a dry run and a real one.*
  Students skim code; they do not skim a sentence that says "this is the important
  line."
- **Print something after each step** — the shape of a table, the number of rows,
  the value of a parameter. Evidence, not decoration. It turns a silent cell into
  a checkpoint.
- **Ask for a prediction before every solve or fit.** *Write down what you expect
  before you run this.* A result the student had no expectation about teaches
  nothing, because there is nothing for it to contradict.

### Don't

- **No function definitions in the teaching section.** None. If you need one, you
  are either past the teaching section or the step should be a cell.
- **No loop that hides a decision.** Looping over years to build a table is fine.
  Looping over technologies whose parameters each have different reasoning is not
  — write them out.
- **No configuration dictionary at the top** that the rest reads from. It looks
  tidy and it makes every subsequent cell a lookup rather than a decision.
- **Never put the abstraction before the thing it abstracts.**

### The inversion — check for this first

A notebook opens with a large helper function, then follows it with a beautifully
narrated walkthrough of the same material. The narration is good; its *position*
is wrong. The student met the abstracted version before the thing it abstracts.

**The fix costs no new content** — you are reordering cells, not writing. Measure
it: *where does the first function longer than ~8 lines sit, as a percentage of
the way through?* Under ~50% and there is an inversion.

### When to wrap, and how to do it honestly

Wrapping is not forbidden; it is *sequenced*. You wrap when the notebook needs the
same thing several times and the reader has already seen the parts. Three
requirements:

1. **An explicit heading.** "Now the streamlined version." The reader should know
   they've crossed from learning into convenience.
2. **A sentence saying why now.** *We are about to run this a dozen times at
   different sizes, and you have built every one of these components by hand.*
   Without it the wrap reads as a style inconsistency.
3. **A check that the wrapper reproduces the hand-built result.** See Part 4 —
   this is the requirement people skip and it is the one that earns the wrap.

---

### Leave room — the companion rule, for the prose around the code

*Everything above is about the code. This is about the writing around it, and it
matters as much.*

> **A teaching notebook sets up a discussion. It does not hold one.**

If the material states its own conclusions, the class period has been spent before
it begins. The student arrives having been told what to think about the result, and
there is nothing left to say about it out loud. So: build to the question, pose it,
and stop.

**Do not write these:**

- *"This is the part that is actually graded."* The rubric says what is graded.
- *"This is what sinks first-year solar business cases."* That is the finding. Ask
  instead which assumption moved the answer most.
- *"That is not a bug — it is the most useful result here."* This tells the reader
  how to feel about a number before they have thought about it. Ask what would have
  to be true for it to happen.
- *"Ten percent means your day selection is wrong."* Ask whether the error is in the
  selection or the data, and how they could tell.
- *"What you should take from this,"* followed by bolded conclusions. That is a
  lecture wearing a list.

**Distinguish a derivation from a punchline.** Showing *how* an $80 price arises from
two $40 generators is content, and belongs in the notebook. Announcing that it is
"the single most counter-intuitive number in the course" is a line the instructor
should get to deliver.

**Keep the example minimal.** The reader should think *"oh, it looks like this"* —
not read every branch of possible logic, every failure mode, every this-goes-wrong
warning. Show the shape once. One rewritten example went from 55 cells and 3,558
words to 17 and 514, and taught more.

**Finish what you ask for.** If the assignment asks for a diagram, the worked example
draws the diagram. An example that stops short of the deliverable is where the student
most needed to see the shape.

**Match the reader's scale.** Students model the thing in front of them — a car, a
house, one plant. An example at national scale is the wrong thing to imitate, and it
buries the unit conversions that are half the lesson.

**Use placeholders, not answers.** Give a starting bracket and ask the student to
substitute their own values and cite them. The range is the teaching; the citation is
the grading.

**This rule and the "predict before you run" prompt are the same instinct.** Both
refuse to hand over the answer before the reader has formed one. A prediction prompt
does it for a number; leave room does it for the interpretation.

---

## Part 4 — THE BOUNDARY

### Where the two halves contradict each other

| Question | Parts 1–2 say | Part 3 says |
|---|---|---|
| Configuration | Outside code, never hardcoded (rule 2) | No config dict at the top — every cell becomes a lookup rather than a decision |
| Abstraction | One source of truth; never duplicate a function | No function definitions in the teaching section. None. |

Both are right. They are describing different artifacts.

### The resolution

> **`src/` is governed by Parts 1–2. `notebooks/` is governed by Part 3.
> Neither half gets to win on the other's territory.**

Concretely:

- Hardcoded **knobs** in a teaching notebook are **correct**, not debt. Do not
  refactor them into a config dict. See *Tables versus knobs* below for the one
  class of number that does belong in a file.
- A step written out by hand in a notebook that also exists in `src/` is
  **correct**, not duplication. Do not DRY it away.
- Conversely: a helper used by one caller in `src/` is fine; a helper function in
  the *teaching section* of a notebook is not.

### Tables versus knobs — the one class of number that leaves the notebook

The rule above is right about parameters and wrong about instance data, and the
distinction is not stylistic. It falls out of the agreement assertion itself:

> **A number the notebook hands to the package may stay hardcoded — the assertion
> proves both sides used it.
> A number both sides look up independently must live in one file both sides
> read — nothing else can prove they agree.**

Call the first a **knob** and the second a **table**.

- A **knob** is a scalar carrying a concept: a discount rate, a learning rate, a
  breakpoint count — anything the narration explains, or invites the reader to
  change. It stays written out in the cell. Seeing `NBP_REV = 7` beside the
  sentence explaining what a breakpoint mesh does *is* the lesson, and the
  notebook passes it into the package explicitly, so the assertion covers it.
- A **table** is instance data: many entries, indexed by the model's own sets,
  named nowhere in the prose. Typing it into the notebook and again into the
  package duplicates *data* with nothing comparing the copies — the same failure
  as duplicated code, one level down, and harder to spot, because a mismatch
  surfaces as a failed assertion pointing at the model rather than at the number.

So tables live in `data/raw/` and both sides read them. Three requirements make
the loaded version teach *more* than the literals it replaces, not less:

1. **Render the table.** A printed frame reads better than a page of dict
   literals.
2. **Show the key structure.** A frame shows rows and columns; the model indexes
   by `(stage, region)`, or whatever its sets are, and every constraint below
   looks values up by that key. Print the dictionary form so the index set is
   explicit rather than implied by punctuation.
3. **The package takes the data as an argument and never re-reads the file.**
   Then a reader who edits a value sees it flow into both the hand-built model
   and the check, and the assertion stays green. A check that punishes
   experimenting is a check that gets switched off.

### The shape: two folders, three roles

```
src/<pkg>/                  written for a machine to run a thousand times
data/raw/                   the instance tables both sides read
notebooks/
  00_walkthrough.ipynb      THIN: imports the package, holds no logic
  NN_topic.ipynb            TEACHING: builds by hand, asserts agreement
```

Same model, twice, **on purpose**. The notebook builds it by hand because that is
the lesson; the package builds it once because that is the code.

**The thin notebook is the cheapest reconciliation available.** It calls the same
functions the entry point calls and holds no logic of its own, so it cannot
drift — there is nothing in it to go stale. Worth having exactly once, as the
front door: it proves the install works and reproduces the headline numbers
before a reader invests an hour in the teaching notebooks.

### The agreement assertion — the mechanism that makes this safe

Deliberate duplication removes the usual protection, which is that only one copy
exists. Something must replace it. **Every teaching notebook ends with a cell that
imports the package, runs the same case, and asserts the two agree:**

```python
# TOL is set by what the computation supports - see 'The assertion is subject
# to the rule it enforces' below. 1e-9 for closed-form work; for a solver it
# cannot be tighter than the gap you solved to.
from mypkg.models import build_model
packaged = build_model(**PARAMS_USED_ABOVE).solve()
rel = abs(packaged.value - hand_built.value) / abs(hand_built.value)
assert rel < TOL, f"notebook and package disagree by {rel:.2e}"
print(f"notebook and package agree to {rel:.1e}")
```

**A teaching notebook without this cell is not finished.** This is not ceremony.
The failure it prevents is well documented and looks like this:

> One helper function pasted into eight notebooks. Over time three copies drifted.
> A bug was found and fixed — in three of the four places it appeared. The fourth
> was the notebook the published results came from. Nobody noticed for months,
> because nothing compared the copies.

Deliberate duplication is a design. Deliberate duplication with nothing checking
it is just duplication with a story attached.

#### The assertion is subject to the rule it enforces

An agreement assertion states a tolerance, and that tolerance is **two claims at once**. Only one of
them is usually noticed:

- **about the implementations** — that they compute the same model
- **about the computation** — that it is precise enough for the first claim to be testable at all

Get the second wrong and the check passes by coincidence. Measured 2026-09-04: two teaching
notebooks solved a MILP at `mipgap=1e-3` and `1e-6`, then asserted that notebook and package agreed
to `1e-9`. At a 1e-6 gap on an objective of 46,601 the solver may stop **0.047 short of optimal** —
so the assertion demanded agreement a thousand times finer than the solve was asked to deliver. It
held for months on one machine because both sides took the same path to the same vertex, and failed
the first time it ran on Linux.

**Solve at least as tightly as you assert.** If a check claims 1e-9, the computation behind it must
be good to better than 1e-9, or the check is testing **determinism rather than equivalence**.

**And a tolerance is a claim about the INSTANCE as much as the implementation.** That same `1e-9`
also asserted that no two integer solutions lay within a billionth of each other. That is a
statement about the data, and it was false: two solutions sat 3.6e-4 apart, and a coefficient
difference at the 1e-12 level — from deriving one curve two ways, which is the whole point of the
comparison — decided which was optimal. No seed, gap or ordering repairs that. Where the instance is
degenerate, assert the invariant that holds everywhere, record the looser tolerance as a deviation,
and say why.

This is the mirror image of a failure the same project hit four times during its migration: **a loose
MIP gap manufactures agreement** between things that differ. The two are one rule.

> **A tolerance must sit between the noise and the effect** — looser than what the computation
> cannot control, tighter than anything the check exists to catch. Placed at either edge it reports
> the edge.

### Corollary: generated artifacts

If a notebook, document or dataset is **generated by a script**, the script is the
source of truth and the artifact is a build output. Something must check that
regenerating reproduces what shipped. A build script and its output drift exactly
as fast as two pasted copies do, and for the same reason — nobody is comparing
them.

---

### Corollary: the agreement assertion protects the models, not the checks

Part 4 pairs `src/` with `notebooks/` and makes one assertion compare them. An archetype-A project
also has `scripts/run_all.py`, and that script should not hold a third copy of the model — it calls
the package. What it does hold is a second copy of the **checks**: the same invariants, thresholds
and tolerances the notebook asserts, written again in a different file.

**Nothing compares those.** The agreement assertion covers the model implementations and is silent
about the assertions themselves. So a threshold corrected in a notebook does not reach the script,
and the script's copy goes on being wrong with every test passing.

Measured on one repository, 2026-09-04 — every CI-visible failure was this shape:

    a licence guard fixed in the notebook and never in the script
    a plan comparison written four times - two notebooks, two script sections
    an SOS2 threshold written twice
    a component tolerance written three times

**A threshold, tolerance or invariant is a value with copies**, and the duplicate is where the fix
does not reach — sitting outside the very mechanism that protects the model beside it.

**The remedy is not to remember to grep.** That is a requirement living in prose, and Part 6 says
those have already failed. Remove the copies instead: a threshold used in two places **is a
parameter**, and Part 8 already flags parameters living anywhere but config. Put it in the package,
import it in both the notebook and `run_all.py`, and the duplication is gone rather than tracked.

Where it genuinely cannot be shared, **assert the copies against each other**. Two lines that fail
are worth more than an instruction to remember.

---

## Part 5 — Shipping teaching material

Everything here is about the gap between "it runs for me" and "a student can run
it."

- **One click, no install.** Assume a student with a browser, a free account, and
  no software. In practice: a public repo, a hosted-notebook badge, and a first
  cell that installs pinned dependencies plus the package itself. A private repo
  forces token-pasting or vendoring the package into each notebook — which
  re-creates the duplication problem the split exists to remove.
- **Runs top to bottom on a clean machine with no local files.** Test this by
  deleting the files and running the whole thing. If a cell reads a file the
  student doesn't have, it must fail with an *explanation*, not a stack trace:
  fall back to generated data, print loudly that it has done so, and state that
  the fallback is not an acceptable submission.
- **Ship it executed.** Commit the outputs and figures. A reader without a licence,
  a GPU, or twenty minutes should still see what the prose refers to. This is
  rule 5's documented exception, and it is what makes every number in the prose
  checkable by the reader.
- **Respect the free tier explicitly.** Free/community licences and runtimes have
  limits, often undocumented and found only by probing. Anything past the limit
  ships behind a `SMALL = True` / `QUICK = True` switch that is **on by default**,
  printing what it changed and what a full licence would give.
- **Deliberate blanks fail with a message.** Where the student must choose,
  "run all" should not produce a bare `NameError`:

  ```python
  if "choice" not in globals():
      raise NameError("Choose one of the three options above. "
                      "This notebook will not choose for you.")
  ```

- **Tag what you hand out.** Students following a link months later should get the
  version you taught, not the branch you are mid-refactor on.

### Every published repo carries a licence AND a citation

A licence sets the terms of reuse. It does **not** get you cited — MIT requires only that the
copyright notice travel with the code, and no permissive licence compels a citation. These are two
mechanisms and a repo meant to be cited needs both.

**LICENSE** — MIT unless the repo has commercial potential, in which case weigh Apache-2.0 for its
patent grant. UTA encourages open-access models and leaves the choice to the author.

**CITATION.cff** in the repo root. GitHub renders a "Cite this repository" button from it, which is
the whole point: people cite what is easy to cite, and friction is what stops them, not ethics.

**A "How to cite" section** at the top of the README, with the BibTeX ready to paste.

#### The DOI does not need remembering

Zenodo issues **two** DOIs on a connected repo:

- a **version DOI**, new for every release
- a **concept DOI**, which always resolves to the latest version and **never changes**

Put the **concept DOI** in `CITATION.cff`. It is correct for the life of the repo, so this is a
one-time edit and not a per-release chore. The order is forced — you cannot have a DOI before the
first release:

1. Add `CITATION.cff` with no `doi:` field
2. Connect the repo in Zenodo, tag a release
3. Zenodo mints both DOIs
4. Add the concept DOI to `CITATION.cff` and commit
5. Never touch it again

For a paper repo, cross-reference both ways: the paper's DOI in `CITATION.cff`, the code's DOI in
the paper's data-availability statement.

---

---

## Part 6 — Verification: the bugs that produce plausible output

Reading does not find these. Only running does. Every one of the following shipped
and looked fine:

- **A silently empty object.** An API called in the wrong order returns an empty
  model / frame / result. It "succeeds," reports success, evaluates to zero, and
  passes any assertion written against it. Guard with a *shape* assert —
  `assert len(result.rows) > 0`, `assert model.n_constraints > 0` — not a
  status check.
- **Default-argument capture.** `def f(..., n=GLOBAL)` freezes the value at
  definition time. Sweeping `GLOBAL` afterwards changes nothing, silently, and the
  reader concludes the sweep did nothing interesting.
- **Stale embedded source.** Code pasted from a module into a notebook (or into a
  slide, or a doc) is a snapshot. It does not update. See Part 4.
- **Chained assignment / aliasing.** `a = b = c` binds a name to the wrong object.
  Caught by execution, never by review.
- **Cell-order dependence.** A cell that only works because of what an earlier
  *manual* run left in the kernel. A fresh-kernel top-to-bottom execution is the
  only real test; a static scope check catches most of it cheaply.
- **Comparing two different measurements.** A value taken from an early-terminated
  run, differenced against one computed exactly, produced an impossible negative
  statistic. If two numbers are compared, one function should produce both.
- **Comparing two things that were not asked the same question.** A "cost of X"
  came out negative because one configuration was required to satisfy a constraint
  the other was free to ignore. Match the comparison before interpreting the
  difference.

### Assert the theory in code

Domain invariants belong in assertions, not in prose. When they fail, the plumbing
is wrong — not the science. Examples of the shape: a chain of bounds that must stay
ordered, an approximation that must not beat the exact answer it approximates, a
quantity that must be conserved, a value that cannot go negative, a wrapper
reproducing a hand-built result.

### Non-reproducible prose

If prose names a specific outcome — *"it charges in hours 11–16"*, *"the second
iteration is where it drops"* — **verify the answer is unique.** Wherever several
answers tie, different libraries, versions, orderings or seeds hand students
different results and your text is wrong for some of them.

Two fixes, in order of preference: add a small real effect that breaks the tie (a
decay, a cost, a tolerance) — then say so, because ties are a real thing and
detecting one is worth teaching; or, where the degeneracy is *structural* and no
perturbation fixes it, assert only the invariant quantities and **teach the
degeneracy** instead of asserting the path.

### Every number in the prose comes from a run

Not from memory, not from an earlier draft. This decays silently and continuously:
a parameter changes, every downstream figure in the narration is now wrong, and
nothing complains. Automate it — a checker that extracts numbers from markdown and
compares them against the executed outputs — because a human will not re-check
forty figures after every edit.

---

### The published path is not the path you develop on

> **A check that only ever runs where the code already lives will pass forever while the published
> path is broken.**

Measured 2026-09-05: three published repositories carried an *Open In Colab* badge pointing at a
notebook that **could never have run.** Every cell had been compiled and every suite passed.
Neither check touches what a stranger does.

Compiling proves a cell parses. A suite imports the package from a **source checkout**, where the
data already sits in the right place. The published route — install into a fresh interpreter, then
read data — had never once been executed.

Five defects, every one invisible to a passing suite:

| Defect | Why the suite missed it |
|---|---|
| `pip install git+https://…` ships the package, not `data/` | a data directory at the repo root is not package data and is not in the wheel |
| `Path(__file__).resolve().parents[2]` | correct only in a source checkout; from site-packages it lands on `Lib/`, so the error reads like a corrupt download |
| a relative `"../scripts/run_all.py"` | resolves outside the repo the moment the notebook runs from anywhere but its own folder |
| `subprocess.run(capture_output=True)` printing only `.stdout` | swallows stderr; a failing script printed one empty line and looked like it had done nothing |
| an undeclared dependency | `from IPython.display import Image`, unused, surviving a notebook extraction — invisible on Colab, which ships IPython, and fatal anywhere else |

**Before a badge ships, clone the repository from GitHub into a clean environment and execute every
cell.** It is the only check that walks the path a reader walks.

Three rules follow from that list:

- **Never `capture_output=True` while printing only `.stdout`.** Print both streams and the return
  code, or do not capture. That one hid another defect for a full day.
- **Derive paths from the installed package, never from the working directory** or from `__file__`
  walking upward. The two differ only off the development machine, which is where nobody looks.
- **Guard the dependency list with a test that parses imports** and fails on anything not declared
  in `pyproject.toml` or the standard library. **Scan, do not import** — importing may execute the
  model. And **read `pyproject.toml` rather than restating its list inside the test**: a restated
  list is a second copy that nothing compares, so the guard against drift drifts first.

---

#### A check must be shown to fail

**A guard that has only ever passed is indistinguishable from one that cannot fail.**

The dependency guard above was written *because* an undeclared import shipped — and it passed from
the day it was written while hardcoding the very list it checked against, so it would have missed
exactly the change it existed to catch. Nothing about a green run said so.

**Prove it fires: inject the original defect, watch the check fail, restore, watch it pass.**

    AssertionError: imported but not declared in pyproject.toml: ipython (model.py).
      Either add it to [project] dependencies or remove the import.

That is a measurement. A green suite on its own is not.

This is *test the probe before you trust a clean result* (Part 12) in a second setting — there a
search that should return zero, here a test that should pass. **Both are instruments whose negative
result means nothing until they have produced a positive one.**

Two traps specific to guards of this kind, both found while fixing the one above:

- **A conditional import silently deletes the guard.** `tomllib` is standard library from 3.11 and
  these repos declare `>=3.10`. `pytest.importorskip` is the reflex and is **wrong**: on 3.10 it
  skips the test and reports green — this rule's own failure mode wearing a different hat. Declare
  the backport, `tomli; python_version < '3.11'`, so the check always runs.
- **A distribution name is not always the module it installs.** `scikit-learn` installs `sklearn`.
  A name comparison will quietly pass an undeclared import the day someone adds a package where the
  two differ. Record it as a known limit and add an explicit map — **do not loosen the check to
  accommodate it.**

---

### A requirement that lives only in prose has already failed

Written down, a requirement gets read **after** the thing it was meant to prevent. Made to fail, it
gets read **before**.

Six were recorded as prose across 2026-09-02 to 09-04. Every one was cheap to check. Not one
announced itself:

| Recorded as prose | What it actually was |
|---|---|
| “the portable half is byte-identical to the source” | named no version; wrong for a day |
| “`credscan` clean over 111 files” | nothing proved the scanner could fire |
| “substitute `USERNAME`” | the hardcoded repo name beside it was the larger half |
| “see `CLAUDE.md` Part 4” | that file no longer contained a Part 4 |
| “the credential was rotated” | it was scrubbed, not rotated; the key stayed live |
| “the badges point at this repo” | 45 named a branch that did not exist |

> **The moment to check a pre-push requirement is the moment nobody is looking.** A person reads
> prose when they are already looking, which is after the push.

Turn it into something that fails: a test, an assertion, a CI step. **Commit it red** if the
condition is not yet met — a suite that stayed green over 45 badges pointing at a nonexistent branch
was reporting the wrong thing, and making it fail is what turned the requirement from a claim into a
measurement.

**Guard it against passing vacuously.** A check that finds nothing to check must say so rather than
report success over an empty set — `assert found, "no badge URLs found at all"`. A search that
should return zero must first be shown capable of returning non-zero; see Part 12.

#### The address is longer than it looks

`github/<owner>/<repo>/blob/<branch>/<path>` is **four** values. `owner/repo` reads as the whole
address and is two-thirds of one, which is why the branch stayed invisible in 45 files that were
otherwise correct. Same shape as the half-placeholder, one segment further right.

**Set the branch once, machine-wide, so it is never a per-repo question:**

    git config --global init.defaultBranch main

Git still defaults to `master` when this is unset, while GitHub, every badge and every tool assume
`main`. Repos born on GitHub get `main`; repos born from `git init` get `master`. **Nobody chooses
this**, and it silently splits a lab's repos in half.

**The rename is free before the first push and never again.** With no remote, `git branch -m master
main` leaves nothing behind, and badges already naming `main` simply start resolving. After a push
it means renaming a live default branch, which leaves a stale branch that still resolves and serves
quietly older content.

---

## Part 7 — Auditing an existing set of notebooks

Measure, don't estimate. These are the checks that pay, roughly in order:

| Check | How | What "good" looks like |
|---|---|---|
| Does it run? | Execute every notebook in a fresh kernel, `allow_errors=True` | 0 errors; record the wall time |
| Prose vs output | Every number in markdown against the executed outputs | 0 unexplained mismatches |
| Duplication and drift | Hash each function body, group by name across files | 0 names with >1 version |
| The inversion | Position of the first function >8 lines, as % through | no big function before its narration |
| Orphan cells | Code cells with no markdown immediately above | 0 |
| Cell length | Longest cell, in lines | readable without scrolling |
| Predict prompts | Count per notebook | ≥1, before the first result |
| Reproduction asserts | Count per notebook | ≥1 (the Part 4 assertion) |
| Pinning | Unpinned installs; interpreter version vs what ran | 0 unpinned; metadata matches reality |
| Seeds | Set and printed wherever anything is stochastic | all |

Two of these are worth keeping permanently as CI tests rather than running once:
**the prose-number check** and **the duplication check**. They are the two failure
modes that recur, and both are invisible until someone looks.

---

## Part 8 — Anti-patterns

Flag these on sight:

- A notebook that reimplements what a module does, **with nothing checking they
  agree**. (The notebook reimplementing it is fine — see Part 4. The missing check
  is the defect.)
- Parameters buried in function bodies instead of config *(in `src/`)*.
- Instance data typed into both the notebook and the package, with nothing
  comparing the two copies.
- A single `output/` folder mixing intermediates with final results.
- Committing large or regenerable data "just in case."
- `sys.path.insert` hacks instead of a proper installable package.
- Unpinned dependencies in a repo tied to published results or handed to students.
- Deferring the README and tests to "after the paper is done."
- A dashboard that recomputes on every page load.
- Version control by filename: `script_v2.py`, `module.py.bak`, `final_FINAL/`.
- **A shared document duplicated anywhere — a zip, a deck, a PDF, or another repo.** Every
  copy drifts, and a copy inside a container cannot even be diffed, gitignored or checked by
  CI, so it does not merely go stale: nothing can tell you that it has. **Ship a pointer to
  the source.** See Part 0.
- Library-grade rigor for a one-off analysis (over-engineering) or analysis-grade
  looseness for a shared library (under-engineering).
- A helper function above the narration of the same material *(in `notebooks/`)*.
- A teaching notebook whose numbers cannot be checked because it shipped stripped
  of outputs.

---

## Part 9 — Working style

- Explain trade-offs rather than presenting one option as the only choice. The
  *why* matters more than the scaffolding.
- Say when a convention here doesn't fit the actual work. These are defaults, not
  laws — but say it, rather than quietly ignoring one.
- **Verify by running.** Don't say code works — execute it, run the tests, show the
  output. Part 6 exists because this is not optional.
- Prefer the boring, standard tool over the clever one. Research and teaching code
  both outlive their author's memory of them.
- Measure before planning a fix. An audit that reports counts is actionable; one
  that reports impressions is an opinion.

---

## Part 10 — Two things to copy

### The pre-ship checklist

Before a teaching notebook goes to students:

- [ ] Zero function definitions above the "streamlined version" heading.
- [ ] Every code cell in the teaching section has markdown above it.
- [ ] Longest teaching cell is short enough to read without scrolling.
- [ ] At least one "predict before you run" prompt, before the first result.
- [ ] Any wrapper appears *after* the narration, with a reproduction check.
- [ ] The Part 4 agreement assertion is present and passes.
- [ ] Instance tables loaded from one shared file; knobs written out inline.
- [ ] The package takes the data as an argument, so a reader's edit keeps the
      assertion green.
- [ ] Runs top to bottom in a fresh kernel, on a clean machine, with no local files.
- [ ] Shipped executed — outputs and figures committed.
- [ ] Every specific number in the prose came from that run, not from memory.
- [ ] Deliberate blanks fail with a message, not a traceback.
- [ ] Seeds set and printed wherever anything is stochastic.
- [ ] Dependencies pinned with upper bounds; kernel metadata matches what ran.
- [ ] **Branch checked before the first push** — every badge and install URL names the branch the
      repo is actually on. Free to fix now; a live rename later.
- [ ] **Repo name confirmed** — it freezes every badge and install line; a rename does not redirect
      what has already been copied out.
- [ ] Each of the two above enforced by something that **fails**, not by a line in the README.
- [ ] **The badge was clicked** — or its equivalent run: a fresh clone from GitHub, into a clean
      environment, every cell executed. Compiling and a green suite do not cover this.
- [ ] No `capture_output=True` that prints only one stream.
- [ ] **Every guard has been watched to fail** — defect injected, check red, restored, check green.

### The prompt block

Paste this into a chat when asking an assistant to write or revise teaching code.

> **Teaching-code style — follow this exactly.**
>
> Write the top of the notebook step by step, not abstracted. One idea per cell,
> with a markdown cell above each code cell explaining what it does and why.
> **No function definitions and no loops in the teaching section** unless the loop
> is genuinely mechanical repetition of an identical step. Print something after
> each step so the reader can see it worked.
>
> Where a single argument or line carries the concept, say so in the markdown
> explicitly. Before any solve, fit or simulation, add a one-line prompt asking the
> reader to predict the result first.
>
> If the notebook needs the same construction several times, you may add a
> streamlined version **at the bottom**, under a heading that says so, with one
> sentence explaining why it is being wrapped now.
>
> Do not put a helper function before the narrated walkthrough of the same
> material. If one already exists there, move it to the bottom — or, if the project
> has a package, move it out of the notebook into the package.
>
> **If a package holds the same model, the notebook's last cell must import it,
> run the same case, and assert the two agree to a tolerance the computation actually
> supports.** Deliberate
> duplication is fine; deliberate duplication with nothing comparing the copies is
> how a fix gets applied in three places out of four.
>
> **Split the numbers into tables and knobs.** A knob is a scalar carrying a
> concept — a rate, a count, a limit, anything the narration explains or invites
> the reader to change. Knobs stay written out in the cell, and the notebook hands
> them to the package explicitly, so the assertion already covers them. A table is
> instance data — many entries, indexed by the model's sets, named nowhere in the
> prose. Tables live in one file both the notebook and the package read, because
> if each types its own copy a failed assertion cannot distinguish a typo in the
> data from a bug in a constraint. Load the table, render it, and then print the
> dictionary form so the key — `gen`, `(stage, region)`, whatever the model looks
> values up by — is explicit rather than implied by punctuation. Have the package
> take the data as an argument and never re-read the file, so a reader's edit
> flows into both the hand-built model and the check and the assertion stays
> green. Then add a commented-out worked example of overriding one entry.
>
> Every specific number in the prose must come from actually running the code, not
> from memory. If the prose names a particular outcome, check the answer is unique
> — where several answers tie, different libraries or seeds produce different results
> and the text is wrong for some readers. Break the tie with a real effect rather
> than vaguer prose; where the degeneracy is structural, assert the invariants and
> teach the degeneracy.
>
> The notebook must run top to bottom on a clean machine with no local data files:
> fall back to generated data with a loud message saying the fallback is not an
> acceptable submission. Where the reader must make a choice, raise an explanatory
> error rather than letting it crash with a `NameError`.

---

## Part 12 — Working alongside other sessions

*(Part 11 is reserved for a project's own file — see Part 0.)*

Several sessions run at once on this machine, in different folders, sometimes on one repo. These
rules are about shared mutable state and about how you know a thing you claim to know.

### The one-writer rule, stated properly

> **At most one chat may WRITE to a given folder at a time.**
> Any number may read.

The rule is about **shared mutable state**, not about chats. Two chats are only dangerous when
they can touch the same thing. Which case you are in decides everything:

| Situation | Safe? | Why |
|---|---|---|
| **Different folders** | **Yes — no coordination needed** | Separate files, separate repos, separate memory. Run as many as you like. |
| **Same folder, no git, different files** | **Mostly** | Each edits its own files. Two remaining risks: a folder-wide operation (a rename, a cleanup script), and both editing a shared `TODO`/`CONTEXT` file. |
| **Same folder, same git repo** | **No — this is the one that bites** | Even editing *different* files, they share git state: one index, one HEAD, one branch. |

That third row is the non-obvious one. Git state is shared even when files are not:

- One chat's commit sweeps in whatever the other chat has staged (verified in a scratch repo)
- A `git checkout` or `git reset` in one chat changes files under the other chat's feet, silently
- `.git/index.lock` contention makes one of them block or error

#### So: can one chat do PowerPoints while another does reports?

**Yes — put them in different folders and it is completely fine.** Decks in the presentations
folder, reports in the project folder. That is the good case and needs no ceremony.

**Same folder is the question to ask.** If both are in one folder and it is a git repo, apply §2.
If it is not a repo and they genuinely touch different files, it usually works — just keep both of
them out of any shared index file, and do not let either run something folder-wide.

---

### The branch rule — it is actually a WORKTREE rule

You half-remembered this one, and the distinction matters:

**A branch alone does not help. It makes things worse.**

Two chats in one folder are in one working directory. Branches do not change that — there is still
exactly one set of files on disk. If chat A runs `git checkout other-branch`, every file in the
folder changes underneath chat B mid-task, and B has no idea. That is worse than no branching.

**A worktree is what actually isolates them.** It gives each chat its **own directory** *and* its
own branch, backed by the same repository:

```bash
git worktree add ../REE-figures figures-work
```

Now chat A works in `REE 4301/`, chat B works in `REE-figures/`. Different folders on disk, so
they physically cannot overwrite each other. Same repo underneath, so you merge normally when done.
Claude Code has this built in — a chat can enter a worktree and work isolated.

**Rule:** parallel writers on one project → worktrees, never branches-in-one-folder.

---

### Committing when you are not the only writer

```bash
git commit -m "message" -- path/one.md path/two.md
```

**Not** `git add <paths>` followed by a plain `git commit`. A plain `git commit` takes the
**entire index**, including files another session staged. Verified in a scratch repo 2026-09-02:
with `a.txt` staged by a simulated other session, `git add b.txt && git commit` committed *both*;
`git commit -- b.txt` committed only `b.txt` and left `a.txt` staged.

Otherwise:
- **Commit is the handoff.** Before leaving a chat, have it commit its own work.
- **Orient before writing.** New chat in a repo starts with `git log --oneline -5` and `git status`.
- Never leave a dirty tree for the next agent.

---

### Verify the outcome, not the step

**A step reporting success is not evidence that it worked.** This came up four separate times on
2026-09-03, in four different tools, and it is the single most repeated lesson of that day:

| The step said | What was actually true |
|---|---|
| Script parsed cleanly | It had never been run |
| Script ran and reported "stored" | The masked prompt swallowed the paste; 1 character stored |
| Checker flagged a value red | The value was a valid numeric id; the *check* was wrong |
| `git push` succeeded | Netlify built a different branch; the site never changed |

Each was caught by looking at the **result** rather than the exit code — the token's length, the
site's HTML, the file's bytes.

**So: name the observable that proves the goal, and check that.**

| Doing | Do not verify | Verify |
|---|---|---|
| Setting a credential | "the command ran" | its length and that a call using it succeeds |
| Deploying a site | "the push succeeded" | fetch the live URL and grep for something only the new build contains |
| Writing a script | "it parsed" | run it |
| Porting code | "it runs" | its output matches the original's |
| A DNS change | "the site loads" | A **and** MX both still resolve |

**It runs in both directions.** One *failure* is not evidence either. An OSF token was reported
broken on a single 401 and told to be regenerated; a retry returned 200. Against a flaky remote
service, one call is not a measurement - retry before concluding a credential is dead, especially
when the remedy is to destroy and replace a working one.

The failure this prevents is the worst-shaped one: **nothing errors.** A push that succeeds against
the wrong branch reports success at every layer, so the search starts by looking for a build failure
that never happened.

#### Two corollaries, both learned on 2026-09-03

**Absence of revision is weak evidence. Evidence of use is strong.** Asked whether a teaching rule
was still current, "nobody has edited the file since" barely answers it — a rule can sit unrevised
because it was abandoned. What settled it was finding three commits over the following five hours
whose messages were the rule being enforced. *Look for the thing being used, not for the absence of
someone changing it.* The second is falsifiable; the first is not.

**State your normalisation before quoting a hash.** Two sessions compared the same file and
quoted different md5s — one hashing raw bytes, the other CRLF-normalised. Both were correct; the
files were identical. On Windows the gap is exactly one CR per line, which for a 630-line file is
630 bytes:

```
raw bytes       32,436 B   md5 cd02e41f63d4
CRLF-normalised 31,806 B   md5 db1eda85607d
```

Neither number is wrong and neither is comparable to the other. **A hash quoted without its
normalisation is not evidence** — and two sessions trading mismatched hashes for one file is exactly
what reads as drift later. Say which you used, or quote line counts, which do not vary.

**Check whether you can answer before saying you cannot.** A session asked this one for git history
on the grounds that it "could read the file but not its history" — while working in a git repo, which
it had already run `git log` against earlier in the same session. It had the tool, had used it there,
and still framed the question as out of reach. The same shape as every other error here: **a
conclusion that felt settled and was never tested.** Before handing a question off as unanswerable,
spend one command finding out.

#### A third corollary, 2026-09-04 — test the probe before you trust a clean result

Scanning a repo's whole history for credential-shaped values returned **zero matches.** I nearly
recorded “nothing exposed”. The probe was broken — a wrong `git grep` invocation against a commit
tree, so it searched nothing. **Searching nothing and finding nothing looks exactly like searching
everything and finding nothing.**

What caught it was running the same probe against a commit already known to contain the string. It
returned four files at once.

> **A search that is supposed to return zero must first be shown capable of returning non-zero.**
> Point it at a known positive — an old commit, a copy, a line you add on purpose — and confirm it
> fires. Only then does a clean result mean anything.

This is the sharpest form of the pattern already in this section: **a narrow check that agrees with
itself.** It is worst for absence checks — secret scans, “did the substitution leave survivors”,
“is the old name gone” — because there the *desired* answer and the *broken* answer are the same
output, so nothing about the result invites a second look.

#### A fourth corollary, 2026-09-04 — never conclude from sanitized output

Checking whether a credential was in a repo's history, the output was piped through a redactor so
no secret would print. It came back `WLSACCESSID: "<REDACTED>"`, which was read as a live value.

**That `<REDACTED>` was the redactor's own output.** The text underneath was a placeholder reading
`REDACTED-CREDENTIAL-ROTATED` — the scrub had already run. The sanitizer had destroyed exactly the
information the conclusion depended on.

Every other failure in this section is a broken tool returning **nothing**. This is the mirror
image: an intact tool returning **something**, where the something was manufactured by the safety
measure.

> **Redact for display. To decide, ask a question whose ANSWER is safe to print** — a count, a
> boolean, a length, a match against a known-safe placeholder. `grep -c "REDACTED-CREDENTIAL-ROTATED"`
> returns `3` and leaks nothing.

### A scrub and a rotation are two claims with two kinds of evidence

A note once read: *"scrubbed from all 29 commits and the credential rotated."* Every clause true but
one, and the true clauses made the false one credible. The scrub had run; the rotation never had, and
the key stayed live in shared storage for a further day.

**They are not degrees of the same remedy.** A scrub changes what a repository *shows*. A rotation
changes what the credential *does*. Only the second closes an exposure, and no amount of history
rewriting un-exposes a key that has existed in a working tree.

> **Record them as separate items with separate evidence, never in one sentence.** A scrub produces
> a diff you can point at. A rotation produces an **authentication failure** you can point at. A
> rotation claimed with no failed auth behind it is an assertion, not a finding.

What let it stand for a day: the machine's own credential pair was a *different* pair, and it was
dead. **From inside a folder, a key that has stopped working is indistinguishable from one that was
rotated.**

And the reason this matters more than an ordinary stale note: **a false all-clear is worse than no
note.** Silence invites a check. "Rotated" forecloses one.


### When to use a subagent

The decision rule. A subagent's context is sealed from yours.

**The one-line test:**

> **Spawn when the search is wide and the answer is narrow, and nothing gets written.**

Everything else follows from that. A subagent's context is sealed off, which is why a 154,000-token
exploration can cost the parent 2,000 — and why the subagent cannot know anything you did not type
into its brief.

#### Spawn

- **Wide search, narrow answer.** "Find every copy of the Code Standard across Documents" —
  thousands of files read, one paragraph back. This is the archetype.
- **A long self-contained investigation** with a clear question and a bounded scope.
- **Parallel independent characterisation** — "summarise what each of these 20 folders contains",
  three at once.

Prefer the **`Explore`** type for pure lookup. It is read-only, which removes the main hazard by
construction rather than by instruction.

#### Do not spawn

- **When you could do it in a few tool calls.** Briefing costs more than the work.
- **When the task needs what you already know.** Every fact must be re-serialised by hand. If the
  briefing would be longer than just doing the job, spawning has already lost.
- **For anything that writes to shared state.** A cold subagent is, by construction, the last thing
  that could know another session owns that folder. To write into someone else's folder, **message
  the owning session.**
- **For anything irreversible** — GitHub, DNS, Netlify, credentials, publishing. Not because
  subagents are careless, but because the safety mechanism on those actions is *confirming with
  Jones*, and a subagent reports to its parent, not to him. Spawning removes the human from the loop
  precisely where the loop matters.
- **When you would need three rounds.** That is a session, not a subagent.

#### The rule that outranks the others

**A subagent's report is a claim, not a result.** It is exactly the shape of success signal that
*Verify the outcome, not the step* warns about — confident, summarised, and produced by
something that cannot see its own blind spots. Verify the parts you will act on, the same way you
would verify a peer's message.

### An unattended process reports; it does not write

A scheduled or overnight run has nobody watching it, and that changes what it may safely do.

**The safety mechanism for a write is a person who can see the result and undo it.** At 3am there is
no such person, so a wrong write stays wrong until someone stumbles on it — and **a scheduled
session cannot be stopped by the session that scheduled it.** It is not a subagent: no parent, no
stop signal, no control channel. It is an independent session that happened to be started by a
timer, and killing it means the user doing it by hand.

So an unattended run gets **read access and produces findings**. A supervised session acts on them.

Learned from a reconciliation task given write authority and told to commit and push. Its prompt did
guard the one-writer problem — check for live sessions first, downgrade to read-only if any are
found — but **that protects against collision, not against the two things that actually happen when
nobody is watching: hanging, and being confidently wrong.** It hung mid-turn for six hours and had
to be killed from the sidebar. It wrote nothing, by luck rather than by design.

**A subagent is not the alternative.** A subagent lives inside its parent's turn and cannot exist at
3am, which was the entire requirement. The choice is never subagent versus scheduled task — it is
what authority the scheduled task is given.

#### For work at this scale specifically

The inventory jobs — 60 project folders, 17 class folders, ~200 GB — are the good case: wide read,
narrow answer, no writes. The GitHub, DNS and Zenodo work is the bad case, all of it irreversible
and all of it needing accumulated context.

**Peers and subagents are not substitutes.** A peer session catches what you did not think to ask,
because it has its own context and arrived from somewhere else. A subagent answers exactly what you
asked, cheaply, and will never volunteer that the question was wrong.

---

## The one-line versions

> **Engineering:** if a clean clone can't reproduce it with one command, it's broken.
>
> **Teaching:** abstraction is the reward for understanding, not the route to it.
> Put it at the bottom.
>
> **The boundary:** keep both copies on purpose — and make one assertion compare them.
