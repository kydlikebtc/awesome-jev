"""A Jev release changes compat.json alone, as the MCP server and the weekly
claims issue see it (I23): check_model_string's hint is built from compat.json,
and the claims issue sums up rows whose cited file only moved its pinned model
version and says how long ago a person read the platform pages. Workflow shell
runs as GitHub runs it — `bash -e` — with a stub `gh`. No network."""

from __future__ import annotations

import contextlib
import io
import json
import os
import pathlib
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "scripts"))

import lint_docs  # noqa: E402
import verify_claims as vc  # noqa: E402
from test_discover_workflow import GH_STUB  # noqa: E402
from test_mcp_caveats import load_server  # noqa: E402
from test_weekly_jobs import WORKFLOWS, run_block, step_lines  # noqa: E402

SMALL = {
    "as_of": "2031-01-01",
    "platforms": [
        {"name": "Vendor", "official": True, "model": "acme-latest · jev-9.1.0", "endpoint": "e", "env": "K"},
        {"name": "Gate A", "model": "acme/jev-9.1 · ~acme/jev", "endpoint": "e", "env": "K"},
        {"name": "Gate B", "model": "jev-9.1.0 (pinned)", "endpoint": "e", "env": "K"},
        {"name": "Gate C", "model": "acme/jev-9.1 · ~acme/jev", "endpoint": "e", "env": "K"},
    ],
    "limits": [],
    "not_model_strings": [{"s": "acme/jev-9", "why": "Nobody documents it."}],
}


class HintTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = load_server()

    def test_the_hint_is_compat_json_and_nothing_else(self):
        with mock.patch.object(self.server, "COMPAT", SMALL):
            answer = self.server.check_model_string(model="acme/jev-9")
        self.assertIs(answer["valid"], False)
        self.assertEqual(
            answer["hint"],
            "The versioned id is jev-9.1.0, with aliases acme-latest. Gateways and SDKs rename it: "
            "acme/jev-9.1 or ~acme/jev on Gate A and Gate C. `acme/jev-9`: Nobody documents it. "
            "Pin a version rather than an alias once you have tuned any threshold.",
        )

    def test_the_real_hint_names_every_string_and_every_refuted_one(self):
        hint = self.server.check_model_string(model="typesafe/jev-1")["hint"]
        for platform in self.server.COMPAT["platforms"]:
            for model in self.server._accepted(platform):
                self.assertIn(model, hint)
        for item in self.server.COMPAT["not_model_strings"]:
            self.assertIn(f"`{item['s']}`: {item['why']}", hint)

    def test_jev_1_14_pin_is_accepted_on_the_documented_native_surface(self):
        answer = self.server.check_model_string(model="jev-1.14.0")
        self.assertIs(answer["valid"], True)
        self.assertEqual(
            [(s["surface"], s["endpoint"], s["env"]) for s in answer["surfaces"]],
            [("TypeSafe API (direct)", "POST /v1/systemone", "TYPESAFE_API_KEY")],
        )

    def test_new_native_pin_keeps_the_previous_pin_and_aliases_valid(self):
        for model in ("jev-1.13.0", "jev-latest", "jev-preview"):
            with self.subTest(model=model):
                answer = self.server.check_model_string(model=model)
                self.assertIs(answer["valid"], True)
                self.assertIn("TypeSafe API (direct)", [s["surface"] for s in answer["surfaces"]])

    def test_native_release_does_not_validate_guessed_gateway_ids(self):
        for model in ("typesafe/jev-1.14", "typesafe-ai/jev-1.14", "jev-1.14"):
            with self.subTest(model=model):
                answer = self.server.check_model_string(model=model)
                self.assertIs(answer["valid"], False)
                self.assertIn("jev-1.14.0", answer["valid_strings"])

    def test_a_release_moves_the_hint_with_compat_json(self):
        released, old = lint_docs.simulated_compat(self.server.COMPAT, "jev-99.0.0")
        with mock.patch.object(self.server, "COMPAT", released):
            hint = self.server.check_model_string(model="typesafe/jev-1")["hint"]
            self.assertIs(self.server.check_model_string(model="jev-99.0.0")["valid"], True)
        self.assertIn("jev-99.0.0", hint)
        # Only compat.json's own prose (its `why` lines) may still name the old
        # version, and lint_docs.py reports that prose in the rehearsal.
        refuted = " ".join(f"`{i['s']}`: {i['why']}" for i in released["not_model_strings"])
        self.assertIn(refuted, hint)
        self.assertNotIn(old, hint.replace(refuted, ""))

    def test_a_remark_in_the_cell_is_not_part_of_the_string(self):
        surfaces = [s["surface"] for s in self.server.check_model_string(model="jev-latest")["surfaces"]]
        remarked = [p["name"] for p in self.server.COMPAT["platforms"] if "jev-latest (" in p["model"]]
        for name in remarked:
            self.assertIn(name, surfaces)
        self.assertFalse([m for m in self.server.check_model_string(model="x")["valid_strings"] if "(" in m])


