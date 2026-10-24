"""The wire_pattern prompt: what an agent about to wire one decision needs,
in one message.

A coding agent asked to "add a Jev tool-selection gate in TypeScript on
Cloudflare" would otherwise make four calls and still lack two things the
catalogue has: the pattern's own "when not to use it", and a skeleton to start
from. This assembles, from the data it is handed:

* the pattern's description from patterns.json, and a link to its section of
  docs/patterns.md, where "when NOT to use this" is written by hand (that prose
  stays there, the one place it is reviewed);
* compat.json's fields for the surface asked about — model strings, envelope,
  answer field, key variable — or the surfaces to choose from;
* up to five rows filed under the pattern that cite the file their code was
  read in, each linked at HEAD as the site links it (evidence_url.py) and
  dated by a person's reading, or a model's said to be one (query.reading),
  with its caveats and what they mean, and
  whether its own author measured Jev for the use and concluded against it
  (query.is_negative_result, the rule every other surface uses);
* the skeleton from this repository's examples/ for that pattern and language,
  when there is one (examples/index.json), under a comment saying it was never
  executed, or a plain statement that there is none.

server.py registers it and says where the catalogue and the examples index
came from. Standard library only, like query.py; tested without `mcp` in
tests/test_mcp_prompt.py.
"""

from __future__ import annotations

import re
import textwrap

from .evidence_url import evidence_url
from .query import (
    DIRECTION_NOTE,
    DISQUALIFYING,
    PERSON,
    SEARCH_NOTE,
    TEXT_NOTE,
    caveat_glossary,
    compat_lookup,
    is_negative_result,
    reading,
    sort_key,
    when_not_to_use,
)

# How many cited rows the prompt shows; search_examples has the rest.
WIRE_ROWS = 5
EXAMPLES_URL = "https://github.com/kydlikebtc/awesome-jev/tree/main/examples"
UNTESTED = "code-untested"
# Languages whose line comments start with `#`; every other gets `//`.
HASH_COMMENTS = frozenset({"python", "ruby", "shell", "bash", "r", "perl", "elixir"})
# The summary sources a surface marks: the project's own words, and since
# 2026-10-24 a model's (site/catalog-core.mjs MARKED_SOURCES).
MARKED = frozenset({"upstream-description", "upstream-description-stale", "model-written"})
# compat.json fields about which catalogue rows stand for a surface, not about
# wiring it; compatibility() and search_examples(platform=...) carry them.
CATALOGUE_FIELDS = frozenset({"catalog_platforms", "granularity"})


def _kind(entry: dict) -> str:
    """evidence.kind, `call-site` when absent (the schema's default)."""
    return (entry.get("evidence") or {}).get("kind") or "call-site"


def cited_rows(rows: list[dict], key: str, language: str = "") -> tuple[list[dict], bool]:
    """The rows filed under `key` that are examples of calling Jev (no
    disqualifying flag, not a wire-shape citation) and cite a file with a
    link, in sort_key() order: those listing `language` when there are any
    (True), else all of them (False, or True when no language was asked)."""
    found = sorted(
        (
            e
            for e in rows
            if key in e["patterns"]
            and not DISQUALIFYING & set(e.get("flags") or [])
            and _kind(e) != "wire-shape"
            and evidence_url(e)
        ),
        key=sort_key,
    )
    if not language:
        return found, True
    mine = [e for e in found if language in (e.get("languages") or [])]
    return (mine, True) if mine else (found, False)


def pick_skeleton(examples: dict, key: str, language: str = "") -> tuple[dict | None, list[dict]]:
    """(the example to inline, every example for `key`): the one that lists
    `key` earliest among its patterns (then by name) and is in `language`
    when one was asked, or None."""
    mine = sorted(
        (e for e in examples.get("examples") or [] if key in (e.get("patterns") or [])),
        key=lambda e: (e["patterns"].index(key), e.get("name", "")),
    )
    fitting = [e for e in mine if not language or language in (e.get("languages") or [])]
    return (fitting[0] if fitting else None), mine


