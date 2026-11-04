#!/usr/bin/env python3
"""Hold launches/*.json and makers/*.json to the launch board's rules.

The schemas (schema/launch.schema.json, schema/maker.schema.json) say what each
file may hold; this says what they cannot: that a week's file is named for its
week, that its products are catalogued products, that a closed week has a
result for every launch and ranks 1 to n, that a product launches at most once
in 60 days, that a maker launching their own product is one of its makers,
and that a maker profile belongs to someone the catalogue names. The rules
themselves are in scripts/launches.py; this file only applies them, and lives
apart so the site build, which imports launches.py, does not import lint.py.

Run: python3 scripts/check_launches.py     # exit 1 on any problem
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import launches as L  # noqa: E402
import lint  # noqa: E402  (the catalogue's own draft-07 validator)


def check(catalog: list[dict], launch_files: dict[str, object], maker_files: dict[str, object],
          launch_schema: dict, maker_schema: dict) -> list[str]:
    """Every problem with the week and maker files, or []."""
    problems: list[str] = []
    rows = {r["slug"]: r for r in catalog if isinstance(r, dict) and "slug" in r}
    last_launch: dict[str, tuple[dt.date, str]] = {}
    for name in sorted(launch_files):
        data = launch_files[name]
        where = f"launches/{name}.json"
        if isinstance(data, str):
            problems.append(f"{where}: {data}")
            continue
        problems += [f"{where}: {e}" for e in lint.validate(data, launch_schema, "$").errors]
        if not isinstance(data, dict) or not isinstance(data.get("launches"), list):
            continue
        if data.get("week") != name:
            problems.append(f"{where}: week {data.get('week')!r} does not match the file name")
            continue
        try:
            monday, sunday = L.week_days(name)
        except ValueError as exc:
            problems.append(f"{where}: {exc}")
            continue
        status = data.get("status")
        closed = status == "closed"
        if closed != ("closed_on" in data) or closed != ("rules" in data):
            problems.append(f"{where}: closed_on and rules belong on a closed week, and only there")
        if data.get("rules") and data["rules"] not in L.RULES:
            problems.append(f"{where}: rules {data['rules']!r} is not one scripts/launches.py knows")
        if closed and L.day(data.get("closed_on")) and L.day(data["closed_on"]) <= sunday:
            problems.append(f"{where}: closed_on {data['closed_on']} is not after the week's Sunday {sunday}")
        if not closed and ("voters" in data or "returning_voters" in data):
            problems.append(f"{where}: voters and returning_voters are counted when the week closes, and only then")
        voters, returning = data.get("voters"), data.get("returning_voters")
        if isinstance(voters, int) and isinstance(returning, int) and returning > voters:
            problems.append(f"{where}: more returning voters ({returning}) than voters ({voters})")
        if isinstance(voters, int):
            cast = sum(int((x.get("result") or {}).get("votes") or 0) for x in data["launches"] if isinstance(x, dict))
            if voters > cast:
                problems.append(f"{where}: {voters} voters, but only {cast} votes on the board")
        seen_products: set[str] = set()
        ranks: list[int] = []
        for i, launch in enumerate(data["launches"]):
            at = f"{where} launches[{i}]"
            if not isinstance(launch, dict):
                continue
            slug = launch.get("product")
            row = rows.get(slug)
            if row is None:
                problems.append(f"{at}: product {slug!r} is not in catalog.json")
            elif not L.is_product(row):
                problems.append(f"{at}: {slug} is a {row.get('kind')} row without code or flagged "
                                f"as no example; only {', '.join(L.BOARD_KINDS)} rows with code launch")
            if slug in seen_products:
                problems.append(f"{at}: {slug} is on this week twice")
            seen_products.add(slug)
            submitted = L.day(launch.get("submitted_on"))
            if submitted and submitted > sunday:
                problems.append(f"{at}: submitted_on {launch['submitted_on']} is after the week ended")
            if "tier_at_open" in launch and status not in ("open", "closed"):
                problems.append(f"{at}: tier_at_open is written when the week opens")
            held = launch.get("status") in ("held", "removed")
            if held != ("reason" in launch):
                problems.append(f"{at}: a held or removed launch says why in `reason`, and only those do")
            if row is not None and launch.get("role") == "maker" and isinstance(launch.get("submitted_by"), str):
                if L.login_key(launch["submitted_by"]) not in {L.login_key(m) for m in L.makers_of(row)}:
                    problems.append(f"{at}: role maker, but {launch['submitted_by']} is not in {slug}'s makers")
            has_result = "result" in launch
            if closed and launch.get("status") == "scheduled" and not has_result:
                problems.append(f"{at}: the week is closed but this launch has no result")
            if has_result and not (closed and launch.get("status") == "scheduled"):
                problems.append(f"{at}: only a scheduled launch in a closed week has a result")
            if has_result and isinstance(launch["result"], dict):
                result = launch["result"]
                if isinstance(result.get("rank"), int):
                    ranks.append(result["rank"])
                if isinstance(result.get("votes"), int) and isinstance(result.get("discounted"), int) \
                        and result["discounted"] > result["votes"]:
                    problems.append(f"{at}: more votes discounted than cast")
                if isinstance(result.get("votes"), int) and isinstance(result.get("counted"), (int, float)) \
                        and result["counted"] > result["votes"]:
                    problems.append(f"{at}: more counted than cast")
            if launch.get("status") == "scheduled" and slug:
                before = last_launch.get(slug)
                if before and (monday - before[0]).days < L.RELAUNCH_DAYS:
                    problems.append(f"{at}: {slug} launched in {before[1]}; a product launches at most "
                                    f"once in {L.RELAUNCH_DAYS} days")
                last_launch[slug] = (monday, name)
        if closed and sorted(ranks) != list(range(1, len(ranks) + 1)):
            problems.append(f"{where}: ranks are not 1 to {len(ranks)}, each once")
    known = {L.login_key(m) for r in rows.values() for m in L.makers_of(r)}
    for name in sorted(maker_files):
        data = maker_files[name]
        where = f"makers/{name}.json"
        if isinstance(data, str):
            problems.append(f"{where}: {data}")
            continue
        problems += [f"{where}: {e}" for e in lint.validate(data, maker_schema, "$").errors]
        if isinstance(data, dict) and data.get("login") != name:
            problems.append(f"{where}: login {data.get('login')!r} does not match the file name")
        if L.login_key(name) not in known:
            problems.append(f"{where}: no catalogued row names {name} as a maker; a profile is for a maker page")
    return problems


def check_repository() -> list[str]:
    catalog = json.loads((L.ROOT / "catalog.json").read_text(encoding="utf-8"))
    return check(
        catalog, L.load_dir(L.LAUNCH_DIR), L.load_dir(L.MAKER_DIR),
        json.loads(L.LAUNCH_SCHEMA.read_text(encoding="utf-8")),
        json.loads(L.MAKER_SCHEMA.read_text(encoding="utf-8")),
    )


def main() -> int:
    problems = check_repository()
    for problem in problems:
        print(f"  error {problem}")
    files = len(L.load_dir(L.LAUNCH_DIR)) + len(L.load_dir(L.MAKER_DIR))
    print(f"launches: {files} file(s), {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
