"""Primitive text signals (I14): verify_claims.py reads the one file a row's
evidence cites, and records in `primitives_seen` which primitives' request or
answer shapes that file's text contains. A machine text signal, never a person's
reading: question_types stays the only field any rule, filter or count of
"primitive claims" reads. No network: the _github calls are replaced."""

from __future__ import annotations

import contextlib
import io
import json
import os
import pathlib
import re
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import _github  # noqa: E402
import _stats  # noqa: E402
import build_assets  # noqa: E402
import build_readme  # noqa: E402
import verify_claims as vc  # noqa: E402

SCRIPTS = pathlib.Path(__file__).resolve().parents[1]


def base_row(slug: str, **extra) -> dict:
    return {
        "slug": slug,
        "url": f"https://github.com/a/{slug}",
        "kind": "project",
        "has_code": True,
        "evidence": {"path": "src/x.py", "matched": ["system_one"]},
        **extra,
    }


class ShapeTest(unittest.TestCase):
    """What counts as a primitive's shape, and what is only a word."""

    POSITIVE = (
        ('{"type": "choice", "criteria": {"a": "A"}}', ["choice"]),
        ("q = {'type': 'score', 'criteria': levels}", ["score"]),
        ("questions: { urgent: { type: 'noul', instructions } }", ["noul"]),
        ('export type Q = { type: "score"; criteria: string[] }', ["score"]),
        ('{"type" => "noul", "instructions" => text}', ["noul"]),
        ('{:type => "choice"}', ["choice"]),
        ('append(s, "{\\"q\\":{\\"type\\":\\"noul\\",\\"instructions\\":\\"x\\"}}");', ["noul"]),
        ('"department": Choice(instructions="Which team")', ["choice"]),
        ("native[key] = sdk.Score(instructions=x, criteria=levels)", ["score"]),
        ("func Noul(instructions string) Question {", ["noul"]),
        ("print(f\"{answers['urgent'].noul:.2f}\")", ["noul"]),
        ('x = answer.noul; y = {"type": "score"}; z = Choice(', ["choice", "score", "noul"]),
    )
    NEGATIVE = (
        "Pick the best choice, then score it. Noul is the yes-no primitive.",
        "random.choice(options)",
        "model.score(X, y)",
        "best = answer.choice; level = answer.score",
        'SimpleNamespace(type="noul", noul=0.9)',
        '@click.option("--mode", type=click.Choice(["fast", "slow"]))',
        '{"type": "boolean"}',
        'const field = { subtype: "choice" }',
        'TypeNoul = "noul"',
        "if self.nouls: pass",
        "NoulAnswer(probability=0.3)",
    )

    def test_shapes_name_their_primitive(self):
        for text, expected in self.POSITIVE:
            with self.subTest(text=text):
                self.assertEqual(vc.primitive_signals(text), expected)

    def test_words_and_lookalikes_are_not_shapes(self):
        for text in self.NEGATIVE:
            with self.subTest(text=text):
                self.assertEqual(vc.primitive_signals(text), [])

    def test_the_answer_is_in_the_schemas_order_and_unique(self):
        text = '.noul .noul "type": "noul" Score( {"type": "choice"}'
        self.assertEqual(vc.primitive_signals(text), ["choice", "score", "noul"])
        schema = json.loads((SCRIPTS.parent / "schema" / "entry.schema.json").read_text())
        for field in ("question_types", "primitives_seen"):
            with self.subTest(field=field):
                self.assertEqual(tuple(schema["properties"][field]["items"]["enum"]), vc.PRIMITIVES)

    def test_weak_words_are_whole_words_only(self):
        self.assertEqual(vc.weak_words("score = choices; Noul"), ["Noul", "score"])
        self.assertEqual(vc.weak_words("noulish Scores"), [])


