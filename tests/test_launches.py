"""The launch board's rules (scripts/launches.py, checked by
scripts/check_launches.py), the vote reader
(scripts/launch_votes.py) and the board's pages (scripts/site_products.py),
since 2026-11-03 (docs/launches.md).

Everything here runs on made-up rows and saved GraphQL answers; nothing reads
the network or a generated file.
"""

from __future__ import annotations

import copy
import json
import pathlib
import posixpath
import re
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import datetime as dt  # noqa: E402

import check_launches  # noqa: E402
import launch_votes  # noqa: E402
import launches  # noqa: E402
import lint  # noqa: E402
import site_pages  # noqa: E402

LAUNCH_SCHEMA = json.loads((ROOT / "schema" / "launch.schema.json").read_text())
MAKER_SCHEMA = json.loads((ROOT / "schema" / "maker.schema.json").read_text())
TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text())
PATTERNS = [
    {"key": "tool-selection", "en": "Tool selection", "zh": "工具选择", "blurb_en": "Which tool.", "blurb_zh": "工具。"},
    {"key": "safety-gating", "en": "Safety gating", "zh": "安全闸门", "blurb_en": "Let it through?", "blurb_zh": "放行？"},
]


def row(slug: str, **fields) -> dict:
    base = {
        "slug": slug,
        "title": slug.title(),
        "summary": f"{slug} summary",
        "summary_zh": f"{slug} 摘要",
        "url": f"https://github.com/o/{slug}",
        "kind": "project",
        "has_code": True,
        "patterns": ["tool-selection"],
        "first_seen": "2026-11-03",
        "author": {"name": "o", "url": "https://github.com/o"},
        "evidence": {"path": "src/a.py", "matched": ["/v1/systemone"], "model_read_on": "2026-11-03"},
    }
    return {key: value for key, value in {**base, **fields}.items() if value is not None}


def launch(product: str, **fields) -> dict:
    base = {
        "product": product,
        "issue": 100,
        "submitted_by": "o",
        "role": "maker",
        "submitted_on": "2026-11-12",
        "tagline": f"{product} in a line",
        "status": "scheduled",
    }
    return {key: value for key, value in {**base, **fields}.items() if value is not None}


def week(name: str, status: str, items: list[dict], **fields) -> dict:
    return {"week": name, "status": status, "launches": items, **fields}


CATALOG = [
    row("alpha", makers=["o"], stars=10),
    row("beta", evidence={"path": "b.py", "matched": ["x"], "read_on": "2026-10-01"}, stars=3, makers=["o"]),
    row("gamma", evidence=None, stars=50, first_seen="2026-10-28", makers=["o"]),
    row("delta", flags=["not-jev"]),
    row("essay", kind="article", has_code=False),
    row("quiet", repo_pushed_at="2026-08-01T00:00:00Z", stars=99),
]


def check(launch_files: dict, maker_files: dict | None = None, catalog=CATALOG) -> list[str]:
    return check_launches.check(catalog, launch_files, maker_files or {}, LAUNCH_SCHEMA, MAKER_SCHEMA)


