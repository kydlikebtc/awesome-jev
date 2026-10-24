"""What a row's `observed_thresholds` records, and the rules lint.py keeps on it.

"What threshold should I use?" is the question people building on Jev ask
most, and the catalogue used to answer it with a number copied out of one row's
notes by hand. `observed_thresholds` records instead, per row, the constants
the one file `evidence.path` cites compares a Jev answer with, as that file
writes them (schema/entry.schema.json):

* `question_type`: the primitive whose answer is compared;
* `compares`: which quantity of that answer: a `noul`'s `probability`, a
  `choice`'s or `score`'s `confidence`, one option's `probability`, or a
  `score`'s value (`score`). It names Jev's answer, whatever the project's
  variable is called;
* `value`: the constant;
* `decision`: what the code does, and on which side of the constant;
* `source`: the text in the file that holds the constant. It must be one of
  `evidence.matched`, so the weekly `claims` run re-reads it like every other
  matched string: a project that moves its threshold turns the claim red, and
  a person re-reads the file;
* `read_on`: the day a person read it, and (since 2026-10-24) `model_read_on`
  the day a model did, kept apart. With neither, a script or a model read the
  file and nobody recorded a reading; docs/review-queue.md lists those rows,
  and the model's readings in a section of their own.

An observation, never a recommendation: a threshold is one project's policy for
what being wrong costs it, tuned (if at all) on its own data and model version.
A `noul` probability is not a `choice` confidence, and nothing here moves from
one to the other. `_stats` counts the rows and the lowest and highest constant
per question type and quantity; SKILL.md and examples/README.md state those as
build_docs inline values, never as typed numbers (lint_docs rejects a decimal
range typed outside a marker).

What lint holds (lint.check_thresholds):
* the field needs `evidence`: every source is a string in the cited file;
* not on a `not-jev` row: its answers are another model's, whose calibration
  says nothing about Jev's;
* not on a row citing this repository's own files: examples/ here show this
  repository's starting points, not an observation of anyone's policy;
* each `source` is one of `evidence.matched`, and `value` is written in it;
* the answer the question type returns carries the compared quantity (a `noul`
  answer is a probability alone: ANSWERS);
* a probability or a confidence is at most 1;
* each `read_on` and `model_read_on` is a real date, not in the future.

Stdlib only, like the rest of scripts/.
"""

from __future__ import annotations

import datetime as dt
import re

from sibling_lists import SELF

FIELD = "observed_thresholds"
NOT_JEV = "not-jev"
QUESTION_TYPES = ("choice", "score", "noul")
COMPARES = ("probability", "confidence", "score")
# The quantities each primitive's answer carries, as the vendor documents the
# answer shapes (the figure's PRIMS in build_assets.py says the same; a test
# holds the two together): a noul returns one probability and no confidence,
# a choice a confidence and a probability per option, a score its value, a
# confidence and a probability per level.
ANSWERS = {
    "noul": ("probability",),
    "choice": ("confidence", "probability"),
    "score": ("score", "confidence", "probability"),
}
# Quantities that live between 0 and 1. A score's value is on its levels' scale.
UNIT = ("probability", "confidence")
# A number as source code writes one: 0.7, 0.70, .5, 2.0, 1. Not a digit inside
# an identifier (p_2) or a version (1.13.0).
NUMBER = re.compile(r"(?<![\w.])(?:\d+\.\d*|\.\d+|\d+)(?![\w.])")
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
# A person's reading and a model's (query.READ_ON, query.MODEL_READ_ON).
READINGS = frozenset({"read_on", "model_read_on"})


def recorded(entry: dict) -> list[dict]:
    """The row's thresholds (well-formed items only)."""
    items = entry.get(FIELD)
    return [item for item in items if isinstance(item, dict)] if isinstance(items, list) else []


def sources(entry: dict) -> set[str]:
    """The evidence.matched strings the row's thresholds stand on."""
    return {item["source"] for item in recorded(entry) if isinstance(item.get("source"), str)}


