#!/usr/bin/env python3
"""Validate catalog.json and retired.json.

Two layers of checking:

1. A self-contained JSON Schema (draft-07 subset) validator. The repo ships no
   Python dependencies on purpose so CI is just `setup-python` with no install
   step, and a contributor can run this on a bare interpreter.
2. Cross-entry invariants a per-entry schema cannot express: slug and URL
   uniqueness across both files, both files in slug order (fix with
   scripts/sort_catalog.py), status codes matching the file an entry lives
   in, date sanity, and the honesty rules that keep flags meaningful.

Every check returns its Findings (errors, warnings) instead of printing or
collecting into module state; only main() prints. scripts/tests/test_lint.py
pins each rule with a row that breaks exactly that rule, and fails when the
schema uses a keyword validate() does not enforce.

Exit code is 0 when clean, 1 when any error was found. Warnings never fail the
build; they are advice for a reviewer.

With --base REV, lint also compares catalog.json with the one where this
history left REV (git merge-base) and warns about a row the change adds whose
machine-translated Chinese leaves out a number its English gives
(scripts/zh_audit.py). Rows already filed are left to docs/zh-queue.md.
check.py passes the base: HEAD^1 on a pull request in CI, origin/main with --fix.

Run: python3 scripts/lint.py
     python3 scripts/lint.py --base origin/main    # also the warnings about rows added since
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
from typing import Any, NamedTuple

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _stats import shadow_path_unflagged  # noqa: E402
from measurements import model_problems as measurement_model_problems  # noqa: E402
from measurements import negative_flag_problems  # noqa: E402
from measurements import row_problems as measurement_problems  # noqa: E402
from picker import problems as picker_problems  # noqa: E402
from platform_values import problems as platform_problems  # noqa: E402
from sibling_lists import FIX as CITATION_FIX  # noqa: E402
from sibling_lists import citation_problems, listed_urls, read_lists, unlisted_citations  # noqa: E402
from thresholds import row_problems as threshold_problems  # noqa: E402
from wire import row_problems as wire_problems  # noqa: E402
from zh_audit import new_rows_since  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
RETIRED = ROOT / "retired.json"
SCHEMA = ROOT / "schema" / "entry.schema.json"
PATTERNS_FILE = ROOT / "patterns.json"
TAXONOMY_FILE = ROOT / "taxonomy.json"
COMPAT_FILE = ROOT / "compat.json"
PICKER_FILE = ROOT / "picker.json"
SIBLINGS = ROOT / "docs" / "sibling-lists.txt"

# Places we accept as TypeSafe AI speaking for itself. `official: true` anywhere
# else is a mistake: the community site at jevai.org is not the vendor, and a
# third-party integration is not official just because the vendor is mentioned.
OFFICIAL_HOSTS = (
    "typesafe.ai",
    "docs.typesafe.ai",
    "blog.typesafe.ai",
)

# The vendor's own GitHub org. A repo under any other owner is not official even
# when its code is a first-party integration published by that other vendor.
OFFICIAL_URL_PREFIXES = ("https://github.com/typesafe-ai/",)

# The one spelling of "the project's own author or maintainer proposed this row"
# in sources[].catalog, and the flag that discloses it on every surface. Each
# implies the other; see check_self_submission.
SELF_SUBMISSION_SOURCE = "author submission"
SELF_SUBMISSION_FLAG = "self-submitted"
# Spellings close enough that the writer clearly meant the declaration above.
# Rejected rather than accepted, so the rule cannot be evaded by a typo.
SELF_SUBMISSION_NEAR_MISS = re.compile(r"\b(?:author|self)[\s_-]*submi", re.IGNORECASE)

# Flags a reader cannot interpret without a reason; each needs a `notes` line.
# scripts/review_rows.py holds a pull request's new rows to the same list.
FLAGS_NEEDING_NOTES = ("ai-generated", "unverified-claims", "code-untested")

# The first field of every draft row scripts/discover_drafts.py writes: what a
# script filled in and what a person still has to do. A row that still has it
# is a script's findings, not a row anyone completed, and this is the only rule
# that keeps one out as it is (an empty summary fails, but one word passes).
# The schema does not know the field either, so such a row fails twice; this
# message is the one that says why.
DRAFT_FIELD = "_draft"

# A `kind: alternative` row is not built on Jev, so the file its evidence cites
# shows Jev's request shape: served, reimplemented, or sent to Jev to compare
# against. `evidence.kind` has to say so; without it the citation is counted
# and shown as a call site, which it is not.
ALTERNATIVE_EVIDENCE_KIND = "wire-shape"

# A script's text signal about the one file `evidence` cites (verify_claims.py
# --write-signals). Without that file it says nothing. It is never a claim
# about primitives: every rule below that asks what a row claims reads
# question_types, and none reads this.
PRIMITIVES_SEEN = "primitives_seen"

# GitHub's own facts about the linked repository, as the weekly refresh records
# them (scripts/refresh_metadata.py): two UTC timestamps and the default
# branch's commit count. They describe a GitHub repository, so a row naming
# none cannot carry them; `single-commit` restates a count of one, so the two
# must agree whenever the count is recorded, as `no-license` and repo_license
# "unknown" must. A timestamp is bounded by tomorrow rather than today: it is
# UTC, and a person checking in a time zone behind UTC is still on yesterday.
REPO_TIMESTAMPS = ("repo_created_at", "repo_pushed_at")
REPO_COMMITS = "repo_commits"
SINGLE_COMMIT_FLAG = "single-commit"

# A `sources` item shaped `{"catalog": "owner/name", "url":
# "https://github.com/owner/name"}` records that the sibling directory at that
# URL links the row's repository (sibling_lists.is_citation). The weekly run
# writes them (scripts/attribute_sources.py): after every source a person
# wrote, sorted by URL ignoring case, only for a list docs/sibling-lists.txt
# names and only on a row with a GitHub repository of its own. A row keeps at
# least one other source, since a citation says who else links a project, not
# where the row was found. The rules live beside the shape in sibling_lists.py;
# CITATION_FIX (imported from there) puts a hand-edited row right.

# `summary_source: curated` says a person wrote the summary for this catalogue,
# so CONTRIBUTING's "no marketing copy" is theirs to keep, and lint warns when a
# word from this list or an emoji is in it. A summary labelled as the project's
# own description quotes the project and is not warned about: rewording it would
# put unreviewed text in the project's name, and a row without the label says
# nothing about who wrote it. A warning, not an error: the list points at the
# usual suspects, and a reviewer decides.
CURATED = "curated"
MARKETING_WORDS = re.compile(
    r"\b(?:revolutionary|game[- ]chang\w*|ultimate|powerful|(?:blazing|lightning)[- ]fast"
    r"|cutting[- ]edge|world[- ]class|best[- ]in[- ]class|next[- ]gen(?:eration)?"
    r"|seamless(?:ly)?|supercharg\w*|effortless(?:ly)?|unleash\w*|100% free)\b",
    re.IGNORECASE,
)
# Text written as instructions to a model, in a field agents read: the MCP
# server, llms.txt and the site's api/v1 files hand titles, summaries and notes
# to agents, and most summaries are a project's own GitHub description, copied
# unreviewed for intent. Every answer says the text is data, never instructions
# (TEXT_NOTE in src/awesome_jev_mcp/query.py); this refuses the plain cases
# before they are published: an order to drop earlier instructions, a role
# reassigned, a chat template's role tokens, a line addressed to AI readers, an
# order to keep something from the user. Since 2026-10-24, when no row matched.
# A row about prompt injection describes the attack rather than quoting it.
INSTRUCTION_FIELDS = ("title", "summary", "summary_zh", "notes", "notes_zh")
INSTRUCTIONS = re.compile(
    r"\b(?:ignore|disregard|forget|override)\s+(?:all\s+|any\s+|the\s+|your\s+)?"
    r"(?:previous|prior|above|earlier|preceding|system)\s+(?:instructions?|prompts?|rules|messages?|context)\b"
    # A role reassigned: "you are now a", not "you are now ready".
    r"|\byou\s+are\s+now\s+(?:an?|acting\s+as|DAN)\b"
    r"|\byou\s+are\s+(?:an?|the)\s+(?:\w+\s+)?(?:ai|llm|(?:large\s+)?language\s+model|assistant)\b"
    # Addressed to AI readers: "If you are an AI reading this,", "Note to AI agents:";
    # not "if you are an AI researcher" or "sends a message to the agent".
    r"|\bif\s+you\s+are\s+(?:an?\s+)?(?:ai|llm|(?:large\s+)?language\s+model)"
    r"(?:\s+(?:agent|assistant|model|system))?\s*(?:[,:]|reading\b|processing\b)"
    r"|\b(?:(?:note|message|important)\s+(?:to|for)|attention)\s+(?:the\s+|any\s+|all\s+)?"
    r"(?:ai|llms?|agents?|assistants?|models?|bots?)(?:\s+(?:agents?|models?|assistants?|readers?))?\s*:"
    r"|\b(?:do\s+not|don't|never)\s+(?:tell|inform|mention\s+(?:this|it)\s+to|reveal\s+(?:this\s+|it\s+)?to)"
    r"\s+the\s+user\b"
    r"|</?\s*(?:system|assistant|user)\s*>|\[/?(?:INST|SYS)\]|<\|(?:im_start|im_end|system|endoftext)\|>"
    r"|(?:忽略|无视|忘记|忽视)(?:之前|以上|前面|先前|上述)的?(?:所有)?(?:指令|指示|提示|规则)"
    # "你现在是一个…助手", not "告诉你现在是哪个版本".
    r"|你现在是(?:一个|一名|一位)"
    r"|如果你是(?:一个)?\s*(?:AI|人工智能|大模型|大语言模型|语言模型)(?:助手|智能体|模型)?\s*(?:[，,：:]|正在|在读)",
    re.IGNORECASE,
)
# Pictographs, the two symbol blocks emoji are drawn from, and the variation
# selector that turns a symbol into one. Arrows (→) and keyboard symbols (⌘),
# which summaries use for meaning, are outside these ranges.
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F]")


class Findings(NamedTuple):
    """What a check found, in order. Errors fail the build; warnings are advice."""

    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()


class Report:
    """Collects one check's findings as `where: message` lines, in order."""

    def __init__(self) -> None:
        self._errors: list[str] = []
        self._warnings: list[str] = []

    def err(self, where: str, message: str) -> None:
        self._errors.append(f"{where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self._warnings.append(f"{where}: {message}")

    def add(self, found: Findings) -> None:
        """Append another check's findings after the ones collected so far."""
        self._errors.extend(found.errors)
        self._warnings.extend(found.warnings)

    def findings(self) -> Findings:
        return Findings(tuple(self._errors), tuple(self._warnings))


# --------------------------------------------------------------------------
# Minimal draft-07 validator
# --------------------------------------------------------------------------

# Deliberately loose: we only need to catch a contributor pasting a bare word
# or a mailto: where a link belongs. check_links.py does the real verification.
URI_RE = re.compile(r"^[a-z][a-z0-9+.\-]*://[^\s]+$", re.IGNORECASE)

# The keywords validate() enforces. A keyword it does not know is silently
# ignored, not rejected, so scripts/tests/test_lint.py fails when the schema
# uses anything outside these sets: implement it in validate() first.
SUPPORTED_KEYWORDS = frozenset(
    {
        "type",
        "enum",
        "minLength",
        "maxLength",
        "pattern",
        "format",
        "minimum",
        "maximum",
        "minItems",
        "maxItems",
        "uniqueItems",
        "items",
        "properties",
        "required",
        "additionalProperties",
    }
)
# Keywords that describe and constrain nothing; validate() never reads them.
ANNOTATION_KEYWORDS = frozenset({"$schema", "$id", "title", "description", "default"})
# The only `format` validate() checks. Any other value would be ignored.
SUPPORTED_FORMATS = frozenset({"uri"})
# The types type_ok() knows. It raises on any other.
SUPPORTED_TYPES = frozenset({"object", "array", "string", "integer", "number", "boolean", "null"})


def type_ok(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        # bool is an int subclass in Python; a flag is not a count.
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    raise ValueError(f"unhandled schema type {expected!r}")


def validate(value: Any, schema: dict, path: str) -> Findings:
    """Walk `schema` against `value` and return every mismatch as an error."""
    report = Report()
    if "type" in schema and not type_ok(value, schema["type"]):
        report.err(path, f"expected {schema['type']}, got {type(value).__name__}")
        return report.findings()

    if "enum" in schema and value not in schema["enum"]:
        allowed = ", ".join(map(str, schema["enum"]))
        report.err(path, f"{value!r} is not one of: {allowed}")

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            report.err(path, f"shorter than minLength {schema['minLength']}")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            report.err(path, f"{len(value)} chars exceeds maxLength {schema['maxLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            report.err(path, f"{value!r} does not match {schema['pattern']}")
        if schema.get("format") == "uri" and not URI_RE.match(value):
            report.err(path, f"{value!r} is not a URI")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            report.err(path, f"{value} below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            report.err(path, f"{value} above maximum {schema['maximum']}")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            report.err(path, f"needs at least {schema['minItems']} item(s)")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            report.err(path, f"has {len(value)} items, max {schema['maxItems']}")
        if schema.get("uniqueItems"):
            seen: list[Any] = []
            for item in value:
                if item in seen:
                    report.err(path, f"duplicate item {item!r}")
                seen.append(item)
        if "items" in schema:
            for i, item in enumerate(value):
                report.add(validate(item, schema["items"], f"{path}[{i}]"))

    if isinstance(value, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                report.err(path, f"missing required field {key!r}")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    report.err(path, f"unknown field {key!r}")
        for key, sub in props.items():
            if key in value:
                report.add(validate(value[key], sub, f"{path}.{key}"))
    return report.findings()


# --------------------------------------------------------------------------
# Invariants across entries
# --------------------------------------------------------------------------


def parse_date(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)
    except (ValueError, TypeError):
        return None


def check_entry_invariants(
    entry: dict, path: str, *, retired: bool, today: dt.date | None = None
) -> Findings:
    """The rules one row must follow that its schema cannot express.

    `today` bounds the dates; it defaults to the real date and is a parameter
    only so tests can fix it.
    """
    report = Report()
    slug = entry.get("slug", "?")
    if today is None:
        today = dt.date.today()

    if DRAFT_FIELD in entry:
        report.err(
            path,
            f"{slug}: is a discovery draft, not a row: read the call site, complete it as its "
            f"{DRAFT_FIELD!r} lines say, then delete that field",
        )

    # An entry claiming code should say what language it is in, and a question
    # type is a claim about code. These keep `has_code` filters trustworthy.
    if entry.get("has_code") and not entry.get("languages"):
        report.warn(path, f"{slug}: has_code is true but languages is empty")
    if entry.get("question_types") and not entry.get("has_code"):
        report.err(path, f"{slug}: question_types set but has_code is not true")

    # A claim about code must be re-checkable, or say why it is not. For a
    # primitive claim this was a warning until 2026-09-27, when no row broke it
    # any more. The same day it grew to every row with code in a GitHub
    # repository: keyed on question_types alone, 34 rows with code carried
    # neither and nothing noticed. A retired row's repository is gone, so
    # there is nothing left there to read. `evidence_none` (`not-yet-backfilled`
    # included) is always an honest way to satisfy it.
    claims_primitives = bool(entry.get("question_types"))
    readable_code = bool(entry.get("has_code")) and on_github(entry) and not retired
    if (claims_primitives or readable_code) and not (
        entry.get("evidence") or entry.get("evidence_none")
    ):
        what = "claims primitives" if claims_primitives else "has code in a GitHub repository"
        report.err(
            path,
            f"{slug}: {what} but carries neither evidence nor evidence_none. "
            f"Run 'python3 scripts/verify_claims.py --discover --only {slug}' to propose a "
            "call site, or set evidence_none to say why no file can be cited "
            "(docs-page, no-jev-call-site, not-yet-backfilled, ...)",
        )

    # Evidence without a repository to read it from cannot be verified.
    if entry.get("evidence") and not on_github(entry):
        report.err(
            path,
            f"{slug}: has evidence but no GitHub repository to re-read it from",
        )
    if entry.get("evidence") and entry.get("evidence_none"):
        report.err(path, f"{slug}: has both evidence and evidence_none; they are exclusive")
    if PRIMITIVES_SEEN in entry and not entry.get("evidence"):
        report.err(
            path,
            f"{slug}: has {PRIMITIVES_SEEN} but no evidence: it is a text signal about the file "
            "evidence cites, written by verify_claims.py --write-signals; remove it",
        )
    evidence = entry.get("evidence")
    if (
        entry.get("kind") == "alternative"
        and isinstance(evidence, dict)
        and evidence.get("kind") != ALTERNATIVE_EVIDENCE_KIND
    ):
        report.err(
            path,
            f"{slug}: kind is 'alternative', so its evidence shows Jev's request shape, not the "
            f"project building on Jev; set evidence.kind to {ALTERNATIVE_EVIDENCE_KIND!r}",
        )

    if shadow_path_unflagged(entry):
        report.warn(
            path,
            f"{slug}: evidence.path {evidence['path']!r} names a shadow or dry run but the row lacks the "
            "shadow-mode-only flag: read the call, and flag it if nothing it returns reaches a decision",
        )
    report.add(check_curated_summary(entry, path))
    report.add(check_instructions(entry, path))

    # `official` is a factual claim about who published the thing, so it is
    # checked against the vendor's own hosts and GitHub org rather than trusted.
    if entry.get("official"):
        url = entry.get("url", "")
        host = re.sub(r"^https://([^/]+).*$", r"\1", url).lower()
        host_ok = any(host == h or host.endswith("." + h) for h in OFFICIAL_HOSTS)
        path_ok = any(url.startswith(prefix) for prefix in OFFICIAL_URL_PREFIXES)
        if not (host_ok or path_ok):
            report.err(
                path,
                f"{slug}: official is true but {url!r} is not published by TypeSafe AI",
            )

    # A flag that needs explaining is worse than no flag at all.
    flags = entry.get("flags", [])
    report.add(check_self_submission(entry, path, flags))
    for flag in FLAGS_NEEDING_NOTES:
        if flag in flags and not entry.get("notes"):
            report.warn(
                path,
                f"{slug}: flagged {flag!r} but notes is empty, so a reader gets no reason",
            )

    # "overview" means the entry surveys the space rather than showing one
    # pattern. Mixing it with a specific pattern makes both filters lie.
    patterns = entry.get("patterns", [])
    if "overview" in patterns and len(patterns) > 1:
        report.err(path, f"{slug}: 'overview' cannot be combined with specific patterns")

    # Dates must be real and not from the future. patterns_reviewed is a
    # person's reading, and a reading cannot happen tomorrow either.
    for field in ("published", "first_seen", "checked", "patterns_reviewed"):
        if field in entry:
            parsed = parse_date(entry[field])
            if parsed is None:
                report.err(path, f"{slug}: {field} is not a valid date")
            elif parsed > today:
                report.err(path, f"{slug}: {field} {entry[field]} is in the future")

    published, checked = (
        parse_date(entry.get("published", "")),
        parse_date(entry.get("checked", "")),
    )
    if published and checked and published > checked:
        report.err(
            path,
            f"{slug}: published {entry['published']} is after checked {entry['checked']}",
        )

    # The status code has to agree with the file the entry lives in, otherwise
    # "everything in catalog.json was reachable" stops being true.
    status = entry.get("link_status")
    if status is not None:
        if retired and 200 <= status < 300:
            report.err(path, f"{slug}: retired entries must not carry a 2xx status ({status})")
        if not retired and not 200 <= status < 300:
            report.err(
                path,
                f"{slug}: status {status} does not belong in catalog.json; move it to retired.json",
            )

    if retired and not entry.get("notes"):
        report.err(path, f"{slug}: retired entries need notes saying why they were retired")

    # `no-license` and repo_license "unknown" state the same fact twice, so they
    # must agree. They drifted once: a project added a LICENSE upstream, the
    # weekly refresh noticed, and the row kept its flag because that refresh
    # was never merged — a row simultaneously claiming MIT and no licence.
    if "repo_license" in entry:
        unlicensed = entry["repo_license"] == "unknown"
        if unlicensed and "no-license" not in flags:
            report.err(
                path,
                f"{slug}: repo_license is 'unknown' but the row lacks the no-license flag",
            )
        if not unlicensed and "no-license" in flags:
            report.err(
                path,
                f"{slug}: flagged no-license but repo_license is {entry['repo_license']!r}",
            )
    report.add(check_repository_facts(entry, path, flags, today))
    report.add(check_sibling_citations(entry, path))
    report.add(check_measurement(entry, path, today))
    report.add(check_wire(entry, path, today))
    report.add(check_thresholds(entry, path, today))
    return report.findings()


def check_measurement(entry: dict, path: str, today: dt.date) -> Findings:
    """A benchmark's `measurement`, and the negative-result flag that says the
    same on a row of any other kind: the rules live in scripts/measurements.py."""
    report = Report()
    for problem in [*measurement_problems(entry, today), *negative_flag_problems(entry)]:
        report.err(path, f"{entry.get('slug', '?')}: {problem}")
    return report.findings()


def check_wire(entry: dict, path: str, today: dt.date) -> Findings:
    """An alternative row's `wire`: the rules live in scripts/wire.py."""
    report = Report()
    for problem in wire_problems(entry, today, on_github=on_github(entry)):
        report.err(path, f"{entry.get('slug', '?')}: {problem}")
    return report.findings()


def check_thresholds(entry: dict, path: str, today: dt.date) -> Findings:
    """A row's `observed_thresholds`: the rules live in scripts/thresholds.py."""
    report = Report()
    for problem in threshold_problems(entry, today):
        report.err(path, f"{entry.get('slug', '?')}: {problem}")
    return report.findings()


def check_sibling_citations(entry: dict, path: str) -> Findings:
    """Sibling-list citations in `sources` (sibling_lists.citation_problems)."""
    report = Report()
    for problem in citation_problems(entry):
        report.err(path, f"{entry.get('slug', '?')}: {problem}")
    return report.findings()


def check_citation_lists(catalog: list, listed: list[str]) -> Findings:
    """Every sibling-list citation in catalog.json names a list
    docs/sibling-lists.txt names. One error per list, however many rows cite it.
    retired.json keeps what its rows had when they were retired."""
    report = Report()
    for url, rows in unlisted_citations(catalog, listed).items():
        report.err(
            "catalog.json",
            f"{rows} row(s) cite {url} in sources, a list docs/sibling-lists.txt does not name; "
            f"run {CITATION_FIX} to drop them",
        )
    return report.findings()


def parse_timestamp(value: object) -> dt.datetime | None:
    try:
        return dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")  # type: ignore[arg-type]
    except (ValueError, TypeError):
        return None


def check_repository_facts(entry: dict, path: str, flags: list, today: dt.date) -> Findings:
    """GitHub's dates and commit count: only on a GitHub row, real, not from
    the future, and `single-commit` exactly when the count is one."""
    report = Report()
    slug = entry.get("slug", "?")
    present = [field for field in (*REPO_TIMESTAMPS, REPO_COMMITS) if field in entry]
    if present and not on_github(entry):
        report.err(
            path,
            f"{slug}: has {', '.join(present)} but no GitHub repository: they are GitHub's facts "
            "about one, written by refresh_metadata.py; remove them",
        )
    for field in REPO_TIMESTAMPS:
        if field in entry:
            parsed = parse_timestamp(entry[field])
            if parsed is None:
                report.err(path, f"{slug}: {field} is not a valid UTC timestamp")
            elif parsed.date() > today + dt.timedelta(days=1):
                report.err(path, f"{slug}: {field} {entry[field]} is in the future")
    commits = entry.get(REPO_COMMITS)
    if isinstance(commits, int):
        if commits == 1 and SINGLE_COMMIT_FLAG not in flags:
            report.err(path, f"{slug}: repo_commits is 1 but the row lacks the {SINGLE_COMMIT_FLAG} flag")
        if commits > 1 and SINGLE_COMMIT_FLAG in flags:
            report.err(path, f"{slug}: flagged {SINGLE_COMMIT_FLAG} but repo_commits is {commits}")
    return report.findings()


def on_github(entry: dict) -> bool:
    """The row names a GitHub repository in `url` or `repo`, where a file can be read."""
    return any("github.com" in str(entry.get(field) or "") for field in ("url", "repo"))


def check_curated_summary(entry: dict, path: str) -> Findings:
    """A summary a person wrote for this catalogue reads like one: no marketing
    words, no emoji. Only rows labelled `summary_source: curated`; see CURATED."""
    report = Report()
    summary = entry.get("summary")
    if entry.get("summary_source") != CURATED or not isinstance(summary, str):
        return report.findings()
    slug = entry.get("slug", "?")
    words = sorted({match.group(0).lower() for match in MARKETING_WORDS.finditer(summary)})
    if words:
        report.warn(
            path,
            f"{slug}: summary_source is curated but the summary uses marketing words "
            f"({', '.join(words)}); say what decision the project makes instead",
        )
    if EMOJI.search(summary):
        report.warn(path, f"{slug}: summary_source is curated but the summary contains emoji")
    return report.findings()


def check_instructions(entry: dict, path: str) -> Findings:
    """No text an agent reads is written as instructions to it; see INSTRUCTIONS."""
    report = Report()
    slug = entry.get("slug", "?")
    for field in INSTRUCTION_FIELDS:
        value = entry.get(field)
        match = INSTRUCTIONS.search(value) if isinstance(value, str) else None
        if match:
            report.err(
                path,
                f"{slug}: {field} reads as an instruction to a model ({match.group(0)!r}). Agents read "
                "this text (the MCP server, llms.txt, the site's api/v1): say what the project does "
                "rather than quoting it",
            )
    return report.findings()


def check_self_submission(entry: dict, path: str, flags: list) -> Findings:
    """`author submission` in sources and the `self-submitted` flag go together.

    The source string is where a contributor declares the relationship; the
    flag is what the READMEs, the pattern pages, the site and the MCP server
    show a reader. Either one without the other means a surface is silent about
    it. Purely declarative on purpose: nothing is inferred from a GitHub handle
    (rarely filled, and an owner is often an org) or from the wording of a note.
    """
    report = Report()
    slug = entry.get("slug", "?")
    sources = [s for s in entry.get("sources", []) if isinstance(s, dict)]
    names = [s.get("catalog") for s in sources if isinstance(s.get("catalog"), str)]
    for name in names:
        if name != SELF_SUBMISSION_SOURCE and SELF_SUBMISSION_NEAR_MISS.search(name):
            report.err(
                path,
                f"{slug}: source catalog {name!r} looks like a self-submission; write "
                f"exactly {SELF_SUBMISSION_SOURCE!r} so lint and every surface recognise it",
            )
    declared = SELF_SUBMISSION_SOURCE in names
    flagged = SELF_SUBMISSION_FLAG in flags
    if declared and not flagged:
        report.err(
            path,
            f"{slug}: a source is {SELF_SUBMISSION_SOURCE!r} but flags lacks "
            f"{SELF_SUBMISSION_FLAG!r}; add it so every surface discloses the relationship",
        )
    if flagged and not declared:
        report.err(
            path,
            f"{slug}: flagged {SELF_SUBMISSION_FLAG} but no source has catalog "
            f"{SELF_SUBMISSION_SOURCE!r}; add that source (url: the pull request or "
            "issue that proposed the row) or drop the flag",
        )
    return report.findings()


def check_slug_order(label: str, data: list) -> Findings:
    """Both data files stay in slug order.

    The order is meaningless to readers (every generator sorts for itself), but
    when each new row was appended at the end, every two pull requests adding
    rows edited the same lines and conflicted. In slug order they insert at
    different places. One error per file, with the fix, not one per row.
    """
    from sort_catalog import COMMAND, order_problem

    report = Report()
    problem = order_problem(data)
    if problem:
        report.err(label, f"{problem}; run `{COMMAND}` and commit the result")
    return report.findings()


def check_patterns(schema: dict, patterns: list) -> Findings:
    """patterns.json labels exactly the patterns the schema allows, every text filled in.

    patterns.json feeds both README generators and the MCP server. If it
    drifts from the schema enum, a pattern is either unlabelled in a figure
    or unusable in the catalog, and both fail far from the cause.
    """
    report = Report()
    taxonomy = {p["key"] for p in patterns}
    enum = set(schema["properties"]["patterns"]["items"]["enum"])
    for key in sorted(enum - taxonomy):
        report.err(
            "patterns.json",
            f"schema allows {key!r} but patterns.json has no label for it",
        )
    for key in sorted(taxonomy - enum):
        report.err(
            "patterns.json",
            f"patterns.json labels {key!r} but the schema does not allow it",
        )
    # The site shows the short blurb, the README the long one. Both must
    # exist, or the site falls back to a raw slug without complaint.
    for p in patterns:
        for field in ("en", "zh", "blurb_en", "blurb_zh", "short_en", "short_zh"):
            if not p.get(field):
                report.err("patterns.json", f"{p['key']!r} has no {field}")
    return report.findings()


def check_languages(schema: dict, lang_ext: dict) -> Findings:
    """Every language the schema accepts has file extensions in _github.LANG_EXT, and no other.

    The scanners find code by extension. A language the schema accepts but
    _github.LANG_EXT does not map is one discovery can never see: C and C++
    were missing, so three database extensions looked test-only.
    """
    report = Report()
    langs = set(schema["properties"]["languages"]["items"]["enum"])
    for lang in sorted(langs - set(lang_ext)):
        report.err("scripts/_github.py", f"schema language {lang!r} has no file extensions in LANG_EXT")
    for lang in sorted(set(lang_ext) - langs):
        report.err("scripts/_github.py", f"LANG_EXT maps {lang!r}, which the schema does not allow")
    return report.findings()


def check_taxonomy(schema: dict, labels: dict) -> Findings:
    """taxonomy.json labels exactly the kinds, flags, summary sources and
    measurement directions and metrics the schema allows, every text filled in.

    taxonomy.json holds those labels for both the README and the site. A key the
    schema allows but taxonomy.json lacks raises in build_readme but renders as
    a raw slug on the site — loud in one place, silent in the other.
    """
    report = Report()
    measurement = schema["properties"]["measurement"]["properties"]
    for group, enum in (
        ("kinds", schema["properties"]["kind"]["enum"]),
        ("flags", schema["properties"]["flags"]["items"]["enum"]),
        ("summary_sources", schema["properties"]["summary_source"]["enum"]),
        ("measurement_directions", measurement["direction"]["enum"]),
        ("measurement_metrics", measurement["metrics"]["items"]["enum"]),
    ):
        have = [item["key"] for item in labels[group]]
        for key in sorted(set(enum) - set(have)):
            report.err(
                "taxonomy.json",
                f"schema allows {group[:-1]} {key!r} but it has no label",
            )
        for key in sorted(set(have) - set(enum)):
            report.err(
                "taxonomy.json",
                f"labels {group[:-1]} {key!r} but the schema does not allow it",
            )
        for item in labels[group]:
            for field in ("en", "zh", "blurb_en", "blurb_zh"):
                if not item.get(field):
                    report.err(
                        "taxonomy.json",
                        f"{group[:-1]} {item['key']!r} has no {field}",
                    )
    return report.findings()


def check_entries(schema: dict, catalog: list, retired: list) -> Findings:
    """Each row against the schema and its invariants, then the rules that span rows.

    Slugs and URLs are unique across both files together, and each file is in
    slug order.
    """
    report = Report()
    slugs: dict[str, str] = {}
    urls: dict[str, str] = {}

    for label, data, is_retired in (
        ("catalog.json", catalog, False),
        ("retired.json", retired, True),
    ):
        for i, entry in enumerate(data):
            path = f"{label}[{i}]"
            if not isinstance(entry, dict):
                report.err(path, "entry must be an object")
                continue
            report.add(validate(entry, schema, path))
            report.add(check_entry_invariants(entry, path, retired=is_retired))

            slug = entry.get("slug")
            if isinstance(slug, str):
                if slug in slugs:
                    report.err(path, f"duplicate slug {slug!r}, already used in {slugs[slug]}")
                else:
                    slugs[slug] = path

            url = entry.get("url")
            if isinstance(url, str):
                # Trailing slashes and casing are the usual way a duplicate sneaks in.
                key = url.rstrip("/").lower()
                if key in urls:
                    report.err(path, f"duplicate url {url!r}, already used in {urls[key]}")
                else:
                    urls[key] = path

        report.add(check_slug_order(label, data))
    return report.findings()


def check_all(schema: dict, catalog: Any, retired: Any) -> Findings:
    """Every check lint runs, in the order it reports them.

    The label files are checked first. A data file that is not an array ends
    the run there, since none of its rows can be read.
    """
    report = Report()
    if PATTERNS_FILE.exists():
        report.add(check_patterns(schema, json.loads(PATTERNS_FILE.read_text())["patterns"]))

    sys.path.insert(0, str(ROOT / "scripts"))
    from _github import LANG_EXT

    report.add(check_languages(schema, LANG_EXT))

    if TAXONOMY_FILE.exists():
        report.add(check_taxonomy(schema, json.loads(TAXONOMY_FILE.read_text())))

    if PICKER_FILE.exists() and PATTERNS_FILE.exists():
        patterns = json.loads(PATTERNS_FILE.read_text())["patterns"]
        report.add(check_picker(schema, patterns, json.loads(PICKER_FILE.read_text())))

    for name, data in (("catalog.json", catalog), ("retired.json", retired)):
        if not isinstance(data, list):
            report.err(name, "top level must be an array of entries")
            return report.findings()

    report.add(check_entries(schema, catalog, retired))
    listed = listed_urls(read_lists(SIBLINGS)) if SIBLINGS.exists() else []
    report.add(check_citation_lists(catalog, listed))
    if COMPAT_FILE.exists() and TAXONOMY_FILE.exists():
        compat, taxonomy = json.loads(COMPAT_FILE.read_text()), json.loads(TAXONOMY_FILE.read_text())
        report.add(check_platform_values(catalog, retired, compat, taxonomy))
    if COMPAT_FILE.exists():
        report.add(check_measurement_models(catalog, retired, json.loads(COMPAT_FILE.read_text())))
    return report.findings()


def check_picker(schema: dict, patterns: list[dict], picker: Any) -> Findings:
    """picker.json, the primitive picker: a decision list whose every step
    cites docs.typesafe.ai, whose leaves name known patterns and primitives,
    and whose text states no number or answer field. The rules live in
    scripts/picker.py."""
    report = Report()
    primitives = schema["properties"]["question_types"]["items"]["enum"]
    for where, message in picker_problems(picker, [p["key"] for p in patterns], primitives):
        report.err(where, message)
    return report.findings()


def check_measurement_models(catalog: list, retired: list, compat: dict) -> Findings:
    """Every measurement.model_string is a string compat.json lists (scripts/measurements.py)."""
    report = Report()
    for where, message in measurement_model_problems(catalog, retired, compat):
        report.err(where, message)
    return report.findings()


def check_platform_values(catalog: list, retired: list, compat: dict, taxonomy: dict) -> Findings:
    """Every value a row records in `platforms` is claimed by a compat.json
    surface (its catalog_platforms) or listed in taxonomy.json's
    platforms_without_surface, and those two lists keep their own rules. The
    rules live in scripts/platform_values.py."""
    report = Report()
    for where, message in platform_problems(catalog, retired, compat, taxonomy):
        report.err(where, message)
    return report.findings()


def check_new_translations(catalog: list, base: str) -> tuple[Findings, str]:
    """Rows `catalog` adds since commit `base` whose machine translation drops a
    number the English gives, and a note for the log. Warnings only: the rule is
    a text comparison (scripts/zh_audit.py), not a reading."""
    report = Report()
    found, note = new_rows_since(catalog, base, ROOT)
    for where, message in found:
        report.warn(where, message)
    return report.findings(), note


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--base", metavar="REV", help="also warn about rows added since this commit")
    args = parser.parse_args([] if argv is None else argv)
    for required_file in (CATALOG, RETIRED, SCHEMA):
        if not required_file.exists():
            print(
                f"error: {required_file.relative_to(ROOT)} is missing", file=sys.stderr
            )
            return 1

    schema = json.loads(SCHEMA.read_text())
    catalog = json.loads(CATALOG.read_text())
    retired = json.loads(RETIRED.read_text())

    findings = check_all(schema, catalog, retired)
    if args.base and isinstance(catalog, list):
        new, note = check_new_translations(catalog, args.base)
        print(f"note: {note}")
        findings = Findings(findings.errors, findings.warnings + new.warnings)
    print_report(findings)
    if isinstance(catalog, list) and isinstance(retired, list):
        print(
            f"checked {len(catalog)} catalog entr{'y' if len(catalog) == 1 else 'ies'} "
            f"and {len(retired)} retired"
        )
    return 1 if findings.errors else 0


def print_report(findings: Findings) -> None:
    for warning in findings.warnings:
        print(f"warning: {warning}")
    for error in findings.errors:
        print(f"error: {error}", file=sys.stderr)
    if findings.errors:
        print(f"\n{len(findings.errors)} error(s)", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
