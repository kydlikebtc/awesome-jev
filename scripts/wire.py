"""What an alternative row's `wire` records, and the rules lint.py keeps on it.

A `kind: alternative` row is a project that is not Jev: a reimplementation of
its interface, a server that answers Jev-shaped requests with another model,
or a project that sends Jev the same requests to compare. The catalogue says
little else about them, and a reader cannot tell "same route, yes/no spelled
`boolean`" from "open weights behind the same route" from "a proxy in front of
another provider's model". `wire` records, field by field, what the project's
own files show about the interface it offers (schema/entry.schema.json):

* `endpoint`: the method and path its server answers a decision request on;
* `yesno_spelling`: the `type` its requests give Jev's yes/no question;
* `answer_field`: the key a yes/no answer's probability is read from;
* `confidence_field`: the key a choice or score answer's confidence is read from;
* `envelope`: `top-level` when state and questions sit at the top of the
  request body, as in Jev's own API; `wrapped` when they sit inside another field;
* `weights`: where its answers come from in the default configuration:
  `open`, a model whose weights you can run yourself (published, or produced by
  the project's own training code); `closed`, a model only the project runs;
  `proxy`, another provider's hosted model, which the server calls and reshapes;
* `base_model`: that answering model, as the cited file names it;
* `calls_real_jev_as_baseline`: a cited file sends Jev the same requests to
  compare with. Only `true` is recorded: no string can show a call is absent;
* `comparison_url`: where the project publishes a comparison with Jev;
* `source`: the files those were read in, each `{path, matched, read_on}` as
  `evidence` is. Every matched string must still be in its file, and
  scripts/verify_claims.py re-reads them every week. `read_on` dates a person's
  reading and (since 2026-10-24) `model_read_on` a model's, kept apart; with
  neither, a script or a model read the files and nobody recorded a reading.

Nothing in it is inferred: a field the cited files do not show is left out, and
every surface prints a dash for it. A compatible interface implies nothing
about calibration, so every surface that shows `wire` shows the not-jev caveat
and CALIBRATION_NOTE (the second sentence of taxonomy.json's not-jev blurb) on
every row.

What lint holds (lint.check_wire):
* `wire` only on a kind: alternative row that carries the not-jev flag and a
  GitHub repository to read the cited files in;
* at least one field besides `source`, and no file cited twice;
* each value copied out of a file (the endpoint's path, yesno_spelling,
  answer_field, confidence_field, base_model) is inside one of the matched
  strings, so the string backing it is what the weekly run re-reads;
* calls_real_jev_as_baseline needs a matched string naming Jev's own host or a
  gateway's id for Jev (REAL_JEV_SIGNALS): a floor, not proof, like the words
  measurements.NEGATIVE_NOTE_SOURCE asks for;
* each `read_on` and `model_read_on` is a real date, not in the future.

docs/compatibility.md ("Compatible interfaces that are not Jev") and the site's
Compatibility view show these rows; docs/review-queue.md lists those no person
has read. site/catalog-core.mjs selects the same rows (scripts/tests/wire_cases.json).

Stdlib only, like the rest of scripts/.
"""

from __future__ import annotations

import datetime as dt

FIELD = "wire"
# A person's reading and a model's (query.READ_ON, query.MODEL_READ_ON).
READINGS = ("read_on", "model_read_on")
KIND = "alternative"
NOT_JEV = "not-jev"
SOURCE = "source"
ENDPOINT = "endpoint"
BASELINE = "calls_real_jev_as_baseline"
COMPARISON = "comparison_url"
WEIGHTS = ("open", "closed", "proxy")
ENVELOPES = ("top-level", "wrapped")
# Values written as the cited file writes them; each must sit inside a matched string.
COPIED = ("yesno_spelling", "answer_field", "confidence_field", "base_model")
# Jev's own API host, and the ids gateways give it (Vercel's typesafe-ai/jev;
# typesafe/jev on OpenRouter, Cloudflare and AI/ML API). A local server may
# accept `jev-latest` as an alias, so a bare model name shows no call to Jev.
REAL_JEV_SIGNALS = ("api.typesafe.ai", "typesafe-ai/jev", "typesafe/jev")
# The second sentence of taxonomy.json's not-jev blurbs, in both languages
# (a test holds them there). The first sentence, "Does not call Jev at all", is
# not repeated beside `wire`: some of these projects do call Jev, to compare.
CALIBRATION_NOTE = "A compatible API does not imply compatible calibration, so thresholds do not transfer."
CALIBRATION_NOTE_ZH = "协议兼容不等于校准兼容，所以阈值不能迁移。"


def wire_of(entry: dict) -> dict | None:
    value = entry.get(FIELD) if isinstance(entry, dict) else None
    return value if isinstance(value, dict) else None


