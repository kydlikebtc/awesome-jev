"""draft_from_issue.py and new-entry.yml (X2, 2026-10-24): a new-entry issue is
answered with a first read of its repository and, for a call site, a draft row
built from GitHub, the file and the form, which lint refuses until a person
completes it. Everything the issue's author wrote stays inside the JSON block.
No network: inspect() is replaced."""

from __future__ import annotations

import copy
import datetime as dt
import json
import os
import pathlib
import re
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "scripts" / "tests"))

import draft_from_issue as dfi  # noqa: E402
import lint  # noqa: E402
from test_discover_drafts import TODAY, completed, found, lint_row  # noqa: E402
from test_weekly_jobs import run_block, step_lines  # noqa: E402

FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "new-entry.yml"
WORKFLOW = ROOT / ".github" / "workflows" / "new-entry.yml"


def body(url="https://github.com/acme/jev-tool", *, read=True, primitives=("noul",), boxes=(), notes="",
         summary="Gates each shell command with a noul; code owns the 0.8 threshold.", patterns="safety-gating",
         is_jev=None) -> str:
    """An issue body as GitHub renders the form."""
    def box(label, on):
        return f"- [{'x' if on else ' '}] {label}"
    caveats = [*dfi.CAVEAT_FLAGS, *dfi.CAVEAT_CHOICES, dfi.OWN]
    return "\n\n".join([
        f"### URL\n\n{url}",
        "### Title\n\nJev Tool",
        f"### What does it actually demonstrate?\n\n{summary}",
        f"### Does it call Jev?\n\n{is_jev or (dfi.READ_IT if read else 'Not sure')}",
        "### Which primitives does the code actually call?\n\n"
        + "\n".join(box(f"`{p}`", p in primitives) for p in dfi.PRIMITIVES),
        f"### Which decision pattern(s)?\n\n{patterns}",
        "### Anything a reader deserves to know before clicking?\n\n"
        + "\n".join(box(label, label in boxes) for label in caveats),
        f"### Notes\n\n{notes or '_No response_'}",
        "### Confirmation\n\n- [x] I opened this link and wrote the summary from what was actually there",
    ])


def issue(text: str, number: int = 99) -> dict:
    return {"number": number, "html_url": f"https://github.com/kydlikebtc/awesome-jev/issues/{number}", "body": text}


def reply(text: str, result: dict | None = None) -> str:
    return dfi.comment(issue(text), read=lambda slug: result or found(), today=TODAY)


def drafted(text: str) -> dict:
    """The draft row a comment carries."""
    match = re.search(r"^(`{3,})json\n(.*?)\n\1$", reply(text), re.MULTILINE | re.DOTALL)
    assert match, "no draft in the comment"
    return json.loads(match.group(2))


class FormTest(unittest.TestCase):
    """The parser knows the form as it is: a renamed label would otherwise
    silently drop that answer."""

    def test_every_heading_of_the_form_is_known(self):
        labels = re.findall(r"^      label: (.+)$", FORM.read_text(), re.MULTILINE)
        self.assertEqual(labels, list(dfi.FIELDS))

    def test_every_caveat_box_is_mapped_or_passed_on(self):
        text = FORM.read_text()
        section = text.split("id: caveats", 1)[1].split("  - type:", 1)[0]
        options = [json.loads(o) if o.startswith('"') else o for o in re.findall(r"- label: (.+)$", section, re.M)]
        self.assertEqual(sorted(options), sorted([*dfi.CAVEAT_FLAGS, *dfi.CAVEAT_CHOICES, dfi.OWN]))
        flags = {f["key"] for f in json.loads((ROOT / "taxonomy.json").read_text())["flags"]}
        self.assertLessEqual(set(dfi.CAVEAT_FLAGS.values()), flags)

    def test_the_dropdown_answers_it_reads_are_the_forms(self):
        text = FORM.read_text()
        self.assertIn(f'- "{dfi.READ_IT}"', text)
        self.assertIn(f'- "{dfi.ALTERNATIVE}"', text)

    def test_answers_are_read_by_heading(self):
        form = dfi.parse_form(body(notes="See ### URL\n\nhttps://github.com/evil/x").replace("\n", "\r\n"))
        self.assertEqual(form["url"], "https://github.com/acme/jev-tool")
        self.assertEqual(form["title"], "Jev Tool")
        self.assertIn("evil/x", form["notes"], "a heading typed in an answer stays in that answer")
        self.assertEqual(dfi.ticked(form["primitives"]), ["`noul`"])
        self.assertEqual(dfi.parse_form(body())["notes"], "", "_No response_ is no answer")

    def test_a_repository_or_a_page_inside_one(self):
        cases = {
            "https://github.com/Acme/Jev-Tool": "acme/jev-tool",
            "https://github.com/acme/jev-tool/": "acme/jev-tool",
            "https://github.com/acme/jev-tool.git": "acme/jev-tool",
            "https://github.com/acme/mono/tree/main/examples/jev": "acme/mono",
            "https://example.com/acme/jev-tool": None,
            "github.com/acme/jev-tool": None,
            "": None,
        }
        for url, slug in cases.items():
            with self.subTest(url=url):
                self.assertEqual(dfi.repository(url), slug)


