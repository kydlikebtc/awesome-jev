"""A model's row from the discovery queue: scripts/model_draft.py (E1).

The scheduled drafting runs start each row with the script and check it with
--check before it goes into catalog.json. These tests pin both: what a draft
fills in (the model tier's fields, the strings the cited file holds) and what
it refuses to draft, and what --check refuses in a finished row (a person's
fields, a string the file no longer holds, a slug or candidate already
settled). No network: the file a row cites is handed in.
"""

from __future__ import annotations

import contextlib
import copy
import datetime as dt
import io
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import lint  # noqa: E402
import model_draft as md  # noqa: E402

TODAY = dt.date(2026, 10, 30)
BODY = 'API_URL = "https://api.typesafe.ai/v1/systemone"\nMODEL = "jev-latest"\nclient.choice(state, options)\n'


def fetcher(files: dict[str, str]):
    """A raw_get stand-in: `owner/name:path` to the file's text, None when absent."""
    return lambda repo, branch, path: files.get(f"{repo}:{path}")


class Root:
    """A repository root in a temporary directory, with the real schema,
    compat.json and taxonomy.json and the row files and lists given."""

    def __init__(self, catalog=(), retired=(), declined="", held=""):
        self._dir = tempfile.TemporaryDirectory()
        self.path = pathlib.Path(self._dir.name)
        (self.path / "docs").mkdir()
        (self.path / "schema").mkdir()
        for name in ("compat.json", "taxonomy.json", "schema/entry.schema.json"):
            (self.path / name).write_text((ROOT / name).read_text(encoding="utf-8"), encoding="utf-8")
        (self.path / "catalog.json").write_text(json.dumps(list(catalog)), encoding="utf-8")
        (self.path / "retired.json").write_text(json.dumps(list(retired)), encoding="utf-8")
        (self.path / "docs" / "declined.txt").write_text(declined, encoding="utf-8")
        (self.path / "docs" / "held.txt").write_text(held, encoding="utf-8")

    def close(self) -> None:
        self._dir.cleanup()


def quietly(fn, *args, **kwargs):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fn(*args, **kwargs)
    return code, out.getvalue(), err.getvalue()


def finished(draft: dict) -> dict:
    """The draft as a model completes it."""
    row = copy.deepcopy(draft)
    del row[lint.DRAFT_FIELD]
    row.update(
        summary="A support bot that asks Jev which of three queues a ticket belongs in before a person reads it.",
        summary_zh="一个客服机器人，在人工阅读之前先让 Jev 判断工单属于三个队列中的哪一个。",
        kind="project",
        patterns=["intent-routing"],
        question_types=["choice"],
        platforms=["typesafe-api"],
        repo_license="MIT",
    )
    return row


class DraftTest(unittest.TestCase):
    def setUp(self):
        self.root = Root(
            catalog=[{"slug": "taken", "url": "https://github.com/acme/taken"}],
            declined="acme/no  # a wrapper of a wrapper\n",
            held="acme/wait  # its questions live in recipe files\n",
        )
        self.out = self.root.path / "drafts"
        self.files = fetcher({
            "acme/desk-bot:src/route.py": BODY,
            "acme/quiet:src/util.py": "print('nothing here')\n",
            "acme/tested:tests/test_jev.py": BODY,
        })

    def tearDown(self):
        self.root.close()

    def start(self, repo, path, **kwargs):
        return quietly(md.start, repo, path, str(self.out), fetch=self.files, root=self.root.path,
                       today=TODAY, **kwargs)

    def test_a_draft_carries_the_model_tier_and_the_strings_the_file_holds(self):
        code, _, _ = self.start("acme/desk-bot", "src/route.py")
        self.assertEqual(code, 0)
        row = json.loads((self.out / "desk-bot.json").read_text(encoding="utf-8"))
        self.assertEqual(next(iter(row)), lint.DRAFT_FIELD)
        self.assertEqual(row["summary_source"], "model-written")
        self.assertIs(row["zh_machine"], True)
        self.assertEqual(row["evidence"], {
            "path": "src/route.py",
            "matched": ["api.typesafe.ai", "jev-latest", "/v1/systemone"],
            "model_read_on": "2026-10-30",
        })
        self.assertEqual(row["languages"], ["python"])
        self.assertEqual(row["first_seen"], "2026-10-30")
        self.assertIn("by an AI assistant", row["notes"])
        self.assertIn("2026-10-30", row["notes_zh"])
        self.assertNotIn("read_on", row["evidence"])
        self.assertNotIn("patterns_reviewed", row)
        self.assertNotIn("stars", row)

    def test_lint_refuses_a_draft_as_it_is(self):
        self.start("acme/desk-bot", "src/route.py")
        row = json.loads((self.out / "desk-bot.json").read_text(encoding="utf-8"))
        found = lint.check_entry_invariants(row, "draft", retired=False, today=TODAY)
        self.assertTrue(any(lint.DRAFT_FIELD in e for e in found.errors))

    def test_it_will_not_draft_what_is_settled_or_held(self):
        for repo, said in (
            ("acme/taken", "already catalogued as taken"),
            ("Acme/No", "declined in docs/declined.txt: a wrapper of a wrapper"),
            ("acme/wait", "held for a person in docs/held.txt: its questions live in recipe files"),
        ):
            with self.subTest(repo=repo):
                code, _, err = self.start(repo, "src/route.py")
                self.assertEqual(code, 1)
                self.assertIn(said, err)
        self.assertFalse(self.out.exists())

    def test_a_file_without_a_call_site_string_says_so(self):
        code, _, err = self.start("acme/quiet", "src/util.py")
        self.assertEqual(code, 0)
        row = json.loads((self.out / "quiet.json").read_text(encoding="utf-8"))
        self.assertEqual(row["evidence"]["matched"], [])
        self.assertIn("holds none of the strings", row[lint.DRAFT_FIELD][1])
        self.assertIn("no Jev call-site string", err)

    def test_a_test_file_is_named_as_one(self):
        self.start("acme/tested", "tests/test_jev.py")
        row = json.loads((self.out / "tested.json").read_text(encoding="utf-8"))
        self.assertTrue(any("looks like a test" in line for line in row[lint.DRAFT_FIELD]))

    def test_a_missing_file_writes_nothing(self):
        code, _, err = self.start("acme/desk-bot", "src/gone.py")
        self.assertEqual(code, 1)
        self.assertIn("could not be read", err)
        self.assertFalse(self.out.exists())

    def test_an_existing_draft_is_kept(self):
        self.start("acme/desk-bot", "src/route.py")
        code, _, err = self.start("acme/desk-bot", "src/route.py", slug="desk-bot")
        self.assertEqual(code, 1)
        self.assertIn("exists", err)


