#!/usr/bin/env python3
"""The per-pattern JSON files the site serves to agents: site/api/v1/.

catalog.json runs to megabytes (docs/method.md dates its size), and no agent
reads it whole. Without the MCP server an agent's natural way in is one file
per decision pattern, so the Pages deploy writes

  api/v1/index.json             every pattern: key, name, description, how many
                                rows file under it, its file's URL and size,
                                plus links to the other published files
  api/v1/patterns/<key>.json    every row filed under that pattern

beside the site. A row is shaped exactly as the MCP server's search returns it
(`compact()` in src/awesome_jev_mcp/query.py) and in the same order
(`sort_key()`), so an agent gets one shape from either route. query.py is
standard library only and is loaded by its path: importing its package would
also run data.py, which the site does not need. pages.yml lists the file among
the scripts whose change redeploys the site (tests/test_site_api.py).

Nothing is filtered out. A pattern file holds as many rows as stats.json's
`by_pattern` counts, caveated rows included with their `caveats`; the index and
every file name the caveats that mean a row is not an example of calling Jev,
which the MCP server leaves out by default. The only date is the catalogue's
own (`last_sweep`), never the time of the build, so two deploys of the same
data serve the same bytes.

assemble_site.py writes the files (site/api/ is gitignored, like every other
copy under site/), and check_site_data.py holds them to a rebuild and to
stats.json before Pages publishes anything. Within v1 fields may be added; one
removed or renamed would be v2, at a new path.

llms_text() is here too: the llms.txt Pages serves, with its inline values
refilled as build_docs.py would. The committed file can trail a merge by the
regenerate job's commit, and a push by that bot starts no Pages run.
"""

from __future__ import annotations

import importlib.util
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _markers import replace_inline  # noqa: E402
from build_docs import inline_values  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPOSITORY = "https://github.com/kydlikebtc/awesome-jev"

# Files this module loads by path rather than by import, relative to the
# repository. pages.yml must list each (tests/test_site_api.py).
BY_PATH = ("src/awesome_jev_mcp/query.py",)

API_VERSION = 1
API_DIR = f"api/v{API_VERSION}"
INDEX = f"{API_DIR}/index.json"

ABOUT = (
    "The awesome-jev catalogue split by decision pattern, for agents that cannot read "
    "catalog.json whole. Each pattern file lists every row filed under that pattern (a row "
    "can sit under several), shaped and ordered as the awesome-jev MCP server's "
    "search_examples returns them: official rows first, then rows with code, then by stars. "
    "A row whose caveats include one of not_examples is not an example of deciding with Jev "
    "(not-jev: it never calls Jev; shadow-mode-only: nothing Jev returns reaches a user-visible decision); "
    "the MCP server leaves such rows out by default, these files keep them, caveats attached, "
    "so the counts match the catalogue. last_sweep is the newest dated successful link check in the catalogue, "
    "not the time these files were built. Within api_version 1 fields may be added; none "
    "is removed or renamed."
)


def load_query():
    """src/awesome_jev_mcp/query.py, by path (see the module docstring)."""
    name = "awesome_jev_query"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, ROOT / BY_PATH[0])
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


query = load_query()


def pattern_path(key: str) -> str:
    return f"{API_DIR}/patterns/{key}.json"


def dump(payload: dict, *, pretty: bool = False) -> str:
    """One file's text. Pattern files are compact, since an agent pays for
    every byte; the index is small enough to indent for a person."""
    if pretty:
        return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"


def pattern_rows(catalog: list[dict], key: str) -> list[dict]:
    """The MCP server's awesome-jev://patterns/{key} rows, one definition."""
    return query.pattern_rows(catalog, key)