class TypeScriptSdkHelperTest(unittest.TestCase):
    """The TypeScript SDK builds questions with choice(), score() and noul()
    from @typesafe-ai/sdk (its README: `category: choice("What is this ticket
    about?", {...})`). A lower-case name is only a shape when the file imports
    it from the SDK by name and calls it."""

    POSITIVE = (
        ('import { choice, TypeSafeClient } from "@typesafe-ai/sdk";\n'
         'const q = { category: choice("What is this ticket about?", { billing: "Billing" }) };', ["choice"]),
        ("import { noul as yes } from '@typesafe-ai/sdk'\nconst q = { urgent: yes('Is it urgent?') };", ["noul"]),
        ('import {\n  TypeSafeClient,\n  score,\n  noul,\n} from "@typesafe-ai/sdk";\n'
         "const q = { severity: score ('How bad?', levels), done: noul('Done?') };", ["score", "noul"]),
        ('import TypeSafe, { choice } from "@typesafe-ai/sdk";\nchoice("Pick", opts);', ["choice"]),
    )
    NEGATIVE = (
        # Imported, never called.
        'import { choice, noul } from "@typesafe-ai/sdk";\nexport { choice, noul };',
        # Called, but not the SDK's.
        'import { choice } from "./random";\nchoice(items);',
        "from random import choice\nchoice(options)",
        # A method of the same name.
        'import { choice } from "@typesafe-ai/sdk";\nconst pick = rng.choice(xs);',
        # Only the type is imported.
        'import type { choice } from "@typesafe-ai/sdk";\nchoice(x);',
        # The alias is called, not the name it hides.
        'import { score as level } from "@typesafe-ai/sdk";\nscore(x);',
    )

    def test_an_sdk_helper_imported_and_called_names_its_primitive(self):
        for text, expected in self.POSITIVE:
            with self.subTest(text=text):
                self.assertEqual(vc.primitive_signals(text), expected)

    def test_a_lower_case_name_alone_is_not_a_shape(self):
        for text in self.NEGATIVE:
            with self.subTest(text=text):
                self.assertEqual(vc.primitive_signals(text), [])


class Files:
    """A fake raw host: {(branch, path): body}; a missing key is a 404."""

    def __init__(self, files: dict, *, branch: str | None = "main"):
        self.files = files
        self.branch = branch

    def raw_get(self, repo, branch, path, **_):
        value = self.files.get((repo, branch, path))
        if isinstance(value, BaseException):
            raise value
        return value

    def default_branch(self, repo):
        return self.branch

    def patch(self, test: unittest.TestCase) -> None:
        for name in ("raw_get", "default_branch"):
            patcher = mock.patch.object(vc, name, getattr(self, name))
            patcher.start()
            test.addCleanup(patcher.stop)


class CheckTest(unittest.TestCase):
    def test_a_claim_that_holds_reports_the_signals_of_the_file_it_read(self):
        for files, where in (
            ({("a/r", "HEAD", "src/x.py"): 'system_one(q={"type": "noul"})'}, "HEAD"),
            ({("a/r", "main", "src/x.py"): "system_one(Choice(...))"}, "main"),
        ):
            with self.subTest(read_at=where):
                Files(files).patch(self)
                result = vc.check(base_row("r"))
                self.assertEqual(result["status"], "ok")
                self.assertEqual(result["primitive_signals"], ["noul"] if where == "HEAD" else ["choice"])

    def test_a_failed_claim_carries_no_signals(self):
        Files({("a/r", "main", "src/x.py"): '{"type": "noul"}'}).patch(self)
        result = vc.check(base_row("r"))
        self.assertEqual(result["status"], "claim-gone")
        self.assertNotIn("primitive_signals", result)

    def test_discover_reports_the_signals_of_the_file_it_proposes(self):
        tree = {"tree": [{"type": "blob", "path": "jev.py"}]}
        body = 'client.system_one(questions={"q": Noul(instructions="x")}) # score'
        with mock.patch.object(vc, "default_branch", return_value="main"), \
             mock.patch.object(vc, "api_get", return_value=tree), \
             mock.patch.object(vc, "raw_get", return_value=body):
            proposal = vc.discover({"slug": "d", "url": "https://github.com/a/d", "has_code": True})
        self.assertEqual(proposal["matched"], ["system_one", "Noul", "score"])
        self.assertEqual(proposal["primitive_signals"], ["noul"])


class MainRun:
    """Run verify_claims.main() over a temporary catalog.json."""

    def __init__(self, test: unittest.TestCase, rows: list[dict], files: Files):
        tmp = tempfile.TemporaryDirectory()
        test.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        self.catalog = self.dir / "catalog.json"
        self.catalog.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
        self.summary = self.dir / "summary.md"
        self.files = files

    def __call__(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(vc, "CATALOG", self.catalog), \
             mock.patch.object(sys, "argv", ["verify_claims.py", *argv]), \
             mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(self.summary)}), \
             mock.patch.object(vc, "raw_get", self.files.raw_get), \
             mock.patch.object(vc, "default_branch", self.files.default_branch), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = vc.main()
        return code, out.getvalue(), err.getvalue()

    def rows(self) -> dict[str, dict]:
        return {row["slug"]: row for row in json.loads(self.catalog.read_text())}


