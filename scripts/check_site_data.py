#!/usr/bin/env python3
"""Verify site/catalog.json matches the catalog at the repo root.

The Pages job copies catalog.json into site/ at build time. This guards against
publishing a site that reads a stale or truncated copy — the failure mode where
the README says 40 entries and the site quietly shows 12.

It also holds site/index.html's link-preview block to one of two states. In git
(and after a plain assemble) it must be the placeholder, so a catalogue number
can never be committed there again; after `assemble_site.py --deploy` it must be
exactly the tags the current stats produce, so Pages cannot publish a page whose
link preview is missing or stale.

And it holds the files published for agents to what the catalogue gives:
site/llms.txt to llms.txt with its values refilled, and site/api/v1/ to a
rebuild from site/catalog.json, with each pattern file holding as many rows as
stats.json's by_pattern counts and the index listing exactly patterns.json's
keys (scripts/site_api.py). The plain pages (scripts/site_pages.py: one per
pattern, what's new, the feeds, the sitemap) are held to a rebuild the same
way, and none may be missing or left over.

Run: python3 scripts/check_site_data.py
     python3 scripts/check_site_data.py --deploy    # pages.yml, after assemble --deploy
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import site_api  # noqa: E402
import site_pages  # noqa: E402
from assemble_site import (  # noqa: E402
    META_PLACEHOLDER, PUBLISHED, ROOT, RUNTIME_FILES, SITE_URL, meta_block, meta_body, page_files, stats_payload,
)
from check_collections import validate_collections  # noqa: E402

# The site renders these fields unconditionally; a missing one is a blank cell.
REQUIRED = ("slug", "title", "summary", "summary_zh", "url", "kind", "patterns")


def meta_problem(index_html: str, stats: dict, *, deploy: bool) -> str | None:
    """Why site/index.html's `meta` block is wrong for this stage, or None."""
    body = meta_body(index_html)
    if deploy:
        if body != " ".join(meta_block(stats).split()):
            return (
                "site/index.html's link-preview tags are missing or stale for a deploy; "
                "run 'python3 scripts/assemble_site.py --deploy' first"
            )
        return None
    if body != META_PLACEHOLDER:
        return (
            "site/index.html's meta block must hold only the placeholder "
            f"{META_PLACEHOLDER!r}: the link-preview tags are written at deploy, never "
            "committed. If you ran 'assemble_site.py --deploy' locally, restore it with "
            "'git checkout -- site/index.html'"
        )
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="require the link-preview tags written by assemble_site.py --deploy",
    )
    args = parser.parse_args(argv)
    current = stats_payload()

    for name in RUNTIME_FILES:
        copy = ROOT / "site" / name
        if not copy.exists():
            print(f"error: site/{name} is missing; the Pages job should copy it in", file=sys.stderr)
            return 1
        if name == "llms.txt":
            # Published with its inline values refilled from the current stats.
            if copy.read_text() != site_api.llms_text((ROOT / name).read_text(), current):
                print(f"error: site/{name} is not {name} with current values; run assemble_site.py", file=sys.stderr)
                return 1
            print(f"site/{name} is {name} with its values refilled from _stats.compute()")
            continue
        if json.loads((ROOT / name).read_text()) != json.loads(copy.read_text()):
            print(f"error: site/{name} differs from {name}", file=sys.stderr)
            return 1
        print(f"site/{name} matches {name}")

    # stats.json is derived, not copied, so it is compared with a recompute.
    stats = ROOT / "site" / "stats.json"
    if not stats.exists() or json.loads(stats.read_text()) != stats_payload():
        print("error: site/stats.json is missing or stale; run assemble_site.py", file=sys.stderr)
        return 1
    print("site/stats.json matches _stats.compute()")

    problem = meta_problem((ROOT / "site" / "index.html").read_text(), stats_payload(), deploy=args.deploy)
    if problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    print(
        "site/index.html carries the current link-preview tags"
        if args.deploy
        else "site/index.html carries the link-preview placeholder, as committed"
    )

    catalog = json.loads((ROOT / "site" / "catalog.json").read_text())
    patterns = json.loads((ROOT / "site" / "patterns.json").read_text())["patterns"]
    problems = site_api.api_problems(
        ROOT / "site", catalog, patterns, current,
        site_url=SITE_URL, published=PUBLISHED,
    )
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    print(
        f"site/{site_api.INDEX} and {len(patterns)} pattern file(s) match a rebuild from site/catalog.json; "
        "each holds as many rows as stats.json's by_pattern counts"
    )

    problems = site_pages.page_problems(ROOT / "site", page_files())
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    print(
        f"site/{site_pages.PATTERN_DIR}/ and {', '.join(site_pages.TOP_FILES)} match a rebuild "
        "from the published files"
    )

    collections = json.loads((ROOT / "site" / "collections.json").read_text())
    errors = validate_collections(collections, catalog)
    if errors:
        for error in errors:
            print(f"error: site/{error}", file=sys.stderr)
        return 1
    print("site/collections.json references valid catalog entries")

    for entry in catalog:
        missing = [field for field in REQUIRED if field not in entry]
        if missing:
            print(
                f"error: entry {entry.get('slug', '?')!r} is missing {missing} "
                "which the site needs to render",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