class RowsTest(unittest.TestCase):
    def test_a_product_is_a_project_plugin_sdk_or_integration_with_code_that_is_an_example(self):
        self.assertTrue(launches.is_product(row("a")))
        for kind in ("plugin", "sdk", "integration"):
            self.assertTrue(launches.is_product(row("a", kind=kind)))
        self.assertFalse(launches.is_product(row("a", kind="article")))
        self.assertFalse(launches.is_product(row("a", kind="benchmark")))
        self.assertFalse(launches.is_product(row("a", has_code=False)))
        self.assertFalse(launches.is_product(row("a", flags=["not-jev"])))
        self.assertFalse(launches.is_product(row("a", flags=["shadow-mode-only"])))
        self.assertTrue(launches.is_product(row("a", flags=["no-license"])))

    def test_the_tier_is_who_read_the_cited_file(self):
        self.assertEqual(launches.tier(row("a", evidence={"path": "x", "read_on": "2026-10-01"})), "person")
        self.assertEqual(launches.tier(row("a", evidence={"path": "x", "read_on": "2026-10-01",
                                                          "model_read_on": "2026-10-02"})), "person")
        self.assertEqual(launches.tier(row("a")), "model")
        self.assertEqual(launches.tier(row("a", evidence={"path": "x", "matched": ["y"]})), "file")
        self.assertEqual(launches.tier(row("a", evidence=None)), "none")

    def test_today_is_the_newest_day_the_data_records(self):
        rows = [row("a", first_seen="2026-10-01", checked="2026-11-02"), row("b", first_seen="2026-10-30")]
        self.assertEqual(launches.as_of(rows), dt.date(2026, 11, 2))
        self.assertIsNone(launches.as_of([]))

    def test_a_row_is_quiet_after_sixty_days_without_a_push(self):
        today = dt.date(2026, 11, 3)
        self.assertTrue(launches.quiet(row("a", repo_pushed_at="2026-09-03T10:00:00Z"), today))
        self.assertFalse(launches.quiet(row("a", repo_pushed_at="2026-09-04T10:00:00Z"), today))
        self.assertFalse(launches.quiet(row("a"), today))

    def test_makers_are_the_makers_field_or_the_author_s_github_login(self):
        self.assertEqual(launches.makers_of(row("a", makers=["Alice", "bob"])), ["Alice", "bob"])
        self.assertEqual(launches.makers_of(row("a")), ["o"])
        self.assertEqual(launches.makers_of(row("a", author={"name": "x", "url": "https://example.com/x"})), [])
        self.assertEqual(launches.makers_of(row("a", author={"name": "x", "url": "https://github.com/o/repo"})), [])
        self.assertEqual(launches.makers_of(row("a", author=None)), [])


class WeeksTest(unittest.TestCase):
    def test_weeks_are_iso_weeks_from_monday(self):
        self.assertEqual(launches.week_of(dt.date(2026, 11, 3)), "2026-W45")
        self.assertEqual(launches.week_days("2026-W45"), (dt.date(2026, 11, 2), dt.date(2026, 11, 8)))
        self.assertEqual(launches.week_of(dt.date(2025, 12, 29)), "2026-W01")
        with self.assertRaises(ValueError):
            launches.week_days("2026-45")

    def test_new_this_week_is_the_newest_week_s_products_strongest_evidence_first(self):
        name, rows = launches.new_this_week(CATALOG)
        self.assertEqual(name, "2026-W45")
        # beta (a person read it) before alpha (a model); gamma came the week
        # before; delta and essay are no products; quiet has not been pushed
        # for over sixty days.
        self.assertEqual([r["slug"] for r in rows], ["beta", "alpha"])

    def test_new_this_week_of_nothing(self):
        self.assertEqual(launches.new_this_week([]), (None, []))


def vote(login: str, at: str = "2026-11-17T10:00:00Z", born: str | None = "2020-01-01T00:00:00Z") -> dict:
    return {"login": login, "at": at, "account_created": born}


class VotesTest(unittest.TestCase):
    def test_a_vote_inside_the_week_counts_once(self):
        tally = launches.weigh(
            [vote("a"), vote("A", at="2026-11-18T00:00:00Z"), vote("b", at="2026-11-22T23:59:00Z"),
             vote("early", at="2026-11-15T23:59:59Z"), vote("late", at="2026-11-23T00:00:00Z")],
            own=[], week="2026-W47",
        )
        self.assertEqual(tally, {"votes": 2, "counted": 2.0, "discounted": 0})

    def test_the_product_s_own_votes_count_nothing(self):
        tally = launches.weigh([vote("Maker"), vote("x")], own=["maker"], week="2026-W47")
        self.assertEqual(tally, {"votes": 2, "counted": 1.0, "discounted": 1})

    def test_a_young_or_unknown_account_counts_half(self):
        tally = launches.weigh(
            [vote("new", born="2026-11-01T00:00:00Z"), vote("month", born="2026-10-18T00:00:00Z"),
             vote("unknown", born=None)],
            own=[], week="2026-W47",
        )
        self.assertEqual(tally, {"votes": 3, "counted": 2.0, "discounted": 2})

    def test_ranks_go_by_counted_votes_then_evidence_then_submission(self):
        rows = {r["slug"]: r for r in CATALOG}
        items = [
            launch("alpha", result={"counted": 5}),
            launch("beta", result={"counted": 5}),
            launch("gamma", result={"counted": 9}),
            launch("quiet", result={"counted": 0}, submitted_on="2026-11-10"),
            launch("delta", status="held", reason="not an example"),
        ]
        ordered = launches.rank(items, rows)
        self.assertEqual([x["product"] for x in ordered], ["gamma", "beta", "alpha", "quiet"])
        self.assertEqual([x["result"]["rank"] for x in ordered], [1, 2, 3, 4])
        self.assertEqual([x["result"].get("badges") for x in ordered], [["week-1"], ["week-2"], ["week-3"], None])
        self.assertNotIn("result", items[-1])

    def test_no_badge_without_a_vote(self):
        ordered = launches.rank([launch("alpha", result={"counted": 0})], {r["slug"]: r for r in CATALOG})
        self.assertNotIn("badges", ordered[0]["result"])


