#!/usr/bin/env python3
"""Check that the published repository description still matches the catalogue.

The description is the single most-read sentence this project publishes — it is
what appears in GitHub search, in the social card and in every link preview —
and it was the one claim in the whole repository that nothing could check. It
lives in GitHub's database, not in git, so it sat at "148 verified examples"
while the catalogue grew to 805 and no build ever went red.

That is precisely the failure mode the catalogue exists to argue against, so it
gets the same treatment as everything else: a number that is asserted in public
has to be re-derivable from the data.

Since 2026-09-27 the sentence is `_stats.pitch_public()`. It stated the count
floored to the hundred until 2026-11-05, and states none since, so it goes
stale only when its wording changes, never with the catalogue. And drift is
reported rather than failed: fixing it needs admin rights on the repository,
which no workflow token holds, and a check that turns `main` red over something
CI cannot fix teaches everyone to ignore red. `.github/workflows/description.yml`
runs this with `--report` on every push to `main` and keeps one open issue,
labelled `description`, carrying the exact command.

Read-only. A missing token or an unreachable API is reported as `skipped`, not
as drift: a network hiccup must not open an issue nobody can act on.

Usage:
  python3 scripts/check_description.py              # a person: exit 1 on drift
  python3 scripts/check_description.py --report F   # CI: on drift write the issue
                                                    # body to F, warn, exit 0
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
from _github import SELF, api_get, graphql, token  # noqa: E402


def edit_command(text: str) -> str:
    """A paste-ready fix. Double quotes keep the apostrophe in "AI's" readable;
    the four characters that stay special inside them are escaped."""
    escaped = re.sub(r'([\\"$`])', r"\\\1", text)
    return f'gh repo edit {SELF} --description "{escaped}"'


def set_output(name: str, value: str) -> None:
    """Tell the workflow what happened: match, drift or skipped."""
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(f"{name}={value}\n")


def step_summary(text: str) -> None:
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(text + "\n")


def issue_body(published: str, expected: str, entries: int) -> str:
    return "\n".join(
        [
            "The GitHub repository description no longer matches the catalogue's",
            "public pitch, `_stats.pitch_public()` in `scripts/_stats.py` — the same",
            "sentence the site uses for its `og:description`. CI cannot fix this:",
            "editing the description needs admin rights, which the workflow token",
            "does not have.",
            "",
            f"**Published:** {published or '(empty)'}",
            "",
            f"**Expected:** {expected}",
            "",
            f"The catalogue holds {entries:,} entries. The pitch states no count, so it "
            "changes only when its wording is edited.",
            "",
            "Run this once, as a repository admin:",
            "",
            "```bash",
            edit_command(expected),
            "```",
            "",
            "The next run on `main` after that — any push, or Actions → description →",
            "Run workflow — closes this issue.",
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--report",
        type=pathlib.Path,
        help="on drift, write an issue body here, warn and exit 0 instead of 1",
    )
    args = parser.parse_args(argv)
    if args.report:
        # A body left by an earlier run must never be filed as this run's drift.
        args.report.unlink(missing_ok=True)

    stats = _stats.compute()
    expected = _stats.pitch_public(stats)

    if not token():
        print(f"skipped: no GITHUB_TOKEN. Catalogue holds {stats['entries']} entries.")
        print(f"  the description should read: {expected}")
        set_output("status", "skipped")
        return 0

    data = api_get(f"/repos/{SELF}")
    # api_get answers a refused read with {"blocked": True}: a dict, but not the
    # repository, and its missing description must not be reported as drift.
    if not isinstance(data, dict) or data.get("blocked"):
        print(f"skipped: could not read the {SELF} description.")
        set_output("status", "skipped")
        return 0

    report_social_preview()

    description = (data.get("description") or "").strip()
    if description == expected:
        print(f"description matches the catalogue's pitch ({stats['entries']} entries; the pitch states no count)")
        set_output("status", "match")
        return 0

    # The whole sentence is compared, not just its number. The same sentence is
    # the site's og:description (assemble_site.py), so an exact match here is what
    # guarantees a link to the repo and a link to the site say the same thing.
    command = edit_command(expected)
    print("drift: the published repository description differs from the catalogue's pitch.")
    print(f"  published: {description or '(empty)'}")
    print(f"  expected:  {expected}")
    print()
    print("Fix it with (needs admin rights; the workflow token cannot):")
    print(f"  {command}")
    set_output("status", "drift")
    if args.report is None:
        return 1

    body = issue_body(description, expected, stats["entries"])
    args.report.write_text(body + "\n", encoding="utf-8")
    step_summary("## Repository description is out of date\n\n" + body)
    print(
        "::warning title=Repository description::The published description is out of "
        "date. The step summary and the issue labelled description carry the command."
    )
    return 0


def report_social_preview() -> None:
    """Informational only. The social preview is the one image nothing can
    regenerate — GitHub has no upload API — so it is the durable card, whose
    only figure is a floor that growth can only understate. All CI can do is
    say whether it has been uploaded."""
    owner, name = SELF.split("/")
    data = graphql(
        f'{{ repository(owner: "{owner}", name: "{name}") {{ usesCustomOpenGraphImage }} }}'
    )
    uploaded = ((data or {}).get("repository") or {}).get("usesCustomOpenGraphImage")
    if uploaded is None:
        print("social preview: could not be read")
    elif uploaded:
        print("social preview: custom card uploaded (durable; its count is a floor)")
    else:
        print(
            "notice: no custom social preview is uploaded, so GitHub shows its generated "
            "card, which quotes the description checked below. To use the designed card, "
            "download https://kydlikebtc.github.io/awesome-jev/img/card.png and upload it "
            "at Settings → General → Social preview."
        )


if __name__ == "__main__":
    sys.exit(main())