def body(signals: str) -> str:
    return f"client.system_one()\n{signals}\n"


class JsonTest(unittest.TestCase):
    def test_json_lists_the_signals_of_every_claim_that_held(self):
        files = Files({
            ("a/one", "HEAD", "src/x.py"): body('{"type": "score"}'),
            ("a/two", "HEAD", "src/x.py"): body("nothing here"),
        })
        run = MainRun(self, [base_row("one"), base_row("two"), base_row("three")], files)
        code, out, _ = run("--json")
        report = json.loads(out)
        self.assertEqual(code, 1)  # three's file is gone: the claims check still fails
        self.assertEqual(report["primitive_signals"], {"one": ["score"]})
        self.assertEqual([r["slug"] for r in report["failed"]], ["three"])


class WriteSignalsTest(unittest.TestCase):
    LIMITED = _github.RateLimited("raw", "HTTP 429 again after the wait")

    def setUp(self):
        self.rows = [
            base_row("added"),
            base_row("same", primitives_seen=["noul"]),
            base_row("changed", primitives_seen=["noul"]),
            base_row("emptied", primitives_seen=["score"]),
            base_row("gone", primitives_seen=["choice"]),
            base_row("unread", primitives_seen=["choice"]),
            base_row("person", question_types=["choice"]),
            {"slug": "no-evidence", "url": "https://github.com/a/no-evidence", "kind": "article"},
        ]
        self.files = Files({
            ("a/added", "HEAD", "src/x.py"): body('Choice( {"type": "noul"}'),
            ("a/same", "HEAD", "src/x.py"): body("a.noul"),
            ("a/changed", "HEAD", "src/x.py"): body("a.noul Score("),
            ("a/emptied", "HEAD", "src/x.py"): body("a score, as a word"),
            ("a/gone", "main", "src/x.py"): "the call was removed",
            ("a/unread", "HEAD", "src/x.py"): self.LIMITED,
            ("a/person", "HEAD", "src/x.py"): body("a.noul"),
            ("a/no-evidence", "HEAD", "src/x.py"): body("a.noul"),
        })
        self.run_main = MainRun(self, self.rows, self.files)

    def test_each_row_gets_what_its_file_shows_now(self):
        code, out, _ = self.run_main("--write-signals")
        self.assertEqual(code, 0, "claims failures are the claims job's alarm, not this one's")
        rows = self.run_main.rows()
        self.assertEqual(rows["added"]["primitives_seen"], ["choice", "noul"])
        self.assertEqual(rows["same"]["primitives_seen"], ["noul"])
        self.assertEqual(rows["changed"]["primitives_seen"], ["score", "noul"])
        self.assertNotIn("primitives_seen", rows["emptied"])
        self.assertNotIn("primitives_seen", rows["gone"], "a file that no longer shows the claim shows no signal")
        self.assertEqual(rows["unread"]["primitives_seen"], ["choice"], "a read the rate limit stopped changes nothing")
        self.assertEqual(rows["person"]["primitives_seen"], ["noul"])
        self.assertEqual(rows["person"]["question_types"], ["choice"], "a person's reading is never touched")
        self.assertNotIn("primitives_seen", rows["no-evidence"])
        last = out.strip().splitlines()[-1]
        self.assertEqual(
            last,
            "primitive text signals: 7 row(s) with evidence; 2 added, 1 changed, 2 removed, "
            "1 unchanged; 1 not read (GitHub rate limit or no repository); "
            "experimental features: 0 row(s) changed",
        )
        for line in ("  + added: choice, noul", "  ~ changed: noul -> score, noul",
                     "  - emptied: score (no shape in the file)", "  - gone: choice (claim-gone)"):
            self.assertIn(line, out)

    def test_the_field_sits_right_after_evidence_and_nothing_else_moves(self):
        self.run_main("--write-signals")
        text = self.run_main.catalog.read_text()
        self.assertEqual(text, json.dumps(json.loads(text), indent=2, ensure_ascii=False) + "\n")
        for slug, row in self.run_main.rows().items():
            original = next(r for r in self.rows if r["slug"] == slug)
            keys = [k for k in row if k != "primitives_seen"]
            with self.subTest(slug=slug):
                self.assertEqual(keys, [k for k in original if k != "primitives_seen"])
                if "primitives_seen" in row:
                    order = list(row)
                    self.assertEqual(order.index("primitives_seen"), order.index("evidence") + 1)

    def test_a_second_run_changes_nothing_and_does_not_write(self):
        self.run_main("--write-signals")
        before = self.run_main.catalog.read_bytes()
        with mock.patch.object(pathlib.Path, "write_text", side_effect=AssertionError("wrote")):
            code, out, _ = self.run_main("--write-signals")
        self.assertEqual(code, 0)
        self.assertEqual(self.run_main.catalog.read_bytes(), before)
        self.assertIn("0 added, 0 changed, 0 removed, 6 unchanged; 1 not read", out)
        self.assertIn("nothing to write", out)

    def test_only_limits_the_run_to_one_row(self):
        code, out, _ = self.run_main("--write-signals", "--only", "added")
        rows = self.run_main.rows()
        self.assertEqual(rows["added"]["primitives_seen"], ["choice", "noul"])
        self.assertEqual(rows["emptied"]["primitives_seen"], ["score"])
        self.assertIn("1 row(s) with evidence; 1 added", out)

    def test_the_job_summary_says_what_the_field_is(self):
        self.run_main("--write-signals")
        summary = self.run_main.summary.read_text()
        self.assertIn("## Primitive text signals", summary)
        self.assertIn("not a person's reading", summary)
        self.assertNotIn("verified", summary.lower())

    def test_every_read_outcome_has_one_meaning(self):
        # ok: the file's signals; the file, the claim or the repository gone:
        # nothing; no read at all (rate limit, no GitHub repository): unchanged.
        rows = [base_row(slug, primitives_seen=["choice"]) for slug in
                ("ok", "claim-gone", "path-gone", "repo-gone", "skipped", "no-repo")]
        results = [{"slug": "ok", "status": "ok", "primitive_signals": ["noul"]}] + [
            {"slug": slug, "status": slug} for slug in ("claim-gone", "path-gone", "repo-gone", "skipped", "no-repo")
        ]
        out, outcome = vc.apply_signals(rows, results)
        seen = {row["slug"]: row.get("primitives_seen") for row in out}
        self.assertEqual(seen, {"ok": ["noul"], "claim-gone": None, "path-gone": None, "repo-gone": None,
                                "skipped": ["choice"], "no-repo": ["choice"]})
        self.assertEqual(len(outcome["removed"]), 3)
        self.assertEqual(len(outcome["unread"]), 2)

    def test_write_signals_and_discover_do_not_combine(self):
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stderr(io.StringIO()):
                self.run_main("--write-signals", "--discover")


