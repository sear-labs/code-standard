"""Smoke test for an Archetype A repository.

Copy to `tests/test_smoke.py`, set the three constants below, run it, then
break something on purpose and watch it fail. A test you have only ever seen
pass is not evidence -- see "Watch it fail", below.

RUNS WITHOUT A SOLVER. Nothing here imports gurobipy, and nothing here should.
CI has no licence, and a suite that cannot run on a clean machine is the thing
Part 1 rule 6 exists to prevent. Almost everything that actually breaks in a
research repo breaks before the solver is reached: a missing file, a path that
existed on one laptop, a column that was renamed, a table that stops a year
short of the horizon.

DELETE WHAT DOES NOT APPLY. A test that skips forever is noise, and a test kept
because it came with the template is worse than one you wrote badly on purpose.

Watch it fail
-------------
    pytest -q                                    # green
    <edit a CSV: make one number negative>       # break it
    pytest -q -k negative                        # MUST go red. If it does not,
                                                 # the test is broken, not the data
    git checkout <that file>                     # restore
    pytest -q                                    # green again

Check the edit actually landed before trusting the red. Measured 2026-09-15: an
injection that silently failed to modify the file produced a confident green
tick that meant nothing at all.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd
import pytest

# ------------------------------------------------------------------ set these
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"          # the folder holding instance tables
NOTEBOOKS = ROOT / "notebooks"

CSVS = sorted(DATA.rglob("*.csv"))
NBS = sorted(NOTEBOOKS.glob("*.ipynb"))

# Filenames the notebooks load. Adjust to your repo's idiom -- this matches
# `pd.read_csv(DATA_DIR + 'name.csv')`. Grep one notebook before assuming.
READ_PATTERN = r"read_csv\(\s*DATA_DIR\s*\+\s*['\"]([^'\"]+)['\"]"


# ------------------------------------------------------------------ the data
def test_instance_tables_exist():
    assert CSVS, f"no instance tables found under {DATA}"


@pytest.mark.parametrize("csv", CSVS, ids=lambda p: p.name)
def test_table_parses_and_is_not_empty(csv):
    df = pd.read_csv(csv)
    assert not df.empty, f"{csv.name} parsed to zero rows"
    assert not df.columns.str.contains("^Unnamed").all(), (
        f"{csv.name} has no real header row"
    )


@pytest.mark.parametrize("csv", CSVS, ids=lambda p: p.name)
def test_no_negative_quantities(csv):
    """Costs, demands, capacities and emissions factors cannot be negative.

    THIS IS THE ONE TO REPLACE FIRST. It is a placeholder for your domain's
    real invariants -- whatever must be true of any correct input or output.
    Totals that have to balance. Shares that have to sum to one. A conversion
    efficiency that cannot exceed unity. Those catch real bugs; a sign check
    catches typos.
    """
    num = pd.read_csv(csv).select_dtypes("number")
    bad = num.lt(0).any()
    offenders = sorted(bad[bad].index.tolist())
    assert not offenders, f"{csv.name} has negative values in {offenders}"


def test_no_missing_values():
    """Blanks are usually a join that silently dropped rows.

    Where a blank is DELIBERATE -- a sentinel, an intentionally absent
    combination -- do not relax this test into tolerating blanks generally.
    Pin the structure instead, so the exception stays an exception:

        def test_sentinel_rows_are_exactly_the_unnamed_rows():
            df = pd.read_csv(DATA / "rec_prod_cost.csv")
            unnamed, sentinel = df["Variable"].isna(), df["Cost"] == 9999
            assert unnamed.equals(sentinel)
            assert df.loc[~unnamed, "Cost"].max() < 9999

    That is from a real repo. A big-M of 9999 marking impossible routes was
    undocumented anywhere; the test is now the documentation, and it goes red
    if a real row loses its name or a blocked route gets priced.
    """
    empties = [
        f"{c.name}: {int(pd.read_csv(c).isna().sum().sum())}"
        for c in CSVS
        if pd.read_csv(c).isna().sum().sum()
    ]
    assert not empties, "missing values in " + "; ".join(empties)


# ------------------------------------------------------------- the notebooks
def _notebook_reads(nb_path: Path) -> list[str]:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    src = "\n".join(
        "".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"
    )
    return re.findall(READ_PATTERN, src)


@pytest.mark.parametrize("nb", NBS, ids=lambda p: p.name)
def test_every_notebook_read_resolves_to_a_real_file(nb):
    """The highest-value test here, and the cheapest.

    A notebook reading a file that does not exist fails only when somebody
    runs it, which for a research notebook can be months. Measured on one
    migration: 79 reads across six notebooks, all broken, found by hand.
    """
    reads = _notebook_reads(nb)
    if not reads:
        pytest.skip("no matching reads in this notebook")
    missing = sorted({r for r in reads if not (DATA / r).is_file()})
    assert not missing, f"{nb.name} reads files that do not exist: {missing}"


@pytest.mark.parametrize("nb", NBS, ids=lambda p: p.name)
def test_no_hardcoded_absolute_paths(nb):
    text = nb.read_text(encoding="utf-8")
    hits = re.findall(r"[A-Za-z]:\\\\+Users[^\"']{0,80}", text)
    assert not hits, f"{nb.name} carries absolute paths: {hits[:3]}"


@pytest.mark.parametrize("nb", NBS, ids=lambda p: p.name)
def test_no_credentials_in_notebooks(nb):
    """A licence key reaches the notebook through os.environ or not at all.

    This one cannot undo an exposure -- a credential already committed is in
    history forever, and the remedy is to rotate it. What this prevents is the
    SECOND time, which is how it usually happens: the key comes back when
    somebody copies a working cell out of an older notebook.

    Extend the field list to whatever your tooling uses.
    """
    text = nb.read_text(encoding="utf-8")
    for field in ("WLSACCESSID", "WLSSECRET", "LICENSEID", "API_KEY", "TOKEN"):
        for m in re.finditer(rf"{field}\\?\"\s*:\s*([^,\n]+)", text):
            assert "environ" in m.group(1), (
                f"{nb.name}: {field} is not read from os.environ"
            )
