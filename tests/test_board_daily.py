"""The daily star reading (scripts/daily_stars.py) and the workflow that runs
it every day and refreshes the board and both READMEs (board-daily.yml),
since 2026-11-10.

Everything here runs on made-up rows and saved GraphQL answers; nothing reads
the network.
"""

from __future__ import annotations

import contextlib
import io
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "board-daily.yml"
sys.path.insert(0, str(ROOT / "scripts"))

import daily_stars  # noqa: E402
import launches  # noqa: E402
import watchdog  # noqa: E402


def row(slug: str, *, kind: str = "project", url: str | None = None, **extra) -> dict:
    return {"slug": slug, "title": slug.title(), "kind": kind, "url": url or f"https://github.com/o/{slug}",
            "has_code": True, **extra}


CATALOG = [
    row("alpha"), row("beta"), row("gamma"),
    row("essay", kind="article"),  # not a product
    row("delta", flags=["not-jev"]),  # not a product
    row("site", url="https://example.com/site"),  # no GitHub repository
    row("own", url="https://github.com/kydlikebtc/awesome-jev"),  # this repository's own
]


class FakeGraphQL:
    """Answers each aliased lookup from `stars`; a repository missing from it is
    not found, and a batch in `fail` gets no answer at all."""

    def __init__(self, stars: dict[str, int], fail: tuple[int, ...] = ()):
        self.stars, self.fail, self.calls = stars, fail, []

    def __call__(self, query: str, variables: dict) -> dict | None:
        self.calls.append((query, variables))
        if len(self.calls) in self.fail:
            return None
        data = {"rateLimit": {"cost": 1, "remaining": 999}}
        for key, owner in variables.items():
            if key.startswith("o"):
                name = variables["n" + key[1:]]
                n = self.stars.get(f"{owner}/{name}")
                data["r" + key[1:]] = None if n is None else {"stargazerCount": n}
        return {"data": data}


def run(tmp: str, *args: str, ask) -> tuple[int, str, str]:
    folder = pathlib.Path(tmp)
    (folder / "catalog.json").write_text(json.dumps(CATALOG))
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = daily_stars.main(["--catalog", str(folder / "catalog.json"), "--dir", str(folder / "daily"), *args],
                                ask=ask)
    return code, out.getvalue(), err.getvalue()