class StatsTest(unittest.TestCase):
    """_stats counts the two layers apart and never adds a signal to a reading."""

    ROWS = [
        {"slug": "both", "question_types": ["noul", "choice"], "primitives_seen": ["score", "noul"]},
        {"slug": "seen", "primitives_seen": ["noul"]},
        {"slug": "read", "question_types": ["score"]},
        {"slug": "none"},
    ]

    def test_signal_only_is_what_the_text_adds_to_the_reading(self):
        self.assertEqual([_stats.signal_only(r) for r in self.ROWS], [["score"], ["noul"], [], []])
        self.assertEqual(
            _stats.primitive_layers(self.ROWS),
            {
                "choice": {"read": 1, "signal_only": 0},
                "score": {"read": 1, "signal_only": 1},
                "noul": {"read": 1, "signal_only": 1},
            },
        )
        self.assertEqual(_stats.PRIMITIVES, vc.PRIMITIVES)

    def test_a_models_reading_of_the_call_site_is_in_neither_layer(self):
        model = {"slug": "m", "question_types": ["noul"], "primitives_seen": ["noul", "score"],
                 "evidence": {"path": "a.py", "matched": ["x"], "model_read_on": "2026-10-24"}}
        person = {**model, "slug": "p", "evidence": {**model["evidence"], "read_on": "2026-10-24"}}
        self.assertTrue(_stats.primitives_by_model(model))
        self.assertFalse(_stats.primitives_by_model(person), "a person's reading of the call site wins")
        self.assertFalse(_stats.primitives_by_model({"slug": "bare", "question_types": ["noul"]}))
        self.assertFalse(_stats.primitives_by_model({"slug": "none", "evidence": model["evidence"]}))
        layers = _stats.primitive_layers([model, person])
        self.assertEqual(layers["noul"], {"read": 1, "signal_only": 0})
        self.assertEqual(layers["score"], {"read": 0, "signal_only": 2})

    def test_a_primitive_claim_is_counted_from_question_types_only(self):
        catalog, retired, patterns, compat, schema = _stats.load()
        signal_everywhere = [dict(e, primitives_seen=["choice", "score", "noul"]) for e in catalog]
        with mock.patch.object(_stats, "load", return_value=(signal_everywhere, retired, patterns, compat, schema)):
            fake = _stats.compute()
        real = _stats.compute()
        self.assertEqual(fake["primitive_rows"], real["primitive_rows"])
        self.assertEqual(fake["primitive_rows_cited"], real["primitive_rows_cited"])
        self.assertEqual(fake["primitive_signal_rows"], len(catalog))
        self.assertEqual(fake["primitive_signal_only_rows"], len(catalog) - real["primitive_rows"])
        for name in vc.PRIMITIVES:
            with self.subTest(primitive=name):
                self.assertEqual(fake["primitive_layers"][name]["read"], real["primitive_layers"][name]["read"])
                # A model's reading is a reading, so never a signal, and is counted in neither.
                by_model = sum(1 for e in catalog if _stats.primitives_by_model(e) and name in e["question_types"])
                self.assertEqual(
                    fake["primitive_layers"][name]["read"] + fake["primitive_layers"][name]["signal_only"] + by_model,
                    len(catalog),
                )


