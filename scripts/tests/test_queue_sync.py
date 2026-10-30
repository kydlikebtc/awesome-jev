"""The discovery issue's description as a queue (I05, phase C): each candidate's
state derived from the repository's files, rendered the same way every time.

A candidate is a repository .discover/seen.json records as calls-jev. It is
catalogued when a row in catalog.json links to it, catalogued and since
retired when only retired.json does, declined when docs/declined.txt names it,
and otherwise still to read, or parked when .discover/facts.json says it is
weak on two counts (since 2026-10-24), or held when docs/held.txt names it
(since 2026-10-30). No network.
"""

from __future__ import annotations

import contextlib
import io
import json
import pathlib
import random
import re
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import discover_candidates as dc  # noqa: E402
import discover_facts as df  # noqa: E402
import discover_seen as ds  # noqa: E402
import queue_sync as qs  # noqa: E402
from readme import rows as readme_rows  # noqa: E402


def v(on: str, verdict: str = "calls-jev") -> dict:
    return {"on": on, "verdict": verdict}


def entry(slug: str, url: str, **extra) -> dict:
    return {"slug": slug, "url": url, **extra}


SEEN = {
    "acme/listed": v("2026-09-17"),
    "acme/two-rows": v("2026-09-17"),
    "acme/via-repo": v("2026-09-10"),
    "gone/away": v("2026-09-03"),
    "no/thanks": v("2026-09-24"),
    "both/ways": v("2026-09-24"),
    "zeta/late": v("2026-09-24"),
    "alpha/early": v("2026-09-03"),
    "aaa/newest": v("2026-09-24"),
    "quiet/one": v("2026-09-24", "no-signal"),
    "readme/only": v("2026-09-24", "mentions-only"),
}
CATALOG = [
    entry("listed", "https://github.com/Acme/Listed"),
    entry("two-rows-b", "https://github.com/acme/two-rows/tree/main/examples/b"),
    entry("two-rows-a", "https://github.com/acme/two-rows"),
    entry("via-repo", "https://docs.example.com/guide", repo="https://github.com/acme/via-repo"),
    entry("both-ways", "https://github.com/both/ways"),
    entry("not-a-candidate", "https://github.com/some/other"),
]
RETIRED = [entry("gone-away", "https://github.com/gone/away", link_status=404)]
DECLINED = {"no/thanks": "README claims Jev, code never calls it", "both/ways": "declined first"}


def derive(seen=SEEN, catalog=CATALOG, retired=RETIRED, declined=DECLINED):
    return {c.repo: c for c in qs.derive(seen, catalog, retired, declined)}


class DeriveTest(unittest.TestCase):
    def test_each_candidate_gets_the_state_the_files_give_it(self):
        got = {repo: c.state for repo, c in derive().items()}
        self.assertEqual(got, {
            "acme/listed": "catalogued",
            "acme/two-rows": "catalogued",
            "acme/via-repo": "catalogued",
            "gone/away": "retired",
            "no/thanks": "declined",
            "both/ways": "catalogued",
            "zeta/late": "open",
            "alpha/early": "open",
            "aaa/newest": "open",
        })

    def test_only_calls_jev_verdicts_are_candidates(self):
        self.assertNotIn("quiet/one", derive())
        self.assertNotIn("readme/only", derive())
        self.assertEqual(qs.derive({}, CATALOG, RETIRED, DECLINED), [])

    def test_a_row_matches_by_url_or_repo_whatever_the_case(self):
        got = derive()
        self.assertEqual(got["acme/listed"].rows, ("listed",))
        self.assertEqual(got["acme/via-repo"].rows, ("via-repo",))
        self.assertEqual(got["acme/two-rows"].rows, ("two-rows-a", "two-rows-b"), "every row, by slug")

    def test_a_row_wins_over_a_retirement_and_either_over_a_decline(self):
        got = derive(retired=RETIRED + [entry("listed-old", "https://github.com/acme/listed", link_status=410)])
        self.assertEqual((got["acme/listed"].state, got["acme/listed"].rows), ("catalogued", ("listed",)))
        got = derive(declined={**DECLINED, "gone/away": "x"})
        self.assertEqual(got["gone/away"].state, "retired")
        self.assertEqual(derive()["both/ways"].state, "catalogued")

    def test_a_decline_keeps_its_reason_and_the_read_date_travels(self):
        got = derive()
        self.assertEqual(got["no/thanks"].reason, "README claims Jev, code never calls it")
        self.assertEqual(got["alpha/early"].read_on, "2026-09-03")

    def test_rows_that_are_not_objects_or_not_on_github_are_skipped(self):
        got = derive(catalog=["junk", entry("elsewhere", "https://example.com/acme/listed")] + CATALOG[1:])
        self.assertEqual(got["acme/listed"].state, "open")


