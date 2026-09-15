# `templates/` — scaffolding that is copied on purpose

**The standard is pointed at, never copied. These files are the opposite: copy them.**

That looks like a contradiction and is not, so the reason is written here rather than left to be
inferred — because the next person to tidy this repository will otherwise delete one rule or the
other.

## Why a document must not be copied but a test must

A **copied document drifts silently.** Measured across two days in September 2026: one project's
copy of the standard ran 46 lines behind, another 28 behind *while appearing stamped with a source
version*, and four scaffolding zips carried not a stale copy but this document's predecessor, a
whole generation back. Nothing reported any of it, and nothing could — a prose file has no way to
notice that it disagrees with its source.

A **copied test drifts loudly.** It runs, on every push, and when it stops matching the repository
it goes red and names the file. That is the same property the standard spends Part 6 asking for.
The failure mode that makes copying a document unacceptable does not exist here.

The evidence for this is already in the repository. `gitignore-starter` is the one artifact the
standard has ever shipped, and it is the rule with the highest compliance — seven repositories
migrated in one morning in September 2026, all seven with `.gitignore` as the first commit, before
any other file. Every rule described only in prose in that same batch produced the directory and
not the substance: seven `tests/` folders holding one `.gitkeep` each, and no CI anywhere.

> **Ship the artifact for anything that can fail. Ship the pointer for everything else.**

## What is here

| | |
|---|---|
| `tests/test_smoke.py` | Licence-free smoke test for Archetype A. Set three constants, delete what does not apply. |
| `.github/workflows/ci.yml` | Runs that suite on a clean machine on every push. No secrets, no configuration. |
| `CITATION.cff` | Citation metadata, with the three things this organisation has got wrong called out inline. |

Each file carries its guidance in its own comments, so it travels with the copy. Read them.

**There is deliberately no `CLAUDE.md` template here.** Dropping it from the scaffolding was a
decision taken 2026-09-03 for the reason in the section above; a project's `CLAUDE.md` names this
repository and adds only its own Part 11. The root `README.md` shows the shape.

## Using them

```bash
cp -r <code-standard>/templates/tests            tests/
cp -r <code-standard>/templates/.github          .github/
cp    <code-standard>/templates/CITATION.cff     CITATION.cff
```

Then, in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
# An archived original (Archetype P) is never corrected, and notebooks are
# narrative rather than modules. Neither is what CI is guarding.
extend-exclude = ["archive", "notebooks"]
```

Run `pytest -q` and `ruff check .` **before** the first push. A CI run that is red on day one gets
switched off by the end of the week, and then the repository has a badge instead of a guard.

Finally, and this is the step that is actually skipped: **break something and watch each test fail.**
The procedure is in the header of `test_smoke.py`. A test you have only ever seen pass is not
evidence — it may be passing because it is correct, or because it is looking in the wrong place. A
green run cannot tell those apart.

## The steps no file can carry

Copying scaffolding fixes the half of the standard that is a file. The other half is not, and it is
invisible for exactly that reason — nothing in a working tree represents any of the following, so
an assistant editing files in a repository cannot do them and will not report them missing.

- [ ] **Topics on the repository.** Both halves of the name — subject *and* method — plus language
      and status. These are GitHub metadata, not a file. They are also the standard's prescribed
      alternative to renaming a repo whose name is hard to search, so skipping them means paying
      the expensive fix later. *(Measured 2026-09-15: ten new repositories, zero topics between
      them, while every established repository in the organisation had six or more.)*
- [ ] **A one-line description** leading with the term the other audience would search for.
- [ ] **Confirm the repo name against the publication record**, not against the source folder's
      name. Whether work is published, and in what venue, is in a CV or in Crossref — never in the
      repository. A year appended without a venue asserts a publication that does not exist.
- [ ] **Confirm the author list against the paper**, not against who was on the project.
- [ ] **Rename now if it is going to be renamed.** The cost is near zero while the repo is private
      with no badges, no releases and no deposit, and it never gets cheaper.
- [ ] **Rotate any credential that has ever been committed** — the redaction commit is not the fix,
      and a repository going from public to private does not undo the months it was public.
- [ ] **Check the upstream you copied from.** A credential redacted downstream is still live in the
      repository it came from.
- [ ] **Archive rather than delete** anything superseded, so links from other repositories survive.
- [ ] **Zenodo, if it will be cited** — public repo first, licence set explicitly on the deposit
      (it defaults to CC-BY), then the *concept* DOI into `CITATION.cff` once and never again.

**Absence of evidence is not evidence of absence, and the tooling makes that trap easy.** An
unauthenticated query about an account returns what *you* can see, not what is there:
`public_repos: 0` on an account holding ninety private repositories reads exactly like an empty
account. Before concluding that something is empty, check that you had the access to see it.
