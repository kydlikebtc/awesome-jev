#!/usr/bin/env python3
"""Generate the tables in docs/compatibility.md from compat.json.

The platform matrix is the repo's most-cited original asset, so it follows the
same rule as the catalog: one machine-readable source, generated presentation.
The site reads the same compat.json, which means the doc and the site cannot
drift apart — the failure mode that would quietly make the matrix useless.

Only the regions between the markers below are rewritten; the prose around
them is hand-written and left alone. One inline value, `<!--n:as_of-->`, is
compat.json's `as_of`: the day a person last read every platform's page. It is
written as that date, never as an age, which would be wrong a day later; the
weekly claims run reports how old it is.

The last table's "Catalogued examples" column is the one part read from
catalog.json: how many rows record in `platforms` one of the values the
surface lists in its `catalog_platforms`, linked to those rows on the site,
and "coarse" where that value does not tell the surface apart from another
route. The count follows the rule the MCP server and lint use
(scripts/platform_values.py), so the page, the site and search_examples agree.

The table between the `alternatives` markers ("Compatible interfaces that are
not Jev") is read from catalog.json alone: every `kind: alternative` row that
records its interface in `wire` (scripts/wire.py), in star-band order, each
with the not-jev caveat and the calibration sentence of taxonomy.json's blurb,
its other caveats, and who has read the cited files: a person, or (since
2026-10-24) only a model, which the table says in words. The *Weights* column
is always there, because open weights and a proxy in front of another
provider's model look the same from the route. A field the cited files do not
show is a dash. The alternative rows that record no interface are
counted under the table, not listed. The site's Compatibility view shows the
same rows (site/catalog-core.mjs wireRows).

Run: python3 scripts/build_compat.py
     python3 scripts/build_compat.py --check    # CI: fail if out of date
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _markers import normalise, replace_block, replace_inline  # noqa: E402
from evidence_url import evidence_url, repository  # noqa: E402
from platform_values import load_query, surface_counts  # noqa: E402
from readme.rows import md_url, star_band, star_label  # noqa: E402
import wire  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMPAT = ROOT / "compat.json"
CATALOG = ROOT / "catalog.json"
TAXONOMY = ROOT / "taxonomy.json"
DOC = ROOT / "docs" / "compatibility.md"
SITE = "https://kydlikebtc.github.io/awesome-jev/"
# The table that also says how many catalogue rows stand for each surface.
EXAMPLES = ("notes", "Catalogued examples")

# Each block is (marker-name, header row, row builder). A dash in the data
# means the surface does not expose that concept, and is printed as-is.
BLOCKS = {
    "models": (
        ["Surface", "Model string to send"],
        lambda p: [link(p), code_list(p["model"])],
    ),
    "yesno": (
        ["Surface", "Type name", "Read the answer from"],
        lambda p: [link(p), code(p["yesno"]), code(p["answer_field"])],
    ),
    "confidence": (
        ["Surface", "Where `choice` / `score` confidence lives"],
        lambda p: [link(p), p["confidence"]],
    ),
    "envelope": (
        ["Surface", "Request shape", "Endpoint"],
        lambda p: [link(p), p["envelope"], code(p["endpoint"])],
    ),
    "env": (
        ["Surface", "Environment variable"],
        lambda p: [link(p), code(p["env"])],
    ),
    "notes": (
        ["Surface", "Worth knowing"],
        lambda p: [link(p), p.get("notes", "—")],
    ),
}


def code(value: str) -> str:
    return "—" if value.strip() == "—" else f"`{value}`"


def code_list(value: str) -> str:
    """Wrap each of several dot-separated names in its own backticks."""
    if value.strip() == "—":
        return "—"
    return " · ".join(f"`{part.strip()}`" for part in value.split("·"))


def link(platform: dict) -> str:
    name = platform["name"]
    if platform.get("official"):
        name += " ⭐"
    url = platform.get("url")
    return f"[{name}]({url})" if url else name


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    out = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(" --- " for _ in header) + "|",
    ]
    out += [
        "| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |"
        for row in rows
    ]
    return out


def examples_cell(platform: dict, counts: dict[str, int]) -> str:
    """How many rows record one of the surface's catalog_platforms, linked to
    them on the site, then those values, and "coarse" when a value does not
    tell this surface apart from another route. A dash when none is listed."""
    values = platform.get("catalog_platforms") or []
    if not values:
        return "—"
    coarse = " (coarse)" if platform.get("granularity") == load_query().COARSE else ""
    link = f"[{counts[platform['id']]}]({SITE}?platform={platform['id']}&lang=en)"
    return f"{link} · {', '.join(f'`{v}`' for v in values)}{coarse}"


# §7, Compatible interfaces that are not Jev: catalog.json's alternative rows
# that record their interface (wire). The labels are this page's; the site
# has its own in both languages.
ALTERNATIVES = "alternatives"
WIRE_COLUMNS = [
    "Row", "Weights", "Answering model", "Endpoint", "Envelope", "Yes/no type", "Yes/no answer key",
    "Confidence key", "Calls Jev to compare", "Published comparison", "Read in", "Caveats",
]
WEIGHT_LABELS = {
    "open": "open weights",
    "closed": "closed: only the project runs it",
    "proxy": "proxy: another provider's hosted model",
}
ENVELOPE_LABELS = {"top-level": "top level", "wrapped": "wrapped in another field"}
DASH = "—"


def wire_code(value: object) -> str:
    """A value copied out of a file, as inline code, or a dash when not recorded."""
    if not isinstance(value, str):
        return DASH
    clean = value.replace("`", "'")
    return f"`{clean}`"


def read_in(entry: dict, record: dict) -> str:
    """Each cited file linked where the site links evidence, then who read them."""
    links = []
    for item in wire.sources(record):
        url = evidence_url({**entry, "evidence": {"path": item["path"]}})
        code = wire_code(item["path"])
        links.append(f"[{code}]({md_url(url)})" if url else code)
    people = sorted({item["read_on"] for item in wire.sources(record) if "read_on" in item})
    if wire.person_read(record):
        who = f"read by a person on {', '.join(people)}"
    elif wire.every_file_read(record):
        # Some file only a model has read (model_read_on): never shown as a person's reading.
        models = sorted({item["model_read_on"] for item in wire.sources(record) if "read_on" not in item})
        who = f"read by a model on {', '.join(models)}, not yet checked by a person"
        if people:
            who = f"partly read by a person on {', '.join(people)}, the rest by a model on {', '.join(models)}"
    else:
        who = "not yet read by a person"
    return f"{' · '.join(links)} ({who})"


def caveats(entry: dict, flag_labels: dict[str, str]) -> str:
    """The not-jev caveat with the calibration sentence, on every row, then the
    row's other flags in taxonomy order, then a negative result."""
    flags = set(entry.get("flags") or [])
    others = [label for key, label in flag_labels.items() if key in flags and key != wire.NOT_JEV]
    if load_query().is_negative_result(entry):
        others.append("negative result, author-stated, not reproduced here")
    text = f"**{flag_labels[wire.NOT_JEV]}**: {wire.CALIBRATION_NOTE}"
    return text + "".join(f" · {label}" for label in others)