class RenderTest(unittest.TestCase):
    def body(self, **kwargs) -> str:
        return qs.render(qs.derive(SEEN, CATALOG, RETIRED, DECLINED), **kwargs)

    def test_each_state_has_its_line(self):
        lines = self.body().splitlines()
        for line in (
            "- [ ] [alpha/early](https://github.com/alpha/early) · read by script 2026-09-03 · "
            "`python3 scripts/discover_candidates.py --only alpha/early`",
            f"- [x] [acme/listed](https://github.com/acme/listed) → [`listed`]({qs.SITE}?lang=en#listed)",
            f"- [x] [acme/two-rows](https://github.com/acme/two-rows) → [`two-rows-a`]({qs.SITE}?lang=en#two-rows-a),"
            f" [`two-rows-b`]({qs.SITE}?lang=en#two-rows-b)",
            "- [x] [gone/away](https://github.com/gone/away) → `gone-away`, since retired (`retired.json`)",
            "- [x] ~~[no/thanks](https://github.com/no/thanks)~~ · declined: README claims Jev, code never calls it",
        ):
            self.assertIn(line, lines)

    def test_counts_and_order(self):
        body = self.body()
        self.assertIn(
            "**3** to read · **0** held · **0** parked · **4** catalogued · **1** declined · **1** catalogued and since retired", body
        )
        opened = re.findall(r"^- \[ \] \[([^\]]+)\]", body, re.M)
        self.assertEqual(opened, ["alpha/early", "aaa/newest", "zeta/late"], "oldest read first, then by name")
        done = re.findall(r"^- \[x\] \[([^\]]+)\]", body, re.M)
        self.assertEqual(done, ["acme/listed", "acme/two-rows", "acme/via-repo", "both/ways", "gone/away"])
        self.assertLess(body.index("### To read · 待读"), body.index("<summary>Catalogued · 已收录 (4)</summary>"))
        self.assertLess(body.index("<summary>Catalogued · 已收录 (4)</summary>"),
                        body.index("<summary>Declined · 已拒收 (1)</summary>"))
        self.assertLess(body.index("<summary>Declined · 已拒收 (1)</summary>"),
                        body.index("<summary>Catalogued and since retired · 收录后已退役 (1)</summary>"))
        self.assertIn("<summary>Catalogued · 已收录 (4)</summary>\n\n- [x]", body, "a blank line lets the list render")

    def test_says_how_to_claim_in_both_languages_only_when_something_is_open(self):
        body = self.body()
        self.assertIn(dc.CLAIM_EN, body)
        self.assertIn(dc.CLAIM_ZH, body)
        self.assertLess(body.index("comment `claim owner/name`"), body.index("- [ ] "))
        zh = next(line for line in body.splitlines() if line.startswith("发现队列"))
        self.assertTrue(zh.endswith(" <sub>(机翻)</sub>"), "model-written Chinese is marked")
        settled = qs.render(qs.derive({"no/thanks": v("2026-09-24")}, CATALOG, RETIRED, DECLINED))
        self.assertNotIn("claim owner/name", settled)
        self.assertIn("Nothing to read: every candidate so far is catalogued or declined.", settled)
        self.assertIn("No candidate yet", qs.render([]))

    def test_headings_counts_and_notes_are_in_both_languages(self):
        # Principle f: the description is read by people in either language,
        # and the Chinese is marked as model-written.
        body = self.body()
        self.assertIn("待读 **3** · 等人看 **0** · 暂缓 **0** · 已收录 **4** · 已拒收 **1** · 收录后已退役 **1** <sub>(机翻)</sub>", body)
        self.assertIn("本描述里的中文（包括下面的标题和计数）都由模型写成。 <sub>(机翻)</sub>", body)
        settled = qs.render(qs.derive({"no/thanks": v("2026-09-24")}, CATALOG, RETIRED, DECLINED))
        self.assertIn("没有待读的候选：迄今每个候选都已收录或已拒收。 <sub>(机翻)</sub>", settled)
        self.assertIn("还没有候选：", qs.render([]))
        self.assertIn("另有 2 个未列出", self.body(open_shown=1, done_shown=2))
        for heading in re.findall(r"^(?:### |<summary>)(.+?)(?: \(\d+\)</summary>)?$", body, re.M):
            self.assertRegex(heading, r"[a-z] · [\u4e00-\u9fff]", "every heading in both languages")

    def test_an_open_date_is_the_scripts_read_not_a_persons(self):
        # Principle c: a person's reading and a script's are different claims.
        opened = [line for line in self.body().splitlines() if line.startswith("- [ ] ")]
        self.assertTrue(opened)
        for line in opened:
            self.assertRegex(line, r" · read by script \d{4}-\d{2}-\d{2} · ")

    def test_the_description_says_it_is_written_by_a_script(self):
        first = self.body().splitlines()[0]
        self.assertTrue(first.startswith("<!-- Written by scripts/queue_sync.py"), first)
        self.assertTrue(first.endswith("-->"))

    def test_a_decline_reason_cannot_ping_or_start_markup(self):
        body = qs.render(qs.derive({"no/thanks": v("2026-09-24")}, [], [], {"no/thanks": "@someone | <b>x</b>"}))
        line = next(line for line in body.splitlines() if "no/thanks" in line and "declined" in line)
        self.assertIn("@⁠someone \\| &lt;b>x&lt;/b>", line)
        self.assertIn("declined: no reason given",
                      qs.render(qs.derive({"no/thanks": v("2026-09-24")}, [], [], {"no/thanks": ""})))

    def test_same_files_same_bytes_whatever_their_order(self):
        body = self.body()
        rng = random.Random(5)
        for _ in range(20):
            seen = dict(rng.sample(list(SEEN.items()), len(SEEN)))
            catalog = rng.sample(CATALOG, len(CATALOG))
            declined = dict(rng.sample(list(DECLINED.items()), len(DECLINED)))
            self.assertEqual(qs.render(qs.derive(seen, catalog, RETIRED, declined)), body)

    def test_no_date_but_the_reads(self):
        body = self.body()
        self.assertEqual(set(re.findall(r"\d{4}-\d{2}-\d{2}", body)), {"2026-09-03", "2026-09-24"})
        self.assertNotRegex(body, r"(?i)\b(today|ago|yesterday)\b")

    def test_long_lists_are_capped_and_the_whole_fits_github(self):
        seen = {f"owner-{i:04d}/{'n' * 60}-{i}": v("2026-09-24") for i in range(3000)}
        declined = {repo: "x" * 150 for repo in list(seen)[:1500]}
        body = qs.body(qs.derive(seen, [], [], declined))
        self.assertLessEqual(len(body), qs.MAX_CHARS)
        shown = len(re.findall(r"^- \[ \] ", body, re.M))
        self.assertLess(shown, 1500)
        self.assertIn(f"- …and {1500 - shown} more, not shown to keep this description under GitHub's limit.", body)
        self.assertEqual(body, qs.body(qs.derive(dict(reversed(list(seen.items()))), [], [], declined)))
        small = self.body(open_shown=1, done_shown=2)
        self.assertEqual(len(re.findall(r"^- \[ \] ", small, re.M)), 1)
        self.assertEqual(small.count("- …and 2 more"), 2, "two of three to read, two of four catalogued")

    def test_the_site_link_is_the_sites(self):
        self.assertEqual(qs.SITE, readme_rows.SITE)


