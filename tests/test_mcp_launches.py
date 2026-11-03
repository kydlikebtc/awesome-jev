"""The launch board as agents read it (L18 of the 2026-11-03 launch-board
plan): the MCP server's launch_board and top_launches tools, the site's
api/v1/launches.json, and where the server gets the weeks from.

query.py answers all three on made-up weeks and rows; server.py is read
through the stubbed loader of test_mcp_caveats.py; data.load_launches is
walked rung by rung with a fake site. Standard library only; nothing reaches
the network.
"""

from __future__ import annotations

import copy
import datetime as dt
import email.message
import json
import os
import pathlib
import sys
import tempfile
import unittest
import urllib.error
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from awesome_jev_mcp import data, query  # noqa: E402
from test_mcp_caveats import load_server  # noqa: E402
from test_mcp_query import PATTERNS, row  # noqa: E402

import launches  # noqa: E402
import site_api  # noqa: E402

FLAGS = [
    {"key": "single-commit", "blurb_en": "One commit."},
    {"key": "vendor-reported", "blurb_en": "The vendor's numbers."},
]

ROWS = [
    row("alpha", has_code=True, evidence={"file": "a.py", "read_on": "2026-11-01"}),
    row("beta", has_code=True, patterns=["safety-gating"], evidence={"file": "b.py", "model_read_on": "2026-11-01"},
        flags=["single-commit"]),
    row("gamma", has_code=True, patterns=["safety-gating", "tool-selection"], evidence={"file": "c.py"}),
    row("delta", has_code=True),
]


def launch(product, *, status="scheduled", role="maker", issue=1, **fields):
    return {"product": product, "issue": issue, "submitted_by": f"{product}-dev", "role": role,
            "submitted_on": "2026-11-05", "tagline": f"{product} decides things", "status": status, **fields}


def result(rank, counted, votes=None):
    return {"votes": votes if votes is not None else int(counted), "counted": counted, "discounted": 0, "rank": rank}


WEEKS = [
    {"week": "2026-W45", "status": "closed", "closed_on": "2026-11-09", "rules": "v1", "launches": [
        launch("beta", discussion=11, result=result(2, 3.0)),
        launch("alpha", discussion=10, result={**result(1, 7.5, 8), "badges": ["week-1"]}),
        launch("delta", status="removed", reason="a ring of new accounts"),
    ]},
    {"week": "2026-W46", "status": "closed", "closed_on": "2026-11-16", "rules": "v1", "launches": [
        launch("gamma", discussion=20, result=result(1, 2.0)),
        launch("beta", discussion=21, result=result(2, 1.0)),
    ]},
    {"week": "2026-W47", "status": "open", "launches": [
        launch("delta", discussion=30), launch("alpha", discussion=31, role="hunter"),
        launch("gamma", status="held", reason="a fork"),
    ]},
    {"week": "2026-W48", "status": "scheduled", "launches": [launch("gamma")]},
]

TODAY = dt.date(2026, 11, 18)  # Wednesday of 2026-W47


def products(view: dict) -> list[str]:
    return [x["product"] for x in view["launches"]]