def row_repository(entry: dict) -> str | None:
    """owner/name of the repository the cited files are read in, as their links
    spell it (site/catalog-core.mjs wireRepository), or None off GitHub."""
    found = repository(entry.get("repo")) or repository(entry.get("url"))
    return f"{found[0]}/{found[1]}" if found else None


def wire_row(entry: dict, flag_labels: dict[str, str]) -> list[str]:
    record = wire.wire_of(entry)
    # Titles repeat (openjev, OpenJev, open-jev, Open-Jev), so the repository follows.
    found = row_repository(entry)
    title = f"[{entry['title']}]({SITE}?lang=en#{urllib.parse.quote(entry['slug'])})"
    title += f" <sub>{found}</sub>" if found else ""
    band = star_label(entry.get("stars"))
    title += f" {band}" if band else ""
    comparison = record.get(wire.COMPARISON)
    return [
        title,
        WEIGHT_LABELS.get(record.get("weights"), DASH),
        wire_code(record.get("base_model")),
        wire_code(record.get(wire.ENDPOINT)),
        ENVELOPE_LABELS.get(record.get("envelope"), DASH),
        wire_code(record.get("yesno_spelling")),
        wire_code(record.get("answer_field")),
        wire_code(record.get("confidence_field")),
        "yes" if record.get(wire.BASELINE) is True else DASH,
        f"[link]({md_url(comparison)})" if isinstance(comparison, str) else DASH,
        read_in(entry, record),
        caveats(entry, flag_labels),
    ]


