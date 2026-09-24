#!/usr/bin/env python3
"""Validate the curated entry points against the live catalog, without dependencies.

Collections keep only an entry slug and bilingual editorial guidance. URLs,
titles and verification records always come from catalog.json. Removing an
entry from the catalog must also remove or replace its collection reference.

Run: python3 scripts/check_collections.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
COLLECTION_IDS = ("first-call", "build", "measured")
COLLECTION_FIELDS = {"id", "title", "title_zh", "description", "description_zh", "entries"}
ENTRY_FIELDS = {"slug", "reason", "reason_zh", "caution", "caution_zh"}


def validate_collections(data: Any, catalog: list[dict]) -> list[str]:
    """Return actionable errors, including malformed data that cannot render."""
    errors: list[str] = []

    def fields(value: Any, expected: set[str], path: str) -> bool:
        if not isinstance(value, dict):
            errors.append(f"{path}: expected an object")
            return False
        for key in sorted(expected - value.keys()):
            errors.append(f"{path}: missing {key}")
        for key in sorted(value.keys() - expected):
            errors.append(f"{path}: unknown field {key}")
        return True

    def text_fields(value: dict, names: set[str], path: str) -> None:
        for name in sorted(names):
            text = value.get(name)
            if not isinstance(text, str) or not text.strip():
                errors.append(f"{path}.{name}: expected non-empty text")
            elif text != text.strip():
                errors.append(f"{path}.{name}: remove surrounding whitespace")
            elif name.endswith("_zh") and not re.search(r"[\u3400-\u9fff]", text):
                errors.append(f"{path}.{name}: expected Chinese text")

    if not fields(data, {"collections"}, "collections.json"):
        return errors
    groups = data.get("collections")
    if not isinstance(groups, list):
        return errors + ["collections.json.collections: expected an array"]

    by_slug = {e["slug"]: e for e in catalog}
    ids: list[str] = []
    selected: set[str] = set()
    for i, group in enumerate(groups):
        path = f"collections[{i}]"
        if not fields(group, COLLECTION_FIELDS, path):
            continue
        text_fields(group, COLLECTION_FIELDS - {"entries"}, path)
        group_id = group.get("id")
        if isinstance(group_id, str):
            ids.append(group_id)
        entries = group.get("entries")
        if not isinstance(entries, list):
            errors.append(f"{path}.entries: expected an array")
            continue
        if not 4 <= len(entries) <= 6:
            errors.append(f"{path}.entries: keep each entry point focused at 4–6 entries")
        seen: set[str] = set()
        for j, entry in enumerate(entries):
            entry_path = f"{path}.entries[{j}]"
            if not fields(entry, ENTRY_FIELDS, entry_path):
                continue
            text_fields(entry, ENTRY_FIELDS, entry_path)
            slug = entry.get("slug")
            if not isinstance(slug, str):
                continue
            if slug in seen:
                errors.append(f"{entry_path}: duplicate slug {slug!r} in collection")
            elif slug in selected:
                errors.append(f"{entry_path}: {slug!r} already appears in another collection")
            seen.add(slug)
            selected.add(slug)
            if slug not in by_slug:
                errors.append(f"{entry_path}: {slug!r} is not in catalog.json")
                continue
            source = by_slug[slug]
            if group_id == "build" and not source.get("has_code"):
                errors.append(f"{entry_path}: build entries must have code to adapt")
            if group_id == "measured" and (
                source.get("kind") != "benchmark" or source.get("official")
            ):
                errors.append(f"{entry_path}: measured entries must be third-party benchmarks")

    if sorted(ids) != sorted(COLLECTION_IDS):
        errors.append("collections: require exactly one first-call, build and measured collection")
    return errors


def main() -> int:
    try:
        data = json.loads((ROOT / "collections.json").read_text())
        catalog = json.loads((ROOT / "catalog.json").read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    errors = validate_collections(data, catalog)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    count = sum(len(group["entries"]) for group in data["collections"])
    print(f"collections: {len(data['collections'])} bilingual entry points, {count} catalog entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