class BoardTest(unittest.TestCase):
    def board(self, **kwargs):
        return query.launch_board(WEEKS, ROWS, FLAGS, today=TODAY, **kwargs)

    def test_the_board_is_the_running_week_the_last_closed_one_and_the_next(self):
        answer = self.board()
        self.assertEqual((answer["running"]["week"], answer["last_closed"]["week"], answer["next"]["week"]),
                         ("2026-W47", "2026-W46", "2026-W48"))
        self.assertEqual((answer["running"]["from"], answer["running"]["to"]), ("2026-11-16", "2026-11-22"))
        self.assertEqual(answer["today"], "2026-11-18")
        self.assertIn("never added together", answer["note"])

    def test_a_running_week_is_shuffled_without_counts_and_leaves_out_what_is_held(self):
        running = self.board()["running"]
        on = [x for x in WEEKS[2]["launches"] if x["status"] == "scheduled"]
        self.assertEqual(products(running), [x["product"] for x in launches.shuffled(on, "2026-W47")])
        self.assertNotIn("gamma", products(running))
        self.assertFalse(any("result" in x for x in running["launches"]))
        alpha = next(x for x in running["launches"] if x["product"] == "alpha")
        self.assertEqual(alpha["vote"], "https://github.com/kydlikebtc/awesome-jev/discussions/31")
        self.assertEqual((alpha["role"], alpha["evidence"], alpha["page"]),
                         ("hunter", "person", "https://kydlikebtc.github.io/awesome-jev/products/alpha.html"))

    def test_a_closed_week_is_ranked_with_its_counts_and_its_page(self):
        week = self.board(week="2026-W45")["week"]
        self.assertEqual(products(week), ["alpha", "beta"])
        self.assertEqual(week["launches"][0]["result"]["badges"], ["week-1"])
        self.assertEqual(week["page"], "https://kydlikebtc.github.io/awesome-jev/weeks/2026-W45.html")
        self.assertEqual(week["launches"][1]["evidence"], "model")

    def test_caveats_travel_with_each_launch_and_are_explained_once(self):
        answer = self.board(week="2026-W45")
        beta = answer["week"]["launches"][1]
        self.assertEqual(beta["caveats"], ["single-commit"])
        self.assertEqual(answer["caveat_glossary"], {"single-commit": "One commit."})
        self.assertNotIn("caveat_glossary", self.board(week="2026-W48"))

    def test_a_week_not_on_file_or_not_a_week_says_so(self):
        self.assertEqual(self.board(week="2026-W40")["weeks_on_file"], ["2026-W45", "2026-W46", "2026-W47", "2026-W48"])
        self.assertIn("not an ISO week", self.board(week="next")["error"])

    def test_before_any_week_the_board_says_how_it_starts(self):
        answer = query.launch_board([], ROWS, FLAGS, today=TODAY)
        self.assertIn("No launch week is on file", answer["empty"])
        self.assertTrue(answer["submit"].endswith("template=launch.yml"))

    def test_the_answer_leaves_the_weeks_and_rows_as_they_were(self):
        weeks, rows = copy.deepcopy(WEEKS), copy.deepcopy(ROWS)
        query.launch_board(weeks, rows, FLAGS, today=TODAY)
        query.top_launches(weeks, rows, PATTERNS, FLAGS)
        query.launches_api(weeks, rows)
        self.assertEqual((weeks, rows), (WEEKS, ROWS))


class TopTest(unittest.TestCase):
    def test_each_product_once_at_its_best_week(self):
        answer = query.top_launches(WEEKS, ROWS, PATTERNS, FLAGS)
        self.assertEqual([(x["product"], x["week"], x["result"]["rank"]) for x in answer["launches"]],
                         [("alpha", "2026-W45", 1), ("gamma", "2026-W46", 1), ("beta", "2026-W45", 2)])
        self.assertEqual(answer["products"], 3)
        self.assertIn("a rank says more than a count", answer["note"])

    def test_a_pattern_keeps_only_the_products_filed_under_it(self):
        answer = query.top_launches(WEEKS, ROWS, PATTERNS, FLAGS, pattern="safety-gating", limit=1)
        self.assertEqual([x["product"] for x in answer["launches"]], ["gamma"])
        self.assertEqual(answer["products"], 2)
        self.assertIn("valid_patterns", query.top_launches(WEEKS, ROWS, PATTERNS, FLAGS, pattern="nope"))
        empty = query.top_launches(WEEKS, ROWS, PATTERNS, FLAGS, pattern="human-escalation")
        self.assertEqual(empty["launches"], [])
        self.assertIn("filed under human-escalation", empty["empty"])


class SharedRulesTest(unittest.TestCase):
    def test_the_scripts_and_the_server_read_one_tier_and_one_order(self):
        for entry in ROWS:
            self.assertEqual(launches.tier(entry), query.launch_tier(entry))
        self.assertEqual(launches.TIERS, query.LAUNCH_TIERS)
        on = WEEKS[2]["launches"]
        self.assertEqual(launches.shuffled(on, "2026-W47"), query.launch_order(on, "2026-W47"))
        self.assertEqual(launches.week_days("2026-W47"), query.week_span("2026-W47"))


class SiteApiTest(unittest.TestCase):
    STATS = {"last_sweep": "2026-11-01", "entries": 4, "retired": 0,
             "by_pattern": {"tool-selection": 3, "safety-gating": 2, "human-escalation": 0, "overview": 0}}

    def files(self, weeks=WEEKS):
        return site_api.api_files(ROWS, PATTERNS, self.STATS, site_url="https://x/", published=(), launch_weeks=weeks)

    def test_launches_json_holds_every_week_as_filed_and_as_shown(self):
        files = self.files()
        body = json.loads(files[site_api.LAUNCHES])
        self.assertEqual(body["api_version"], 1)
        self.assertEqual(body["weeks"], WEEKS)
        self.assertEqual(body["board"][0], query.week_view(WEEKS[0], {e["slug"]: e for e in ROWS}))
        index = json.loads(files[site_api.INDEX])
        self.assertEqual(index["launches"]["url"], "https://x/api/v1/launches.json")
        self.assertEqual((index["launches"]["weeks"], index["launches"]["bytes"]),
                         (4, len(files[site_api.LAUNCHES].encode())))

    def test_a_stale_launches_file_is_caught_before_publishing(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = pathlib.Path(tmp)
            site_api.write_api(site, self.files(WEEKS[:2]))
            problems = site_api.api_problems(site, ROWS, PATTERNS, self.STATS, site_url="https://x/", published=(),
                                             launch_weeks=WEEKS)
        self.assertTrue(any("launches.json is stale" in p for p in problems), problems)


class _Response:
    def __init__(self, body: bytes, etag: str):
        self.body = body
        self.headers = email.message.Message()
        self.headers["ETag"] = etag

    def read(self) -> bytes:
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *exc) -> bool:
        return False


class LadderTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = pathlib.Path(tmp.name)
        self.outside = self.tmp / "installed" / "awesome_jev_mcp"
        self.outside.mkdir(parents=True)
        env = mock.patch.dict(os.environ)
        env.start()
        self.addCleanup(env.stop)
        os.environ.pop("AWESOME_JEV_CATALOG", None)
        cache = mock.patch.object(data, "cache_dir", return_value=self.tmp / "cache")
        cache.start()
        self.addCleanup(cache.stop)
        self.requests: list[str] = []
        self.offline = False
        net = mock.patch.object(data.urllib.request, "urlopen", self.site)
        net.start()
        self.addCleanup(net.stop)

    def site(self, request, timeout=None):
        self.requests.append(request.full_url)
        if self.offline:
            raise urllib.error.URLError("offline")
        body = json.dumps({"api_version": 1, "weeks": WEEKS[:1]}).encode()
        return _Response(body, 'W/"w1"')

    def weeks_dir(self, where: pathlib.Path, weeks) -> pathlib.Path:
        (where / "launches").mkdir(parents=True, exist_ok=True)
        for week in weeks:
            (where / "launches" / f"{week['week']}.json").write_text(json.dumps(week))
        (where / "launches" / "broken.json").write_text("{")
        return where

    def test_an_override_with_weeks_beats_the_rest(self):
        override = self.weeks_dir(self.tmp / "override", WEEKS[:2])
        os.environ["AWESOME_JEV_CATALOG"] = str(override)
        self.assertEqual(data.load_launches(self.outside), (WEEKS[:2], f"from AWESOME_JEV_CATALOG={override}"))
        self.assertEqual(self.requests, [])

    def test_a_checkout_answers_even_with_no_week_on_file(self):
        repo = self.tmp / "repo"
        repo.mkdir()
        (repo / ".git").mkdir()
        (repo / "catalog.json").write_text("[]")
        self.assertEqual(data.load_launches(repo), ([], f"from the repository at {repo.resolve()}"))
        self.weeks_dir(repo, WEEKS[1:3])
        self.assertEqual(data.load_launches(repo)[0], WEEKS[1:3])
        self.assertEqual(self.requests, [])

    def test_without_a_checkout_the_site_answers_then_the_cache_then_nothing(self):
        self.assertEqual(data.load_launches(self.outside), (WEEKS[:1], "fetched from the site"))
        self.assertEqual(self.requests, ["https://kydlikebtc.github.io/awesome-jev/api/v1/launches.json"])
        self.offline = True
        weeks, line = data.load_launches(self.outside)
        self.assertEqual(weeks, WEEKS[:1])
        self.assertTrue(line.startswith("STALE — "), line)
        (self.tmp / "cache" / data.LAUNCHES).unlink()
        weeks, line = data.load_launches(self.outside)
        self.assertIsNone(weeks)
        self.assertIn("could not be read", line)


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = load_server()

    def test_the_tools_answer_with_query_and_name_both_sources(self):
        s = self.server
        with mock.patch.object(s, "_launch_weeks", lambda: (WEEKS, "from a test")):
            answer = s.launch_board(week="2026-W45")
            top = s.top_launches(pattern="safety-gating")
        self.assertEqual(answer["launch_data"], "from a test")
        self.assertEqual(answer["data"], s.PROVENANCE.line())
        self.assertEqual(answer["week"], query.launch_board(WEEKS, s.CATALOG, s.FLAGS, today=TODAY, week="2026-W45")["week"])
        self.assertEqual(top["pattern"], "safety-gating")

    def test_with_no_weeks_to_read_the_tool_says_why(self):
        s = self.server
        with mock.patch.object(s, "_launch_weeks", lambda: (None, "no source had the launch weeks")):
            answer = s.launch_board()
        self.assertEqual(answer["error"], "no source had the launch weeks")


if __name__ == "__main__":
    unittest.main()
