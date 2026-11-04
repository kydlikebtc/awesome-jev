"""The launch board's moving parts (docs/launches.md, since 2026-11-03): the
launch issue's check and the week's collection (scripts/launch_intake.py),
opening and closing a week (scripts/launch_week.py), and the pages a closed
week adds (scripts/site_products.py).

Everything runs on made-up rows, issues and GraphQL answers; nothing reads the
network.
"""

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

import check_launches  # noqa: E402
import launch_intake  # noqa: E402
import launch_votes  # noqa: E402
import launch_week  # noqa: E402
import launches  # noqa: E402
import site_pages  # noqa: E402
from test_launches import CATALOG, LAUNCH_SCHEMA, MAKER_SCHEMA, build, launch, row, week  # noqa: E402

FORM_CONFIRMED = "\n".join(f"- [x] {c}" for c in launch_intake.CONFIRMS)


def body(product: str = "alpha", role: str = launch_intake.MAKER, tagline: str = "Routes tickets with one Choice",
         tagline_zh: str = "_No response_", confirm: str = FORM_CONFIRMED) -> str:
    return (f"### Product\n\n{product}\n\n### Who is launching it?\n\n{role}\n\n"
            f"### One line about it\n\n{tagline}\n\n### The same line in Chinese (optional)\n\n{tagline_zh}\n\n"
            f"### Confirmation\n\n{confirm}\n")


def issue(number: int = 81, login: str = "o", created: str = "2026-11-12T10:00:00Z", **form) -> dict:
    return {"number": number, "user": {"login": login}, "created_at": created, "body": body(**form)}


class FakeLookup(launch_intake.Lookup):
    def __init__(self, repos=None, users=None, members=()):
        self.repos = repos if repos is not None else {}
        self.users = users if users is not None else {}
        self.members = set(members)

    def repo(self, full_name):
        return self.repos.get(full_name, {"owner": {"login": full_name.split("/")[0], "type": "User"}, "fork": False})

    def user(self, login):
        return self.users.get(login, {"created_at": "2020-01-01T00:00:00Z"})

    def public_member(self, org, login):
        return (org, login) in self.members


def assess(i: dict, *, weeks=(), catalog=CATALOG, lookup=None) -> dict:
    return launch_intake.assess(i, catalog, list(weeks), lookup=lookup or FakeLookup())


class TargetWeekTest(unittest.TestCase):
    def test_by_thursday_it_is_next_week_after_that_the_week_after(self):
        cases = {
            "2026-11-09T00:00:00Z": "2026-W47",  # Monday
            "2026-11-12T23:59:59Z": "2026-W47",  # Thursday, last second
            "2026-11-13T00:00:00Z": "2026-W48",  # Friday
            "2026-11-15T23:00:00Z": "2026-W48",  # Sunday
            "2026-12-31T12:00:00Z": "2027-W01",  # across the year
        }
        for created, expected in cases.items():
            with self.subTest(created=created):
                opened = launch_intake.opened_at({"created_at": created})
                self.assertEqual(launch_intake.target_week(opened), expected)