def alternatives_block(catalog: list, taxonomy: dict) -> str:
    """The table, in star-band order (never exact stars, never file order),
    then how many alternative rows record no interface."""
    flag_labels = {flag["key"]: flag["en"] for flag in taxonomy["flags"]}
    rows = sorted(wire.wired(catalog), key=lambda e: (-star_band(e.get("stars")), e["title"].lower(), e["slug"]))
    rest = len(wire.unwired(catalog))
    lines = table(WIRE_COLUMNS, [wire_row(e, flag_labels) for e in rows]) if rows else ["No row records its interface yet."]
    if rest == 1:
        tail = ("1 more `alternative` row carries no `wire` record: no one has recorded an interface from its "
                "files yet, or its files show none.")
    else:
        tail = (f"{rest} more `alternative` rows carry no `wire` record: no one has recorded an interface from "
                "their files yet, or their files show none.")
    lines += ["", tail]
    return "\n".join(lines)


def limits_table(limits: list[dict]) -> list[str]:
    rows = [[f"**{item['k']}**", item["v"], item["why"]] for item in limits]
    return table(["", "Limit", "Why it matters"], rows)


def build(
    data: dict | None = None, text: str | None = None, catalog: list | None = None, taxonomy: dict | None = None
) -> str:
    """docs/compatibility.md regenerated from compat.json (or from `data`,
    applied to `text`: lint_docs.py's release rehearsal renders a compat.json
    that does not exist yet), catalog.json (or `catalog`) and taxonomy.json
    (or `taxonomy`)."""
    data = json.loads(COMPAT.read_text()) if data is None else data
    platforms = data["platforms"]
    text = DOC.read_text() if text is None else text
    catalog = json.loads(CATALOG.read_text()) if catalog is None else catalog
    counts = surface_counts(data, catalog)

    for name, (header, row_of) in BLOCKS.items():
        rows = [row_of(p) for p in platforms]
        if name == EXAMPLES[0]:
            header = [*header, EXAMPLES[1]]
            rows = [[*row, examples_cell(p, counts)] for row, p in zip(rows, platforms)]
        body = "\n".join(table(header, rows))
        text = replace_block(text, name, body, where="docs/compatibility.md")

    if "<!-- limits:start -->" in text:
        body = "\n".join(limits_table(data["limits"]))
        text = replace_block(text, "limits", body, where="docs/compatibility.md")

    if f"<!-- {ALTERNATIVES}:start -->" in text:
        taxonomy = json.loads(TAXONOMY.read_text()) if taxonomy is None else taxonomy
        body = alternatives_block(catalog, taxonomy)
        text = replace_block(text, ALTERNATIVES, body, where="docs/compatibility.md")

    return replace_inline(text, {"as_of": data["as_of"]}, where="docs/compatibility.md")



def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail instead of writing")
    args = parser.parse_args()

    rendered = build()
    current = DOC.read_text()

    if rendered == current:
        print("docs/compatibility.md is up to date")
        return 0
    if normalise(rendered) == normalise(current):
        print("docs/compatibility.md is up to date (formatting differs, data matches)")
        return 0
    if args.check:
        print(
            "error: docs/compatibility.md is out of sync with compat.json.\n"
            "Run 'python3 scripts/build_compat.py' and commit the result.",
            file=sys.stderr,
        )
        return 1

    DOC.write_text(rendered)
    data = json.loads(COMPAT.read_text())
    catalog = json.loads(CATALOG.read_text())
    counts = surface_counts(data, catalog)
    print(
        f"wrote docs/compatibility.md from {len(data['platforms'])} platforms "
        f"and {len(data['limits'])} limits; catalogued examples per surface: "
        + ", ".join(f"{key} {n}" for key, n in counts.items())
        + f"; alternatives recording their interface (wire): {len(wire.wired(catalog))}, "
        f"without: {len(wire.unwired(catalog))}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
