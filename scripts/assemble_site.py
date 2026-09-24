#!/usr/bin/env python3
"""Assemble site/ for publishing: copy in the data, and write stats.json.

The same step for the Pages deploy and for a local preview, so the two cannot
differ. The list of runtime files lives here and nowhere else: pages.yml used to
spell out the copies while check_site_data.py kept its own list, which is how
site/compat.json once went unignored while site/catalog.json was.

stats.json is _stats.compute() — the definitions the README badges and the docs
use. The site's headline figures and the live social card both read it, rather
than each recounting "link-verified" in JavaScript.

Run: python3 scripts/assemble_site.py
     python3 -m http.server --directory site      # then open localhost:8000
"""

from __future__ import annotations

import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402

ROOT = _stats.ROOT
SITE = ROOT / "site"

# Every data file the site fetches at runtime, copied verbatim.
RUNTIME_FILES = ("catalog.json", "compat.json", "patterns.json", "taxonomy.json", "collections.json")


def stats_payload() -> dict:
    return _stats.compute()


def main() -> int:
    for name in RUNTIME_FILES:
        shutil.copyfile(ROOT / name, SITE / name)
    (SITE / "stats.json").write_text(json.dumps(stats_payload(), ensure_ascii=False))
    # Pages serves the artifact as-is; .nojekyll stops Jekyll touching it.
    (SITE / ".nojekyll").touch()
    print(f"assembled site/: {', '.join(RUNTIME_FILES)}, stats.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
