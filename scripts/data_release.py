#!/usr/bin/env python3
"""The notes for a monthly data release: `catalog-<YYYY-MM>` (D2).

catalog.json changes every day, so a paper, an agent or another list citing
"awesome-jev" cites a moving target. Once a month .github/workflows/
data-release.yml tags main as `catalog-<YYYY-MM>`, named for the month the data
runs to, and publishes a GitHub Release with catalog.json, retired.json and
the entry schema attached: a fixed copy anyone can pin and cite by its URL.

This prints that release's notes: how many rows the catalogue holds, and which
rows arrived and which were retired since the previous `catalog-*` tag, read
from git (`git show <tag>:catalog.json`), so the notes say what changed between
two copies a reader can download. It writes nothing; the workflow creates the
tag and the release. A tag named like the PyPI package's
(`awesome-jev-mcp-v*`) is publish.yml's; these never start it.

Run: python3 scripts/data_release.py --tag catalog-2026-11 [--previous catalog-2026-10]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TAG = re.compile(r"^catalog-\d{4}-(0[1-9]|1[0-2])$")
LISTED = 60
REPO = "kydlikebtc/awesome-jev"


def at(ref: str, path: str, root: pathlib.Path = ROOT) -> list:
    """A JSON array file as it was at a git ref."""
    out = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=root, capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def slugs(rows: list) -> set[str]:
    return {r["slug"] for r in rows if isinstance(r, dict) and "slug" in r}


def listed(names: list[str]) -> str:
    shown = ", ".join(f"`{n}`" for n in names[:LISTED])
    more = len(names) - LISTED
    return shown + (f", and {more} more" if more > 0 else "")


def notes(tag: str, catalog: list, retired: list, *, previous: str = "",
          old_catalog: list | None = None, old_retired: list | None = None) -> str:
    month = tag.removeprefix("catalog-")
    lines = [
        f"Catalogue data to the end of {month}: **{len(catalog)}** rows in `catalog.json` and "
        f"**{len(retired)}** in `retired.json`, with the entry schema they follow. CC0-1.0, like the "
        "repository's data.",
        "",
        f"截至 {month} 月底的目录数据：`catalog.json` 共 **{len(catalog)}** 行，`retired.json` 共 "
        f"**{len(retired)}** 行，并附条目 schema。与仓库数据一样采用 CC0-1.0。",
        "",
    ]
    if previous and old_catalog is not None:
        now, before = slugs(catalog), slugs(old_catalog)
        newly_retired = sorted(slugs(retired) - slugs(old_retired or []))
        added = sorted(now - before)
        lines += [
            f"Since [{previous}](https://github.com/{REPO}/releases/tag/{previous}): "
            f"**{len(added)}** rows added, **{len(newly_retired)}** retired. · "
            f"自 {previous} 以来：新增 **{len(added)}** 行，退役 **{len(newly_retired)}** 行。",
            "",
        ]
        if added:
            lines += [f"Added · 新增: {listed(added)}", ""]
        if newly_retired:
            lines += [f"Retired · 退役: {listed(newly_retired)}", ""]
    else:
        lines += ["The first data release. · 第一个数据版本。", ""]
    lines += [
        "Stars, licences and link checks are as of the weekly refresh before the tag; a row's `evidence` "
        "says who read its cited file and when. Cite this release by its URL; the repository's own "
        "`catalog.json` keeps changing. · 星标、许可证和链接检查以打标签前的每周刷新为准；"
        "每行的 `evidence` 说明谁在何时读过所引文件。引用时请用本版本的链接，仓库里的 `catalog.json` 会持续变化。",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--tag", required=True, help="catalog-YYYY-MM")
    parser.add_argument("--previous", default="", help="the previous catalog-* tag, if there is one")
    args = parser.parse_args(argv)
    for name in filter(None, (args.tag, args.previous)):
        if not TAG.match(name):
            print(f"error: {name!r} is not catalog-YYYY-MM", file=sys.stderr)
            return 2
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    retired = json.loads((ROOT / "retired.json").read_text(encoding="utf-8"))
    old_catalog = old_retired = None
    if args.previous:
        old_catalog, old_retired = at(args.previous, "catalog.json"), at(args.previous, "retired.json")
    sys.stdout.write(notes(args.tag, catalog, retired, previous=args.previous,
                           old_catalog=old_catalog, old_retired=old_retired))
    return 0


if __name__ == "__main__":
    sys.exit(main())
