"""scripts/snapshot_traffic.py keeps GitHub's 14 days of repository traffic in
history/traffic/ when a TRAFFIC_TOKEN secret exists, and does nothing without
one (since 2026-10-24)."""

from __future__ import annotations

import contextlib
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import snapshot_traffic  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
ANSWERS = {
    "traffic/views?per=day": {"count": 40, "uniques": 12, "views": [{"timestamp": "2026-10-20T00:00:00Z", "count": 40, "uniques": 12}]},
    "traffic/clones?per=day": {"count": 6, "uniques": 3, "clones": []},
    "traffic/popular/referrers": [{"referrer": "github.com", "count": 20, "uniques": 8},
                                  {"referrer": "news.ycombinator.com", "count": 9, "uniques": 7}],
    "traffic/popular/paths": [{"path": "/kydlikebtc/awesome-jev", "title": "awesome-jev", "count": 30, "uniques": 10}],
}


class SnapshotTest(unittest.TestCase):
    def run_main(self, *, token: str | None, refuse: str = "", date: str = "2026-10-28"):
        def fetch(path: str, used: str):
            self.assertEqual(used, token)
            endpoint = path.split("/repos/kydlikebtc/awesome-jev/", 1)[1]
            return (403, None) if endpoint == refuse else (200, ANSWERS[endpoint])

        environ = {"GITHUB_REPOSITORY": "kydlikebtc/awesome-jev", **({"TRAFFIC_TOKEN": token} if token is not None else {})}
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            out = io.StringIO()
            with mock.patch.dict(os.environ, environ, clear=True), \
                    mock.patch.object(snapshot_traffic, "ROOT", root), \
                    mock.patch.object(snapshot_traffic, "fetch", side_effect=fetch) as fetched, \
                    mock.patch.object(snapshot_traffic._github, "step_summary"), \
                    contextlib.redirect_stdout(out):
                code = snapshot_traffic.main(["--date", date])
            files = {p.relative_to(root).as_posix(): json.loads(p.read_text()) for p in root.rglob("*.json")}
            return code, out.getvalue(), files, fetched.call_count

    def test_without_the_secret_nothing_is_asked_or_written(self):
        for token in (None, "", "  "):
            with self.subTest(token=token):
                code, out, files, asked = self.run_main(token=token)
                self.assertEqual((code, files, asked), (0, {}, 0))
                self.assertIn("no TRAFFIC_TOKEN", out)

    def test_with_it_the_four_answers_are_kept_under_their_names(self):
        code, out, files, asked = self.run_main(token="secret")
        self.assertEqual((code, asked), (0, 4))
        snapshot = files["history/traffic/2026-10-28.json"]
        self.assertEqual(list(snapshot), ["generated", "about", "date", "repository", "views", "clones", "referrers", "paths"])
        self.assertEqual(snapshot["views"], ANSWERS["traffic/views?per=day"])
        self.assertEqual(snapshot["referrers"][1]["referrer"], "news.ycombinator.com")
        self.assertEqual(snapshot["date"], "2026-10-28")
        self.assertIn("40 views (12 unique), 6 clones (3 unique); top referrers: github.com 20", out)

    def test_a_refused_endpoint_writes_nothing_and_says_why(self):
        code, out, files, _ = self.run_main(token="secret", refuse="traffic/popular/paths")
        self.assertEqual((code, files), (1, {}))
        self.assertIn("paths: token lacks Administration: read", out)

    def test_the_snapshot_never_lands_beside_the_count_snapshots(self):
        # snapshot_stats.load_history() reads history/*.json; these live a level down.
        self.assertEqual(snapshot_traffic.DIR.as_posix(), "history/traffic")


class WorkflowTest(unittest.TestCase):
    def test_the_weekly_refresh_runs_it_before_the_commit_that_stages_history(self):
        text = (ROOT / ".github" / "workflows" / "metadata.yml").read_text(encoding="utf-8")
        step = text.index("- name: Keep a dated snapshot of the repository's traffic")
        commit = text.index("- name: Rebuild everything generated from those facts, and commit it here")
        self.assertLess(step, commit)
        block = text[step:commit]
        self.assertIn("continue-on-error: true", block)
        self.assertIn("TRAFFIC_TOKEN: ${{ secrets.TRAFFIC_TOKEN }}", block)
        self.assertIn("python3 scripts/snapshot_traffic.py", block)
        self.assertRegex(text[commit:], r"git add -A [^\n]* history\n")


if __name__ == "__main__":
    unittest.main()