class AssessTest(unittest.TestCase):
    def test_a_maker_on_the_row_is_ready(self):
        result = assess(issue())
        self.assertEqual(result["verdict"], "ready", result)
        self.assertEqual(result["week"], "2026-W47")
        self.assertEqual(result["maker"], "named as a maker on the row")
        self.assertEqual(result["launch"], {
            "product": "alpha", "issue": 81, "submitted_by": "o", "role": "maker",
            "submitted_on": "2026-11-12", "tagline": "Routes tickets with one Choice", "status": "scheduled",
        })

    def test_the_product_can_be_named_by_url_or_site_address(self):
        for answer in ("https://github.com/o/alpha", "https://github.com/O/Alpha/", "<https://github.com/o/alpha>",
                       "https://kydlikebtc.github.io/awesome-jev/#alpha",
                       "https://kydlikebtc.github.io/awesome-jev/products/alpha.html", "ALPHA"):
            with self.subTest(answer=answer):
                self.assertEqual(assess(issue(product=answer))["row"], "alpha")

    def test_what_is_not_catalogued_or_not_a_product_is_refused_with_the_way_on(self):
        result = assess(issue(product="https://github.com/x/unknown"))
        self.assertEqual(result["verdict"], "refused")
        self.assertIn("new-entry", result["problems"][0])
        for slug in ("delta", "essay"):
            with self.subTest(slug=slug):
                result = assess(issue(product=slug))
                self.assertEqual(result["verdict"], "refused")
                self.assertIn("only project, plugin, sdk, integration rows with code launch", result["problems"][0])

    def test_lines_and_boxes_are_checked(self):
        self.assertEqual(assess(issue(tagline="x" * 81))["verdict"], "refused")
        self.assertEqual(assess(issue(tagline="ab"))["verdict"], "refused")
        self.assertEqual(assess(issue(tagline_zh="长" * 61))["verdict"], "refused")
        self.assertEqual(assess(issue(confirm="- [x] " + launch_intake.CONFIRMS[0]))["verdict"], "refused")
        self.assertEqual(assess(issue(role="Somebody"))["verdict"], "refused")
        ok = assess(issue(tagline="  Routes   tickets\n", tagline_zh="一次 Choice 分派工单"))
        self.assertEqual(ok["launch"]["tagline"], "Routes tickets")
        self.assertEqual(ok["launch"]["tagline_zh"], "一次 Choice 分派工单")

    def test_a_product_launches_at_most_once_in_sixty_days(self):
        before = week("2026-W40", "closed", [launch("alpha", result={"votes": 0, "counted": 0, "discounted": 0, "rank": 1})],
                      closed_on="2026-10-05", rules="v1")
        result = assess(issue(), weeks=[before])
        self.assertEqual(result["verdict"], "refused")
        self.assertIn("launched in 2026-W40", result["problems"][0])
        # 2026-W40 began on Monday 2026-09-28; 60 days on, the first Monday is 2026-11-30.
        self.assertIn("in the week of Monday 2026-11-30", result["problems"][0])
        long_ago = dict(before, week="2026-W30")
        self.assertEqual(assess(issue(), weeks=[long_ago])["verdict"], "ready")

    def test_a_maker_is_confirmed_by_owning_the_repository_or_public_membership(self):
        row_by_org = row("orgwork", url="https://github.com/acme/orgwork", author={"name": "Acme", "url": "https://github.com/acme"})
        catalog = CATALOG + [row_by_org]
        lookup = FakeLookup(repos={"acme/orgwork": {"owner": {"login": "acme", "type": "Organization"}, "fork": False}},
                            members={("acme", "dev")})
        result = assess(issue(login="dev", product="orgwork"), catalog=catalog, lookup=lookup)
        self.assertEqual((result["verdict"], result["maker"]), ("ready", "a public member of acme"))
        stranger = assess(issue(login="stranger", product="orgwork"), catalog=catalog, lookup=lookup)
        self.assertEqual(stranger["verdict"], "held")
        # Filed as a hunter's until a person confirms it.
        self.assertEqual(stranger["launch"]["role"], "hunter")
        self.assertIn("says they made it", stranger["launch"]["reason"])

    def test_a_hunter_needs_no_confirming(self):
        result = assess(issue(login="h", role=launch_intake.HUNTER))
        self.assertEqual((result["verdict"], result["launch"]["role"]), ("ready", "hunter"))

    def test_a_fork_a_quiet_repository_and_a_new_account_are_held(self):
        fork = FakeLookup(repos={"o/alpha": {"owner": {"login": "o", "type": "User"}, "fork": True,
                                             "parent": {"full_name": "up/alpha"}}})
        result = assess(issue(), lookup=fork)
        self.assertEqual(result["verdict"], "held")
        self.assertIn("fork of up/alpha", result["launch"]["reason"])
        self.assertIn("no push", assess(issue(product="quiet", role=launch_intake.HUNTER, login="h"))["launch"]["reason"])
        young = FakeLookup(users={"o": {"created_at": "2026-11-01T00:00:00Z"}})
        self.assertIn("younger than 30 days", assess(issue(), lookup=young)["launch"]["reason"])
        unknown = FakeLookup(users={"o": None})
        self.assertIn("could not be read", assess(issue(), lookup=unknown)["launch"]["reason"])

    def test_an_issue_already_on_a_week_says_so(self):
        on = week("2026-W47", "scheduled", [launch("alpha", issue=81)])
        result = assess(issue(), weeks=[on])
        self.assertEqual((result["verdict"], result["week"]), ("collected", "2026-W47"))
        self.assertIn("is on **2026-W47**", launch_intake.comment(result))

    def test_the_comment_quotes_the_launch_where_markdown_cannot_render(self):
        text = launch_intake.comment(assess(issue(tagline="@everyone ```json </details> [x](y)")))
        self.assertTrue(text.startswith(launch_intake.MARKER))
        self.assertIn("Ready for **2026-W47**", text)
        quoted = text.split("````json\n", 1)[1].split("\n````", 1)[0]
        self.assertEqual(json.loads(quoted)["tagline"], "@everyone ```json </details> [x](y)")
        refused = launch_intake.comment(assess(issue(product="nope")))
        self.assertIn("cannot put the launch on the board yet", refused)
        self.assertIn("Edit the issue", refused)

    def test_a_launch_the_check_writes_passes_the_file_check(self):
        for i in (issue(), issue(login="h", role=launch_intake.HUNTER, product="beta"),
                  issue(login="stranger", product="gamma", tagline_zh="中文一句")):
            result = assess(i)
            data = {"2026-W47": week("2026-W47", "scheduled", [result["launch"]])}
            with self.subTest(issue=i["user"]["login"]):
                self.assertEqual(check_launches.check(CATALOG, data, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])


