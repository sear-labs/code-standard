# CODE AND TEACHING STANDARD

*Portable. Nothing below is specific to one course, language, library or project.*

**How to use this:**
- Drop it in a repo root as `CLAUDE.md` — Claude Code reads it automatically every session.
- Or put it at `~/.claude/CLAUDE.md` to apply to every repo on the machine.
- Or paste it into a Claude Project's custom instructions for non-code chats about the work.

When starting a new repo: *"Scaffold this as a [archetype] per CLAUDE.md."*
When starting a teaching notebook: *"Teaching-code style per CLAUDE.md Part 3."*

---


## What each Part is for

Two standards live here and they are used differently. This is the map; the index above is
the address list.

    ASKING "WHAT DO I ACTUALLY DO?"        start here
      Part 2b   a folder that is not a repo - how to shape it
      Part 2c   starting a project, and retiring one, and what each step creates
      Part 10   two checklists, written to be copied

    ASKING "IS THIS ALLOWED / IS THIS RIGHT?"
      Part 1    the invariant core - eight rules that apply to everything, plus naming
      Part 4    THE BOUNDARY - where the engineering and teaching halves contradict, and
                which one wins. If you read one section, read this one.
      Part 8    anti-patterns, stated as things not to do

    ASKING "HOW DO I BUILD THIS PARTICULAR THING?"
      Part 2    archetypes - the shapes a repo takes. Reference, not a walkthrough.
      Part 3    Archetype T: code somebody learns from. Contradicts Part 1 on purpose.
      Part 5    shipping teaching material: licence, citation, DOI

    ASKING "HOW DO I KNOW IT IS TRUE?"
      Part 6    the bugs that produce plausible output, and how to catch them
      Part 7    auditing notebooks you did not write
      Part 12   working alongside other sessions, and verifying rather than assuming

    Part 9      working style
    Part 11     reserved for the project's own file - see "How this document reaches a project"

**Part 0 is about the document, not about the work.** If you are looking for a rule, you are
in the wrong section; use the map above. Read Part 0 when you want to change something here,
or when you need to know why it is one file.

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
      a local clone, if you have one                faster; e.g. C:\Users\<you>\dev\repo\ops\code-standard

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

**In the paper, the VERSION DOI. In `CITATION.cff`, the concept DOI.** They are different
requests and the difference only appears later. `CITATION.cff` answers *how do I cite this
software* - which should follow corrections, so the concept DOI is right and never needs
touching. A data-availability statement answers *what produced these numbers* - which must not
follow corrections, because the paper's numbers came from one version and a corrected repo
produces others.

Since this repo stays unlocked precisely so errata can land, that drift is not hypothetical:
it is the intended behaviour of the policy. A paper naming the concept DOI resolves, forever,
to code that no longer matches it - and it resolves successfully, which is why nothing reports
it.

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

**Where a fact goes is decided by its scope, and the routing is this:**

    a fact about THE MACHINE     that machine's ~/.claude/CLAUDE.md
    a fact about ONE PROJECT     that project's CLAUDE.md Part 11, or its memory/
    a PORTABLE RULE              petition this document. Never write it elsewhere, and
                                 never write it twice.
    HISTORY and REASONING        a dated note

> **This table lived for three days inside a subordinate document that pointed here for it.**
> A notebook retired its own rules on 2026-09-04 with a redirect line reading "where things go
> -> Standard, Part 0". It never arrived, and Part 0 stated the roles above without the routing
> below them - so the only written copy of the routing rule sat in the one document that says
> it is not the authority. Found 2026-09-07, which is the failure this Part exists to prevent,
> one level up.

**Candidate rules wait in one queue, and every entry leaves it.** An inference that is not yet
a rule - something one session concluded that another should know, before anyone can say
whether it is portable - goes to a single global carry-forward file, reached by URL from each
machine's `~/.claude/CLAUDE.md` the way this document is. It is a queue and not a library:
every entry exits by being promoted here, pushed down into a project, or dropped as
not-a-pattern. **One file, not one per domain** - the floor of two independent sightings is
unreachable from inside a single domain, and per-domain carry-forward already exists as
`memory/`. An entry that will not exit is the signal that something is mis-filed.

**To amend it, petition — do not edit locally.** A session that hits something this document gets
wrong or fails to cover writes the proposed text out in full and opens it against
<https://github.com/sear-labs/code-standard> — as a pull request where it has access, or as a
dated note handed to Jones where it does not. Whoever merges checks it against what is already
recorded and commits it with provenance in the message. **Sessions do not amend their own working
copy of the standard.**

> **The address is the repository, never a folder.** This instruction named a local path until
> 2026-09-06, by which time that folder had moved and the route to amending this document pointed
> at nothing. A path is true of one machine — the rule two sections above says exactly that, and
> this paragraph was its counter-example.

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

**Approvals stay at zero; "somebody else read it" does not.** The two are different claims and
only the first is a GitHub setting. Where the table above gives merge rights to more than one
person, **a change is merged by someone other than its author** - not because an approval
authorises it, but because the value of review was never in the count. Where merge rights rest
with one person, that is impossible and the honest position is to say so rather than to
configure a requirement that would deadlock: a sole maintainer's protection is the pull request
as a rate limiter and a record, which is what this section already says it is.

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

   **A range is not a record.** `pandas>=2.0,<4` says what the code tolerates; it does not
   say what ran, and re-solving it next month installs something else. Ship both: the range,
   so a reader can install; and a resolved list — `pip freeze`, a lock file, whatever the
   tool produces — committed beside the results it produced. The interpreter version is
   already held to this standard in the sentence above; the libraries are the larger half of
   the same claim.

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

