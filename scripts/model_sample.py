#!/usr/bin/env python3
"""The monthly check of model readings: pick the rows, record the answers (T1).

Since 2026-10-24 a model reads call sites for this catalogue, and every surface
shows those rows as a model's reading (`evidence.model_read_on`). Whether those
readings hold up was never measured. Once a month a person checks a sample:

    python3 scripts/model_sample.py --month 2026-12

prints 20 rows picked at random among those whose call site only a model has
read, never one an earlier month sampled, as a Markdown table to send the
person: each row's link, its cited file, its summary, and the patterns and
primitives the model recorded, with a column to mark agree or disagree. The
pick is seeded by the month, so running it again prints the same rows.

The person's answers go into docs/model-checks.json, one object per month:

    {"month": "2026-12", "by": "croa", "on": "2026-12-04",
     "rows": {"<slug>": "agree", "<slug>": "disagree"},
     "notes": {"<slug>": "why, for a disagreement"}}

`--check` validates that file (lint-style, exit 1 on a problem), and
docs/status.md prints the latest month's count (scripts/_stats.py,
model_checks()). Agreeing with a row is not reading its call site: a row moves
to a person's reading (`evidence.read_on`) only when the person says they read
the file.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import random
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from evidence_url import evidence_url  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKS = ROOT / "docs" / "model-checks.json"
SITE = "https://kydlikebtc.github.io/awesome-jev/"
SIZE = 20
MONTH = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
ANSWERS = ("agree", "disagree")


def model_only(entry: dict) -> bool:
    """The row's call site was read by a model and by no person."""
    evidence = entry.get("evidence")
    return isinstance(evidence, dict) and bool(evidence.get("model_read_on")) and not evidence.get("read_on")


def load_checks(path: pathlib.Path = CHECKS) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get("checks", [])


def sampled_before(checks: list[dict]) -> set[str]:
    return {slug for check in checks for slug in (check.get("rows") or {})}


def pick(catalog: list[dict], month: str, checks: list[dict], size: int = SIZE) -> list[dict]:
    """`size` model-only rows not sampled before, chosen by a generator seeded
    with the month, in slug order."""
    done = sampled_before([c for c in checks if c.get("month") != month])
    pool = sorted((e for e in catalog if model_only(e) and e["slug"] not in done), key=lambda e: e["slug"])
    chosen = random.Random(f"awesome-jev model check {month}").sample(pool, min(size, len(pool)))
    return sorted(chosen, key=lambda e: e["slug"])


def cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def table(rows: list[dict]) -> str:
    lines = [
        "| # | 行 | 引用的文件 | 摘要 | 模式 | 原语 | 同意？ |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for i, e in enumerate(rows, 1):
        url = evidence_url(e)
        path = e["evidence"]["path"]
        cited = f"[{cell(path)}]({url})" if url else f"`{cell(path)}`"
        summary = e.get("summary_zh") or e.get("summary") or ""
        lines.append(
            f"| {i} | [{e['slug']}]({SITE}?lang=zh#{urllib.parse.quote(e['slug'])}) | {cited} | {cell(summary)} | "
            f"{', '.join(e.get('patterns') or []) or '—'} | {', '.join(e.get('question_types') or []) or '—'} |  |"
        )
    return "\n".join(lines) + "\n"


def problems(data: object, slugs: set[str]) -> list[str]:
    """Why docs/model-checks.json is not what this script reads."""
    if not isinstance(data, dict) or not isinstance(data.get("checks"), list):
        return ["docs/model-checks.json: must be an object with a `checks` array"]
    found, months, seen = [], set(), set()
    for i, check in enumerate(data["checks"]):
        where = f"checks[{i}]"
        if not isinstance(check, dict):
            found.append(f"{where}: must be an object")
            continue
        month = check.get("month")
        if not isinstance(month, str) or not MONTH.match(month):
            found.append(f"{where}: month must be YYYY-MM")
        elif month in months:
            found.append(f"{where}: {month} is checked twice")
        months.add(month)
        if not check.get("by"):
            found.append(f"{where}: `by` names the person who checked")
        try:
            dt.date.fromisoformat(str(check.get("on")))
        except ValueError:
            found.append(f"{where}: `on` must be the date of the check, YYYY-MM-DD")
        rows = check.get("rows")
        if not isinstance(rows, dict) or not rows or len(rows) > SIZE:
            found.append(f"{where}: rows must map 1 to {SIZE} slugs to an answer")
            continue
        for slug, answer in rows.items():
            if answer not in ANSWERS:
                found.append(f"{where}: {slug}: answer must be one of {', '.join(ANSWERS)}")
            if slug not in slugs:
                found.append(f"{where}: {slug} is in neither catalog.json nor retired.json")
            if slug in seen:
                found.append(f"{where}: {slug} was sampled in an earlier month")
        seen |= set(rows)
        notes = check.get("notes", {})
        if not isinstance(notes, dict) or set(notes) - set(rows):
            found.append(f"{where}: notes must map sampled slugs to text")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--month", help="YYYY-MM: print that month's sample")
    mode.add_argument("--check", action="store_true", help="validate docs/model-checks.json")
    parser.add_argument("--size", type=int, default=SIZE, help=argparse.SUPPRESS)
    parser.add_argument("--root", type=pathlib.Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    catalog = json.loads((args.root / "catalog.json").read_text(encoding="utf-8"))
    path = args.root / "docs" / "model-checks.json"
    if args.check:
        retired = json.loads((args.root / "retired.json").read_text(encoding="utf-8"))
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"checks": []}
        found = problems(data, {e["slug"] for e in catalog + retired})
        for problem in found:
            print(f"error: {problem}", file=sys.stderr)
        print(f"model checks: {len(data.get('checks') or [])} month(s), {len(found)} problem(s)")
        return 1 if found else 0
    if not MONTH.match(args.month):
        print(f"error: --month {args.month!r} is not YYYY-MM", file=sys.stderr)
        return 2
    rows = pick(catalog, args.month, load_checks(path), args.size)
    sys.stdout.write(table(rows))
    print(f"\n{len(rows)} of the rows only a model has read, picked for {args.month}.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