class CollectTest(unittest.TestCase):
    def test_the_week_gets_each_launch_once_in_issue_order(self):
        issues = [
            issue(number=90, login="h", role=launch_intake.HUNTER, product="beta"),
            issue(number=85),
            issue(number=86, product="alpha"),  # the same product again
            issue(number=87, product="nope"),
            issue(number=88, created="2026-11-13T09:00:00Z", product="gamma"),  # for the week after
        ]
        data, changed, notes = launch_intake.collect("2026-W47", issues, json.loads(json.dumps(CATALOG)), [],
                                                     lookup=FakeLookup())
        self.assertEqual([(x["issue"], x["product"]) for x in data["launches"]], [(85, "alpha"), (90, "beta")])
        self.assertEqual(data["status"], "scheduled")
        self.assertEqual(changed, ["alpha"])  # its maker's line becomes the row's tagline
        self.assertTrue(any("#86" in n and "already" in n for n in notes), notes)
        self.assertTrue(any("#87" in n and "not launched" in n for n in notes), notes)
        self.assertFalse(any("#88" in n for n in notes), notes)

    def test_a_confirmed_maker_is_added_to_the_row_so_the_file_check_passes(self):
        catalog = json.loads(json.dumps(CATALOG)) + [
            row("orgwork", url="https://github.com/acme/orgwork", author={"name": "Acme", "url": "https://github.com/acme"},
                tagline="Its own line")]
        lookup = FakeLookup(repos={"acme/orgwork": {"owner": {"login": "acme", "type": "Organization"}, "fork": False}},
                            members={("acme", "dev")})
        data, changed, _ = launch_intake.collect("2026-W47", [issue(login="dev", product="orgwork")], catalog, [],
                                                 lookup=lookup)
        done = next(r for r in catalog if r["slug"] == "orgwork")
        self.assertEqual(changed, ["orgwork"])
        self.assertEqual(done["makers"], ["acme", "dev"])
        self.assertEqual(done["tagline"], "Its own line")  # a row's own line is kept
        self.assertEqual(list(done).index("makers"), list(done).index("author") + 1)
        self.assertEqual(check_launches.check(catalog, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])

    def test_an_open_week_takes_no_more(self):
        with self.assertRaises(ValueError):
            launch_intake.collect("2026-W47", [issue()], CATALOG, [week("2026-W47", "open", [])], lookup=FakeLookup())

    def test_the_command_writes_the_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(CATALOG))
            code = launch_intake.main(["--collect", "2026-W47", "--live", "--root", tmp], lookup=FakeLookup(),
                                      issues_for=lambda repo: [issue()], comments_for=None)
            self.assertEqual(code, 0)
            data = json.loads((root / "launches" / "2026-W47.json").read_text())
            self.assertEqual(data["launches"][0]["product"], "alpha")
            alpha = next(r for r in json.loads((root / "catalog.json").read_text()) if r["slug"] == "alpha")
            self.assertEqual(alpha["tagline"], "Routes tickets with one Choice")
            self.assertEqual(launch_intake.main(["--collect", "47", "--root", tmp], lookup=FakeLookup(),
                                                issues_for=lambda repo: []), 2)

    def test_by_default_it_collects_with_the_facts_the_check_comment_recorded(self):
        # The workflow's check, with a token, reads GitHub and records what it read.
        org_row = row("orgwork", url="https://github.com/acme/orgwork",
                      author={"name": "Acme", "url": "https://github.com/acme"})
        catalog = CATALOG + [org_row]
        live = FakeLookup(repos={"acme/orgwork": {"owner": {"login": "acme", "type": "Organization"}, "fork": False,
                                                  "description": "not kept"}},
                          users={"dev": {"created_at": "2019-05-01T00:00:00Z", "name": "not kept"}},
                          members={("acme", "dev")})
        recorder = launch_intake.Recorder(live)
        opened = issue(number=82, login="dev", product="orgwork", tagline="--> <b>@x</b>")
        result = launch_intake.assess(opened, catalog, [], lookup=recorder)
        text = launch_intake.comment(result, recorder.facts)
        self.assertEqual(result["verdict"], "ready")
        hidden = text.splitlines()[1]
        self.assertTrue(hidden.startswith("<!-- launch-intake-facts {") and hidden.endswith("} -->"), hidden)
        self.assertEqual(hidden.count("-->"), 1)
        self.assertNotIn("not kept", hidden)
        bot = {"user": {"login": "github-actions[bot]"}, "body": text}
        forged = {"user": {"login": "dev"}, "body": text.replace('"fork": false', '"fork": true')}
        self.assertEqual(launch_intake.recorded_facts([bot, forged]), recorder.facts)
        self.assertIsNone(launch_intake.recorded_facts([forged]))

        # The Friday task, with no token, collects from that comment: the same verdict.
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(catalog))
            comments = {82: [bot], 83: []}
            stray = issue(number=83, login="h", role=launch_intake.HUNTER, product="beta")
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = launch_intake.main(["--collect", "2026-W47", "--root", tmp], lookup=FakeLookup(users={"dev": None}),
                                          issues_for=lambda repo: [opened, stray],
                                          comments_for=lambda repo, number: comments[number])
            self.assertEqual(code, 0)
            data = json.loads((root / "launches" / "2026-W47.json").read_text())
            self.assertEqual([(x["product"], x["role"], x["status"]) for x in data["launches"]],
                             [("orgwork", "maker", "scheduled")])
            self.assertIn("#83: no check comment", out.getvalue())
            done = next(r for r in json.loads((root / "catalog.json").read_text()) if r["slug"] == "orgwork")
            self.assertEqual(done["makers"], ["acme", "dev"])

    def test_a_fact_the_comment_did_not_record_holds_the_launch(self):
        result = launch_intake.assess(issue(), CATALOG, [], lookup=launch_intake.Recorded({}))
        self.assertEqual(result["verdict"], "held")
        self.assertIn("could not be read", result["launch"]["reason"])


class UnreadTest(unittest.TestCase):
    """L28: the products about to launch whose call site nobody has read, so
    the daily task reads them before their week opens."""

    CATALOG = CATALOG + [row("fileonly", evidence={"path": "x.py", "matched": ["y"]})]
    WEEKS = [
        week("2026-W46", "open", [launch("gamma", issue=70)]),  # open: its evidence is already on file
        week("2026-W47", "scheduled", [
            launch("alpha", issue=100),  # a model read it
            launch("gamma", issue=101, status="held", reason="maker not confirmed"),
            launch("fileonly", issue=102, status="removed", reason="withdrawn"),  # not launching here
        ]),
    ]
    ISSUES = [
        issue(number=105, product="fileonly"),
        issue(number=101, product="gamma"),  # filed already
        issue(number=103, product="beta"),  # a person read it
        issue(number=104, product="nope"),  # not catalogued
        issue(number=106, product="https://github.com/o/fileonly"),  # the same product again
    ]

    def test_each_product_once_soonest_first_and_only_what_nobody_read(self):
        found = launch_intake.unread(self.CATALOG, self.WEEKS, self.ISSUES)
        self.assertEqual(found, [
            ("gamma", "none", "", "https://github.com/o/gamma", "launches/2026-W47.json"),
            ("fileonly", "file", "x.py", "https://github.com/o/fileonly", "issue #105"),
        ])

    def test_the_command_lists_them_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(self.CATALOG))
            (root / "launches").mkdir()
            for w in self.WEEKS:
                (root / "launches" / f"{w['week']}.json").write_text(json.dumps(w))
            before = sorted(p.read_text() for p in root.rglob("*.json"))
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = launch_intake.main(["--unread", "--root", tmp], lookup=FakeLookup(),
                                          issues_for=lambda repo: self.ISSUES)
            self.assertEqual(code, 0)
            self.assertEqual(out.getvalue().splitlines(), [
                "gamma\tnone\tno file cited\thttps://github.com/o/gamma\tlaunches/2026-W47.json",
                "fileonly\tfile\tx.py\thttps://github.com/o/fileonly\tissue #105",
            ])
            self.assertIn("2 product(s)", err.getvalue())
            self.assertEqual(sorted(p.read_text() for p in root.rglob("*.json")), before)


# --------------------------------------------------------------------------
# Opening and closing a week
# --------------------------------------------------------------------------


def repo_answer(enabled=True, categories=("Launches",)):
    return {"data": {"repository": {"id": "R1", "hasDiscussionsEnabled": enabled, "discussionCategories": {
        "nodes": [{"id": f"C-{name}", "name": name} for name in categories]}}}}