CLOSED = week("2026-W46", "closed", [
    launch("alpha", submitted_on="2026-11-05", discussion=7,
           result={"votes": 4, "counted": 3.5, "discounted": 1, "rank": 1, "badges": ["week-1"]}),
    launch("beta", submitted_on="2026-11-05", role="hunter", submitted_by="h",
           result={"votes": 0, "counted": 0, "discounted": 0, "rank": 2}),
    launch("gamma", status="removed", reason="vote ring", submitted_on="2026-11-06"),
], closed_on="2026-11-16", rules="v1")
OPEN = week("2026-W47", "open", [launch("gamma", discussion=9), launch("quiet", submitted_by="o")])


class CheckTest(unittest.TestCase):
    def test_good_files_pass(self):
        self.assertEqual(check({"2026-W46": CLOSED, "2026-W47": OPEN},
                               {"o": {"login": "o", "name": "O", "bio": "Makes things."}}), [])

    def test_the_repository_s_own_files_pass(self):
        self.assertEqual(check_launches.check_repository(), [])

    def test_the_schemas_use_only_what_the_validator_enforces(self):
        def keywords(node):
            if isinstance(node, dict):
                for key, value in node.items():
                    yield key
                    if key == "properties":
                        for sub in value.values():
                            yield from keywords(sub)
                    elif isinstance(value, dict):
                        yield from keywords(value)
        allowed = lint.SUPPORTED_KEYWORDS | lint.ANNOTATION_KEYWORDS
        for schema in (LAUNCH_SCHEMA, MAKER_SCHEMA):
            self.assertLessEqual(set(keywords(schema)), allowed)

    def problems(self, mutate) -> list[str]:
        files = {"2026-W46": copy.deepcopy(CLOSED), "2026-W47": copy.deepcopy(OPEN)}
        mutate(files)
        return check(files)

    def assertProblem(self, mutate, text: str):
        found = self.problems(mutate)
        self.assertTrue(any(text in p for p in found), found)

    def test_the_week_matches_its_file(self):
        self.assertProblem(lambda f: f["2026-W47"].update(week="2026-W48"), "does not match the file name")

    def test_a_product_must_be_catalogued_and_a_product(self):
        self.assertProblem(lambda f: f["2026-W47"]["launches"].append(launch("nope")), "not in catalog.json")
        self.assertProblem(lambda f: f["2026-W47"]["launches"].append(launch("essay")), "only project")
        self.assertProblem(lambda f: f["2026-W47"]["launches"].append(launch("delta")), "only project")

    def test_a_product_is_on_a_week_once(self):
        self.assertProblem(lambda f: f["2026-W47"]["launches"].append(launch("quiet")), "twice")

    def test_held_and_removed_say_why_and_nothing_else_does(self):
        self.assertProblem(lambda f: f["2026-W47"]["launches"][0].update(status="held"), "says why")
        self.assertProblem(lambda f: f["2026-W47"]["launches"][0].update(reason="why"), "says why")

    def test_a_maker_launch_comes_from_a_maker(self):
        self.assertProblem(lambda f: f["2026-W47"]["launches"][1].update(submitted_by="h"), "not in quiet's makers")
        # quiet names no makers; its author's GitHub login is its maker.
        self.assertEqual(self.problems(lambda f: None), [])

    def test_results_only_on_a_closed_week_and_on_every_scheduled_launch_there(self):
        self.assertProblem(
            lambda f: f["2026-W47"]["launches"][0].update(result={"votes": 1, "counted": 1, "discounted": 0, "rank": 1}),
            "only a scheduled launch in a closed week",
        )
        self.assertProblem(lambda f: f["2026-W46"]["launches"][0].pop("result"), "has no result")
        self.assertProblem(lambda f: f["2026-W46"].pop("closed_on"), "closed_on and rules")
        self.assertProblem(lambda f: f["2026-W47"].update(rules="v1"), "closed_on and rules")
        self.assertProblem(lambda f: f["2026-W46"].update(rules="v9"), "not one scripts/launches.py knows")
        self.assertProblem(lambda f: f["2026-W46"].update(closed_on="2026-11-15"), "not after the week's Sunday")

    def test_ranks_run_from_one(self):
        self.assertProblem(lambda f: f["2026-W46"]["launches"][1]["result"].update(rank=3), "ranks are not 1 to 2")

    def test_counts_cannot_exceed_the_votes(self):
        self.assertProblem(lambda f: f["2026-W46"]["launches"][0]["result"].update(counted=9), "more counted")
        self.assertProblem(lambda f: f["2026-W46"]["launches"][0]["result"].update(discounted=9), "more votes discounted")

    def test_a_product_launches_at_most_once_in_sixty_days(self):
        def again(files):
            files["2026-W47"]["launches"].append(launch("alpha"))
        self.assertProblem(again, "at most once in 60 days")

    def test_the_schema_is_applied(self):
        self.assertProblem(lambda f: f["2026-W47"].update(status="live"), "is not one of")
        self.assertProblem(lambda f: f["2026-W47"]["launches"][0].update(tagline="x"), "minLength")

    def test_a_file_that_does_not_parse_is_reported(self):
        self.assertTrue(any("does not parse" in p for p in check({"2026-W47": "does not parse: x"})))

    def test_a_maker_profile_belongs_to_a_maker(self):
        found = check({}, {"nobody": {"login": "nobody"}})
        self.assertTrue(any("no catalogued row names nobody" in p for p in found), found)
        found = check({}, {"o": {"login": "other"}})
        self.assertTrue(any("does not match the file name" in p for p in found), found)
        found = check({}, {"o": {"login": "o", "url": "http://insecure"}})
        self.assertTrue(any("does not match" in p for p in found), found)


