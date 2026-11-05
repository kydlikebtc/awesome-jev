"""The site's link-preview tags are written at deploy, never committed (I01).

They quote the catalogue size, so while build_docs.py kept them in git every
pull request that added a row also had to carry a changed site/index.html. Git
now holds a placeholder; `assemble_site.py --deploy` writes the tags into the
Pages artifact, and check_site_data.py holds each stage to its own state.
"""

from __future__ import annotations

import contextlib
import io
import json
import pathlib
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import _stats
import assemble_site
import build_docs
import check_site_data
from _markers import read_block

INDEX = ROOT / "site" / "index.html"


def outside_meta(text: str) -> str:
    head, _, rest = text.partition("<!-- meta:start -->")
    return head + rest.partition("<!-- meta:end -->")[2]


class CommittedIndexTest(unittest.TestCase):
    def test_git_holds_only_the_placeholder(self):
        text = INDEX.read_text()
        self.assertEqual(assemble_site.meta_body(text), assemble_site.META_PLACEHOLDER)
        entries = len(json.loads((ROOT / "catalog.json").read_text()))
        self.assertNotIn(str(entries), read_block(text, "meta", where="site/index.html"))
        self.assertNotIn("og:description", text)

    def test_build_docs_no_longer_touches_the_site(self):
        self.assertNotIn(INDEX, build_docs.render())
        self.assertFalse(hasattr(build_docs, "meta_block"))

    def test_placeholder_is_a_valid_html5_comment(self):
        placeholder = assemble_site.META_PLACEHOLDER
        self.assertTrue(placeholder.startswith("<!-- ") and placeholder.endswith(" -->"))
        self.assertNotIn("--", placeholder[4:-3])


class MetaProblemTest(unittest.TestCase):
    stats = {"entries": 1207}

    def filled(self, stats=None):
        return assemble_site.fill_meta(INDEX.read_text(), stats or self.stats)

    def test_placeholder_is_right_in_git_and_wrong_for_a_deploy(self):
        text = INDEX.read_text()
        self.assertIsNone(check_site_data.meta_problem(text, self.stats, deploy=False))
        self.assertIn("--deploy", check_site_data.meta_problem(text, self.stats, deploy=True))

    def test_filled_tags_are_right_for_a_deploy_and_wrong_in_git(self):
        text = self.filled()
        self.assertIsNone(check_site_data.meta_problem(text, self.stats, deploy=True))
        self.assertIn("git checkout", check_site_data.meta_problem(text, self.stats, deploy=False))

    def test_stale_tags_fail_a_deploy(self):
        # Within the same hundred the description is unchanged; the exact
        # count in the image alt still has to be current.
        stale = self.filled({"entries": 1206})
        self.assertIsNotNone(check_site_data.meta_problem(stale, self.stats, deploy=True))

    def test_deployed_description_is_the_public_pitch(self):
        pitch = _stats.pitch_public(self.stats).replace("'", "&#x27;")
        text = self.filled()
        self.assertIn(f'<meta name="description" content="{pitch}" />', text)
        self.assertIn(f'<meta property="og:description" content="{pitch}" />', text)
        self.assertIn("1207 public resources", text)


