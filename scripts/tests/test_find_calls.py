"""Searching a candidate's whole default branch: scripts/find_calls.py.

The weekly upkeep runs it before it declines a held candidate for having no
call site (MAINTAINING.md, rule 1). These tests pin what it reads (code files
and Jev-named scripts, not READMEs, dependencies or symbolic links), the order
it lists them in (the project's own files before tests), its exit codes, and
the clone it makes: one commit deep, over HTTPS, with symbolic links checked
out as plain files. No network: the clone is replaced.
"""

from __future__ import annotations

import contextlib
import io
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import find_calls  # noqa: E402

CALL = 'URL = "https://api.typesafe.ai/v1/systemone"\nclient = TypeSafeClient()\n'


def tree(root: pathlib.Path, files: dict[str, str]) -> None:
    for rel, body in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(self.enterContext(tempfile.TemporaryDirectory()))

    def test_lists_the_projects_files_before_its_tests(self):
        tree(self.root, {
            "tests/test_client.py": CALL,
            "src/client.py": CALL,
            "app/main.ts": 'fetch("https://api.typesafe.ai/v1/systemone")\n',
            "src/util.py": "def choice(options):\n    return options[0]\n",
        })
        hits = find_calls.search(self.root)
        self.assertEqual([path for path, _ in hits], ["app/main.ts", "src/client.py", "tests/test_client.py"])
        self.assertEqual(hits[1][1], ["api.typesafe.ai", "/v1/systemone", "TypeSafeClient"])

    def test_reads_only_the_candidates_own_code(self):
        tree(self.root, {
            "README.md": CALL,
            "docs/example.txt": CALL,
            "node_modules/sdk/index.js": CALL,
            "vendor/lib/client.go": CALL,
            "bin/jev": "#!/bin/sh\ncurl https://api.typesafe.ai/v1/systemone\n",
        })
        self.assertEqual([path for path, _ in find_calls.search(self.root)], ["bin/jev"])

    def test_never_follows_a_symbolic_link(self):
        outside = pathlib.Path(self.enterContext(tempfile.TemporaryDirectory()))
        tree(outside, {"secret.py": CALL, "lib/client.py": CALL})
        os.symlink(outside / "secret.py", self.root / "linked.py")
        os.symlink(outside / "lib", self.root / "lib")
        self.assertEqual(find_calls.search(self.root), [])

    def test_skips_a_file_too_large_to_be_written_by_hand(self):
        tree(self.root, {"dist/bundle.min.js": CALL + "x" * find_calls.MAX_BYTES})
        self.assertEqual(find_calls.search(self.root), [])


class MainTest(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(self.enterContext(tempfile.TemporaryDirectory()))

    def run_main(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = find_calls.main(list(argv))
        return code, out.getvalue(), err.getvalue()

    def test_a_match_prints_its_path_and_strings_and_exits_0(self):
        tree(self.root, {"src/client.py": CALL})
        code, out, _ = self.run_main("acme/tool", "--dir", str(self.root))
        self.assertEqual(code, 0)
        self.assertEqual(out, "src/client.py\tapi.typesafe.ai, /v1/systemone, TypeSafeClient\n")

    def test_no_match_exits_1_and_says_so(self):
        tree(self.root, {"src/client.py": "print('hello')\n"})
        code, out, err = self.run_main("https://github.com/Acme/Tool", "--dir", str(self.root))
        self.assertEqual((code, out), (1, ""))
        self.assertIn("acme/tool: no code file holds a call-site string", err)

    def test_a_failed_clone_exits_2_with_gits_reason(self):
        with mock.patch.object(find_calls, "clone", return_value="fatal: repository not found"):
            code, out, err = self.run_main("acme/gone")
        self.assertEqual((code, out), (2, ""))
        self.assertIn("acme/gone: could not clone it: fatal: repository not found", err)

    def test_searches_what_the_clone_wrote(self):
        def fake_clone(slug, into):
            tree(into, {"index.js": CALL})
            return None

        with mock.patch.object(find_calls, "clone", side_effect=fake_clone):
            code, out, _ = self.run_main("acme/tool")
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("index.js\t"))

    def test_refuses_what_is_not_a_repository(self):
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            find_calls.main(["not a repo"])


class CloneTest(unittest.TestCase):
    def test_clones_one_commit_over_https_without_symbolic_links(self):
        done = subprocess.CompletedProcess([], 0, "", "")
        with mock.patch.object(find_calls.subprocess, "run", return_value=done) as run:
            self.assertIsNone(find_calls.clone("acme/tool", pathlib.Path("/tmp/x")))
        command = run.call_args.args[0]
        self.assertEqual(command[:5], ["git", "-c", "core.symlinks=false", "-c", "protocol.file.allow=never"])
        self.assertIn("--depth", command)
        self.assertEqual(command[command.index("--depth") + 1], "1")
        self.assertEqual(command[-3:], ["--", "https://github.com/acme/tool.git", "/tmp/x"])
        self.assertEqual(run.call_args.kwargs["env"]["GIT_TERMINAL_PROMPT"], "0")

    def test_reports_gits_last_line(self):
        done = subprocess.CompletedProcess([], 128, "", "Cloning...\nfatal: repository 'x' not found\n")
        with mock.patch.object(find_calls.subprocess, "run", return_value=done):
            self.assertEqual(find_calls.clone("acme/gone", pathlib.Path("/tmp/x")), "fatal: repository 'x' not found")

    def test_a_clone_that_hangs_is_a_failure(self):
        with mock.patch.object(find_calls.subprocess, "run", side_effect=subprocess.TimeoutExpired("git", 1)):
            self.assertIn("no answer", find_calls.clone("acme/slow", pathlib.Path("/tmp/x")))


if __name__ == "__main__":
    unittest.main()