def page(answer_nodes: list[dict], *, total: int | None = None, more: bool = False, cursor: str | None = None) -> dict:
    return {"data": {"repository": {"discussion": {
        "number": 12, "url": "https://github.com/kydlikebtc/awesome-jev/discussions/12",
        "reactions": {"totalCount": total if total is not None else len(answer_nodes),
                      "pageInfo": {"hasNextPage": more, "endCursor": cursor}, "nodes": answer_nodes},
    }}}}


def node(login: str | None, at: str = "2026-11-17T10:00:00Z", born: str = "2020-01-01T00:00:00Z") -> dict:
    return {"createdAt": at, "user": {"login": login, "createdAt": born} if login else None}


class VoteReaderTest(unittest.TestCase):
    def test_votes_come_from_every_page_and_a_deleted_account_is_left_out(self):
        read = launch_votes.votes_from([page([node("a"), node(None)], total=3, more=True, cursor="c1"),
                                        page([node("b")], total=3)])
        self.assertEqual(read["discussion"], 12)
        self.assertEqual(read["total"], 3)
        self.assertEqual([v["login"] for v in read["votes"]], ["a", "b"])
        self.assertEqual(read["votes"][0], {"login": "a", "at": "2026-11-17T10:00:00Z",
                                            "account_created": "2020-01-01T00:00:00Z"})

    def test_a_missing_discussion_is_an_error(self):
        with self.assertRaises(launch_votes.ReadError):
            launch_votes.votes_from([{"data": {"repository": {"discussion": None}},
                                      "errors": [{"message": "Could not resolve to a Discussion"}]}])

    def test_the_reader_follows_the_cursor(self):
        asked = []

        def ask(query, variables):
            asked.append(variables["after"])
            return page([node("a")], more=not asked[1:], cursor="next")

        pages = launch_votes.fetch_pages(12, ask=ask)
        self.assertEqual(asked, [None, "next"])
        self.assertEqual(len(pages), 2)

    def test_no_answer_is_an_error(self):
        with self.assertRaises(launch_votes.ReadError):
            launch_votes.fetch_pages(12, ask=lambda q, v: None)

    def test_the_summary_counts_and_never_names_a_voter(self):
        read = launch_votes.votes_from([page([node("secret-voter"), node("other")])])
        tally = launches.weigh(read["votes"], own=["other"], week="2026-W47")
        text = launch_votes.summary(read, tally, "2026-W47")
        self.assertIn("thumbs-up reactions: 2", text)
        self.assertIn("2 vote(s), counted 1.0", text)
        self.assertNotIn("secret-voter", text)

    def test_the_command_line_reads_a_fixture_and_writes_no_file_unasked(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = pathlib.Path(directory) / "answers.json"
            fixture.write_text(json.dumps([page([node("a")])]))
            out = pathlib.Path(directory) / "votes.json"
            self.assertEqual(launch_votes.main(["--fixture", str(fixture), "--week", "2026-W47", "--out", str(out)]), 0)
            self.assertEqual(json.loads(out.read_text())["tally"]["votes"], 1)
            self.assertEqual(sorted(p.name for p in pathlib.Path(directory).iterdir()), ["answers.json", "votes.json"])

    def test_the_workflow_runs_by_hand_reads_discussions_and_passes_inputs_through_env(self):
        text = (ROOT / ".github" / "workflows" / "launch-votes.yml").read_text()
        self.assertIn("workflow_dispatch:", text)
        self.assertNotIn("schedule:", text)
        self.assertIn("discussions: read", text)
        self.assertNotIn("write", text.split("permissions:", 1)[1].split("jobs:", 1)[0])
        run = text.split("run: |", 1)[1]
        self.assertNotIn("${{", run)


def build(catalog=CATALOG, weeks=(), makers=None) -> dict[str, str]:
    return site_pages.pages(catalog, [], PATTERNS, TAXONOMY, launch_weeks=list(weeks), maker_profiles=makers or {})


class PagesTest(unittest.TestCase):
    def test_a_page_per_product_and_maker(self):
        files = build()
        products = {rel for rel in files if rel.startswith("products/")}
        self.assertEqual(products, {f"products/{s}.html" for s in ("alpha", "beta", "gamma", "quiet")})
        self.assertIn("makers/o.html", files)
        self.assertIn("makers/index.html", files)

    def test_a_product_page_says_what_jev_decides_and_who_read_the_file(self):
        text = build()["products/beta.html"]
        self.assertIn('href="../patterns/tool-selection.html"', text)
        self.assertIn("a person read the call site", text)
        self.assertIn("有人读过调用点", text)
        self.assertIn("2026-10-01", text)
        self.assertIn("Not launched yet.", text)
        self.assertIn('href="../makers/o.html"', text)
        gamma = build()["products/gamma.html"]
        self.assertIn("no file cited", gamma)

    def test_a_maker_login_is_lower_case_in_its_address(self):
        files = build(catalog=[row("alpha", makers=["Alice"])])
        self.assertIn("makers/alice.html", files)
        self.assertIn('href="../makers/alice.html">Alice</a>', files["products/alpha.html"])

    def test_a_maker_profile_adds_its_words(self):
        files = build(makers={"o": {"login": "o", "name": "Oh", "bio": "Builds deciders.", "bio_zh": "做决策器。"}})
        self.assertIn("<h1>Oh</h1>", files["makers/o.html"])
        self.assertIn("Builds deciders.", files["makers/o.html"])

    def test_the_board_lists_new_products_before_any_launch(self):
        files = build()
        self.assertIn("No launch has opened yet.", files["launches.html"])
        self.assertLess(files["launches.html"].index('id="new-beta"'), files["launches.html"].index('id="new-alpha"'))
        self.assertNotIn('id="new-quiet"', files["launches.html"])
        self.assertIn("本周新收录", files["launches.zh.html"])

    def test_a_running_week_hides_its_counts_and_a_closed_one_shows_them(self):
        files = build(weeks=[CLOSED, OPEN])
        board = files["launches.html"]
        running = board.split("This week: 2026-W47", 1)[1].split("Last week", 1)[0]
        self.assertIn("discussions/9", running)
        self.assertNotIn("votes", running)
        closed = board.split("Last week: 2026-W46", 1)[1]
        self.assertLess(closed.index('id="alpha"'), closed.index('id="beta"'))
        self.assertIn("4 votes, 3.5 counted", closed)
        self.assertNotIn('id="gamma"', closed)  # removed

    def test_the_running_order_is_the_same_in_every_build(self):
        many = [launch(s) for s in ("alpha", "beta", "gamma", "quiet")]
        for x in many:
            x["submitted_by"] = "o"
        a = build(weeks=[week("2026-W47", "open", many)])["launches.html"]
        b = build(weeks=[week("2026-W47", "open", list(reversed(many)))])["launches.html"]
        self.assertEqual(a, b)

    def test_a_product_page_lists_its_launches(self):
        text = build(weeks=[CLOSED, OPEN])["products/alpha.html"]
        self.assertIn('<a href="../weeks/2026-W46.html">2026-W46</a>: #1 of the week · 4 votes, 3.5 counted', text)
        self.assertIn("discussions/7", text)
        gamma = build(weeks=[CLOSED, OPEN])["products/gamma.html"]
        self.assertIn("2026-W47: on the board this week", gamma)
        self.assertNotIn("2026-W46", gamma)  # its removed launch is not shown

    def test_the_weekly_results_feed_has_a_closed_week_s_ranking(self):
        import xml.etree.ElementTree as ET

        atom = "{http://www.w3.org/2005/Atom}"
        files = build(weeks=[CLOSED, OPEN])
        self.assertIn('href="launches.xml" type="application/atom+xml"', files["launches.html"])
        self.assertIn('href="launches.zh.xml" type="application/atom+xml"', files["launches.zh.html"])
        feed = ET.fromstring(files["launches.xml"])
        entries = feed.findall(f"{atom}entry")
        self.assertEqual([e.findtext(f"{atom}title") for e in entries], ["Launches of 2026-W46"])  # not the open week
        self.assertEqual(feed.findtext(f"{atom}updated"), "2026-11-16T00:00:00Z")
        self.assertEqual(entries[0].find(f"{atom}link").get("href"),
                         "https://kydlikebtc.github.io/awesome-jev/weeks/2026-W46.html")
        content = entries[0].findtext(f"{atom}content")
        self.assertLess(content.index("#1 Alpha"), content.index("#2 Beta"))
        self.assertIn("4 votes, 3.5 counted; evidence: a model read the call site", content)
        self.assertNotIn("Gamma", content)  # removed
        zh = ET.fromstring(files["launches.zh.xml"])
        self.assertIn("第 1 名 Alpha", zh.find(f"{atom}entry").findtext(f"{atom}content"))
        # Before any week closes the feed is valid and empty.
        empty = ET.fromstring(build()["launches.xml"])
        self.assertEqual(empty.findall(f"{atom}entry"), [])

    def test_no_text_becomes_markup(self):
        hostile = "<script>alert(1)</script>"
        files = build(catalog=[row("alpha", title=hostile, summary=hostile, tagline=hostile, makers=["o"])],
                      weeks=[week("2026-W47", "open", [launch("alpha", tagline=hostile)])])
        for rel, text in files.items():
            self.assertNotIn("<script", text, rel)

    def test_every_link_within_the_site_lands_on_a_file_it_serves(self):
        files = build(weeks=[CLOSED, OPEN])
        served = set(files) | {"index.html", "favicon.svg", "fonts/fonts.css"}
        for rel, text in files.items():
            if not rel.endswith(".html"):
                continue
            for link in re.findall(r'href="([^"]*)"', text):
                if link.startswith(("https://", "http://", "#")):
                    continue
                target = posixpath.join(posixpath.dirname(rel), link.split("#")[0].split("?")[0])
                if target == "" or target.endswith("/"):
                    target = posixpath.join(target, "index.html")
                self.assertIn(posixpath.normpath(target), served, f"{rel} links {link}")


if __name__ == "__main__":
    unittest.main()
