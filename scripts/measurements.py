"""What a benchmark row's `measurement` holds, and the rules lint.py keeps on it.

A kind: benchmark row may carry `measurement` (schema/entry.schema.json): what
its own author measured, indexed field by field from the author's report — the
task, named datasets, comparators, kinds of metric, n, the model string, when,
whether per-item data is published, whether the protocol was fixed first, and
the author's own `direction`. Nothing in it was measured or reproduced here.
`read_on` dates a person's reading of the report against the fields, and
(since 2026-10-24) `model_read_on` a model's, kept apart; with neither, a
script or a model filled them in and nobody read them back (docs/review-queue.md
lists those rows, and the model's readings in a section of their own).

How a measurement is read — which rows have one, how a direction is shown — is
the MCP package's query.py, loaded by its path as platform_values.py loads it,
so lint, the generated pages and the server read the same thing.
site/catalog-core.mjs applies the same rules on the site.

What lint holds (lint.check_measurement, lint.check_measurement_models):
* a measurement only on a kind: benchmark row;
* `as_of`, or the row's `published`, dates it: model versions move, and a
  measurement is of the model served that day;
* `as_of`, `read_on` and `model_read_on` are real dates, not in the future,
  and nobody read the report before the measurement was taken;
* `model_string` is a string compat.json lists on some surface (a string it
  does not list is left out of the row rather than recorded).

A negative result — a row whose own author measured Jev for its use and
concluded against it — is recorded in exactly one place. A benchmark says so
in `measurement.direction` (unfavourable); a row of any other kind carries the
`negative-result` flag, and lint (negative_flag_problems) holds it there: never
on a benchmark, where the flag and the direction could disagree, and always
with `notes` that say where the conclusion comes from: a link, a pull request
or issue number, or the measurement itself. Every surface derives "negative"
from either through query.is_negative_result().

Stdlib only, like the rest of scripts/.
"""

from __future__ import annotations

import datetime as dt
import re

from platform_values import load_query

KIND = "benchmark"
FIELD = "measurement"
DATED = ("as_of", "read_on", "model_read_on")
NEGATIVE_FLAG = "negative-result"
# What a negative-result row's notes must hold: a link, a pull request or issue
# number, or a word naming what was measured. The words are a floor: a note
# with one can still say little, which a reviewer reads for.
NEGATIVE_NOTE_SOURCE = re.compile(
    r"https?://|\b(?:PR|pull request|issue)\s*#?\d+|#\d+"
    r"|\b(?:measur\w*|recall|accuracy|precision|F1|nDCG|MRR|ECE|Brier|calibrat\w*|latency|cost|tokens?"
    r"|tied|benchmark\w*|scorecard|evaluat\w*)\b",
    re.IGNORECASE,
)


def _date(value: object) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def row_problems(entry: dict, today: dt.date) -> list[str]:
    """Each way one row's measurement breaks a rule that needs no other file."""
    if FIELD not in entry:
        return []
    found: list[str] = []
    if entry.get("kind") != KIND:
        found.append(
            f"has a measurement but kind is {entry.get('kind')!r}: a measurement indexes a benchmark's "
            "own report, so it belongs only on a kind: benchmark row"
        )
    measurement = entry[FIELD]
    if not isinstance(measurement, dict):
        return found  # the schema says what it should be
    if "as_of" not in measurement and not entry.get("published"):
        found.append(
            "has a measurement with no as_of and no published date: give the day the author gives for "
            "the measurement, or the day its results were first committed or posted, as measurement.as_of"
        )
    dates = {}
    for field in DATED:
        if field in measurement:
            parsed = _date(measurement[field])
            if parsed is None:
                found.append(f"measurement.{field} is not a valid date")
            elif parsed > today:
                found.append(f"measurement.{field} {measurement[field]} is in the future")
            else:
                dates[field] = parsed
    for field in DATED[1:]:
        if field in dates and "as_of" in dates and dates[field] < dates["as_of"]:
            found.append(
                f"measurement.{field} {measurement[field]} is before as_of {measurement['as_of']}: nobody "
                "can read the report of a measurement not yet taken"
            )
    return found