def f(stars: int, commits: int, pushed: str = "2026-10-01", readme: bool = True, **extra) -> dict:
    return {"stars": stars, "commits": commits, "pushed": pushed, "readme": readme, "archived": False, **extra}


class FactsTest(unittest.TestCase):
    """Since 2026-10-24: GitHub's figures order the candidates to read, and
    the weakest are parked, which decides nothing."""

    SEEN = {
        "few/stars": v("2026-09-03"),
        "many/stars": v("2026-09-24"),
        "same/stars-more-commits": v("2026-09-24"),
        "same/stars-later-push": v("2026-09-24"),
        "not/measured": v("2026-09-10"),
        "one/commit": v("2026-09-03"),
        "bare/repo": v("2026-09-03"),
        "gone/now": v("2026-09-03"),
        "old/name": v("2026-09-03"),
        "older/name": v("2026-09-03"),
    }
    FACTS = {
        "few/stars": f(2, 40),
        "many/stars": f(90, 3),
        "same/stars-more-commits": f(10, 50, "2026-01-01"),
        "same/stars-later-push": f(10, 5, "2026-10-20"),
        "one/commit": f(0, 1),
        "bare/repo": f(4, 1, readme=False),
        "gone/now": {"missing": True},
        "old/name": f(7, 7, name="new/name"),
        "older/name": f(7, 7, name="declined/name"),
    }
    CATALOG = [entry("new-name", "https://github.com/New/Name")]
    DECLINED = {"declined/name": "a fork of a catalogued project"}

    def derive(self, facts=None):
        return qs.derive(self.SEEN, self.CATALOG, [], self.DECLINED, self.FACTS if facts is None else facts)

    def test_to_read_goes_by_stars_then_commits_then_the_latest_push_and_unmeasured_last(self):
        body = qs.render(self.derive())
        opened = re.findall(r"^- \[ \] \[([^\]]+)\]", body, re.M)
        self.assertEqual(opened, [
            "many/stars", "same/stars-more-commits", "same/stars-later-push", "few/stars", "not/measured",
        ])
        line = next(line for line in body.splitlines() if "[many/stars]" in line)
        self.assertIn(" · ★90 · 3 commits · last push 2026-10-01 · read by script 2026-09-24 · ", line)
        line = next(line for line in body.splitlines() if "[not/measured]" in line)
        self.assertIn("(https://github.com/not/measured) · read by script 2026-09-10 · ", line, "no figures, no words")

    def test_two_weak_counts_or_a_missing_repository_park_a_candidate(self):
        got = {c.repo: c for c in self.derive()}
        self.assertEqual(got["one/commit"].state, "parked")
        self.assertEqual(got["one/commit"].reason, "one commit or none, no star")
        self.assertEqual(got["bare/repo"].reason, "one commit or none, no README")
        self.assertEqual(got["gone/now"].reason, df.MISSING)
        for repo in ("few/stars", "many/stars", "not/measured"):
            self.assertEqual(got[repo].state, "open", repo)
        self.assertEqual(df.parked(f(0, 30)), [], "one weak count alone parks nothing")

    def test_the_parked_section_says_nothing_was_decided(self):
        body = qs.render(self.derive())
        self.assertIn("**5** to read · **0** held · **3** parked · **1** catalogued · **1** declined", body)
        self.assertIn("待读 **5** · 等人看 **0** · 暂缓 **3** · ", body)
        start = body.index("<summary>Parked · 暂缓 (3)</summary>")
        self.assertLess(body.index("### To read · 待读"), start)
        self.assertLess(start, body.index("<summary>Catalogued · 已收录 (1)</summary>"))
        section = body[start:body.index("</details>", start)]
        self.assertIn(qs.PARKED_EN, section)
        self.assertIn(qs.PARKED_ZH, section)
        self.assertIn("Not declined", qs.PARKED_EN)
        self.assertTrue(qs.PARKED_ZH.endswith(" <sub>(机翻)</sub>"))
        self.assertNotIn("- [ ] ", section, "no box: nothing is asked of anyone")
        parked = re.findall(r"^- \[([^\]]+)\]\(https://github.com/[^)]+\) · parked: ", section, re.M)
        self.assertEqual(parked, ["bare/repo", "one/commit", "gone/now"], "strongest first, the missing one last")
        line = next(line for line in section.splitlines() if "[bare/repo]" in line)
        self.assertIn(" · parked: one commit or none, no README · ★4 · 1 commit · last push 2026-10-01 · read by ", line)
        self.assertEqual(line.count("README"), 1, "the reason names it once")
        line = next(line for line in section.splitlines() if "[gone/now]" in line)
        self.assertIn(f" · parked: {df.MISSING} · read by script 2026-09-03 · ", line)

    def test_a_renamed_candidate_takes_the_state_of_its_new_name(self):
        got = {c.repo: c for c in self.derive()}
        self.assertEqual((got["old/name"].state, got["old/name"].rows), ("catalogued", ("new-name",)))
        self.assertEqual((got["older/name"].state, got["older/name"].reason), ("declined", "a fork of a catalogued project"))
        # Until the refresh has read it, the cited name is all there is.
        self.assertEqual({c.repo: c.state for c in self.derive(facts={})}["old/name"], "open")

    def test_without_facts_the_queue_reads_as_it_did(self):
        self.assertEqual(
            qs.render(qs.derive(SEEN, CATALOG, RETIRED, DECLINED, {})),
            qs.render(qs.derive(SEEN, CATALOG, RETIRED, DECLINED)),
        )
        settled = qs.render(qs.derive({"one/commit": v("2026-09-03")}, [], [], {}, {"one/commit": f(0, 1)}))
        self.assertIn("Nothing to read but the held and parked candidates below.", settled)
        self.assertIn("除了下面等人看和暂缓的候选，没有待读的。 <sub>(机翻)</sub>", settled)
        self.assertNotIn("claim owner/name", settled)

    def test_same_facts_same_bytes_whatever_their_order(self):
        body = qs.render(self.derive())
        rng = random.Random(7)
        for _ in range(10):
            facts = dict(rng.sample(list(self.FACTS.items()), len(self.FACTS)))
            seen = dict(rng.sample(list(self.SEEN.items()), len(self.SEEN)))
            self.assertEqual(qs.render(qs.derive(seen, self.CATALOG, [], self.DECLINED, facts)), body)