class ReadingTest(unittest.TestCase):
    def test_every_product_with_a_github_repository_is_read_once(self):
        self.assertEqual(daily_stars.products(CATALOG), [("alpha", "o/alpha"), ("beta", "o/beta"), ("gamma", "o/gamma")])

    def test_owners_and_names_travel_as_variables(self):
        query, variables = daily_stars.query_for([("alpha", 'o/al"pha'), ("beta", "o/beta")])
        self.assertNotIn('al"pha', query)
        self.assertEqual(variables["n0"], 'al"pha')
        self.assertIn("r1: repository(owner: $o1, name: $n1) { stargazerCount }", query)

    def test_a_query_covers_a_hundred_repositories_and_a_failed_one_costs_its_batch(self):
        wanted = [(f"p{i:03d}", f"o/p{i:03d}") for i in range(250)]
        ask = FakeGraphQL({repo: 5 for _, repo in wanted}, fail=(2,))
        with contextlib.redirect_stderr(io.StringIO()):
            found = daily_stars.read_stars(wanted, ask)
        self.assertEqual(len(ask.calls), 3)
        self.assertEqual(len(found), 150)
        self.assertNotIn("p150", found)

    def test_the_reading_is_written_in_slug_order_and_rising_reads_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out, _ = run(tmp, "--date", "2026-11-10", ask=FakeGraphQL({"o/beta": 30, "o/alpha": 5}))
            self.assertEqual(code, 0)
            self.assertIn("stars for 2 of 3 products", out)
            path = pathlib.Path(tmp) / "daily" / "2026-11-10.json"
            text = path.read_text()
            self.assertIn('    {"slug":"alpha","stars":5},\n    {"slug":"beta","stars":30}\n', text)
            payload = json.loads(text)
            self.assertEqual(daily_stars.problems(path.name, payload), [])
            self.assertEqual(payload["date"], "2026-11-10")
            after = {**payload, "rows": [{"slug": "alpha", "stars": 50}, {"slug": "beta", "stars": 31}]}
            catalog = [row("alpha"), row("beta")]
            self.assertEqual([x["row"]["slug"] for x in launches.rising(catalog, payload, after)], ["alpha"])

    def test_a_second_run_that_day_rewrites_it_and_an_earlier_date_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            run(tmp, "--date", "2026-11-10", ask=FakeGraphQL({"o/alpha": 5, "o/beta": 6}))
            code, out, _ = run(tmp, "--date", "2026-11-10", ask=FakeGraphQL({"o/alpha": 5, "o/beta": 6}))
            self.assertEqual(code, 0)
            self.assertIn("unchanged", out)
            code, out, _ = run(tmp, "--date", "2026-11-10", ask=FakeGraphQL({"o/alpha": 7, "o/beta": 6}))
            self.assertIn("rewritten", out)
            code, _, err = run(tmp, "--date", "2026-11-09", ask=FakeGraphQL({"o/alpha": 5, "o/beta": 6}))
            self.assertEqual(code, 1)
            self.assertIn("never dated before the newest one", err)

    def test_under_half_answered_writes_nothing_and_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, _, err = run(tmp, "--date", "2026-11-10", ask=FakeGraphQL({"o/alpha": 5}))
            self.assertEqual(code, 1)
            self.assertIn("1 of 3 products, under half", err)
            self.assertFalse((pathlib.Path(tmp) / "daily").exists())

    def test_readings_older_than_two_weeks_are_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = pathlib.Path(tmp) / "daily"
            folder.mkdir()
            for date in ("2026-10-26", "2026-10-27", "2026-11-01"):
                (folder / f"{date}.json").write_text("{}")
            (folder / "notes.txt").write_text("kept")
            code, out, _ = run(tmp, "--date", "2026-11-10", ask=FakeGraphQL({"o/alpha": 5, "o/beta": 6}))
            self.assertEqual(code, 0)
            self.assertIn("deleted 2026-10-26", out)
            self.assertEqual(sorted(p.name for p in folder.iterdir()),
                             ["2026-10-27.json", "2026-11-01.json", "2026-11-10.json", "notes.txt"])

    def test_the_committed_readings_are_shaped_like_readings(self):
        folder = ROOT / "history" / "daily"
        for path in sorted(folder.glob("*.json")) if folder.is_dir() else []:
            with self.subTest(path=path.name):
                self.assertEqual(daily_stars.problems(path.name, json.loads(path.read_text())), [])


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.text = WORKFLOW.read_text()
        self.jobs = self.text.split("jobs:", 1)[1]

    def test_it_runs_every_day_and_the_watchdog_and_retry_watch_it(self):
        self.assertIn('cron: "40 1 * * *"', self.text)
        self.assertIn("board-daily.yml", watchdog.scheduled())
        self.assertEqual(watchdog.allowed_days("board-daily.yml"), watchdog.MAX_DAYS)
        retry = (ROOT / ".github" / "workflows" / "retry.yml").read_text()
        self.assertIn("board-daily,", retry.split("workflows: [", 1)[1].split("]", 1)[0] + ",")

    def test_it_reads_the_stars_regenerates_and_pushes_only_a_checked_commit(self):
        self.assertIn("permissions:\n  contents: write\n  actions: write\n", self.text)
        self.assertIn("python3 scripts/daily_stars.py", self.jobs)
        self.assertLess(self.jobs.index("python3 scripts/daily_stars.py"), self.jobs.index("scripts/regenerate.py"))
        self.assertLess(self.jobs.index("scripts/regenerate.py"), self.jobs.index("git add -A history/daily README.md"))
        self.assertEqual(self.jobs.count("git add -A history/daily README.md README.zh-CN.md docs llms.txt"), 2)
        self.assertIn("if: steps.checks.outcome == 'success'", self.jobs)
        self.assertLess(self.jobs.index("scripts/check.py --ci --quick"), self.jobs.index("git push -q origin HEAD:main"))
        loop = self.jobs.split("for attempt in 1 2 3; do", 1)[1]
        self.assertIn("git reset -q --hard origin/main", loop)
        self.assertIn("python3 scripts/check.py --ci --quick", loop)
        self.assertNotIn("--force", self.jobs)
        self.assertNotIn("HEAD:refs/heads/", self.jobs)
        self.assertNotIn("github.event.", self.jobs)
        self.assertIn("gh workflow run pages.yml --ref main", self.jobs)

    def test_it_never_queues_behind_the_launch_runs(self):
        # A queued run in a concurrency group replaces the one queued before
        # it, so sharing launch-week's group could drop a Monday or Friday run.
        self.assertIn("concurrency:\n  group: board-daily\n  cancel-in-progress: false\n", self.text)

    def test_it_stages_everything_regenerate_writes(self):
        # A generator added to regenerate.py later is committed here too, or
        # the strict checks on the commit would refuse it.
        import regenerate

        staged = self.jobs.split("git add -A history/daily ", 1)[1].split("\n", 1)[0].split()
        for output in regenerate.OUTPUTS:
            with self.subTest(output=output):
                self.assertTrue(any(output == path or output.startswith(path + "/") for path in staged), output)

if __name__ == "__main__":
    unittest.main()