**Because the two forms invert, neither is findable by the other audience's search.** That is
the price of the inversion and it is paid in the organisation's repo list, where both forms
sit together. **Pay it with metadata, never with a rename** — a rename breaks every badge and
install line already copied out, and a topic breaks nothing:

    every repo carries topics naming BOTH halves    lithium, optimization, teaching
    and a one-line description leading with the other form's key term

A topic is editable forever; a name is not. This is the one place where the cheap fix and the
expensive fix are not the same shape.

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
| **A published model written in another modelling language** | **P** — ported model |
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

**P — Ported model** *(a published model whose original is in another modelling language)*

Archetype A, plus a second implementation and the machinery that keeps the two honest. Reach
for it when a result was produced in GAMS, AMPL, R, MATLAB or a spreadsheet, and the barrier
to anyone checking it is **the tool, not the solver**. That distinction is the whole reason
this archetype exists: a commercial solver stops you *running* the model, while a commercial
modelling language stops you *reading* it, and the second is worse.

#### Nine stages, one direction

Archetype A's three data tiers become nine named stages, because a ported model has two of
everything — two models, two sets of outputs — and "input, interim, output" stops
distinguishing them.

    input raw            the original model's own data, wherever it lives
    clean-up code        may require the licensed tool; runs once
    cleaned data         open CSVs. COMMITTED - see below
    model files          the original, kept verbatim, AND the port
    raw output           the original tool's output. Gitignored
    clean-up output code
    cleaned output       tidy, long-format. COMMITTED - this is what everything reads
    analysis code        .py, not notebook
    figures              regenerated by a script, never by running a notebook

**Two of these are committed generated files, and both are deliberate exceptions to Part 1
rule 5.** Cleaned *data* is committed because regenerating it requires the licence it exists
to remove — the usual reasoning runs backwards here. Cleaned *output* is committed because
without it nothing in the repository works from a clean clone.

**Figures read cleaned output, never raw.** A figure that parses the original tool's report
is re-implementing the clean-up stage, and the second copy is the one that drifts. In one
repo that raw format had already dropped 19% of a comparison silently, because it carried a
*varying* number of index columns and a reader assumed a fixed one.

#### Four artifacts, and what each may claim

| | needs | claims |
|---|---|---|
| the original | its own tool | produced the published result; kept **verbatim** |
| the port | a solver | reproduces the original's objective |
| verification notebook | **nothing** | the published result is correct |
| example notebook | a free solver | the formulation runs and behaves |

**Keep the two notebooks' claims apart.** The verification notebook makes the reproduction
claim and needs no solver; the example notebook demonstrates the formulation on whatever it
can actually solve. A reduced instance cannot reproduce a full-horizon result and must not
be presented as trying — stamp the reduction **into the image**, not into markdown beside
it, because a chart gets screenshotted into a slide and the caption does not follow it.

**Where the whole model fits in the example notebook, it should carry the whole model.** The
overlay of a run against the published one is then not a reduction-honesty device but the
affordance that lets a reader change a parameter and see what their change did.

#### Reconcile on the objective, never on the solution

Two implementations of one model agree on the objective. They will **not** agree on every
variable, and demanding that manufactures failures. Degenerate LPs have alternate optima:
in one measured case cost and capacity totals reproduced exactly while dispatch differed by
9–22% on two variables that nothing constrained and nothing costed — the optimum simply did
not determine them.

**State the surviving residual in the repository.** An unexplained residual is
indistinguishable from an unfound bug.

**Read objectives from the solver's own binary output, not from a printed report.** One
report writer emitted two decimals, which is enough to hide a real disagreement *and* enough
to manufacture a fake one.

#### Porting: what an equation-by-equation walk misses

**Grep the source for variable BOUNDS before believing a port is complete.** Walking the
equation list is not sufficient and cannot be: bounds are not equations. One model carried
107 equations and exactly one bound — `ProductionByTechnology.fx(...) = 0`, sitting among
the variable declarations — and omitting it left the objective 1.70 low on 72,412. Too small
to notice, far too large to be arithmetic, and invisible to a check that diffs equations.
Sweep `.fx` `.up` `.lo` in GAMS, `setLB`/`setUB`/`.lb`/`.ub` elsewhere, and **scope the
sweep to the files that produced the published result** — a parallel session's first attempt
globbed a `superseded/` folder and reported bounds from an abandoned variant.

**The sign of a discrepancy says what kind of bug it is.** Too low on a minimisation means
under-constrained: a missing restriction, not a wrong coefficient. That turns "search
everything" into "search for something that restricts".

**A real bug that explains nothing is a trap.** A genuine transcription error, correctly
fixed, moved that objective by exactly zero because the constraint was not binding. Finding
it nearly ended the search.

**"Positive variable defined by an equation" constrains nothing unless the defining
expression can go negative.** Five equations in one model read as constraints and were inert.

#### The port is usually smaller, and that is not an approximation

