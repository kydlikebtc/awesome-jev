#!/usr/bin/env python3
"""Run every generator, so a tree's generated files match its sources.

The sources are catalog.json, retired.json, compat.json, patterns.json,
taxonomy.json, collections.json, watch.json and picker.json, docs/held.txt,
the example code under examples/, and the weekly refresh's snapshots in
history/.
Everything listed in OUTPUTS below is derived from them, whole or in marked
blocks, and is never edited by hand.

Since 2026-09-27 a pull request does not have to carry that output. lint.yml
runs this on every event; on main its `regenerate` job commits the result as
github-actions[bot]. Run it yourself to see what your change will look like,
or to include the regenerated files in a pull request. That is optional, but
if you do include one, check_generated.py requires it to be exactly what this
writes.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/regenerate.py
     python3 scripts/regenerate.py --list    # the output paths present, one per line
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

SCRIPTS = pathlib.Path(__file__).resolve().parent
ROOT = SCRIPTS.parent

# In order, with what each writes. build_readme.py draws the README covers
# before it writes anything, so a cover that no longer fits stops the run
# before a single file has changed.
GENERATORS = (
    (
        "build_readme.py",
        "README.md, README.zh-CN.md, docs/by-pattern/, docs/measured.md, docs/measured.zh-CN.md and the README covers",
    ),
    ("build_assets.py", "the coverage, primitive and primitive-picker figures in docs/assets/"),
    (
        "build_docs.py",
        "the generated values in docs/status.md, docs/sources.md, docs/patterns.md, docs/patterns.zh-CN.md, llms.txt, "
        "skills/awesome-jev/SKILL.md and examples/README.md",
    ),
    ("build_compat.py", "the generated tables in docs/compatibility.md"),
    ("build_review_queue.py", "docs/review-queue.md, the rows a script marks for a person to read"),
    ("build_benchmarks.py", "docs/benchmarks.md and docs/benchmarks.zh-CN.md, the benchmark rows' measurements side by side"),
    ("zh_audit.py", "docs/zh-queue.md, the machine-translated Chinese summaries for a person to replace"),
    ("build_shape.py", "docs/shape.md and docs/shape.zh-CN.md, the catalogue's shape as a dataset"),
    ("build_watch.py", "the What to watch table in docs/status.md, from watch.json"),
    ("build_examples_index.py", "examples/index.json, the examples by decision pattern for the MCP server's prompt"),
)

# Every path those generators write: files they own outright and hand-written
# files carrying their marker blocks alike. check_generated.py compares these
# and the regenerate job commits these; nothing outside them is ever touched.
# .gitattributes marks only the wholly generated ones linguist-generated.
OUTPUTS = (
    "README.md",
    "README.zh-CN.md",
    "docs/by-pattern",
    "docs/measured.md",
    "docs/measured.zh-CN.md",
    "docs/assets",
    "docs/status.md",
    "docs/sources.md",
    "docs/patterns.md",
    "docs/patterns.zh-CN.md",
    "docs/compatibility.md",
    "docs/review-queue.md",
    "docs/benchmarks.md",
    "docs/benchmarks.zh-CN.md",
    "docs/zh-queue.md",
    "docs/shape.md",
    "docs/shape.zh-CN.md",
    "llms.txt",
    "examples/index.json",
    "examples/README.md",
    "skills/awesome-jev/SKILL.md",
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--list", action="store_true", help="print the OUTPUTS present in this tree, one per line, and exit"
    )
    args = parser.parse_args(argv)
    if args.list:
        # Fed to `git add -A --pathspec-from-file=-` by the regenerate job, and
        # git rejects the whole list if one path matches nothing.
        print("\n".join(path for path in OUTPUTS if (ROOT / path).exists()))
        return 0

    for script, writes in GENERATORS:
        print(f"::: {script} — {writes}", flush=True)
        done = subprocess.run([sys.executable, str(SCRIPTS / script)])
        if done.returncode:
            print(
                f"error: {script} failed (exit {done.returncode}); the generators after it did not run",
                file=sys.stderr,
            )
            return done.returncode
    print(f"regenerated with {len(GENERATORS)} generators; outputs: {', '.join(OUTPUTS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
