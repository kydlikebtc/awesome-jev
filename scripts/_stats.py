"""The one definition of every number this project publishes about itself.

build_readme, build_docs, check_description and counts.py each used to count
"with code" or "dated 2xx records" on their own. They happened to agree. A number
that appears in the README badge, the status page, llms.txt, the site meta tags
and the repository description has to be computed once, or sooner or later two
of those surfaces will disagree and a reader will reasonably trust neither.

Stdlib only, like the rest of scripts/.
"""

from __future__ import annotations

import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent

# A pattern holding less than this share of the catalogue is reported as thin.
# A share rather than a count: ten rows was a signal at 148 entries and is
# noise at 800.
THIN_SHARE = 0.025


def load() -> tuple[list[dict], list[dict], list[dict], dict, dict]:
    catalog = json.loads((ROOT / "catalog.json").read_text())
    retired = json.loads((ROOT / "retired.json").read_text())
    patterns = json.loads((ROOT / "patterns.json").read_text())["patterns"]
    compat = json.loads((ROOT / "compat.json").read_text())
    schema = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
    return catalog, retired, patterns, compat, schema


def link_ok(entry: dict) -> bool:
    """A dated successful HTTP response, not a current availability guarantee."""
    return bool(entry.get("checked")) and 200 <= (entry.get("link_status") or 0) < 300


def compute() -> dict:
    catalog, retired, patterns, compat, schema = load()
    by_pattern = Counter(p for e in catalog for p in e["patterns"])
    swept = [e["checked"] for e in catalog if link_ok(e)]
    siblings = [
        line
        for line in (ROOT / "docs" / "sibling-lists.txt").read_text().splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    return {
        "entries": len(catalog),
        "with_code": sum(1 for e in catalog if e.get("has_code")),
        "official": sum(1 for e in catalog if e.get("official")),
        "link_ok": sum(1 for e in catalog if link_ok(e)),
        "link_unstamped": sum(1 for e in catalog if not link_ok(e)),
        "last_sweep": max(swept) if swept else "never",
        "retired": len(retired),
        # Evidence counts recorded citations, not successful CI checks or
        # executed integrations. CI results do not live in catalog.json.
        "evidence_rows": sum(1 for e in catalog if e.get("evidence")),
        # A row with question_types additionally asserts *which* primitives.
        # Different claims; publishing one number for both would overstate it.
        "primitive_rows": sum(1 for e in catalog if e.get("question_types")),
        "primitive_rows_cited": sum(
            1 for e in catalog if e.get("question_types") and e.get("evidence")
        ),
        "no_licence": sum(1 for e in catalog if e.get("repo_license") == "unknown"),
        "zh_hand": sum(1 for e in catalog if not e.get("zh_machine")),
        "patterns_total": len(patterns),
        "patterns_covered": sum(1 for p in patterns if by_pattern[p["key"]]),
        "empty_kinds": [
            k
            for k in schema["properties"]["kind"]["enum"]
            if not any(e["kind"] == k for e in catalog)
        ],
        "platforms": len(compat["platforms"]),
        "sibling_lists": len(siblings),
        "by_pattern": {p["key"]: by_pattern[p["key"]] for p in patterns},
        "kinds": schema["properties"]["kind"]["enum"],
        "fields": list(schema["properties"]),
        "pattern_keys": [p["key"] for p in patterns],
    }


def pitch(stats: dict) -> str:
    """The one-line description used by the GitHub repository and the site's
    meta tags. One function, so the two cannot drift into different sentences."""
    return (
        f"{stats['entries']} public resources for Jev, TypeSafe AI's System One "
        "decision model, indexed by decision pattern. Source citations, dated link "
        "checks and scheduled call-site text checks; runtime and performance are "
        "not independently tested here. EN/中文, JSON schema and platform compatibility."
    )