Modelling languages generate variables over the full cross product of their index sets. Most
of it is structurally empty. Measured: 51 of 765 technology-fuel pairs produced anything, so
a faithful port built 1.56M variables against the original's 18.76M for identical
mathematics. A variable that exists only to be forced to zero is padding, and presolve
removes it anyway.

**Do not report the two sizes as if they were the same measurement.**

#### Boundaries — where this archetype stops applying

Write these beside the rules, or the archetype gets used where it does not fit.

- **Shipping the model as `.mps`/`.sol` dies above roughly 2M nonzeros.** Flat formats run
  about 50 bytes per nonzero against a 100 MB hosting limit. Below that, ship them and verify
  row by row; above it, verify by reconstructing the objective from its cost components
  instead — weaker as proof, better as explanation, and it shows what the number is made of.
  One model's would have been 3.4 GB.
- **"Runs for everyone" requires a free solver for the problem class.** True for LP,
  marginal for MIP, false for MINLP. And a size-limited licence is **not** the fallback: one
  vendor's bundled licence caps at 2,000 variables, where the smallest useful reduction of a
  real model was 4,726. Verify the cap by **solving**, not by declaring variables — that
  vendor enforces it at optimize, so a probe that only declares reports success under a
  licence that then refuses the real build.
- **Committed cleaned output assumes it stays small.** Around 10 MB is comfortable. Compress
  or subset before abandoning the pattern.
- **"The original kept verbatim" holds only for finished work.** For a paper repo it is
  right, and a test should fail if those files change. For active research the original *is*
  the working copy and freezing it is wrong.
- **Presentation choices do not travel.** Splitting an objective into named parts helps at a
  scale where one summation spans millions of terms and hurts everywhere else. Mark such
  choices as local when you make them.


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

### Git and syncing folders: four axes, decided separately

"Clone outside any syncing folder" answers the easy half. The hard half is the folder that
**must** stay synced — work product that belongs on institutional storage, or personal
material whose backup *is* the sync service. Deleting the sync is not available, so the
history has to move instead.

**Four** questions decide a folder's treatment, and they are independent. Conflating any two
produces a rule that contradicts itself:

    how sensitive is it?        ->  may reach a public host, or never
    is it actively developed?   ->  wants git, or does not
    is it in a syncing folder?  ->  .git via a pointer, or .git in place
    how many devices EDIT it?   ->  one writer, or many

**Sensitivity does not decide whether something has git. Activity does.** A private repo is
not made safe by being private, and a folder is not made unversionable by being sensitive.

**The fourth question is the one most easily skipped, and it can veto the other three.**
It is not "how many devices sync it" — everything synced reaches every device. It is how
many devices *record changes*. Ask it before reaching for the pointer treatment below,
because that treatment answers it with "one" whether or not one is the true answer.

#### When the answer is: no git at all

A folder edited from a phone, a tablet and several computers **cannot** take the pointer
treatment, and should not have git.

The reasoning is not that git is too heavy. It is that both available shapes fail. A `.git`
inside the syncing folder corrupts — that is the whole premise of this section. A `.git`
behind a pointer works, but binds history to exactly one machine, so a change made anywhere
else cannot be recorded at all. For a folder whose purpose is capture from wherever the
thought happens, that converts a sync property into a single-device restriction and calls it
a safeguard.

**Use the sync service's own file versioning, and encode the update rule in the filename:**

    dated    YYYY-MM-DD[letter]-slug.md   append-only. Never rewritten; a correction is a
                                          new dated file citing the original.
    undated  <topic>.md                   living. Overwritten in place, because a stale
                                          current-state doc misleads, while a stale dated
                                          one is merely history.

The presence or absence of a date **is** the update rule. Nothing enforces it, nothing can
fail to run, and it behaves identically on a phone. Archive a superseded summary by writing
the new one dated — not by deleting the old.

**Append-only governs a file's claims, not its cross-references.** A dated file is never
rewritten to change what it said. Exactly one edit is permitted afterwards:

    > **SUPERSEDED by [YYYY-MM-DD[x]-slug](...). <one sentence on what changed.>**

at the top, or under the heading of the one section that was overtaken. It asserts nothing
about the subject - it tells a reader who arrived at an old file that a newer one exists.
Without it, append-only guarantees that **the stalest document is the one a search finds
first.** The successor cites the predecessor in turn, so the relation survives either file
being read alone. **And the index carries it**: a supersession that is not in the index has
not happened, because the index is the read path.