def written_in(value: object, source: str) -> bool:
    """`value` appears in `source` as a number, however it is spelled there."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    return any(abs(float(token) - value) < 1e-9 for token in NUMBER.findall(source))


def own_row(entry: dict) -> bool:
    """The row names this repository (its url or repo)."""
    for candidate in (entry.get("repo"), entry.get("url")):
        match = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", str(candidate or ""))
        if match and f"{match.group(1)}/{match.group(2)}".lower() == SELF.lower():
            return True
    return False


def item_problems(item: dict, where: str, matched: list, today: dt.date) -> list[str]:
    problems = []
    question_type, compares, value, source = (item.get(k) for k in ("question_type", "compares", "value", "source"))
    if isinstance(source, str):
        if source not in matched:
            problems.append(
                f"{where}.source {source!r} is not one of evidence.matched: add it there, so the weekly "
                "claims run re-reads the text the threshold stands on"
            )
        if isinstance(value, (int, float)) and not isinstance(value, bool) and not written_in(value, source):
            problems.append(f"{where}.value {value} is not written in its source {source!r}")
    if compares in COMPARES and compares not in ANSWERS.get(question_type, COMPARES):
        problems.append(f"{where}: a {question_type} answer carries no {compares} to compare with")
    if compares in UNIT and isinstance(value, (int, float)) and not isinstance(value, bool) and value > 1:
        problems.append(f"{where}.value {value}: a {compares} is at most 1")
    for field in READINGS:
        if field not in item:
            continue
        read_on = item[field]
        try:
            day = dt.date.fromisoformat(read_on) if isinstance(read_on, str) and DATE.match(read_on) else None
        except ValueError:
            day = None
        if day is None:
            problems.append(f"{where}.{field} is not a valid date")
        elif day > today:
            problems.append(f"{where}.{field} {read_on} is in the future")
    return problems


def row_problems(entry: dict, today: dt.date) -> list[str]:
    """Every rule `observed_thresholds` breaks on this row (none without the field)."""
    items = entry.get(FIELD)
    if not isinstance(items, list):
        return []  # absent, or a shape the schema reports
    evidence = entry.get("evidence")
    matched = evidence.get("matched") if isinstance(evidence, dict) else None
    if not isinstance(matched, list):
        return [
            f"has {FIELD} but no evidence: each threshold's source is text in the file evidence cites; "
            f"cite the file, or remove {FIELD}"
        ]
    problems = []
    if NOT_JEV in (entry.get("flags") or []):
        problems.append(
            f"has {FIELD} but is flagged {NOT_JEV}: its answers are another model's, whose thresholds say "
            f"nothing about Jev's; remove {FIELD}"
        )
    if own_row(entry):
        problems.append(
            f"has {FIELD} but cites this repository's own file, whose constants are its starting points, "
            f"not an observation; remove {FIELD}"
        )
    for i, item in enumerate(items):
        if isinstance(item, dict):
            problems += item_problems(item, f"{FIELD}[{i}]", matched, today)
    return problems


def rows(catalog: list[dict]) -> list[dict]:
    """Rows recording at least one threshold."""
    return [e for e in catalog if recorded(e)]


def unread(catalog: list[dict]) -> list[dict]:
    """Rows with a threshold nobody has read: no `read_on` and no `model_read_on`."""
    return [e for e in catalog if any(not READINGS & set(item) for item in recorded(e))]


def model_read(catalog: list[dict]) -> list[dict]:
    """Rows whose every threshold has a reading, and some only a model's."""
    return [
        e for e in catalog
        if (items := recorded(e))
        and all(READINGS & set(item) for item in items)
        and any("read_on" not in item for item in items)
    ]


def ranges(catalog: list[dict]) -> dict[str, dict]:
    """Per question type and compared quantity (`noul probability`, ...), in
    QUESTION_TYPES then COMPARES order and only where something is recorded:
    rows, thresholds, and the lowest and highest constant. Never mixes two
    quantities: a noul probability and a choice confidence are not one scale."""
    out: dict[str, dict] = {}
    for question_type in QUESTION_TYPES:
        for compares in COMPARES:
            values, slugs = [], set()
            for entry in catalog:
                for item in recorded(entry):
                    value = item.get("value")
                    if (
                        item.get("question_type") == question_type
                        and item.get("compares") == compares
                        and isinstance(value, (int, float))
                        and not isinstance(value, bool)
                    ):
                        values.append(value)
                        slugs.add(entry.get("slug"))
            if values:
                out[f"{question_type} {compares}"] = {
                    "rows": len(slugs),
                    "thresholds": len(values),
                    "low": min(values),
                    "high": max(values),
                }
    return out


def number(value: object) -> str:
    """A constant as prose prints it: 0.55, 0.9, 2 (never 0.9000000001)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return "—"
    return f"{value:g}"