class CommentTest(unittest.TestCase):
    def test_a_call_site_gets_a_draft_lint_refuses(self):
        text = reply(body())
        self.assertTrue(text.startswith(dfi.MARKER))
        self.assertIn("**Call site:** [`src/jev_client.py`](https://github.com/acme/jev-tool/blob/HEAD/src/jev_client.py)", text)
        self.assertIn("`api.typesafe.ai`, `jev-latest`", text)
        self.assertIn("`Closes #99`", text)
        row = drafted(body())
        errors, _ = lint_row(row)
        self.assertTrue(any("is a discovery draft, not a row" in e for e in errors), errors)

    def test_the_form_fills_in_what_it_says(self):
        row = drafted(body(boxes=("I read the code but did not run it",)))
        self.assertEqual(row["title"], "Jev Tool")
        self.assertEqual(row["summary"], "Gates each shell command with a noul; code owns the 0.8 threshold.")
        self.assertEqual(row["patterns"], ["safety-gating"])
        self.assertEqual(row["question_types"], ["noul"])
        self.assertEqual(list(row)[list(row).index("patterns") + 1], "question_types")
        self.assertEqual(row["flags"], ["code-untested"])
        self.assertEqual(row["sources"], [{"catalog": "community submission (issue #99)",
                                           "url": "https://github.com/kydlikebtc/awesome-jev/issues/99"}])
        said = " ".join(row[dfi.DRAFT_FIELD])
        self.assertIn("From issue #99", said)
        self.assertIn("code-untested needs a notes line", said)

    def test_primitives_only_from_someone_who_read_the_call_site(self):
        row = drafted(body(read=False))
        self.assertNotIn("question_types", row)
        self.assertIn("did not say it read the call site", " ".join(row[dfi.DRAFT_FIELD]))

    def test_an_own_project_is_disclosed(self):
        row = drafted(body(boxes=(dfi.OWN,)))
        self.assertIn("self-submitted", row["flags"])
        self.assertEqual(row["sources"][0]["catalog"], lint.SELF_SUBMISSION_SOURCE)

    def test_an_alternative_is_wire_shape_and_not_jev(self):
        row = drafted(body(is_jev=dfi.ALTERNATIVE))
        self.assertEqual(row["kind"], "alternative")
        self.assertEqual(row["evidence"]["kind"], "wire-shape")
        self.assertIn("not-jev", row["flags"])

    def test_a_box_naming_several_flags_is_passed_on(self):
        row = drafted(body(boxes=("Paywalled, marketing content, or looks machine-written",)))
        self.assertNotIn("flags", row)
        self.assertIn("`paywalled`, `marketing` or `ai-generated`", " ".join(row[dfi.DRAFT_FIELD]))

    def test_a_page_inside_the_repository_stays_the_link(self):
        url = "https://github.com/acme/jev-tool/tree/main/examples/gate"
        self.assertEqual(drafted(body(url=url))["url"], url)

    def test_free_text_patterns_keep_the_scripts_guess(self):
        row = drafted(body(patterns="gating, roughly"))
        self.assertEqual(row["patterns"], ["tool-selection"])
        self.assertIn("gating, roughly", " ".join(row[dfi.DRAFT_FIELD]))

    def test_a_completed_draft_passes_lint(self):
        row = completed(drafted(body()))
        row["sources"] = drafted(body())["sources"]
        self.assertEqual(lint_row(row), lint.Findings(), row)

    def test_what_the_author_wrote_stays_inside_the_block(self):
        hostile = "@kydlikebtc ```` </details> [x](javascript:alert(1)) ### URL"
        text = reply(body(summary=hostile, notes=hostile))
        fence = re.search(r"^(`{3,})json$", text, re.MULTILINE).group(1)
        self.assertGreater(len(fence), 4, "the fence outlasts any backtick run in the text")
        outside = re.sub(rf"^{fence}json\n.*?\n{fence}$", "", text, flags=re.MULTILINE | re.DOTALL)
        self.assertNotIn("@kydlikebtc", outside)
        self.assertNotIn("javascript:", outside)
        self.assertEqual(outside.count("</details>"), 1)

    def test_no_call_site_is_not_a_verdict(self):
        text = reply(body(), result={"slug": "acme/jev-tool", "verdict": "mentions-only"})
        self.assertIn("found no Jev call site", text)
        self.assertIn("README mentions Jev", text)
        self.assertIn("reply with its path", text)
        self.assertNotIn("json", text)

    def test_not_a_github_repository(self):
        text = reply(body(url="https://example.com/post"))
        self.assertIn("does not name a GitHub repository", text)

    def test_already_catalogued_names_the_row_and_a_missing_disclosure(self):
        catalog = json.loads((ROOT / "catalog.json").read_text())
        row = next(e for e in catalog if e.get("url", "").startswith("https://github.com/")
                   and "self-submitted" not in (e.get("flags") or []))
        url = row["url"]
        never = mock.Mock(side_effect=AssertionError("a catalogued repository is not read again"))
        text = dfi.comment(issue(body(url=url)), read=never, today=TODAY)
        self.assertIn(f"as [`{row['slug']}`]({dfi.SITE}#{row['slug']})", text)
        self.assertNotIn("self-submitted", text)
        text = dfi.comment(issue(body(url=url, boxes=(dfi.OWN,))), read=never, today=TODAY)
        self.assertIn("adds the `self-submitted` flag with this issue as its source", text)

    def test_retired_and_declined_say_why(self):
        retired = json.loads((ROOT / "retired.json").read_text())[0]
        text = reply(body(url=retired["url"]))
        self.assertIn(f"as `{retired['slug']}` and later retired", text)
        with mock.patch.object(dfi.discover_candidates, "read_declined", return_value={"acme/jev-tool": "a copy"}):
            self.assertIn("declined before (`docs/declined.txt`): a copy.", reply(body()))


