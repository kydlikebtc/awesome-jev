#!/usr/bin/env python3
"""Verify site/catalog.json matches the catalog at the repo root.

The Pages job copies catalog.json into site/ at build time. This guards against
publishing a site that reads a stale or truncated copy — the failure mode where
the README says 40 entries and the site quietly shows 12.

Run: python3 scripts/check_site_data.py
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from assemble_site import ROOT, RUNTIME_FILES, stats_payload  # noqa: E402
from check_collections import validate_collections  # noqa: E402

# The site renders these fields unconditionally; a missing one is a blank cell.
REQUIRED = ("slug", "title", "summary", "summary_zh", "url", "kind", "patterns")


def main() -> int:
    for name in RUNTIME_FILES:
        copy = ROOT / "site" / name
        if not copy.exists():
            print(f"error: site/{name} is missing; the Pages job should copy it in", file=sys.stderr)
            return 1
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

    catalog = json.loads((ROOT / "site" / "catalog.json").read_text())
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