def api_files(
    catalog: list[dict], patterns: list[dict], stats: dict, *, site_url: str, published: tuple[str, ...]
) -> dict[str, str]:
    """Every file under site/api/v1/: path relative to site/ → text.
    `published` names the other files the site serves, linked from the index."""
    files: dict[str, str] = {}
    listed = []
    not_examples = sorted(query.DISQUALIFYING)
    for item in query.pattern_counts(catalog, patterns)["patterns"]:
        key = item["key"]
        rows = pattern_rows(catalog, key)
        text = dump(
            {
                "api_version": API_VERSION,
                "pattern": key,
                "name": item["name"],
                "description": item["description"],
                "last_sweep": stats["last_sweep"],
                "examples": len(rows),
                "not_examples": not_examples,
                "note": query.SEARCH_NOTE,
                "text_note": query.TEXT_NOTE,
                "entries": rows,
            }
        )
        files[pattern_path(key)] = text
        listed.append({**item, "url": site_url + pattern_path(key), "bytes": len(text.encode("utf-8"))})
    files[INDEX] = dump(
        {
            "api_version": API_VERSION,
            "last_sweep": stats["last_sweep"],
            "entries": stats["entries"],
            "retired": stats["retired"],
            "about": ABOUT,
            "not_examples": not_examples,
            "note": query.PATTERNS_NOTE,
            # What each pattern's `evidence` counts are: reports counted, not a
            # verdict (list_patterns carries the same note).
            "evidence_note": query.EVIDENCE_NOTE,
            "patterns": listed,
            "files": {name: site_url + name for name in published},
            "repository": REPOSITORY,
        },
        pretty=True,
    )
    return files


def write_api(site: pathlib.Path, files: dict[str, str]) -> None:
    """Replace site/api/v1/ with `files`, so a pattern that left patterns.json
    leaves no file behind."""
    shutil.rmtree(site / API_DIR, ignore_errors=True)
    for rel, text in files.items():
        path = site / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def api_problems(
    site: pathlib.Path,
    catalog: list[dict],
    patterns: list[dict],
    stats: dict,
    *,
    site_url: str,
    published: tuple[str, ...],
) -> list[str]:
    """Why site/api/v1/ is not what the catalogue gives, or []: every file a
    rebuild would write and no other, each equal to it once parsed, the index's
    sizes those of the files, the index's keys patterns.json's, and every
    pattern file holding as many rows as stats.json's by_pattern counts."""
    expected = api_files(catalog, patterns, stats, site_url=site_url, published=published)
    base = site / API_DIR
    found = {p.relative_to(site).as_posix() for p in base.rglob("*") if p.is_file()} if base.is_dir() else set()
    problems = [f"site/{rel} is missing; run assemble_site.py" for rel in sorted(set(expected) - found)]
    problems += [
        f"site/{rel} is no pattern in patterns.json; run assemble_site.py, which rewrites site/{API_DIR}/ whole"
        for rel in sorted(found - set(expected))
    ]

    served: dict[str, tuple[bytes, object]] = {}
    for rel in sorted(set(expected) & found):
        raw = (site / rel).read_bytes()
        try:
            body = json.loads(raw)
        except ValueError:
            problems.append(f"site/{rel} is not JSON; run assemble_site.py")
            continue
        served[rel] = (raw, body)
        if body != json.loads(expected[rel]):
            problems.append(f"site/{rel} is stale: a rebuild from site/catalog.json differs; run assemble_site.py")

    keys = [p["key"] for p in patterns]
    if INDEX in served:
        index = served[INDEX][1]
        listed = index.get("patterns") if isinstance(index, dict) else None
        listed = listed if isinstance(listed, list) else []
        if [item.get("key") for item in listed if isinstance(item, dict)] != keys:
            problems.append(f"site/{INDEX} does not list patterns.json's keys, in its order")
        for item in listed:
            rel = pattern_path(str(item.get("key"))) if isinstance(item, dict) else ""
            if rel in served and item.get("bytes") != len(served[rel][0]):
                problems.append(
                    f"site/{INDEX} gives {item.get('bytes')} bytes for {item['key']}, "
                    f"but site/{rel} is {len(served[rel][0])} bytes"
                )
    for key in keys:
        rel = pattern_path(key)
        if rel not in served or not isinstance(served[rel][1], dict):
            continue
        rows = served[rel][1].get("entries")
        count = len(rows) if isinstance(rows, list) else 0
        if count != stats["by_pattern"].get(key):
            problems.append(
                f"site/{rel} holds {count} row(s), but by_pattern in stats.json counts "
                f"{stats['by_pattern'].get(key)} under {key}"
            )
    return problems


def llms_text(text: str, stats: dict) -> str:
    """llms.txt with every inline value refilled from `stats`, as build_docs.py
    writes it (llms.txt has inline values only, no blocks; a test holds the
    two equal)."""
    return replace_inline(text, inline_values(stats), where="llms.txt")