class FakeGitHub:
    """GraphQL answers for one repository: its categories, the posts in
    Launches, and each post's reactions."""

    def __init__(self, *, posts=None, reactions=None, enabled=True, categories=("Launches",), fail_on=None,
                 authors=None, issues=None, refuse_comments=False):
        self.posts = dict(posts or {})  # number -> body
        self.authors = dict(authors or {})  # number -> login, github-actions when not given
        self.reactions = reactions or {}  # number -> [node]
        self.enabled, self.categories = enabled, categories
        self.created: list[dict] = []
        self.fail_on = fail_on
        # Launch issues: number -> {"state", "comments": [(login, body)]}; any other number is open, uncommented.
        self.issues = {n: dict(i) for n, i in (issues or {}).items()}
        self.refuse_comments = refuse_comments

    def issue(self, number):
        return self.issues.setdefault(number, {"state": "OPEN", "comments": []})

    def ask(self, query, variables):
        if "issue(number" in query:
            i = self.issue(variables["number"])
            nodes = [{"body": b, "author": {"login": who}} for who, b in i["comments"]]
            return {"data": {"repository": {"issue": {"id": f"I{variables['number']}", "state": i["state"],
                                                      "comments": {"nodes": nodes}}}}}
        if "discussionCategories" in query:
            return repo_answer(self.enabled, self.categories)
        if "discussions(" in query:
            nodes = [{"number": n, "body": b, "author": {"login": self.authors.get(n, "github-actions")}}
                     for n, b in sorted(self.posts.items())]
            return {"data": {"repository": {"discussions": {"pageInfo": {"hasNextPage": False}, "nodes": nodes}}}}
        if "reactions(" in query:
            nodes = self.reactions.get(variables["number"], [])
            return {"data": {"repository": {"discussion": {
                "number": variables["number"], "url": "u", "reactions": {
                    "totalCount": len(nodes), "pageInfo": {"hasNextPage": False}, "nodes": nodes}}}}}
        raise AssertionError(query)

    def mutate(self, query, variables):
        if "addComment" in query:
            if self.refuse_comments:
                return {"errors": [{"message": "Resource not accessible by integration"}]}
            self.issue(int(variables["subject"][1:]))["comments"].append(("github-actions", variables["body"]))
            return {"data": {"addComment": {"commentEdge": {"node": {"id": "C1"}}}}}
        if "closeIssue" in query:
            self.issue(int(variables["issue"][1:]))["state"] = "CLOSED"
            return {"data": {"closeIssue": {"issue": {"number": int(variables["issue"][1:]), "state": "CLOSED"}}}}
        if self.fail_on and self.fail_on in variables["body"]:
            return {"errors": [{"message": "boom"}]}
        number = 100 + len(self.posts)
        self.posts[number] = variables["body"]
        self.created.append(variables)
        return {"data": {"createDiscussion": {"discussion": {"number": number, "url": "u"}}}}


def reaction(login, at="2026-11-17T10:00:00Z", born="2020-01-01T00:00:00Z"):
    return {"createdAt": at, "user": {"login": login, "createdAt": born}}


ROWS = {r["slug"]: r for r in CATALOG}