**An undated file's staleness is a mechanical check, not a stamp.** It carries a `Verified
<date>` line recording when its claims were last checked against reality - the one thing
version control cannot know - while its modified date comes from git and cannot drift. **It is
stale when modified is later than verified.** Measured across 16 such files on 2026-09-07:
five carried a verified date, one carried a date three months in the future, and three had
been modified days after the stamp they still displayed. **A stamp older than its own content
is worse than no stamp**, because it asserts a check that never covered the current text.

**The date goes inside the file and never in its name.** Presence or absence of a date in the
*name* is the entire discriminator above; a dated name on a living file inverts its rule.

**An undated file lives beside what it is about. The subject decides the home; the form does
not.** A folder of them belongs to its own subject - a notebook about tooling holds briefings
about tooling - and a briefing about a project lives in that project, however it is written.
Three forms share the one update rule:

    reference state    what is true now about a topic, read cold by someone with no context
    executable prompt  a job to hand over, with the decisions already made
    editorial          what a body of work concluded, what it is FOR, and what to carry into
      carry-forward    the next thing - argued, not summarised

**The third is the one that goes unwritten**, because it reads like conversation and so feels
already said. It is not a summary and not a status page, and it is usually the only place the
reason behind a decision survives once that decision's outputs are finished.

**There is no fifth location.** A file's location and name declare its update rule before
anyone opens it, and that is a precondition for writing one - not a description of where
things ended up. A document that fits none of these does not get a new folder: it gets
classified, or it is not written. **A folder accumulating documents belonging to none of them
is a defect in the taxonomy rather than a place** - either it earns an archetype in this Part
with its own stated update rule, or its contents are pushed down into what they describe and
it is retired. On 2026-09-07 one such folder held 209 MB and 88 documents with six of its
seven subfolders carrying no history at all, because every session that had something to write
and no legal place to put it wrote there.

This is weaker than git and the weakness should be stated plainly: no commits, no branches,
no `git log`, no atomic multi-file change. What it buys is that every device can write. For
raw capture — ideas, journals, notes — that trade is correct, and the convention above has
been running the `claude-notes` repo's own `notes/` versus `briefings/` split since
2026-09-03.

#### The pointer treatment

**Precondition: exactly one machine edits this worktree.** If that is not true, the previous
subsection applies instead. Everything below assumes a single writer and is unsafe advice
without it.

When the working tree must stay in a syncing folder and the repository is actively
developed, the history moves out and the tree stays:

    git init --separate-git-dir <dev-root>/gitdirs/<name>.git  <worktree>

This leaves a `.git` **file** in the worktree containing one line, `gitdir: <path>`. Git
follows it; the sync client sees a 50-byte text file instead of thousands of loose objects.

Three properties make this safe where a synced `.git` is not. The worktree syncs
continuously and is a normal set of files. The history is on one machine's local disk and is
never touched by two writers. And the pointer file itself syncs, so the arrangement is
*self-announcing* on every other machine rather than silent.

> **`--separate-git-dir` cannot cross a volume boundary.** It is implemented as a rename, so
> a worktree on one drive and a gitdir on another fails with `fatal: … Improper link`. The
> command still creates the pointer's *absence* rather than erroring cleanly, so a script
> that does not check will proceed against a repository it did not migrate. Across volumes:
> copy the `.git` directory, set `core.worktree` in the copy, verify `git --git-dir=… log`
> and `status` against the worktree, and only then remove the original and write the pointer
> by hand.

#### One machine owns the history, and says so

A synced worktree is visible from every machine on the account. **Exactly one machine holds
its gitdir.** The others are expected to fail.

That failure is the enforcement, and it is free: git reports
`fatal: not a git repository: <path>` naming a path that exists on one machine, and the
working tree is untouched. Nothing needs to detect the second machine or defend against it.

**Why one owner rather than two synced ones:** the working tree syncs continuously while
history syncs on whatever schedule the client chooses. Two machines each holding git means
the second sees the first's *committed* work as *uncommitted* changes, and can re-commit it
under its own authorship. That failure is silent, which makes it strictly worse than the
loud failure above.

**Every such worktree carries a `GIT-OWNER.md`** beside the pointer, naming the owning
machine, the gitdir path, and the fact that the error is deliberate. The pointer file does
not explain itself, and the obvious repair on a second machine — re-init, or create the
missing gitdir — is exactly the corruption the arrangement prevents.

##### A rule enforced by a failure needs the failure to explain itself

This is a general obligation, not a detail of this one file. **Any rule whose enforcement
mechanism is an error message will be reported as a bug by whoever meets the error without
knowing the rule** — and reported in good faith, because a red `fatal:` is what a fault
looks like.

Measured across the two-machine migration: the second machine met three pointer files that
failed exactly as designed, and correctly read them as intended behaviour, **because a
`GIT-OWNER.md` sat beside each one.** In the same pass it met four bare mirrors that also
failed exactly as designed — their sources having moved out of reach — with no equivalent
note beside them, and initially reported those as a finding. The difference between the two
readings was entirely the presence of the explainer.

So: where a design chooses a loud failure over a silent one — which this section
recommends twice — the explanation ships **next to the thing that fails**, in the place
someone lands when it does. Not in a decisions log, not in the standard, not in a chat.

**"Beside it" has to be defined for things with nowhere to put a file.** A synced worktree
has an obvious place; a **bare repository has no working tree at all**, so nothing can sit
next to it the way `GIT-OWNER.md` sits next to a pointer. Left unstated, the rule is
unimplementable in exactly the case that produced it — the four mirrors whose designed
failure was read as a finding are bare repos.

For a bare repository, "beside it" is one of:

    a README.md in the directory that CONTAINS the set    covers all of them at once, and is
                                                          where someone lands after an error
    git config --add <a note key> in the repo             travels with the repo itself, and
                                                          survives being moved

Prefer the containing directory's `README.md` when the repos share a fate, which they
usually do. **The obligation is that whoever meets the error finds the explanation without
already knowing the rule** — the medium is whatever satisfies that for the artifact at hand.

#### Backing up a repository that has no remote

A worktree that may never reach a host still needs a backup, and a live `.git` cannot be one:
a bare mirror on the same disk protects against nothing a copy would not, and a mirror in a
syncing folder is the original problem again.

**Use a dated `git bundle`.** A bundle is a single static file, written once and never
concurrently modified, so it is safe inside a syncing folder where a live `.git` is not.

    git -C <worktree> bundle create "<cloud>/<name>-$(date +%Y-%m-%d).bundle" --all
    git -C <worktree> bundle verify "<cloud>/<name>-$(date +%Y-%m-%d).bundle"

> **`bundle verify` needs a repository, and it is not the bundle.** Run without `-C`, from a
> directory that is not a repo — which is what a scheduled job does — it exits **1** with
> `error: need a repository to verify a bundle`, having verified nothing. A job that does not
> check the exit code then writes bundles forever and never verifies one, which is precisely
> the failure this paragraph exists to prevent. Point `-C` at the repository the bundle came
> from.

Three properties are load-bearing. `bundle create` never modifies the source repository.
**Verify immediately** — an unverified backup is a claim, not a measurement. And **date the
filename**, so a bad bundle cannot overwrite a good one.

A bare mirror whose `origin` is a local path is not a backup either way: it is a second copy
on the same disk whose link to the original breaks the moment the original moves or is
deleted, and it goes on reporting success until something asks it to fetch.

---

---

## Part 2c — The life of a project: starting one, and ending one

### Nothing is created for you, and that is the problem

Opening a session in a folder creates **exactly one thing**: a path-keyed directory under
`~/.claude/projects/`, which accumulates that folder's memory and transcripts. Everything
else — git, a remote, a `CLAUDE.md`, a `.claude/` — exists only because somebody made it.

Nothing prompts for the decision, so in practice it is never made. A folder ends in whatever
state its first session happened to leave it, and the reasoning is not recorded anywhere.

**Measured 2026-09-06:** 38 path-keyed directories, 1.1 GB, 84 memory files. **Six were
orphaned** — 633 MB and 12 memory files keyed to folders that no longer exist. One pair was
stranded by renaming a project folder months earlier; one was stranded the same day, by a
migration that had a step for this and applied it only to the folders it already knew about.

### Starting: answer four questions, then act

The four axes are stated in *Git and syncing folders*. Answer them **before** the first
commit, because two of the four are expensive to change afterwards: a remote cannot be
un-published, and a history cannot be un-recorded.

Write the answers into the folder's own `CLAUDE.md` under its Part 11 heading — one sentence
each. A structure whose reason is written down survives the first person who finds it
inconvenient; one whose reason is not gets "tidied" within a year.

### What exists once a project is running

    ~/.claude/projects/<key>/          AUTOMATIC. Memory and transcripts. Keyed by the
                                       absolute path with punctuation replaced by dashes,
                                       so it is orphaned by any rename or move.
    <folder>/CLAUDE.md                 written by you. Points at this standard; adds Part 11.
    <folder>/.claude/settings.local.json   written by the harness as permissions are approved.
    <folder>/.git or .git pointer      only if git was chosen
    the GitHub repository              only if a remote was chosen
    a bundle or mirror                 only if the repo has no remote and needs a backup
    ~/.claude/projects/<key>/<uuid>/    AUTOMATIC, and only if a session spawned a subagent
                                       or overran a tool result. Subagent transcripts and
                                       spilled output. Goes with the transcript.

Seven things, of which **two are created without being asked for and none is removed
automatically.** That asymmetry is what produces orphans.

### Git: when, and when not

**Use git when the thing changes and you would want to know what changed** — code, notebooks,
prose under revision, anything where "what did this look like before" is a real question.

**Do not use git for:**

- **Binaries and finished outputs.** Git stores them badly and history is permanent, so a
  large binary committed once is carried forever. Proposal folders are Word, PDF and Excel;
  see Part 2b.
- **Raw capture edited from several devices.** The pointer treatment binds history to one
  machine, which is wrong for anything written from a phone. See *When the answer is: no git
  at all* for the filename convention that replaces it.
- **Anything whose backup requirement is already met by a sync service** and which nobody
  will ever diff.

**How, when the answer is yes:**

    git init
    # write .gitignore FIRST - see Part 1, "Git history is permanent"
    git check-ignore -v <a file that must never be committed>     # verify, do not assume
    git add . && git commit

The `check-ignore` step is not optional. A credential in history means rotating the
credential, not amending the commit.

### GitHub: when, and when never

**Publish to GitHub when at least one is true:** somebody else needs it; it must survive the
machine; or it will be cited. Absent all three, git alone is enough and a remote is
unmanaged surface.

**Never publish:**

- Anything sensitive, or adjacent to an education record. Consolidated observations about
  students are education-record adjacent even when no name appears — see Part 0.
- Anything that maps a credential exposure. **Publishing a map of an exposure is worse than
  publishing a key that has already been rotated**, because the map says where to look and
  what is still worth trying.
- Work product belonging on institutional storage. Moving it to a personal account does not
  reduce exposure; it relocates it and adds a second copy.

**How:** `gh repo create <name> --private`, with the name built per *Repository names lead
with what the searcher already knows*. Add `LICENSE` **always**, and `CITATION.cff` if it
will be cited — see Part 5. Without a licence the repo is under exclusive copyright, and the
students you handed it to have no permission to run it. Private is the default and public is
the decision.

### Retiring a project: seven things trail it

Deleting the folder handles three of them. **The other four are why orphans accumulate.**

    1  the working tree            delete, ONLY after the replacement is verified to exist
    2  .git, or gitdir + pointer   delete both halves; a pointer left behind names a gitdir
                                   that no longer exists, which reads as corruption
    3  .claude/ in the folder      goes with the folder
    4  CLAUDE.md in the folder     goes with the folder
    5  the GitHub repository       archive rather than delete - archiving is reversible and
                                   says "complete" rather than "gone". Delete only if it
                                   should never have existed.
    6  ~/.claude/projects/<key>/   RENAME it to the successor's key if the work moved;
                                   delete it only if the work is genuinely over. Memory
                                   files are curated and are not logs.
    7  every pointer that names it  briefings, ~/.claude/CLAUDE.md, scheduled tasks, other
                                   projects' CLAUDE.md files. Dated notes are history and
                                   are left alone.

**Before deleting anything, verify the replacement exists.** Clone first, check the file
count and the tracked count, and only then remove the original. And verify "it is all pushed"
rather than accepting it: check `git log --branches --not --remotes`, and compare local tags
against the remote's **peeled** refs.

### Retiring a record

**A session leaves three kinds of thing behind and only one may be deleted on a schedule.**

    RECORD    verbatim, written by the harness, never edited, grows without bound
              ~/.claude/projects/<key>/*.jsonl and everything under <key>/<uuid>/
              ~/.claude/shell-snapshots/, sessions/, backups/
    CURATED   written deliberately, small, and the reason a record can be deleted
              memory/, dated notes, undated briefings, a project's Part 11,
              ~/.claude/CLAUDE.md, this document
    CONFIG    neither a record nor a summary; deleting it changes how sessions behave
              ~/.claude/settings.json - permissions AND hooks - settings.local.json,
              scheduled tasks

**A record is deletable and a curated artifact is not.** That is the whole retention policy.

**Harvest, then delete.** *Before deleting anything, verify the replacement exists* applies
here unchanged, because a record's replacement is a curated artifact:

    1  a NAMED curated artifact holds what the record held - it need NOT be in that folder
    2  a dated note records the harvest, arguing what mattered rather than listing ids
    3  the CONFIG surface is copied out first
    4  only then delete the .jsonl and its <uuid>/ directory

**Step 1 names an artifact; it does not check a directory.** A gate reading "the folder has a
non-empty `memory/`" fails the first correct case it meets - a session working in one folder
whose harvest belongs, by the routing table in Part 0, in another. **A gate that blocks the
routing rule's own outcome is the wrong gate.**

**An empty `memory/` is a signal to look, not a verdict.** Check every place a session can
write, the project folder included. On 2026-09-07 the folder with the most at stake had no
memory file at all, and a subfolder holding the full editorial summary of the same work.

**Age is not the criterion.** The oldest record is as likely as any to be the valuable one,
and the largest are usually the ones already summarised. A rule that deletes by age deletes by
the one property that does not predict value.

**A fact recovered from a record cites the record it came from**, for as long as that record
exists. Afterwards the citation is the only evidence that the fact was read rather than
recalled.

**Archiving a session is not deleting its transcript.** Two operations on two objects, and the
second is not implied by the first.

**Configuration leaves before the record does, and a script it names lives in a repository.**
A hook is executable behaviour, not a preference: removed during a cleanup it does not fail
loudly, it simply stops happening. Config mostly should not sync either, because a hook names
an absolute local path and a synced copy points at nothing on the second machine - failing
silently, again. What travels between machines is the *intent*, which is an undated file's
content; the script itself belongs in a repository and never beside the config.

### Finding what was already left behind

The path key is the absolute path with every non-alphanumeric character replaced by `-`.
That encoding is **lossy** — `:`, `\`, spaces, commas, apostrophes and underscores all become
`-` — so it can be computed forwards and **cannot be reversed**. Any orphan hunt that decodes
a key back into a path will produce false positives.

**Read the path from inside instead.** Each transcript records the session's `cwd`; encode
that and compare it to the directory's own name:

    key == enc(cwd)  and the path exists     -> live
    key == enc(cwd)  and the path is gone    -> ORPHANED
    key != enc(cwd)                          -> the directory was renamed to follow a move,
                                                which is the correct outcome, not a fault

For stale pointers, **enumerate the moves and search for each one.** A sweep for a single old
path is not a sweep for stale pointers: on 2026-09-06 a validated search for one retired root
ran clean while five other dead paths sat in eleven live files, including this document's own
Governance section.

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

This is not a house preference. It is the **expertise reversal effect**: guidance that helps
a novice becomes redundant, and then actively harmful, as the learner's own schema forms.
Worked examples beat unguided problem-solving for novices and the advantage reverses with
expertise - which is exactly why the streamlined version belongs at the bottom rather than
nowhere, and why a style guide written for working engineers is correct for its reader and
wrong for this one.

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

### Accessible to the student who cannot see the figure

**This is a legal obligation, not a courtesy, and it has a date.** A public university is a
Title II entity, and the DOJ's 2024 rule makes WCAG 2.1 Level AA the standard for web content
a covered entity provides or makes available — course material included — from **26 April
2027** for entities serving 50,000 or more. A public repo with a hosted-notebook badge is web
content the university makes available. Nothing about it being a notebook exempts it.

**The three rules above create most of the exposure, so they are where the remedy goes.**
*Ship it executed* commits every rendered figure. *Print something after each step* fills the
notebook with output. *One click, no install* makes it public. None of those is wrong; each
of them ships something that has to be readable by someone who is not reading it with their
eyes.

    every committed figure        carries a text alternative saying what it SHOWS, not what
                                  it is. "Cost falls steeply to about 40 units and is flat
                                  after" - not "line chart of cost versus units."
    every figure that MATTERS     also has its numbers reachable as text or a table. The
                                  reader who cannot see the plot should not have to take the
                                  claim on trust, and this is the same requirement as "every
                                  number in the prose comes from a run", pointed the other way.
    colour                        never the only carrier of meaning. Add markers, line styles,
                                  direct labels. Avoid red/green, green/brown, green/blue and
                                  blue/grey together.
    markdown headings             a real hierarchy, in order, never skipping a level. The
                                  heading structure IS the navigation for a screen reader,
                                  which is why "one idea per cell with a heading above it"
                                  was already the right rule for a second reason.
    link text                     says where it goes. Never "click here" or a bare URL.
    any video or recording        captioned.

**Alt text is a one-sentence cost at authoring time and a project in retrospect.** The
teaching library is organised by topic so one notebook serves several courses across several
years, which means an inaccessible figure is inherited by every course that draws on it. The
library's structure concentrates the remediation exactly as it concentrates the error.

> **Write the alternative text in the same cell as the plot, at the moment you write the
> plot.** A checklist item that says "add alt text before shipping" is a requirement living
> in prose, and Part 6 says those have already failed.

- [ ] **Every committed figure has a text alternative**, colour is not the only carrier of
      meaning, and the markdown headings form a hierarchy that does not skip a level.

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

**A repo that ships data needs a second licence, because the first one does not cover it.**
This document requires instance tables in `data/raw/` and committed figures and results. MIT
and Apache-2.0 speak about *the Software*; they say nothing about a database right, so the
tables a reader was told to edit are the one part of the repo whose terms are unstated.

    code                          MIT, or Apache-2.0 where a patent grant is wanted
    data, tables, figures         CC0 where you want it used with no conditions;
                                  CC-BY where attribution matters and citation norms alone
                                  are not enough
    prose, slides, notebooks-as-text   CC-BY

Say which is which **in the LICENSE file or the README**, by path. A second licence with
nothing saying what it covers is worse than one, because now two documents claim the same
files.

> **Choosing nothing is choosing.** Zenodo's licence field is required and defaults to CC-BY,
> so an unstated choice becomes a stated one at deposit — see the DOI procedure below. And a
> repo with no licence at all is under exclusive copyright: a public host's terms let people
> view and fork, which is not permission to run, modify or teach from it.

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
2. Connect the repo in Zenodo, tag a release. **Set the licence on the deposit explicitly** —
   it is a required field and it defaults to CC-BY, so a repo licensed MIT is deposited under
   a content licence unless you say otherwise.
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

**Which is which, so the question is never reasoned out under pressure:** `master` is **git's**
default and `main` is **GitHub's**. A bare `git init` still produces `master` in git 2.51 unless
`init.defaultBranch` is set; GitHub has created `main` since October 2020, and every badge, raw
URL, Pages build and CI default followed it. **If it deploys to GitHub there is no choice — it is
`main`.**

**The rename is free before the first push and never again.** With no remote, `git branch -m master
main` leaves nothing behind, and badges already naming `main` simply start resolving. After a push
it means renaming a live default branch, which leaves a stale branch that still resolves and serves
quietly older content.

#### When the free window has already passed

Naming the expensive case and stopping there is what this section used to do, and it left the
common situation unanswered. **Rename through the host's own rename**, which moves the branch,
retargets open pull requests and redirects the web UI. Then fix the two things it does not, both
of which are silent:

    existing clones      git branch -m master main
                         git fetch origin --prune
                         git branch -u origin/main main
    hardcoded URLs       every /blob/master/ and /raw/master/ already copied out

**Never rename by creating `main` and leaving `master` behind.** Two branches that both resolve
will drift, and the stale one goes on serving older content to anyone who reaches it — the defect
the rename was meant to remove, now with a second copy. Observed on one repository where the
abandoned branch sat **66 commits** behind while the site itself deployed correctly from `main`:
nothing was broken, nothing reported it, and only a clone or a direct link would have found it.

**A deployed site is not evidence the branches are right.** Check what the host builds from and
what branches exist, separately — the first can be correct while the second is not.

> **`gh api repos/<owner>/<repo>/branches/<name>` is not an existence check.** Asked for a branch
> that does not exist, it has been observed returning **a different branch** rather than failing,
> which reads as confirmation. Use `git ls-remote --heads`, which lists what is actually there.
> Same shape as every other probe in Part 12 that agreed with itself.

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

### A check that runs before you write, not after

Every rule in this section is about noticing that a thing you believed is false. Most of
them were learned after the fact. A session-start check moves that discovery to before the
first write, which is the only point where it is free.

The check runs on session start, in the session's own directory, and **prints nothing when
the repository is healthy** — its output becomes session context, so silence is the correct
result and noise trains the reader to skip it.

    no .git at all              exit silently; not every folder is a repo
    remote unreachable          WARN and proceed - offline, timeout and a dead remote are
                                indistinguishable from here, and none of them is a reason
                                to refuse to work
    confirmed behind            BLOCK - this is the only case where the local state is
                                known wrong
    no remote configured        LOUD EXEMPTION - never a silent pass. A repo with no remote
                                is the case most likely to have no backup at all
    detached HEAD               report; nothing can be compared to a remote from here

**Warn on unreachable, block only on a confirmed "behind."** One rule then covers the slow
remote, the deleted remote and the aeroplane, with no timeout threshold to tune — and
tuning a threshold is how a check acquires a case nobody has tested.

**A repo with no remote must report, not pass.** That is the case the pointer treatment
above creates deliberately, and a silent pass there would hide exactly the repositories
whose backup situation is least automatic.

### Eight traps, each one a check that agreed with itself

Every entry below produced a confident wrong answer, and in each the tool reported success.
They are recorded individually because the general rule — *verify the outcome, not the step* —
did not stop any of them from happening; naming the specific shape is what does.

#### `$?` after a command substitution is not the exit code you think

    printf '%-40s rc=%s\n' "$(basename "$m")" "$?"     # WRONG

Arguments expand left to right, so the command substitution runs first and `$?` reports
*its* status. This was used to verify four bare mirrors; all four reported `rc=0` and one
was actually `rc=128`, against a remote that had been deleted minutes earlier. It is the
same failure as piping into `head` and reading the pipeline's status, arriving by a
different route — and it is worse, because there is no pipe to notice.

**Capture the status into a variable on the very next line, before anything else runs.**

#### An idle session still holds its working directory

An assistant session keeps a live process per session, indefinitely. The operating system
pins that process's working directory, so the folder **cannot be renamed or deleted** while
writes *inside* it still succeed — which makes it read as a permissions problem rather than
a lock. On Windows the error is `Device or resource busy`.

Archiving the session stops the process and releases it; closing its window does not.
**Before any folder-wide move, list the sessions and their working directories.**

#### `rm -rf` on a pinned directory partially succeeds

It removes every child, then fails on the directory itself. You get an error message *and*
an empty folder. Reading only the error concludes nothing happened; the contents are gone.
**Check what remains rather than reading the exit status.**

#### A missing `.git/index` looks exactly like mass deletion

With no index, `git status` reports every path in `HEAD` as a staged deletion and every
path on disk as untracked — 1,530 deletions against 1,521 files present and untouched.
It reads as catastrophe and is nothing: `git reset` rebuilds the index from `HEAD` and
touches no file in the working tree.

**Do not "fix" it by committing.** That is the one action that makes the phantom deletions
real.

#### A tag comparison must peel the ref

`git ls-remote --tags` returns the **tag object** sha for an annotated tag; `git rev-list -n1`
returns the **commit**. Comparing those two manufactures a mismatch on a tag that is
perfectly in sync. Compare against `refs/tags/<name>^{}`, and say which you used — the same
rule as quoting a hash without its normalisation.

#### "No trace" requires enumerating replicas, not deleting the visible copy

A backup exists to be redundant, so by construction there is more than one. Deleting the
copy in front of you removes **redundancy** and leaves the **content**, while producing a
report that says the content is gone.

Measured: a credential was found in one commit of a bare mirror. The mirror was deleted and
the value searched for across every tree on that machine — zero hits, reported as removed.
A second machine held its own copy of the same mirror, which the deletion had just promoted
to the only copy of that history anywhere. The search was correct and the conclusion was
false, because the search's scope was one machine and the claim's scope was all of them.

**Before reporting that something is gone, list where it could be.** Other machines on the
account, bundles, mirrors, the sync service's own trash, and any transcript that quoted it.
A count of locations checked belongs beside the count of hits.

#### A mirror can silently become the last copy

The same event from the other side. A bare mirror whose `origin` is a local path is a weak
backup — but it is also **not safely disposable**, because nothing inside it says whether it
is the last one. Its `origin` still names a path that may no longer exist, and it goes on
reporting success until something asks it to fetch.

Two symmetric errors follow, and a plan should say which it is avoiding: deleting a mirror
that turned out to be the only copy, and preserving one on the assumption it is, when the
content is reachable elsewhere.

#### "Not on `main`" is a claim about trees; content is a claim about blobs

An unreachable commit whose *tree* is absent from `main` has not necessarily lost anything.
The tree records an arrangement; the blobs are the bytes. Measured on six orphaned commits:
three had trees found nowhere on `main`, and **all three referenced zero blobs absent from
it** — the extra objects were the commit and tree containers, not content.

**Stop at the blob level, or the analysis manufactures alarm.** The same shape as comparing
an unpeeled tag ref: a difference at the wrong layer reads as a difference in substance.

---

## The one-line versions

> **Engineering:** if a clean clone can't reproduce it with one command, it's broken.
>
> **Teaching:** abstraction is the reward for understanding, not the route to it.
> Put it at the bottom.
>
> **The boundary:** keep both copies on purpose — and make one assertion compare them.
>
> **Records:** would a stale copy mislead, or merely be old? The first is overwritten, the
> second is never rewritten — and neither is deleted until something curated holds what it held.