class MainTest(unittest.TestCase):
    def test_the_event_is_answered_and_its_number_handed_on(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = pathlib.Path(tmp)
            event = folder / "event.json"
            event.write_text(json.dumps({"action": "opened", "issue": issue(body(), number=27)}))
            output = folder / "output"
            with mock.patch.object(dfi.discover_candidates, "inspect", return_value=found()), \
                 mock.patch.dict(os.environ, {"GITHUB_OUTPUT": str(output)}):
                code = dfi.main(["--event", str(event), "--out", str(folder / "comment.md")])
            self.assertEqual(code, 0)
            self.assertEqual(output.read_text(), "number=27\n")
            self.assertIn("issues/27", (folder / "comment.md").read_text())

    def test_a_dispatched_number_must_be_a_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            for bad in ("27; rm -rf /", "0", "-1", "abc"):
                with self.subTest(bad=bad), mock.patch.object(dfi._github, "api_get") as api:
                    self.assertEqual(dfi.main(["--issue", bad, "--out", f"{tmp}/c.md"]), 2)
                    api.assert_not_called()

    def test_a_pull_request_is_not_answered(self):
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(dfi._github, "api_get", return_value={"number": 5, "pull_request": {}}):
            self.assertEqual(dfi.main(["--issue", "5", "--out", f"{tmp}/c.md"]), 2)


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.text = WORKFLOW.read_text()

    def test_it_can_only_read_and_comment(self):
        self.assertIn("permissions:\n  contents: read\n  issues: write\n\n", self.text)
        self.assertNotIn("pull_request_target", self.text)
        self.assertIn("    types: [opened]\n", self.text)
        self.assertIn("contains(github.event.issue.labels.*.name, 'new entry')", self.text)
        self.assertIn('labels: ["new entry"]', FORM.read_text())

    def test_no_event_value_reaches_the_shell(self):
        for name in ("Read the repository the issue names", "Comment on the issue"):
            with self.subTest(step=name):
                self.assertNotIn("github.event", run_block(step_lines(self.text, name)))
        self.assertIn('          ISSUE: ${{ inputs.issue }}', self.text)
        self.assertIn('          NUMBER: ${{ steps.read.outputs.number }}', self.text)

    def test_a_second_run_rewrites_its_comment(self):
        script = run_block(step_lines(self.text, "Comment on the issue"))
        with tempfile.TemporaryDirectory() as tmp:
            folder = pathlib.Path(tmp)
            stub = folder / "bin" / "gh"
            stub.parent.mkdir()
            # Plays gh: logs each call; `--edit-last` fails while there is no earlier comment.
            stub.write_text(
                "#!/bin/bash\nprintf '%s\\n' \"$*\" >> \"$STUB_LOG\"\n"
                "for a in \"$@\"; do [ \"$a\" = --edit-last ] && [ \"$STUB_FIRST\" = yes ] && exit 1; done\nexit 0\n"
            )
            stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
            for first, calls in (("yes", 2), ("no", 1)):
                log = folder / f"gh-{first}.log"
                env = {**os.environ, "PATH": f"{folder / 'bin'}{os.pathsep}{os.environ['PATH']}",
                       "STUB_LOG": str(log), "STUB_FIRST": first, "NUMBER": "27"}
                done = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c",
                                       script.replace("/tmp/", f"{folder}/")],
                                      cwd=folder, env=env, capture_output=True, text=True)
                with self.subTest(first=first):
                    self.assertEqual(done.returncode, 0, done.stderr)
                    lines = log.read_text().splitlines()
                    self.assertEqual(len(lines), calls)
                    self.assertTrue(lines[0].startswith("issue comment 27 --edit-last --body-file"))


if __name__ == "__main__":
    unittest.main()