class OpenTest(unittest.TestCase):
    def scheduled(self):
        return week("2026-W47", "scheduled", [
            launch("alpha", issue=81), launch("beta", issue=82, role="hunter", submitted_by="h"),
            launch("gamma", issue=83, status="held", reason="a fork"),
        ])

    def test_each_launch_on_the_board_gets_a_post_and_the_week_opens(self):
        gh, data = FakeGitHub(), self.scheduled()
        notes = launch_week.open_week(data, ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
        self.assertEqual(data["status"], "open")
        self.assertEqual(len(gh.created), 2)
        self.assertEqual({x["product"] for x in data["launches"] if "discussion" in x}, {"alpha", "beta"})
        self.assertNotIn("discussion", data["launches"][2])
        self.assertEqual(len(notes), 2)
        first = gh.created[0]
        self.assertEqual(first["category"], "C-Launches")
        self.assertIn("A thumbs-up on this post is a vote", first["body"])
        self.assertIn("<!-- launch 2026-W47 ", first["body"])
        self.assertEqual(check_launches.check(CATALOG, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])

    def test_opening_writes_each_launch_s_evidence_as_it_stood(self):
        gh, data = FakeGitHub(), self.scheduled()
        launch_week.open_week(data, ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
        alpha, beta, gamma = data["launches"]
        # alpha's call site was read by a model, beta's by a person; a held launch opens nothing.
        self.assertEqual((alpha["tier_at_open"], beta["tier_at_open"]), ("model", "person"))
        self.assertNotIn("tier_at_open", gamma)
        self.assertEqual(list(alpha)[-2:], ["discussion", "tier_at_open"])
        self.assertEqual(check_launches.check(CATALOG, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])

    def test_a_post_made_before_is_found_not_made_again(self):
        gh = FakeGitHub(posts={5: "<!-- launch 2026-W47 alpha -->\nold"})
        data = self.scheduled()
        launch_week.open_week(data, ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
        self.assertEqual(data["launches"][0]["discussion"], 5)
        self.assertEqual(len(gh.created), 1)

    def test_a_post_only_counts_as_found_when_the_workflow_or_the_owner_started_it(self):
        gh = FakeGitHub(posts={5: "<!-- launch 2026-W47 alpha -->", 6: "<!-- launch 2026-W47 beta -->",
                               7: "<!-- launch 2026-W47 alpha -->"},
                        authors={5: "someone", 6: "O"})
        data = self.scheduled()
        launch_week.open_week(data, ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
        self.assertEqual({x["product"]: x.get("discussion") for x in data["launches"]},
                         {"alpha": 7, "beta": 6, "gamma": None})
        self.assertEqual(gh.created, [])

    def test_a_failed_post_keeps_what_was_made_and_the_week_scheduled(self):
        gh, data = FakeGitHub(fail_on="2026-W47 beta"), self.scheduled()
        with self.assertRaises(launch_week.WeekError):
            launch_week.open_week(data, ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
        self.assertEqual(data["status"], "scheduled")
        made = [x for x in data["launches"] if "discussion" in x]
        self.assertLessEqual(len(made), 1)

    def test_without_discussions_or_the_category_it_says_what_the_owner_does(self):
        for gh, words in ((FakeGitHub(enabled=False), "Discussions are off"),
                          (FakeGitHub(categories=("General",)), "no Discussion category named 'Launches'")):
            with self.subTest(words=words), self.assertRaises(launch_week.WeekError) as caught:
                launch_week.open_week(self.scheduled(), ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
            self.assertIn(words, str(caught.exception))

    def test_a_week_with_nothing_on_the_board_opens_without_asking_github(self):
        data = week("2026-W47", "scheduled", [launch("gamma", status="held", reason="a fork")])
        launch_week.open_week(data, ROWS, repository="o/r", ask=None, mutate=None)
        self.assertEqual(data["status"], "open")

    def test_user_text_in_a_post_is_inert(self):
        title, text = launch_week.post("2026-W47", launch("alpha", tagline="@all [x](javascript:y) <b>"), ROWS["alpha"])
        self.assertIn("@​all \\[x\\]\\(javascript:y\\) \\<b\\>", text)
        self.assertNotIn("@all", text)
        self.assertTrue(title.startswith("Alpha · "))


class ProbeTest(unittest.TestCase):
    @staticmethod
    def github(create=True, delete=True):
        calls = []

        def mutate(query, variables):
            calls.append((query, variables))
            if "createDiscussion" in query:
                return ({"data": {"createDiscussion": {"discussion": {"id": "D1", "number": 9, "url": "https://x/9"}}}}
                        if create else {"errors": [{"message": "FORBIDDEN"}]})
            return {"data": {"deleteDiscussion": {"discussion": {"number": 9}}}} if delete else None

        return calls, mutate

    def test_the_probe_starts_one_discussion_in_launches_and_deletes_it(self):
        calls, mutate = self.github()
        notes = launch_week.probe("o/r", ask=FakeGitHub().ask, mutate=mutate)
        self.assertEqual([("createDiscussion" in q, v.get("category"), v.get("id")) for q, v in calls],
                         [(True, "C-Launches", None), (False, None, "D1")])
        self.assertIn("can post vote posts", notes[0])

    def test_a_refused_post_or_a_failed_deletion_says_what_a_person_does(self):
        for create, delete, words in ((False, True, "FORBIDDEN"), (True, False, "deletes it by hand: https://x/9")):
            calls, mutate = self.github(create, delete)
            with self.subTest(words=words), self.assertRaises(launch_week.WeekError) as caught:
                launch_week.probe("o/r", ask=FakeGitHub().ask, mutate=mutate)
            self.assertIn(words, str(caught.exception))
            self.assertEqual(len(calls), 1 if not create else 2)

    def test_the_probe_workflow_is_by_hand_and_writes_nothing(self):
        text = (ROOT / ".github" / "workflows" / "launch-probe.yml").read_text()
        self.assertIn("on:\n  workflow_dispatch:\n\npermissions:\n  contents: read\n  discussions: write\n", text)
        self.assertIn("run: python3 scripts/launch_week.py --probe", text)
        self.assertNotIn("git ", text.split("jobs:", 1)[1])
        self.assertNotIn("github.event.", text.split("jobs:", 1)[1])


class CloseTest(unittest.TestCase):
    def open_week(self, *items):
        return week("2026-W47", "open", list(items))

    def test_votes_are_weighed_ranked_and_badged(self):
        reactions = {
            1: [reaction("a"), reaction("b"), reaction("o"), reaction("new", born="2026-11-10T00:00:00Z")],
            2: [reaction("a"), reaction("late", at="2026-11-23T00:00:01Z")],
        }
        data = self.open_week(launch("alpha", discussion=1), launch("beta", discussion=2, role="hunter", submitted_by="h"))
        read = lambda n: [{"login": r["user"]["login"], "at": r["createdAt"], "account_created": r["user"]["createdAt"]}
                          for r in reactions[n]]
        launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 23), read=read)
        alpha, beta = data["launches"]
        self.assertEqual(alpha["result"], {"votes": 4, "counted": 2.5, "discounted": 2, "rank": 1, "badges": ["week-1"]})
        self.assertEqual(beta["result"], {"votes": 1, "counted": 1.0, "discounted": 0, "rank": 2, "badges": ["week-2"]})
        self.assertEqual((data["status"], data["closed_on"], data["rules"]), ("closed", "2026-11-23", "v1"))
        self.assertEqual(list(data), ["week", "status", "closed_on", "rules", "voters", "returning_voters", "launches"])
        # a, b and new (half a vote is still a vote) on alpha, a again on beta; o is alpha's maker, late is late.
        self.assertEqual((data["voters"], data["returning_voters"]), (3, 0))
        self.assertEqual(check_launches.check(CATALOG, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])
        self.assertNotIn("login", json.dumps(data))

    def test_the_close_counts_the_week_s_accounts_and_who_came_back(self):
        def vote(login, at):
            return {"login": login, "at": at, "account_created": "2020-01-01T00:00:00Z"}

        this_week, last_week = "2026-11-17T10:00:00Z", "2026-11-10T10:00:00Z"
        votes = {
            1: [vote("a", this_week), vote("b", this_week), vote("c", this_week)],
            2: [vote("a", this_week), vote("d", this_week)],
            3: [vote("b", last_week), vote("d", last_week), vote("x", last_week)],
            4: [vote("c", last_week), vote("late", this_week)],  # late voted on last week's post this week
        }
        before = week("2026-W46", "closed", [
            launch("gamma", issue=70, discussion=3, role="hunter", submitted_by="h",
                   result={"votes": 3, "counted": 3, "discounted": 0, "rank": 1}),
            launch("quiet", issue=71, discussion=4, result={"votes": 1, "counted": 1, "discounted": 0, "rank": 2}),
        ], closed_on="2026-11-16", rules="v1", voters=4, returning_voters=0)
        data = self.open_week(launch("alpha", discussion=1), launch("beta", discussion=2, role="hunter", submitted_by="h"))
        launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 23), read=lambda n: votes[n], before=before)
        # This week a, b, c and d voted; b, c and d had voted the week before.
        self.assertEqual((data["voters"], data["returning_voters"]), (4, 3))
        self.assertNotIn('"a"', json.dumps(data))
        self.assertEqual(check_launches.check(CATALOG, {"2026-W46": before, "2026-W47": data}, {}, LAUNCH_SCHEMA,
                                              MAKER_SCHEMA), [])

        # A post of the week before that cannot be read now is left out, and said.
        def read(n):
            if n == 4:
                raise launch_votes.ReadError("discussion #4 not found")
            return votes[n]

        notes = launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 24), read=read, before=before)
        self.assertEqual((data["voters"], data["returning_voters"]), (4, 2))
        self.assertTrue(any("post #4 not read" in n for n in notes), notes)

    def test_a_ring_of_new_accounts_is_held_for_a_person(self):
        ring = [{"login": f"n{i}", "at": "2026-11-17T10:00:00Z", "account_created": "2026-11-15T00:00:00Z"} for i in range(8)]
        ring += [{"login": f"old{i}", "at": "2026-11-17T10:00:00Z", "account_created": "2020-01-01"} for i in range(4)]
        data = self.open_week(launch("alpha", discussion=1), launch("beta", discussion=2, role="hunter", submitted_by="h"))
        launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 23), read=lambda n: ring if n == 1 else [])
        alpha, beta = data["launches"]
        self.assertEqual(alpha["status"], "held")
        self.assertIn("8 of 12 votes", alpha["reason"])
        self.assertNotIn("result", alpha)
        self.assertEqual(beta["result"]["rank"], 1)
        self.assertNotIn("badges", beta["result"])  # no vote counted, no badge
        self.assertEqual(check_launches.check(CATALOG, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])

    def test_a_closed_week_is_counted_again_after_a_person_decides(self):
        ring = [{"login": f"n{i}", "at": "2026-11-17T10:00:00Z", "account_created": "2026-11-15"} for i in range(10)]
        data = self.open_week(launch("alpha", discussion=1), launch("beta", discussion=2, role="hunter", submitted_by="h"))
        launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 23), read=lambda n: ring if n == 1 else [])
        alpha = data["launches"][0]
        self.assertEqual(alpha["status"], "held")
        # A person read the votes and let it stand: the recount ranks it.
        alpha.update(status="scheduled", cleared_by="kyd")
        del alpha["reason"]
        launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 24), read=lambda n: ring if n == 1 else [])
        self.assertEqual((alpha["status"], alpha["result"]["rank"]), ("scheduled", 1))
        self.assertEqual(check_launches.check(CATALOG, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])
        # Or removed it: the recount drops its result and ranks the rest.
        alpha.update(status="removed", reason="a ring of new accounts")
        launch_week.close_week(data, ROWS, on=dt.date(2026, 11, 24), read=lambda n: ring if n == 1 else [])
        self.assertNotIn("result", alpha)
        self.assertEqual(data["launches"][1]["result"]["rank"], 1)
        self.assertEqual(check_launches.check(CATALOG, {"2026-W47": data}, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])

    def test_a_week_closes_only_after_its_sunday(self):
        with self.assertRaises(launch_week.WeekError):
            launch_week.close_week(self.open_week(), ROWS, on=dt.date(2026, 11, 22), read=lambda n: [])