class CheckTest(unittest.TestCase):
    def setUp(self):
        self.root = Root(
            catalog=[{"slug": "taken", "url": "https://github.com/acme/taken"}],
            held="acme/wait  # its questions live in recipe files\n",
        )
        self.known = md.files(self.root.path)
        draft = md.draft_row("acme/desk-bot", "src/route.py", BODY, slug="desk-bot", today=TODAY)
        self.row = finished(draft)

    def tearDown(self):
        self.root.close()

    def errors(self, row, body=BODY):
        return md.problems(row, "row.json", self.known, body=body, today=TODAY).errors

    def test_a_finished_draft_passes(self):
        self.assertEqual(self.errors(self.row), ())

    def test_the_command_reads_the_cited_file(self):
        path = self.root.path / "row.json"
        path.write_text(json.dumps(self.row, ensure_ascii=False), encoding="utf-8")
        files = fetcher({"acme/desk-bot:src/route.py": BODY})
        code, out, _ = quietly(md.check, [str(path)], fetch=files, root=self.root.path, today=TODAY)
        self.assertEqual(code, 0)
        self.assertIn("checked 1 row", out)
        code, _, err = quietly(md.check, [str(path)], fetch=fetcher({}), root=self.root.path, today=TODAY)
        self.assertEqual(code, 1)
        self.assertIn("could not be read", err)

    def test_a_string_the_file_no_longer_holds_fails(self):
        row = copy.deepcopy(self.row)
        row["evidence"]["matched"].append('MODEL = "jev-1.13"')
        self.assertTrue(any("does not contain" in e for e in self.errors(row)))
        self.assertEqual(md.problems(row, "row.json", self.known, body=None, today=TODAY).errors, ())

    def test_a_persons_fields_fail(self):
        for change, said in (
            (lambda r: r["evidence"].update(read_on="2026-10-30"), "evidence.read_on is a person's"),
            (lambda r: r.update(patterns_reviewed="2026-10-30"), "patterns_reviewed is a person's"),
            (lambda r: r.update(summary_source="curated"), "summary_source must be 'model-written'"),
            (lambda r: r.update(zh_machine=False), "zh_machine must be true"),
            (lambda r: r["evidence"].pop("model_read_on"), "evidence.model_read_on must be"),
        ):
            row = copy.deepcopy(self.row)
            change(row)
            with self.subTest(said=said):
                self.assertTrue(any(said in e for e in self.errors(row)), self.errors(row))

    def test_the_notes_sentence_is_required_in_both_languages(self):
        for field in ("notes", "notes_zh"):
            row = copy.deepcopy(self.row)
            row[field] = "Something else."
            with self.subTest(field=field):
                self.assertTrue(any(f"{field} must carry the sentence" in e for e in self.errors(row)))

    def test_the_schema_and_lint_rules_apply(self):
        row = copy.deepcopy(self.row)
        row["summary"] = "x" * 301
        row["kind"] = "alternative"
        errors = self.errors(row)
        self.assertTrue(any("summary" in e and "300" in e for e in errors), errors)
        self.assertTrue(any("wire-shape" in e for e in errors), errors)

    def test_a_slug_url_or_held_candidate_already_settled_fails(self):
        for change, said in (
            (lambda r: r.update(slug="taken"), "slug is already used in catalog.json"),
            (lambda r: r.update(url="https://github.com/acme/taken/"), "is already taken in catalog.json"),
            (lambda r: r.update(url="https://github.com/acme/wait"), "held for a person"),
        ):
            row = copy.deepcopy(self.row)
            change(row)
            with self.subTest(said=said):
                self.assertTrue(any(said in e for e in self.errors(row)), self.errors(row))

    def test_the_row_once_added_passes_again(self):
        self.known["catalog"].append(self.row)
        self.assertEqual(self.errors(self.row), ())


class CatalogueTest(unittest.TestCase):
    def test_every_discovery_row_a_model_drafted_passes(self):
        """The rows the drafting runs added before the script existed follow
        what --check asks, so a new row and an old one are held to one rule."""
        known = md.files(ROOT)
        rows = [r for r in known["catalog"] if md.SAID_EN in r.get("notes", "")
                and r.get("evidence", {}).get("model_read_on")]
        self.assertGreater(len(rows), 50)
        for row in rows:
            with self.subTest(slug=row["slug"]):
                found = md.problems(row, row["slug"], known, body=None, today=dt.date.today())
                self.assertEqual(found.errors, ())


if __name__ == "__main__":
    unittest.main()