class SurfaceTest(unittest.TestCase):
    """Every surface shows the two layers under their own names, in EN and ZH,
    and never calls the signal verified or checked."""

    LAYERS = {"choice": {"read": 7101, "signal_only": 7102}, "score": {"read": 7103, "signal_only": 7104},
              "noul": {"read": 7105, "signal_only": 7106}}
    NOT_FOR_A_SIGNAL = re.compile(r"verif|confirm|核实|验证|确认调用", re.I)

    def test_the_figure_draws_both_counts_under_each_primitive(self):
        for lang, read, signal, rows_word in (("en", "read by a person", "text signal only", "rows"),
                                               ("zh", "人读确认", "仅文本信号", "条")):
            for theme in ("light", "dark"):
                with self.subTest(lang=lang, theme=theme):
                    svg = build_assets.primitives_svg(lang, theme, self.LAYERS)
                    self.assertEqual(svg.count(f">{read}<"), 3)
                    self.assertEqual(svg.count(f">{signal}<"), 3)
                    for n in range(7101, 7107):
                        self.assertIn(f"{n} {rows_word}", svg)
                    legend = build_assets.STRINGS[lang]["legend"]
                    self.assertTrue(all(line in svg for line in legend))
                    self.assertIsNone(self.NOT_FOR_A_SIGNAL.search(legend[1]))
        self.assertTrue(build_assets.STRINGS["zh"]["legend"][-1].endswith("(机翻)"))

    def test_the_readmes_explain_the_layers_with_the_published_counts(self):
        from readme import strings  # noqa: E402

        stats = _stats.compute()
        catalog, retired, *_ = _stats.load()
        for pack, mark in ((strings.EN, ""), (strings.ZH, " <sub>(机翻)</sub>")):
            with self.subTest(lang=pack["lang_code"]):
                text = build_readme.render(catalog, retired, pack)
                caption = pack["prims_layers"] + mark
                self.assertIn("\n" + caption + "\n", text)
                bullet = pack["verified_primitives"].format(
                    read=stats["primitive_rows"] - stats["primitive_rows_model"],
                    model=stats["primitive_rows_model"],
                    signal=stats["primitive_signal_rows"],
                    signal_only=stats["primitive_signal_only_rows"],
                )
                self.assertIn(f"- {bullet}{mark}\n", text)
                self.assertIn("primitives_seen", caption)
        self.assertLessEqual({"prims_layers", "verified_primitives"}, strings.ZH_MACHINE)

    def test_the_site_keeps_the_layers_apart(self):
        page = (SCRIPTS.parent / "site" / "index.html").read_text()
        self.assertIn("primitiveLayers(e)", page)
        self.assertIn('primPills(prims.read, "p q")', page)
        self.assertIn('primPills(prims.signalOnly, "p sig")', page)
        self.assertNotIn("(e.question_types || []).map", page, "the reading has its own label now")
        self.assertIn("STATS.primitive_layers", page)
        for key in ("prims_read", "prims_signal", "prims_signal_about", "p_read", "p_signal", "p_rows", "p_layers"):
            with self.subTest(key=key):
                self.assertEqual(len(re.findall(rf"\b{key}:", page)), 2, "one string per language")
        for about in re.findall(r'prims_signal_about: "([^"]+)"', page):
            self.assertIsNone(self.NOT_FOR_A_SIGNAL.search(about.replace("确认调用", "")), about)