class TellTest(unittest.TestCase):
    """L27: each launch's issue hears that its week opened, with the vote
    post, and how it ended."""

    def opened(self):
        gh = FakeGitHub()
        data = week("2026-W47", "scheduled", [
            launch("alpha", issue=81), launch("beta", issue=82, role="hunter", submitted_by="h"),
            launch("gamma", issue=83, status="held", reason="a fork"),
        ])
        launch_week.open_week(data, ROWS, repository="o/r", ask=gh.ask, mutate=gh.mutate)
        return gh, data

    def test_an_opened_week_tells_each_launch_s_issue_and_closes_it_once(self):
        gh, data = self.opened()
        notes = launch_week.tell_issues(data, "opened", repository="o/r", ask=gh.ask, mutate=gh.mutate)
        alpha = next(x for x in data["launches"] if x["product"] == "alpha")
        (who, text), = gh.issues[81]["comments"]
        self.assertEqual(who, "github-actions")
        self.assertIn(f"discussions/{alpha['discussion']}", text)
        self.assertIn("<!-- launch-board 2026-W47 alpha opened -->", text)
        self.assertEqual((gh.issues[81]["state"], gh.issues[82]["state"]), ("CLOSED", "CLOSED"))
        self.assertNotIn(83, gh.issues)  # held: a person decides it, and its issue stays as it is
        self.assertEqual(len(notes), 2)
        again = launch_week.tell_issues(data, "opened", repository="o/r", ask=gh.ask, mutate=gh.mutate)
        self.assertTrue(all(n.endswith("told before") for n in again), again)
        self.assertEqual(len(gh.issues[81]["comments"]), 1)

    def test_a_closed_week_tells_each_result_and_the_badge_line(self):
        gh = FakeGitHub()
        data = week("2026-W47", "closed", [
            launch("alpha", issue=81, discussion=1,
                   result={"votes": 4, "counted": 3.5, "discounted": 1, "rank": 1, "badges": ["week-1"]}),
            launch("beta", issue=82, discussion=2, role="hunter", submitted_by="h",
                   result={"votes": 0, "counted": 0, "discounted": 0, "rank": 2}),
            launch("gamma", issue=83, discussion=3, status="held", reason="8 of 12 votes came from new accounts"),
        ], closed_on="2026-11-23", rules="v1", voters=4, returning_voters=0)
        launch_week.tell_issues(data, "closed", repository="o/r", ask=gh.ask, mutate=gh.mutate)
        alpha, beta, gamma = (gh.issues[n]["comments"][0][1] for n in (81, 82, 83))
        self.assertIn("placed #1 of 2, with 4 votes, 3.5 counted", alpha)
        self.assertIn("[![awesome-jev launches: #1 of 2026-W47](https://kydlikebtc.github.io/awesome-jev/badges/"
                      "alpha.svg)](https://kydlikebtc.github.io/awesome-jev/products/alpha.html)", alpha)
        self.assertIn("placed #2 of 2", beta)
        self.assertNotIn("badge", beta)
        self.assertIn("held for a person before it ranks: 8 of 12 votes", gamma)

    def test_a_comment_github_refuses_never_stops_the_week(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(CATALOG))
            (root / "launches").mkdir()
            (root / "launches" / "2026-W48.json").write_text(json.dumps(
                week("2026-W48", "scheduled", [launch("beta", issue=91, role="hunter", submitted_by="h")])))
            gh = FakeGitHub(refuse_comments=True)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                for action in ("--monday", "--tell"):
                    code = launch_week.main([action, "--on", "2026-11-23", "--repo", "o/r", "--root", tmp],
                                            ask=gh.ask, mutate=gh.mutate)
                    self.assertEqual(code, 0)
            self.assertIn("could not comment (Resource not accessible by integration)", out.getvalue())
            opened = json.loads((root / "launches" / "2026-W48.json").read_text())
            self.assertEqual(opened["status"], "open")
            self.assertEqual(gh.issues[91]["state"], "OPEN")


