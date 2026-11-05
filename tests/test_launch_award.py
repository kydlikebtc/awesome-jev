"""The year's decision award shortlists (scripts/award.py; L23 of the
2026-11-03 launch-board plan), on the made-up rows of test_launches.py."""

from __future__ import annotations

import contextlib
import datetime as dt
import io
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))

import award  # noqa: E402
from test_launches import CATALOG, PATTERNS, launch, row, week  # noqa: E402


def result(rank: int, counted: float) -> dict:
    return {"votes": int(counted), "counted": counted, "discounted": 0, "rank": rank}


ROWS = [
    *CATALOG,
    row("eps", patterns=["tool-selection", "safety-gating"], evidence={"path": "e.py", "matched": ["x"],
                                                                        "read_on": "2026-10-01"}),
]

WEEKS = [
    # Sunday 2026-09-13: before the first award year.
    week("2026-W37", "closed", [launch("eps", result=result(1, 50))]),
    week("2026-W46", "closed", [
        launch("alpha", result=result(2, 4)),
        launch("beta", result=result(1, 9)),
        launch("gamma", result=result(3, 1)),  # cites no file: not eligible
    ]),
    week("2026-W50", "closed", [
        launch("alpha", result=result(1, 3)),
        launch("eps", result=result(2, 2)),
        launch("quiet", status="removed", reason="a ring"),
    ]),
    week("2027-W10", "open", [launch("beta")]),
    # Sunday 2027-09-19: the next award year.
    week("2027-W37", "closed", [launch("beta", result=result(1, 99))]),
]


class AwardTest(unittest.TestCase):
    def test_the_award_year_ends_the_day_before_jev_s_anniversary(self):
        self.assertEqual(award.year_days(2027), (dt.date(2026, 9, 15), dt.date(2027, 9, 14)))

    def test_each_pattern_lists_the_eligible_products_at_their_best_week(self):
        lists = award.shortlists(2027, WEEKS, ROWS, PATTERNS)
        self.assertEqual(list(lists), ["tool-selection", "safety-gating"])
        self.assertEqual([(e["product"], e["week"], e["rank"]) for e in lists["tool-selection"]],
                         [("beta", "2026-W46", 1), ("alpha", "2026-W50", 1), ("eps", "2026-W50", 2)])
        self.assertEqual([(e["product"], e["evidence"]) for e in lists["safety-gating"]], [("eps", "person")])

    def test_a_shortlist_holds_three(self):
        rows = [*ROWS, *(row(f"p{i}") for i in range(5))]
        weeks = [week("2026-W46", "closed", [launch(f"p{i}", result=result(i + 1, 5 - i)) for i in range(5)])]
        self.assertEqual([e["product"] for e in award.shortlists(2027, weeks, rows, PATTERNS)["tool-selection"]],
                         ["p0", "p1", "p2"])

    def test_the_command_prints_a_shortlist_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(ROWS))
            (root / "patterns.json").write_text(json.dumps({"patterns": PATTERNS}))
            (root / "launches").mkdir()
            for w in WEEKS:
                (root / "launches" / f"{w['week']}.json").write_text(json.dumps(w))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(award.main(["--year", "2027", "--root", tmp]), 0)
            self.assertEqual(sorted(p.name for p in root.rglob("*") if p.is_file() and p.parent == root),
                             ["catalog.json", "patterns.json"])
        text = out.getvalue()
        self.assertIn("# Decision award 2027\n", text)
        # The award is the first of each shortlist, said with its reason; nobody picks it.
        self.assertIn("**Award: [Beta](https://kydlikebtc.github.io/awesome-jev/products/beta.html).** Its best week "
                      "was 2026-W46, where it placed #1 with 9 counted votes", text)
        self.assertIn("a person read its call site", text)
        self.assertIn("2. [Alpha](https://kydlikebtc.github.io/awesome-jev/products/alpha.html): #1 in 2026-W50, "
                      "3 votes, 3 counted; evidence: model", text)
        self.assertIn("## Safety gating (`safety-gating`)", text)
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            award.main(["--year", "2026"])

    def test_the_award_is_written_once_when_its_anniversary_has_passed(self):
        self.assertEqual([award.due_year(dt.date(*d)) for d in ((2027, 9, 14), (2027, 9, 15), (2028, 3, 1))],
                         [None, 2027, 2027])
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(ROWS))
            (root / "patterns.json").write_text(json.dumps({"patterns": PATTERNS}))
            (root / "launches").mkdir()
            for w in WEEKS:
                (root / "launches" / f"{w['week']}.json").write_text(json.dumps(w))
            path = root / "docs" / "award" / "2027.md"
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(award.main(["--due", "--on", "2027-08-15", "--root", tmp]), 0)
                self.assertFalse(path.exists())  # not due yet
                self.assertEqual(award.main(["--due", "--on", "2027-09-15", "--root", tmp]), 0)
            written = path.read_text()
            self.assertTrue(written.startswith("# Decision award 2027\n"))
            path.write_text("kept")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                award.main(["--due", "--on", "2027-10-15", "--root", tmp])
            self.assertEqual(path.read_text(), "kept")  # written once, never again
            self.assertIn("2027's is written", out.getvalue())

    def test_the_workflow_runs_monthly_and_pushes_only_a_checked_commit(self):
        text = (ROOT / ".github" / "workflows" / "award.yml").read_text()
        self.assertIn('cron: "0 9 15 * *"', text)
        self.assertIn("python3 scripts/award.py --due", text)
        jobs = text.split("jobs:", 1)[1]
        self.assertLess(jobs.index("scripts/check.py --ci --quick"), jobs.index("git push -q origin HEAD:main"))
        self.assertNotIn("--force", jobs)
        self.assertNotIn("github.event.", jobs)


class EngineTest(unittest.TestCase):
    """docs/launch-engine.md promises the board's rules can be copied without
    the rest of this repository's scripts."""

    @staticmethod
    def local_imports(name: str, seen: set[str] | None = None) -> set[str]:
        import ast

        seen = set() if seen is None else seen
        scripts = ROOT / "scripts"
        local = {p.stem for p in scripts.glob("*.py")}
        for node in ast.walk(ast.parse((scripts / f"{name}.py").read_text())):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else (
                [node.module] if isinstance(node, ast.ImportFrom) and node.module else [])
            for module in (n.split(".")[0] for n in names):
                if module in local and module not in seen:
                    seen.add(module)
                    EngineTest.local_imports(module, seen)
        return seen

    def test_the_rules_import_only_each_other_and_query(self):
        expected = {
            "launches": set(),
            "award": {"launches"},
            "launch_votes": {"_github", "launches"},
            "launch_week": {"_github", "launch_votes", "launches"},
        }
        for name, imports in expected.items():
            with self.subTest(script=name):
                self.assertEqual(self.local_imports(name), imports)
        doc = (ROOT / "docs" / "launch-engine.md").read_text()
        for name in [*expected, "_github"]:
            self.assertIn(f"`scripts/{name}.py`", doc)


if __name__ == "__main__":
    unittest.main()