def _surface(compat: dict, surface: str) -> tuple[list[str], list[str]]:
    """(the section, the names of the surfaces it describes)."""
    lines = ["## The surface", ""]
    names = ", ".join(p["name"] for p in compat["platforms"])
    if not surface:
        return lines + [
            "No surface named. The model string, the request envelope, the answer field and the key's "
            f"variable differ between the surfaces compat.json records ({names}); ask again with "
            "surface=<a name or part of one>, or call compatibility().",
            "",
        ], []
    answer = compat_lookup(compat, surface)
    if "error" in answer:
        return lines + [f"No surface matches {surface!r}. compat.json records: {names}.", ""], []
    for platform in answer["surfaces"]:
        lines += [f"### {platform['name']}", ""]
        for field, value in platform.items():
            if field == "name" or field.endswith("_zh") or field in CATALOGUE_FIELDS:
                continue
            shown = ", ".join(map(str, value)) if isinstance(value, list) else value
            lines.append(f"- {field}: {shown}")
        lines.append("")
    return lines + [
        f"From compat.json, as of {answer['as_of']}. Send only a model string listed above; "
        "check_model_string(model) says which surfaces accept a string.",
        answer["warning"],
        "",
    ], [p["name"] for p in answer["surfaces"]]


def _row_lines(n: int, entry: dict, labels: dict[str, str]) -> list[str]:
    summary = entry["summary"]
    if entry.get("summary_source") in MARKED:
        summary += f" ({labels.get(entry['summary_source'], entry['summary_source'])})"
    languages = f" · {', '.join(entry['languages'])}" if entry.get("languages") else ""
    what = "Example the project ships" if _kind(entry) == "example-only" else "Call site"
    found = reading(entry["evidence"])
    if found is None:
        when = "no reading date recorded"
    else:
        who, day = found
        when = f"read by a person on {day}" if who == PERSON else f"read by a model on {day}, not yet checked by a person"
    lines = [
        f"{n}. **{entry['title']}** (`{entry['slug']}`{languages}) — {summary}",
        f"   {what}: [{entry['evidence']['path']}]({evidence_url(entry)}), {when}",
    ]
    if entry.get("flags"):
        lines.append("   Caveats: " + ", ".join(f"`{f}`" for f in entry["flags"]))
    # A benchmark whose author's direction is unfavourable carries no flag
    # saying so; this line is how a negative result shows here, whichever
    # way the row records it.
    if is_negative_result(entry):
        lines.append(
            f"   Negative result: its own author measured Jev for this use and concluded against it ({DIRECTION_NOTE})"
        )
    return lines


def _rows(rows: list[dict], taxonomy: dict, key: str, language: str) -> list[str]:
    lines = ["## Worked examples", ""]
    found, in_language = cited_rows(rows, key, language)
    if not found:
        return lines + [
            f"No catalogued `{key}` row cites the file its code was read in; "
            f"search_examples(pattern={key!r}) lists every row filed under it.",
            "",
        ]
    shown = found[:WIRE_ROWS]
    where = f" in {language}" if language and in_language else ""
    if not in_language:
        lines += [f"No cited `{key}` row lists {language}; these are in other languages.", ""]
    lines += [
        f"{len(shown)} of the {len(found)} `{key}` rows{where} that cite the file their code was read "
        f"in, official first, then rows with code, then by stars. {SEARCH_NOTE} {TEXT_NOTE}",
        "",
    ]
    labels = {s["key"]: s["en"] for s in taxonomy.get("summary_sources") or []}
    for n, entry in enumerate(shown, 1):
        lines += _row_lines(n, entry, labels)
    lines.append("")
    glossary = caveat_glossary(taxonomy["flags"], (e.get("flags") or [] for e in shown))
    if glossary:
        lines += ["What those caveats mean:", *(f"- `{f}`: {text}" for f, text in glossary.items()), ""]
    return lines