class MondayTest(unittest.TestCase):
    def test_monday_closes_last_week_and_opens_this_one_and_nothing_else(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(CATALOG))
            (root / "launches").mkdir()
            gh = FakeGitHub(reactions={9: [reaction("a")]})
            # Nothing on file: nothing to do, and nothing asked.
            done = launch_week.monday(root, dt.date(2026, 11, 23), repository="o/r", ask=None, mutate=None)
            self.assertIn("nothing to do", done[0])
            (root / "launches" / "2026-W47.json").write_text(json.dumps(
                week("2026-W47", "open", [launch("alpha", discussion=9)])))
            (root / "launches" / "2026-W48.json").write_text(json.dumps(
                week("2026-W48", "scheduled", [launch("beta", issue=91, role="hunter", submitted_by="h")])))
            code = launch_week.main(["--monday", "--on", "2026-11-23", "--repo", "o/r", "--root", tmp],
                                    ask=gh.ask, mutate=gh.mutate)
            self.assertEqual(code, 0)
            closed = json.loads((root / "launches" / "2026-W47.json").read_text())
            opened = json.loads((root / "launches" / "2026-W48.json").read_text())
            self.assertEqual(closed["status"], "closed")
            self.assertEqual(closed["launches"][0]["result"]["votes"], 1)
            self.assertEqual((opened["status"], opened["launches"][0]["discussion"]), ("open", 100))
            files = {p.stem: json.loads(p.read_text()) for p in (root / "launches").glob("*.json")}
            self.assertEqual(check_launches.check(CATALOG, files, {}, LAUNCH_SCHEMA, MAKER_SCHEMA), [])
            self.assertEqual(gh.issues, {})  # nobody is told before the files are on main
            launch_week.main(["--tell", "--on", "2026-11-23", "--repo", "o/r", "--root", tmp],
                             ask=gh.ask, mutate=gh.mutate)
            # Both launches' issues were told, and are closed: alpha's (100) its result, beta's (91) its post.
            self.assertIn("placed #1 of 1", gh.issues[100]["comments"][0][1])
            self.assertIn("discussions/100", gh.issues[91]["comments"][0][1])
            self.assertEqual((gh.issues[100]["state"], gh.issues[91]["state"]), ("CLOSED", "CLOSED"))

    def test_the_workflow_is_weekly_writes_only_counts_and_pushes_only_a_checked_commit(self):
        text = (ROOT / ".github" / "workflows" / "launch-week.yml").read_text()
        self.assertIn('cron: "5 0 * * 1"', text)
        self.assertIn("  discussions: write\n", text)
        self.assertIn("  issues: write\n", text)  # it tells each launch's issue, and closes it
        self.assertIn("run: python3 scripts/launch_week.py --monday", text)
        tell = text.split("- name: Tell each launch's issue what happened\n", 1)[1]
        self.assertTrue(tell.startswith("        if: always() && (steps.land.outputs.landed == 'main' "
                                        "|| steps.commit.outputs.changed == 'false')\n"), tell[:120])
        self.assertIn("run: python3 scripts/launch_week.py --tell", tell)
        self.assertIn("git add -A launches\n", text)
        self.assertIn("if: always() && steps.checks.outcome == 'success'", text)
        self.assertNotIn("--force-with-lease origin HEAD:main", text)
        self.assertNotIn("github.event.", text.split("jobs:", 1)[1])

    def test_the_friday_workflow_files_next_week_and_pushes_only_a_checked_commit(self):
        text = (ROOT / ".github" / "workflows" / "launch-collect.yml").read_text()
        self.assertIn('cron: "20 0 * * 5"', text)  # Friday, after Thursday 23:59 UTC
        self.assertIn("permissions:\n  contents: write\n  issues: read\n  actions: write\n", text)
        self.assertIn("python3 scripts/launch_intake.py --collect next", text)
        self.assertIn("set -o pipefail", text)
        jobs = text.split("jobs:", 1)[1]
        self.assertIn("python3 scripts/regenerate.py", jobs)
        self.assertIn("git add -A launches catalog.json ", jobs)
        self.assertIn("if: steps.checks.outcome == 'success'", jobs)
        self.assertLess(jobs.index("scripts/check.py --ci --quick"), jobs.index("git push -q origin HEAD:main"))
        self.assertNotIn("--force origin HEAD:main", jobs)
        self.assertNotIn("github.event.", jobs)
        self.assertIn("group: launch-week\n", text)  # never at the same time as the Monday run

    def test_next_is_the_week_of_the_coming_monday(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "catalog.json").write_text(json.dumps(CATALOG))
            (root / "launches").mkdir()
            issues = [issue(81, created="2026-11-12T10:00:00Z")]  # a Thursday: for 2026-W47
            with contextlib.redirect_stdout(io.StringIO()) as out:
                code = launch_intake.main(["--collect", "next", "--on", "2026-11-13", "--root", tmp],
                                          lookup=FakeLookup(), issues_for=lambda repo: issues,
                                          comments_for=lambda repo, n: [])
            self.assertEqual(code, 0)
            self.assertIn("2026-W47: 0 launch(es) on file", out.getvalue())  # no check comment: reported
            self.assertIn("#81: no check comment", out.getvalue())

    def test_the_intake_workflow_only_reads_and_comments(self):
        text = (ROOT / ".github" / "workflows" / "launch-intake.yml").read_text()
        self.assertIn("permissions:\n  contents: read\n  issues: write\n", text)
        self.assertNotIn("git push", text)
        self.assertIn("contains(github.event.issue.labels.*.name, 'launch')", text)
        form = (ROOT / ".github" / "ISSUE_TEMPLATE" / "launch.yml").read_text()
        self.assertIn('labels: ["launch"]', form)
        for heading in launch_intake.FIELDS:
            self.assertIn(f"label: {heading}\n", form)
        for option in (launch_intake.MAKER, launch_intake.HUNTER):
            self.assertIn(f'- "{option}"', form)
        for confirm in launch_intake.CONFIRMS:
            self.assertIn(f"- label: {confirm}\n", form)


