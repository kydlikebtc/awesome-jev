#!/usr/bin/env python3
"""Generate README.md and README.zh-CN.md from catalog.json.

catalog.json is the only place a fact is edited. Both READMEs are build
artifacts: CI rejects a hand edit to either, and lint's regenerate job rewrites
both on main after every change, so there is no way to hand-patch one language
and leave the other stale.

Layout logic lives in render() exactly once. The two languages differ only by
the string pack passed in, which is what keeps them structurally identical
instead of slowly diverging.

The code lives in the scripts/readme/ package: strings.py (both string packs),
rows.py (paths, labels, one row), sections.py (render(), one function per
README section) and pages.py (docs/by-pattern/ and docs/measured.md). This
file is the command and the names other scripts and tests import from it.
Patch a name where it is read (readme.sections.START_HERE,
readme.sections.ROOT), not here: nothing reads this module's copies, so a patch
here changes nothing.

Readability rules the package enforces, learned the hard way:

* Long `notes` prose only appears in the curated sections, where there are few
  rows and the note *is* the point. In the big pattern tables it would make
  every row several lines tall and destroy scanning, so those carry short flag
  pills instead and the full note lives in catalog.json and on the site.
* Native links do the navigation. An SVG embedded as an image cannot make its
  labels clickable, so the coverage figure is paired with a real pattern index.
* Anything that is really a table is rendered as a table, not as prose or as a
  comma-separated wall of links.

Run: python3 scripts/build_readme.py
"""

from __future__ import annotations

import json
import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_readme_cover  # noqa: E402
import build_readme_week  # noqa: E402
from readme.pages import (  # noqa: E402
    PAGES_DIR,
    render_measured_page,
    render_page,
    write_measured_pages,
    write_pattern_pages,
)
from readme.rows import (  # noqa: E402
    CATALOG,
    FLAG_LABELS,
    FLAG_ORDER,
    KIND_LABELS,
    KIND_ORDER,
    LANG_LABELS,
    PATTERN_LABELS,
    PATTERN_ORDER,
    PATTERNS_FILE,
    RAW,
    REPO,
    REPO_URL,
    RETIRED,
    ROOT,
    SITE,
    anchor,
    entry_list,
    esc,
    group_by_pattern,
    is_negative,
    label,
    page_name,
    site_link,
    sort_key,
    summary_of,
)
from readme.sections import (  # noqa: E402
    INLINE_MEASURED,
    INLINE_PER_PATTERN,
    START_HERE,
    coverage_note,
    entry_points,
    is_measured,
    preview_version,
    render,
    section_nav,
)
from readme.strings import DATA_FILES, EN, REPO_FILES, ZH  # noqa: E402

__all__ = [
    "CATALOG", "DATA_FILES", "EN", "FLAG_LABELS", "FLAG_ORDER", "INLINE_MEASURED", "INLINE_PER_PATTERN",
    "KIND_LABELS", "KIND_ORDER", "LANG_LABELS", "PAGES_DIR", "PATTERN_LABELS",
    "PATTERN_ORDER", "PATTERNS_FILE", "RAW", "REPO", "REPO_FILES", "REPO_URL",
    "RETIRED", "ROOT", "SITE", "START_HERE", "ZH", "anchor", "coverage_note",
    "entry_list", "entry_points", "esc", "group_by_pattern",
    "is_measured", "is_negative", "label", "main", "page_name", "preview_version", "render",
    "render_measured_page", "render_page", "section_nav", "site_link", "sort_key", "summary_of",
    "write_measured_pages", "write_pattern_pages",
]


def main() -> int:
    catalog = json.loads(CATALOG.read_text())
    retired = json.loads(RETIRED.read_text())

    try:
        # Figures first: each set renders whole before any file is written,
        # so a layout error stops the build before it has touched a file.
        build_readme_week.rendered()
        build_readme_cover.write_covers()
        build_readme_week.write_figures()
        (ROOT / "README.md").write_text(render(catalog, retired, EN))
        (ROOT / "README.zh-CN.md").write_text(render(catalog, retired, ZH))
        pages = write_pattern_pages(catalog)
        measured = write_measured_pages(catalog)
    except (KeyError, build_readme_cover.CoverLayoutError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    counts = Counter(pattern for entry in catalog for pattern in entry["patterns"])
    print(f"wrote README.md and README.zh-CN.md from {len(catalog)} entries")
    print(f"wrote {len(pages)} pattern pages under {PAGES_DIR.relative_to(ROOT)}/")
    reports = sum(1 for entry in catalog if is_measured(entry))
    negatives = sum(1 for entry in catalog if is_measured(entry) and is_negative(entry))
    if measured:
        print(
            f"wrote {' and '.join(str(path.relative_to(ROOT)) for path in measured)}: {reports} independent "
            f"measurement reports and negative results ({negatives} negative, listed first), of which the "
            f"READMEs show up to {INLINE_MEASURED}"
        )
    else:
        print("no independent measurement report in the catalogue: no Measured section and no docs/measured.md")
    if counts:
        print(
            "  top patterns: " + ", ".join(f"{k} {v}" for k, v in counts.most_common(5))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