CLAIMS_STEP = "Open or update an issue when something stops holding"


class ClaimsIssueTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = pathlib.Path(tmp.name)
        stub = self.dir / "bin" / "gh"
        stub.parent.mkdir()
        stub.write_text(GH_STUB)
        stub.chmod(stub.stat().st_mode | stat.S_IXUSR)
        self.lines = step_lines((WORKFLOWS / "claims.yml").read_text(), CLAIMS_STEP)
        self.script = run_block(self.lines).replace("/tmp/", f"{self.dir}/")

    def report(self) -> str:
        """verify_claims.py's real text report on two moved pins and one lost claim."""
        row = {"slug": "a", "url": "https://github.com/o/a", "evidence": {"path": "x.py", "matched": ["jev-1.13", "system_one"]}}
        rows = [row, dict(row, slug="b", url="https://github.com/o/b"),
                dict(row, slug="c", evidence={"path": "x.py", "matched": ["TypeSafeClient"]})]
        with tempfile.TemporaryDirectory() as tmp:
            catalog = pathlib.Path(tmp) / "catalog.json"
            catalog.write_text(json.dumps(rows))
            out = io.StringIO()
            with mock.patch.object(vc, "CATALOG", catalog), mock.patch.object(sys, "argv", ["verify_claims.py"]), \
                 mock.patch.object(vc, "raw_get", return_value='system_one(model="jev-1.14.0")'), \
                 mock.patch.object(vc, "default_branch", return_value="main"), \
                 mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), \
                 contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(vc.main(), 1)
        return out.getvalue()

    def wire_report(self) -> str:
        """The same report on an alternative row whose wire.source file lost its string."""
        row = {"slug": "alt", "kind": "alternative", "url": "https://github.com/o/alt",
               "wire": {"weights": "open", "source": [{"path": "server.py", "matched": ["/v1/systemone"]}]}}
        with tempfile.TemporaryDirectory() as tmp:
            catalog = pathlib.Path(tmp) / "catalog.json"
            catalog.write_text(json.dumps([row]))
            out = io.StringIO()
            with mock.patch.object(vc, "CATALOG", catalog), mock.patch.object(sys, "argv", ["verify_claims.py"]), \
                 mock.patch.object(vc, "raw_get", return_value="@app.post('/v2/decide')"), \
                 mock.patch.object(vc, "default_branch", return_value="main"), \
                 mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), \
                 contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(vc.main(), 1)
        return out.getvalue()

    def run_step(self, claims="0", compat="0", stale="false", age="6", report=None) -> str:
        (self.dir / "report.txt").write_text(self.report() if report is None else report)
        (self.dir / "compat.txt").write_text("11 ok, 0 string-gone, 0 newer-version, 0 unreadable\n")
        env = {
            **os.environ,
            "PATH": f"{self.dir / 'bin'}{os.pathsep}{os.environ['PATH']}",
            "STUB_LOG": str(self.dir / "gh.log"), "STUB_EXISTING": "", "STUB_MISSING": "", "STUB_CURRENT": "",
            "CLAIMS_FAILED": claims, "COMPAT_FAILED": compat, "COMPAT_STALE": stale, "COMPAT_AGE": age,
        }
        done = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-c", self.script],
                              cwd=self.dir, env=env, capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        return (self.dir / "body.md").read_text()

    def test_moved_pins_are_one_line_per_version(self):
        body = self.run_step(claims="1")
        self.assertIn("version-moved: 2 row(s) now pin jev-1.14", body)
        self.assertNotIn("VERSION-MOVED", body)
        self.assertIn("CLAIM-GONE   c", body)
        self.assertIn("--propose-version-rewrite", body)
        self.assertNotIn("compat.json not read lately", body)

    def test_a_wire_source_that_lost_its_strings_is_listed_and_explained(self):
        body = self.run_step(claims="1", report=self.wire_report())
        self.assertIn("CLAIM-GONE   alt  wire.source o/alt@main:server.py no longer contains ['/v1/systemone']", body)
        self.assertIn("a line reading `wire.source`", body)
        self.assertIn("correct\n  `wire`", body)

    def test_an_old_reading_opens_the_issue_with_its_age(self):
        condition = next(line for line in self.lines if line.strip().startswith("if:"))
        self.assertIn("steps.compat.outputs.stale == 'true'", condition)
        self.assertIn("          COMPAT_AGE: ${{ steps.compat.outputs.age }}", self.lines)
        body = self.run_step(stale="true", age="59")
        # Nothing stopped holding: the opening line must not say it did.
        intro = body.split("\n\n", 1)[0]
        self.assertIn("or a reading of the platform pages", intro)
        self.assertIn("### compat.json not read lately", body)
        self.assertIn("A person last read every platform page 59 day(s)", body)
        self.assertNotIn("### Cited call sites", body)

    def test_no_event_value_reaches_the_shell(self):
        self.assertNotIn("github.event", "\n".join(self.lines))


if __name__ == "__main__":
    unittest.main()