# --------------------------------------------------------------------------
# The pages a closed week adds
# --------------------------------------------------------------------------


CLOSED = week("2026-W46", "closed", [
    launch("alpha", discussion=7, result={"votes": 4, "counted": 3.5, "discounted": 1, "rank": 1, "badges": ["week-1"]}),
    launch("beta", role="hunter", submitted_by="h", result={"votes": 0, "counted": 0, "discounted": 0, "rank": 2}),
    launch("gamma", status="removed", reason="a <ring> of new accounts"),
], closed_on="2026-11-16", rules="v1")
NEXT = week("2026-W47", "scheduled", [launch("gamma", issue=120), launch("quiet", status="held", reason="quiet")])


class WeekPagesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = build(weeks=[CLOSED, NEXT])

    def test_a_closed_week_has_a_page_in_each_language_and_a_badge(self):
        for rel in ("weeks/2026-W46.html", "weeks/2026-W46.zh.html", "badges/alpha.svg"):
            self.assertIn(rel, self.files)
        self.assertNotIn("badges/beta.svg", self.files)
        page = self.files["weeks/2026-W46.html"]
        self.assertLess(page.index("products/alpha.html"), page.index("products/beta.html"))
        self.assertIn('href="../products/alpha.html"', page)
        self.assertIn('href="../badges/alpha.svg"', page)
        self.assertIn("counted under rules v1", page)
        self.assertIn("gamma: a &lt;ring&gt; of new accounts", page)
        svg = self.files["badges/alpha.svg"]
        self.assertIn("#1 of 2026-W46", svg)
        self.assertNotIn("<script", svg)
        self.assertNotIn("href", svg)

    def test_the_board_lists_next_week_and_the_past_weeks(self):
        board = self.files["launches.html"]
        self.assertIn("Next week: 2026-W47", board)
        self.assertIn("2026-11-16", board)
        self.assertIn('href="products/gamma.html"', board)
        self.assertNotIn('id="quiet"', board)  # held: not shown
        self.assertIn('<a href="weeks/2026-W46.html">2026-W46: 2 launches, closed 2026-11-16</a>', board)
        self.assertIn('href="weeks/2026-W46.zh.html"', self.files["launches.zh.html"])
        self.assertIn("下周上榜", self.files["products/gamma.html"])

    def test_a_closed_week_says_what_it_measured(self):
        board = self.files["launches.html"]
        last = board.split("Last week: 2026-W46", 1)[1].split("</ol>", 1)[0]
        # Closed before its accounts were counted: that count is left out, not shown as nought.
        self.assertNotIn("accounts voted", last)
        self.assertIn("0 of 2 launches reached 5 counted votes. 1 of 4 votes counted for less than one.", last)
        counted = dict(CLOSED, voters=3, returning_voters=1, launches=[
            dict(x, tier_at_open="model") if x["product"] == "alpha" else dict(x, tier_at_open="file")
            for x in CLOSED["launches"]])
        files = build(weeks=[counted, NEXT])
        line = ("3 accounts voted, 1 of them the week before too. 0 of 2 launches reached 5 counted votes. "
                "When the week opened, a person or a model had read the call site of 1 of 2. "
                "1 of 4 votes counted for less than one.")
        self.assertIn(line, files["launches.html"])
        self.assertIn(line, files["weeks/2026-W46.html"])
        self.assertIn("3 个账号投了票，其中 1 个上周也投过。2 个 Launch 中有 0 个计入的票数达到 5。"
                      "开榜时，2 个中有 1 个的调用点已由人或模型读过。4 票中有 1 票按不足一票计。",
                      files["weeks/2026-W46.zh.html"])

    def test_the_board_says_how_far_the_daily_board_is(self):
        self.assertIn("after 4 weeks in a row with at least 20 launches each. Weeks in a row so far: 0.",
                      self.files["launches.html"])
        self.assertIn("目前已连续 0 周", self.files["launches.zh.html"])

        def closed(name, n):
            return week(name, "closed", [launch(f"p{i}", result={"votes": 0, "counted": 0, "discounted": 0, "rank": i + 1})
                                         for i in range(n)] + [launch("x", status="held", reason="held")])

        full = [closed("2026-W41", 25), closed("2026-W43", 20), closed("2026-W44", 30), closed("2026-W45", 20),
                closed("2026-W46", 21), NEXT]
        self.assertEqual(launches.daily_streak(full), 4)
        self.assertEqual(launches.daily_streak(full[:-2] + [closed("2026-W46", 19)]), 0)
        self.assertEqual(launches.daily_streak(full[:3]), 2)  # 2026-W42 has no file: the run stops there
        self.assertEqual(launches.daily_streak([NEXT]), 0)

    def test_the_board_thanks_hunters(self):
        board = self.files["launches.html"]
        self.assertIn('<a href="https://github.com/h" rel="noopener">h</a>: 1 launched, 0 in a top three', board)
        self.assertNotIn('github.com/o"', board.split("<h2>Hunters</h2>")[1], "a maker's own launch is not hunting")
        weeks = [CLOSED, dict(CLOSED, week="2026-W45", launches=[
            launch("alpha", role="hunter", submitted_by="Z",
                   result={"votes": 1, "counted": 1, "discounted": 0, "rank": 1, "badges": ["week-1"]}),
            launch("beta", role="hunter", submitted_by="H",
                   result={"votes": 0, "counted": 0, "discounted": 0, "rank": 2})]), NEXT]
        self.assertEqual(launches.hunters(weeks), [("h", 2, 0), ("Z", 1, 1)])

    def test_the_week_pages_are_in_the_sitemap_and_link_only_what_is_served(self):
        self.assertIn("weeks/2026-W46.html", self.files["sitemap.xml"])
        week_dirs = {rel.split("/")[0] for rel in self.files if "/" in rel}
        self.assertLessEqual(week_dirs, set(site_pages.DIRS))


if __name__ == "__main__":
    unittest.main()
