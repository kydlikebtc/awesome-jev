"""The monthly check of model readings (T1, 2026-10-31): model_sample.py picks
20 rows whose call site only a model has read, the same rows each time for a
month and never a row an earlier month sampled; `--check` validates
docs/model-checks.json; _stats.model_checks() gives status.md the newest
month's count. No network."""

from __future__ import annotations

import contextlib
import io
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import _stats  # noqa: E402
import build_docs  # noqa: E402
import model_sample  # noqa: E402


def row(slug: str, *, model: bool = True, person: bool = False) -> dict:
    evidence = {"path": "a.py", "matched": ["x"]}
    if model:
        evidence["model_read_on"] = "2026-10-25"
    if person:
        evidence["read_on"] = "2026-10-26"
    return {"slug": slug, "kind": "project", "url": f"https://github.com/o/{slug}", "summary": f"{slug} | piped.", "patterns": ["safety-gating"],
            "question_types": ["noul"], "evidence": evidence}


CATALOG = [row(f"r{i:02d}") for i in range(30)] + [row("read", person=True), row("bare", model=False)]


def check(month: str, rows: dict, **extra) -> dict:
    return {"month": month, "by": "croa", "on": "2026-12-04", "rows": rows, **extra}


class PickTest(unittest.TestCase):
    def test_only_rows_a_model_alone_has_read(self):
        picked = {e["slug"] for e in model_sample.pick(CATALOG, "2026-12", [], size=40)}
        self.assertEqual(len(picked), 30)
        self.assertNotIn("read", picked, "a person read it")
        self.assertNotIn("bare", picked, "nobody read it")

    def test_the_same_month_picks_the_same_rows(self):
        first = model_sample.pick(CATALOG, "2026-12", [])
        self.assertEqual(len(first), model_sample.SIZE)
        self.assertEqual(first, model_sample.pick(list(reversed(CATALOG)), "2026-12", []))
        self.assertNotEqual(first, model_sample.pick(CATALOG, "2027-01", []))

    def test_an_earlier_month_is_never_sampled_again(self):
        december = model_sample.pick(CATALOG, "2026-12", [])
        done = [check("2026-12", {e["slug"]: "agree" for e in december})]
        january = model_sample.pick(CATALOG, "2027-01", done)
        self.assertEqual(len(january), 10, "30 rows, 20 already sampled")
        self.assertFalse({e["slug"] for e in january} & {e["slug"] for e in december})
        self.assertEqual(model_sample.pick(CATALOG, "2026-12", done), december,
                         "the month's own answers do not change its pick")

    def test_the_table_escapes_cells_and_leaves_the_answer_blank(self):
        text = model_sample.table(model_sample.pick(CATALOG, "2026-12", [], size=1))
        line = text.splitlines()[2]
        self.assertIn("\\| piped.", line)
        self.assertRegex(line, r"\[a\.py\]\(https://github\.com/o/r\d\d/blob/HEAD/a\.py\)")
        self.assertTrue(line.endswith("| safety-gating | noul |  |"))


class ProblemsTest(unittest.TestCase):
    SLUGS = {e["slug"] for e in CATALOG}

    def problems(self, *checks: dict) -> list[str]:
        return model_sample.problems({"checks": list(checks)}, self.SLUGS)

    def test_a_good_file(self):
        self.assertEqual(self.problems(
            check("2026-12", {"r01": "agree", "r02": "disagree"}, notes={"r02": "it calls the API, not Jev"}),
            check("2027-01", {"r03": "agree"}),
        ), [])

    def test_what_it_refuses(self):
        found = "\n".join(self.problems(
            check("2026-13", {"r01": "yes"}),
            check("2027-01", {"r01": "agree", "nope": "agree"}, by="", on="soon", notes={"r09": "x"}),
            check("2027-01", {}),
        ))
        for text in ("month must be YYYY-MM", "answer must be one of agree, disagree",
                     "r01 was sampled in an earlier month", "nope is in neither", "`by` names",
                     "`on` must be the date", "notes must map sampled slugs", "2027-01 is checked twice",
                     "rows must map 1 to 20"):
            self.assertIn(text, found)
        self.assertEqual(model_sample.problems([], self.SLUGS), ["docs/model-checks.json: must be an object with a `checks` array"])

    def test_the_committed_file_passes(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(model_sample.main(["--check"]), 0)
        self.assertIn("0 problem(s)", out.getvalue())


class StatusTest(unittest.TestCase):
    def test_the_newest_month_is_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "model-checks.json"
            self.assertIsNone(_stats.model_checks(path))
            path.write_text(json.dumps({"checks": []}))
            self.assertIsNone(_stats.model_checks(path))
            path.write_text(json.dumps({"checks": [
                check("2027-01", {"a": "agree", "b": "disagree", "c": "agree"}),
                check("2026-12", {"d": "agree"}),
            ]}))
            latest = _stats.model_checks(path)
        self.assertEqual(latest, {"month": "2027-01", "sampled": 3, "agreed": 2})
        self.assertEqual(build_docs.model_check_cell(latest), "2 of 3 (2027-01)")
        self.assertEqual(build_docs.model_check_cell(None), "not yet sampled")


if __name__ == "__main__":
    unittest.main()