def sources(wire: dict) -> list[dict]:
    """The well-formed items of wire.source (the schema reports the rest)."""
    items = wire.get(SOURCE)
    if not isinstance(items, list):
        return []
    return [
        item for item in items
        if isinstance(item, dict) and isinstance(item.get("path"), str) and isinstance(item.get("matched"), list)
    ]


def matched(wire: dict) -> list[str]:
    return [text for item in sources(wire) for text in item["matched"] if isinstance(text, str)]


def recorded(wire: dict) -> list[str]:
    """The fields besides `source` a wire record holds."""
    return [key for key in wire if key != SOURCE]


def endpoint_path(value: str) -> str:
    """The path of `POST /v1/systemone`: what the cited file has to show."""
    return value.split(" ", 1)[1] if " " in value else value


def row_problems(entry: dict, today: dt.date, *, on_github: bool) -> list[str]:
    """Each way one row's `wire` breaks a rule the schema cannot express."""
    if FIELD not in entry:
        return []
    found: list[str] = []
    if entry.get("kind") != KIND:
        found.append(
            f"has a wire record but kind is {entry.get('kind')!r}: wire describes the interface a project "
            "that is not Jev offers, so it belongs only on a kind: alternative row"
        )
    if NOT_JEV not in (entry.get("flags") or []):
        found.append(
            f"has a wire record but lacks the {NOT_JEV} flag: a compatible interface is not Jev, and the "
            "flag carries that to every surface"
        )
    if not on_github:
        found.append("has a wire record but no GitHub repository to read wire.source in")
    wire = wire_of(entry)
    if wire is None:
        return found  # the schema says what it should be
    if not recorded(wire):
        found.append("has a wire record that records nothing besides its source: leave wire out instead")
    paths = [item["path"] for item in sources(wire)]
    for path in sorted({p for p in paths if paths.count(p) > 1}):
        found.append(f"wire.source cites {path!r} twice: give each file once, with all its matched strings")
    strings = matched(wire)
    for field in (ENDPOINT, *COPIED):
        value = wire.get(field)
        if not isinstance(value, str):
            continue
        shown = endpoint_path(value) if field == ENDPOINT else value
        if not any(shown in text for text in strings):
            found.append(
                f"wire.{field} {shown!r} is in none of wire.source's matched strings: add the string from the "
                "file that shows it, or leave the field out"
            )
    if wire.get(BASELINE) is True and not any(signal in text for text in strings for signal in REAL_JEV_SIGNALS):
        found.append(
            f"wire.{BASELINE} is true but no matched string names Jev's own host or a gateway's id for it "
            f"({', '.join(REAL_JEV_SIGNALS)}): add the string from the file that sends the request"
        )
    for i, item in enumerate(sources(wire)):
        for field in READINGS:
            if field not in item:
                continue
            try:
                read = dt.date.fromisoformat(item[field])
            except (TypeError, ValueError):
                found.append(f"wire.source[{i}].{field} is not a valid date")
                continue
            if read > today:
                found.append(f"wire.source[{i}].{field} {item[field]} is in the future")
    return found


def wired(catalog: list[dict]) -> list[dict]:
    """The alternative rows that record their interface."""
    return [e for e in catalog if e.get("kind") == KIND and wire_of(e) is not None]


def unwired(catalog: list[dict]) -> list[dict]:
    """The alternative rows that record none: nobody has recorded it from their
    files yet, or their files show none."""
    return [e for e in catalog if e.get("kind") == KIND and wire_of(e) is None]


def person_read(wire: dict) -> bool:
    """Every cited file carries a person's reading date."""
    items = sources(wire)
    return bool(items) and all("read_on" in item for item in items)


def every_file_read(wire: dict) -> bool:
    """Every cited file carries a reading date, a person's or a model's."""
    items = sources(wire)
    return bool(items) and all(any(field in item for field in READINGS) for item in items)


def unread(catalog: list[dict]) -> list[dict]:
    """Rows whose wire nobody has read against every cited file: some file
    carries neither a person's reading nor a model's."""
    return [e for e in wired(catalog) if not every_file_read(wire_of(e))]


def model_read(catalog: list[dict]) -> list[dict]:
    """Rows whose every cited file was read, and some only by a model."""
    return [e for e in wired(catalog) if every_file_read(wire_of(e)) and not person_read(wire_of(e))]


def claims(entry: dict) -> list[dict]:
    """{path, matched} for each file wire.source cites, for the weekly re-read."""
    wire = wire_of(entry)
    if wire is None:
        return []
    return [{"path": item["path"], "matched": list(item["matched"])} for item in sources(wire)]