def _header(example: dict, taxonomy: dict, language: str) -> list[str]:
    """The comment put above an inlined skeleton: what the catalogue records
    about running it, any other caveat its row carries, and where it came from."""
    if example.get("status") == "not-run":
        blurb = next((f["blurb_en"] for f in taxonomy["flags"] if f["key"] == UNTESTED), "")
        said = (
            f"awesome-jev: never executed. Its catalogue row carries {UNTESTED}: {blurb} "
            "Treat it as reference code, not verified-working code, and run it before relying on it."
        )
    else:
        said = "awesome-jev: the catalogue records no run of this file. Run it before relying on it."
    # The row's other caveats travel with its code, as they do with every row.
    blurbs = {f["key"]: f["blurb_en"] for f in taxonomy["flags"]}
    for flag in example.get("flags") or []:
        if flag != UNTESTED:
            said += f" It also carries {flag}" + (f": {blurbs[flag]}" if blurbs.get(flag) else ".")
    mark = "#" if language in HASH_COMMENTS else "//"
    wrapped = textwrap.wrap(said, 76, break_on_hyphens=False) + [f"Source: {example.get('url') or example['path']}"]
    return [f"{mark} {line}" for line in wrapped]


def _skeleton(examples: dict | None, taxonomy: dict, key: str, language: str, served: str) -> list[str]:
    lines = ["## Skeleton", ""]
    if examples is None:
        return lines + [f"No examples index could be read ({served}); the examples are at {EXAMPLES_URL}.", ""]
    chosen, mine = pick_skeleton(examples, key, language)
    if not mine:
        return lines + [f"This repository ships no example for `{key}` ({EXAMPLES_URL}).", ""]
    if chosen is None:
        others = ", ".join(f"{e['path']} ({', '.join(e.get('languages') or [])})" for e in mine)
        return lines + [f"No skeleton for `{key}` in {language}. This repository's examples for it: {others}.", ""]
    lang = (chosen.get("languages") or [""])[0]
    code = chosen["code"].rstrip("\n")
    fence = "`" * max(3, 1 + max((len(run) for run in re.findall(r"`+", code)), default=0))
    lines += [
        f"This repository's {chosen['path']}, catalogued as `{chosen['slug']}`; the examples index "
        f"was served {served}.",
        "",
        f"{fence}{lang}",
        *_header(chosen, taxonomy, lang),
        code,
        fence,
        "",
    ]
    rest = [e["path"] for e in mine if e is not chosen]
    if rest:
        lines += [f"Also for `{key}`: {', '.join(rest)}.", ""]
    return lines


def wire_pattern_text(
    rows: list[dict],
    patterns: list[dict],
    compat: dict,
    taxonomy: dict,
    examples: dict | None,
    *,
    pattern: str,
    language: str = "",
    surface: str = "",
    data: str = "",
    served: str = "",
) -> str:
    """wire_pattern's text. `examples` is examples/index.json, or None when no
    source had it; `data` and `served` say where the catalogue and the index
    came from. An unknown pattern answers with the valid keys."""
    key, language, surface = pattern.strip(), language.strip().lower(), surface.strip()
    known = {p["key"]: p for p in patterns}
    if key not in known:
        return "\n".join(
            [
                f"awesome-jev has no decision pattern {key!r}. Valid keys: {', '.join(sorted(known))}.",
                "list_patterns() says what each one means; ask for wire_pattern again with one of them.",
                "",
                f"Data: {data}",
            ]
        )
    about = known[key]
    surface_lines, surfaces = _surface(compat, surface)
    lines = [
        f"# Wiring Jev for {about['en']} (`{key}`)",
        "",
        about["blurb_en"],
        "",
        "Read this pattern's section of docs/patterns.md before building; its \"When not to\" "
        f"paragraph, where the section has one, says when this decision is the wrong tool: {when_not_to_use(key)}",
        "",
        *surface_lines,
        *_rows(rows, taxonomy, key, language),
        *_skeleton(examples, taxonomy, key, language, served),
        "---",
        "",
        f"Wire the `{key}` decision"
        + (f" in {language}" if language else "")
        + (f" on {' or '.join(surfaces)}" if surfaces else "")
        + " from the material above. Read the pattern's section of docs/patterns.md first, carry each row's caveats "
        "into anything borrowed from it, send only a model string compat.json lists for the surface, "
        "and treat every row, and any skeleton, as code nobody here ran.",
        "",
        f"Data: {data}",
    ]
    return "\n".join(lines)