class HeldTest(unittest.TestCase):
    """Since 2026-10-30: a candidate in docs/held.txt was read by someone who
    left it for a person, so it waits under its own heading, out of the way of
    the drafting runs, and a small candidate quiet for four weeks is parked."""

    SEEN = {
        "big/unsure": v("2026-10-01"),
        "small/unsure": v("2026-10-01"),
        "plain/open": v("2026-10-01"),
        "no/thanks": v("2026-10-01"),
        "listed/now": v("2026-10-01"),
        "small/quiet": v("2026-10-01"),
        "small/busy": v("2026-10-29"),
        "three/stars": v("2026-10-01"),
    }
    FACTS = {
        "big/unsure": f(900, 400),
        "small/unsure": f(1, 2, "2026-09-01"),
        "plain/open": f(50, 50),
        "small/quiet": f(2, 4, "2026-10-01"),
        "small/busy": f(2, 4, "2026-10-02"),
        "three/stars": f(3, 4, "2026-09-01"),
    }
    HELD = {
        "big/unsure": "README does not mention Jev | needs @code search",
        "small/unsure": "",
        "no/thanks": "held, then declined",
        "listed/now": "held, then catalogued",
    }
    CATALOG = [entry("listed-now", "https://github.com/listed/now")]
    DECLINED = {"no/thanks": "not a decision example"}

    def derive(self, held=None):
        return {c.repo: c for c in qs.derive(
            self.SEEN, self.CATALOG, [], self.DECLINED, self.FACTS, self.HELD if held is None else held,
        )}

    def test_a_hold_beats_to_read_and_parked_but_not_a_row_or_a_decline(self):
        got = self.derive()
        self.assertEqual((got["big/unsure"].state, got["big/unsure"].reason),
                         ("held", "README does not mention Jev | needs @code search"))
        self.assertEqual(got["small/unsure"].state, "held", "held even when its figures would park it")
        self.assertEqual(got["no/thanks"].state, "declined")
        self.assertEqual(got["listed/now"].state, "catalogued")
        self.assertEqual(self.derive(held={})["big/unsure"].state, "open")

    def test_a_small_candidate_quiet_for_four_weeks_of_the_queue_is_parked(self):
        got = self.derive()
        # The queue's date is its newest verdict, 2026-10-29: 28 days after 10-01.
        self.assertEqual((got["small/quiet"].state, got["small/quiet"].reason), ("parked", df.QUIET))
        self.assertEqual(got["small/busy"].state, "open", "pushed 27 days before the queue's date")
        self.assertEqual(got["three/stars"].state, "open", "three stars is not small")
        self.assertEqual(got["plain/open"].state, "open")
        self.assertEqual(df.parked(f(2, 4, "2026-01-01")), [], "no date, no quiet rule")

    def test_the_held_section_sits_between_to_read_and_parked_and_asks_nothing(self):
        body = qs.render(list(self.derive().values()))
        self.assertIn("**3** to read · **2** held · **1** parked · ", body)
        self.assertIn("待读 **3** · 等人看 **2** · 暂缓 **1** · ", body)
        start = body.index("<summary>Held for a person · 等人看 (2)</summary>")
        self.assertLess(body.index("### To read · 待读"), start)
        self.assertLess(start, body.index("<summary>Parked · 暂缓 (1)</summary>"))
        section = body[start:body.index("</details>", start)]
        self.assertIn(qs.HELD_EN, section)
        self.assertIn(qs.HELD_ZH, section)
        self.assertNotIn("- [ ] ", section, "no box: it waits on a decision, which lands in the files")
        held = re.findall(r"^- \[([^\]]+)\]\(https://github.com/[^)]+\) · held: ", section, re.M)
        self.assertEqual(held, ["big/unsure", "small/unsure"], "strongest first")
        line = next(line for line in section.splitlines() if "[big/unsure]" in line)
        self.assertNotIn("@code", line, "a reason is outside text, made inert")
        self.assertIn(" · ★900 · 400 commits · last push 2026-10-01 · read by script 2026-10-01", line)
        self.assertIn("[small/unsure](https://github.com/small/unsure) · held: no reason given · ", body)
        self.assertNotIn("[ ] [big/unsure]", body)

    def test_the_command_reads_docs_held_txt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "docs").mkdir()
            (root / "catalog.json").write_text("[]")
            (root / "retired.json").write_text("[]")
            (root / "docs" / "held.txt").write_text(
                "# comment\nBig/Unsure  # left for a person\nsome-row  # a row, not a candidate\n"
            )
            ds.write(root / ".discover" / "seen.json", {"big/unsure": v("2026-10-01")})
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                self.assertEqual(qs.main(["--root", str(root)]), 0)
            self.assertIn("0 open, 1 held, 0 parked", err.getvalue())
            self.assertIn("[big/unsure](https://github.com/big/unsure) · held: left for a person", out.getvalue())


class CommandTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = pathlib.Path(tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "catalog.json").write_text(json.dumps(CATALOG))
        (self.root / "retired.json").write_text(json.dumps(RETIRED))
        (self.root / "docs" / "declined.txt").write_text(
            "# comment line\n" + "".join(f"{repo}  # {why}\n" for repo, why in DECLINED.items())
        )
        ds.write(self.root / ".discover" / "seen.json", SEEN)

    def run_main(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = qs.main(["--root", str(self.root), *argv])
        return code, out.getvalue(), err.getvalue()

    def test_writes_the_description_and_logs_the_counts(self):
        target = self.root / "queue.md"
        code, out, err = self.run_main("--out", str(target))
        self.assertEqual(code, 0, err)
        self.assertEqual(out, "")
        self.assertEqual(target.read_text(encoding="utf-8"), qs.body(qs.derive(SEEN, CATALOG, RETIRED, DECLINED)))
        self.assertIn(
            "discovery queue: 9 candidate(s) among 11 verdict(s): 3 open, 0 held, 0 parked, 4 catalogued, 1 retired, 1 declined",
            err,
        )
        self.assertIn(f"wrote {target}", err)

    def test_prints_it_without_out(self):
        code, out, _ = self.run_main()
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("<!-- Written by scripts/queue_sync.py"))

    def test_a_verdict_file_entry_of_the_wrong_shape_is_reported_and_left_out(self):
        path = self.root / ".discover" / "seen.json"
        data = json.loads(path.read_text())
        data["verdicts"]["Bad Name/x"] = v("2026-09-24")
        path.write_text(json.dumps(data))
        code, out, err = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn("::warning title=Discovery verdicts left out::.discover/seen.json: 1 entry", err)
        self.assertNotIn("Bad Name", out)

    def test_no_verdict_file_is_an_empty_queue_and_no_catalogue_is_an_error(self):
        (self.root / ".discover" / "seen.json").unlink()
        (self.root / "docs" / "declined.txt").unlink()
        code, out, _ = self.run_main()
        self.assertEqual(code, 0)
        self.assertIn("No candidate yet", out)
        (self.root / "catalog.json").unlink()
        code, _, err = self.run_main()
        self.assertEqual(code, 1)
        self.assertIn("error:", err)

    def test_reads_the_facts_file_and_reports_entries_of_the_wrong_shape(self):
        df.write(self.root / ".discover" / "facts.json", {"alpha/early": f(0, 1), "zeta/late": f(3, 9)})
        path = self.root / ".discover" / "facts.json"
        data = json.loads(path.read_text())
        data["facts"]["aaa/newest"] = {"stars": "many"}
        path.write_text(json.dumps(data))
        code, out, err = self.run_main()
        self.assertEqual(code, 0, err)
        self.assertIn("discovery queue: 9 candidate(s) among 11 verdict(s): 2 open, 0 held, 1 parked, ", err)
        self.assertIn("::warning title=Discovery facts left out::.discover/facts.json: 1 entry", err)
        self.assertIn("[zeta/late](https://github.com/zeta/late) · ★3 · 9 commits", out)

    def test_runs_on_this_repository(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(qs.main([]), 0)
        self.assertIn("discovery queue:", err.getvalue())
        self.assertLessEqual(len(out.getvalue()), qs.MAX_CHARS)


if __name__ == "__main__":
    unittest.main()