class ExperimentalTest(unittest.TestCase):
    """experimental_seen (K3, 2026-10-31): Box and the opt-in headers, kept
    apart from the three primitives the catalogue counts."""

    def test_each_feature_as_the_sdks_and_the_wire_spell_it(self):
        cases = {
            '{"type": "box", "instructions": "the dog"}': ["box"],
            "questions = {'dog': {'type': 'box'}}": ["box"],
            '{\\"type\\":\\"box\\"}': ["box"],
            "%{:type => 'box'}": ["box"],
            "const { top, left } = answers.dog.box; x = answers.dog.box.top": ["box"],
            'import { box, noul } from "@typesafe-ai/sdk";\nq = { dog: box("The dog") }': ["box"],
            'import { box as locate } from "@typesafe-ai/sdk";\nlocate("the dog")': ["box"],
            "from typesafe_sdk import Box, Noul\nq = Box(instructions='the dog')": ["box"],
            "from typesafe_sdk.questions import (\n    Choice,\n    Box,\n)\nBox()": ["box"],
            'headers["TypeSafe-Danger-Zone-Images"] = "true"': ["images"],
            "'typesafe-danger-zone-long-context': 'true', 'TypeSafe-Danger-Zone-Images': 'true'": [
                "images", "long-context"],
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(vc.experimental_signals(text), expected)

    def test_what_is_not_box(self):
        for text in (
            "Box(modifier = Modifier.fillMaxSize())",  # Jetpack Compose
            "from gym.spaces import Box\nBox(low=0, high=1)",
            'import { box } from "@typesafe-ai/sdk";',  # imported, never called
            "import type { box } from '@typesafe-ai/sdk'; box()",
            "element.box = rect; style.box",
            "a word: box, a box, the Box",
        ):
            with self.subTest(text=text):
                self.assertEqual(vc.experimental_signals(text), [])

    def test_kept_apart_from_the_primitives(self):
        self.assertNotIn("box", vc.PRIMITIVES)
        self.assertEqual(vc.primitive_signals('{"type": "box"}'), [])
        schema = json.loads((SCRIPTS.parent / "schema" / "entry.schema.json").read_text())
        self.assertEqual(tuple(schema["properties"]["experimental_seen"]["items"]["enum"]), vc.EXPERIMENTAL)

    def test_the_weekly_run_writes_it_after_primitives_seen(self):
        rows = [
            base_row("both", primitives_seen=["noul"]),
            base_row("alone"),
            base_row("dropped", experimental_seen=["images"]),
        ]
        files = Files({
            ("a/both", "HEAD", "src/x.py"): body('a.noul {"type": "box"}'),
            ("a/alone", "HEAD", "src/x.py"): body("TypeSafe-Danger-Zone-Images: true"),
            ("a/dropped", "HEAD", "src/x.py"): body("no header any more"),
        })
        run = MainRun(self, rows, files)
        code, out, _ = run("--write-signals")
        self.assertEqual(code, 0)
        written = run.rows()
        self.assertEqual(list(written["both"])[-2:], ["primitives_seen", "experimental_seen"])
        self.assertEqual(written["both"]["experimental_seen"], ["box"])
        self.assertEqual(list(written["alone"])[-2:], ["evidence", "experimental_seen"])
        self.assertNotIn("experimental_seen", written["dropped"])
        self.assertIn("  - dropped: experimental images", out)
        self.assertTrue(out.strip().splitlines()[-1].endswith("experimental features: 3 row(s) changed"))


class OnlyTheWeeklyRunWritesTest(unittest.TestCase):
    """Like patterns_reviewed the other way round: one script writes the field,
    and it is the script that read the file."""

    WRITE = re.compile(r"""\[\s*["']primitives_seen["']\s*\]\s*=|setdefault\(\s*["']primitives_seen""")

    def test_no_other_script_assigns_the_field(self):
        for path in sorted(SCRIPTS.rglob("*.py")):
            if "tests" in path.parts or path.name == "verify_claims.py":
                continue
            with self.subTest(path=path.name):
                self.assertIsNone(self.WRITE.search(path.read_text(encoding="utf-8")))

    def test_the_writer_never_touches_question_types(self):
        source = (SCRIPTS / "verify_claims.py").read_text()
        self.assertNotRegex(source, r"""\[\s*["']question_types["']\s*\]\s*=""")


if __name__ == "__main__":
    unittest.main()