class AssembleTest(unittest.TestCase):
    """assemble_site.main() and check_site_data.main() against a scratch copy."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = pathlib.Path(tmp.name)
        (self.root / "site").mkdir()
        for name in assemble_site.RUNTIME_FILES:
            (self.root / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, self.root / name)
        self.index = self.root / "site" / "index.html"
        shutil.copyfile(INDEX, self.index)
        for module in (assemble_site, check_site_data):
            for name, value in (("ROOT", self.root), ("SITE", self.root / "site")):
                if hasattr(module, name):
                    patcher = patch.object(module, name, value)
                    patcher.start()
                    self.addCleanup(patcher.stop)

    def run_main(self, main, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(argv)
        return code, out.getvalue() + err.getvalue()

    def test_plain_assemble_leaves_the_tracked_file_alone(self):
        before = self.index.read_text()
        code, _ = self.run_main(assemble_site.main, [])
        self.assertEqual(code, 0)
        self.assertEqual(self.index.read_text(), before)
        code, out = self.run_main(check_site_data.main, [])
        self.assertEqual(code, 0, out)
        self.assertIn("placeholder", out)
        # A plain assemble is not a deployable site.
        code, out = self.run_main(check_site_data.main, ["--deploy"])
        self.assertEqual(code, 1)

    def test_deploy_fills_only_the_meta_block(self):
        before = self.index.read_text()
        code, out = self.run_main(assemble_site.main, ["--deploy"])
        self.assertEqual(code, 0, out)
        after = self.index.read_text()
        self.assertEqual(outside_meta(after), outside_meta(before))
        stats = _stats.compute()
        self.assertEqual(assemble_site.meta_body(after), " ".join(assemble_site.meta_block(stats).split()))
        self.assertIn("no count in the description", out)
        self.assertIn(f"{stats['entries']} in the image alt", out)
        code, out = self.run_main(check_site_data.main, ["--deploy"])
        self.assertEqual(code, 0, out)
        # And the filled file is exactly what must never be committed.
        code, out = self.run_main(check_site_data.main, [])
        self.assertEqual(code, 1)
        self.assertIn("git checkout -- site/index.html", out)

    def test_deploy_twice_is_idempotent(self):
        self.run_main(assemble_site.main, ["--deploy"])
        once = self.index.read_text()
        self.run_main(assemble_site.main, ["--deploy"])
        self.assertEqual(self.index.read_text(), once)


class PagesWiringTest(unittest.TestCase):
    def test_pages_assembles_and_checks_in_deploy_mode(self):
        text = (ROOT / ".github" / "workflows" / "pages.yml").read_text()
        self.assertIn("run: python3 scripts/assemble_site.py --deploy\n", text)
        self.assertIn("run: python3 scripts/check_site_data.py --deploy\n", text)

    def test_pages_rebuilds_when_a_script_it_runs_changes(self):
        # assemble_site.py now writes the meta tags with _markers.py, so a
        # change there must redeploy the site like a change to _stats.py does.
        # Followed through every local import: _stats.py imports classify.py,
        # whose rules feed counts in the site's stats.json.
        import ast

        text = (ROOT / ".github" / "workflows" / "pages.yml").read_text()
        paths = text.split("    paths:\n", 1)[1].split("\n  workflow_dispatch:", 1)[0]
        local = set()
        todo = ["assemble_site", "check_site_data", "render_images"]
        while todo:
            script = todo.pop()
            if script in local:
                continue
            local.add(script)
            for node in ast.walk(ast.parse((ROOT / "scripts" / f"{script}.py").read_text())):
                names = (
                    [alias.name for alias in node.names] if isinstance(node, ast.Import)
                    else [node.module] if isinstance(node, ast.ImportFrom) and node.module
                    else []
                )
                todo.extend(name for name in names if (ROOT / "scripts" / f"{name}.py").exists())
        self.assertIn("_markers", local)
        self.assertIn("classify", local)
        for name in sorted(local):
            self.assertIn(f'      - "scripts/{name}.py"\n', paths, name)

    def test_metadata_no_longer_commits_the_site(self):
        text = (ROOT / ".github" / "workflows" / "metadata.yml").read_text()
        add = next(line for line in text.splitlines() if "git add" in line)
        self.assertNotIn("site/index.html", add)

    def test_metadata_regenerates_with_every_generator(self):
        # Its own list of generators would miss one added to regenerate.py,
        # and the strict lint it dispatches after landing would then go red.
        import regenerate

        text = (ROOT / ".github" / "workflows" / "metadata.yml").read_text()
        self.assertIn("          python3 scripts/regenerate.py\n", text)
        for script, _ in regenerate.GENERATORS:
            self.assertNotIn(f"          python3 scripts/{script}\n", text)
        add = next(line for line in text.splitlines() if "git add" in line)
        for output in regenerate.OUTPUTS:
            self.assertTrue(
                output in add.split() or output.split("/", 1)[0] in add.split(), f"metadata.yml does not stage {output}"
            )


if __name__ == "__main__":
    unittest.main()