def negative_flag_problems(entry: dict) -> list[str]:
    """Each way the negative-result flag on one row breaks its rules."""
    if NEGATIVE_FLAG not in (entry.get("flags") or []):
        return []
    if entry.get("kind") == KIND:
        return [
            f"flagged {NEGATIVE_FLAG} but kind is 'benchmark': a benchmark records its author's conclusion "
            "in measurement.direction (unfavourable) and nowhere else, so the two cannot disagree; remove "
            "the flag"
        ]
    notes = entry.get("notes")
    if not isinstance(notes, str) or not notes.strip():
        return [
            f"flagged {NEGATIVE_FLAG} but notes is empty: say what the author measured and where they "
            "concluded against Jev (a link, a pull request or issue number, or the measurement)"
        ]
    if not NEGATIVE_NOTE_SOURCE.search(notes):
        return [
            f"flagged {NEGATIVE_FLAG} but notes names no link, pull request or issue number, or measurement: "
            "say where the author's conclusion can be read"
        ]
    return []


def accepted_strings(compat: dict) -> list[str]:
    """Every model string compat.json lists on any surface, sorted."""
    query = load_query()
    platforms = [platform for platform in compat.get("platforms") or [] if "model" in platform]
    return sorted({string for platform in platforms for string in query.accepted(platform)})


def model_problems(catalog: list, retired: list, compat: dict) -> list[tuple[str, str]]:
    """(where, message) for each measurement whose model_string compat.json does
    not list. Reads compat.json only when some row records a model string."""
    found: list[tuple[str, str]] = []
    accepted: list[str] | None = None
    for label, rows in (("catalog.json", catalog), ("retired.json", retired)):
        for i, entry in enumerate(rows):
            measurement = entry.get(FIELD) if isinstance(entry, dict) else None
            string = measurement.get("model_string") if isinstance(measurement, dict) else None
            if not isinstance(string, str):
                continue
            if accepted is None:
                accepted = accepted_strings(compat)
            if string in accepted:
                continue
            listed = {**compat, "platforms": [p for p in compat.get("platforms") or [] if "model" in p]}
            reason = load_query().model_string_check(listed, string)["reason"]
            found.append((
                f"{label}[{i}]",
                f"{entry.get('slug', '?')}: measurement.model_string {string!r} is not a string compat.json "
                f"lists ({reason}); record the one the author sent or says answered if compat.json lists "
                f"it, else leave model_string out. Listed: {', '.join(accepted)}",
            ))
    return found


def measured(catalog: list[dict]) -> list[dict]:
    """The rows carrying a measurement object, in the order given."""
    query = load_query()
    return [entry for entry in catalog if query.measurement_of(entry)]


def unread(catalog: list[dict]) -> list[dict]:
    """Measured rows nobody has read against their report: no person
    (measurement.read_on) and no model (measurement.model_read_on)."""
    query = load_query()
    return [entry for entry in measured(catalog) if query.reading(query.measurement_of(entry)) is None]


def model_read(catalog: list[dict]) -> list[dict]:
    """Measured rows whose only reading against their report is a model's."""
    query = load_query()
    return [entry for entry in measured(catalog) if query.read_by(query.measurement_of(entry)) == query.MODEL]


def negative(catalog: list[dict]) -> list[dict]:
    """The negative results (query.is_negative_result), in the order given."""
    query = load_query()
    return [entry for entry in catalog if query.is_negative_result(entry)]


def directions(catalog: list[dict]) -> dict[str, int]:
    """{direction: measured rows whose author states it}, in the schema's order,
    then "not stated" for measured rows whose author states none."""
    query = load_query()
    rows = measured(catalog)
    counts = {key: sum(1 for e in rows if query.measurement_of(e).get("direction") == key) for key in query.DIRECTIONS}
    counts["not stated"] = sum(1 for e in rows if query.measurement_of(e).get("direction") not in query.DIRECTIONS)
    return counts
