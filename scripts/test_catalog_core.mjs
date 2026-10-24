import test from "node:test";
import assert from "node:assert/strict";
import {
  compareEntries, evidenceKind, evidenceUrl, matchesEntry, verification, isIndependentReport, EVIDENCE_KINDS,
  queryFromState, shareUrl, stateFromQuery, TOGGLES, VIEWS, SUMMARY_SOURCES, MARKED_SOURCES, summaryMarks,
  UNINDEXED_KINDS, notIndexedByPattern, PRIMITIVES, primitiveLayers, repositoryFacts, siblingCitations,
  COARSE, platformRows, resolvePlatform, platformChoices, DIRECTIONS, measurementOf,
  NEGATIVE_FLAG, NEGATIVE_DIRECTION, isNegativeResult,
  WIRE_KIND, WIRE_WEIGHTS, wireOf, wireSources, wirePersonRead, wireEveryFileRead, wireRows, wireRemainder,
  wireRepository, pickerSteps, pickerCounts, primitivesReadBy,
} from "../site/catalog-core.mjs";
import { readFileSync } from "node:fs";

const row = (slug, extra = {}) => ({ slug, title: slug, patterns: ["context-compaction"], ...extra });

test("an HTTP success and dated call-site citation never imply an execution", () => {
  const result = verification(row("source", {checked: "2026-09-24", link_status: 200, evidence: {read_on: "2026-09-22"}}));
  assert.equal(result.linkOk, true);
  assert.equal(result.codeRead, "2026-09-22");
  assert.equal(result.runtime, "not-tested");
  assert.equal(result.performance, "not-reproduced");
  assert.equal(verification(row("undated", {link_status: 200})).linkOk, false);
  assert.equal(verification(row("failed", {checked: "2026-09-24", link_status: 404})).linkOk, false);
});

test("a model's reading of the call site is kept apart, and a person's wins", () => {
  const model = verification(row("m", {evidence: {model_read_on: "2026-10-20"}}));
  assert.equal(model.codeRead, null);
  assert.equal(model.codeModelRead, "2026-10-20");
  const both = verification(row("b", {evidence: {read_on: "2026-10-24", model_read_on: "2026-10-20"}}));
  assert.equal(both.codeRead, "2026-10-24");
  assert.equal(both.codeModelRead, null);
  assert.equal(verification(row("none")).codeModelRead, null);
  // The primitives read in that call site are the same reader's.
  const named = {question_types: ["noul"]};
  assert.equal(primitivesReadBy(row("m", {...named, evidence: {model_read_on: "2026-10-20"}})), "model");
  assert.equal(primitivesReadBy(row("b", {...named, evidence: {read_on: "2026-10-24", model_read_on: "2026-10-20"}})), "person");
  assert.equal(primitivesReadBy(row("u", named)), "person");
  assert.equal(primitivesReadBy(row("n", {evidence: {model_read_on: "2026-10-20"}})), null);
});

test("a summary in the project's own words is marked, and Chinese says when a model translated it", () => {
  const schema = JSON.parse(readFileSync(new URL("../schema/entry.schema.json", import.meta.url)));
  assert.deepEqual(SUMMARY_SOURCES, schema.properties.summary_source.enum);
  const taxonomy = JSON.parse(readFileSync(new URL("../taxonomy.json", import.meta.url)));
  assert.deepEqual(taxonomy.summary_sources.map(x => x.key), SUMMARY_SOURCES, "every mark has a label");
  const upstream = row("up", {summary_source: "upstream-description", zh_machine: true});
  assert.deepEqual(summaryMarks(upstream, "en"), ["upstream-description"]);
  assert.deepEqual(summaryMarks(upstream, "zh"), ["upstream-description", "zh-machine"]);
  assert.deepEqual(summaryMarks(row("stale", {summary_source: "upstream-description-stale"}), "en"), ["upstream-description-stale"]);
  // A model's text for the catalogue is marked too (since 2026-10-24).
  assert.deepEqual(summaryMarks(row("model", {summary_source: "model-written", zh_machine: true}), "zh"), ["model-written", "zh-machine"]);
  // A person's text, or no record, carries no source mark; zh_machine only describes the Chinese.
  assert.deepEqual(summaryMarks(row("curated", {summary_source: "curated", zh_machine: true}), "en"), []);
  assert.deepEqual(summaryMarks(row("curated", {summary_source: "curated", zh_machine: true}), "zh"), ["zh-machine"]);
  assert.deepEqual(summaryMarks(row("bare"), "zh"), []);
  assert.deepEqual(summaryMarks(row("odd", {summary_source: "toString", zh_machine: "yes"}), "zh"), []);
  assert.deepEqual(MARKED_SOURCES, SUMMARY_SOURCES.slice(1));
});

test("GitHub's repository facts are shown as recorded days and a count, never an age", () => {
  const facts = repositoryFacts(row("gh", {
    repo_created_at: "2026-09-17T07:03:00Z", repo_pushed_at: "2026-09-17T23:59:59Z", repo_commits: 1,
  }));
  assert.deepEqual(facts, {created: "2026-09-17", pushed: "2026-09-17", commits: 1});
  assert.deepEqual(repositoryFacts(row("none")), {created: null, pushed: null, commits: null});
  // Not GitHub's form: absent, not guessed at.
  const odd = repositoryFacts(row("odd", {repo_created_at: "2026-09-17", repo_pushed_at: 20260917, repo_commits: 0}));
  assert.deepEqual(odd, {created: null, pushed: null, commits: null});
  assert.equal(repositoryFacts(row("str", {repo_commits: "3"})).commits, null);
  // The schema's field names and timestamp form are the ones read here.
  const schema = JSON.parse(readFileSync(new URL("../schema/entry.schema.json", import.meta.url)));
  for (const field of ["repo_created_at", "repo_pushed_at"]) {
    assert.equal(schema.properties[field].pattern, "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$");
  }
  assert.equal(schema.properties.repo_commits.type, "integer");
});

test("a text signal about a primitive never becomes a person's reading of it", () => {
  const schema = JSON.parse(readFileSync(new URL("../schema/entry.schema.json", import.meta.url)));
  assert.deepEqual(PRIMITIVES, schema.properties.question_types.items.enum);
  assert.deepEqual(PRIMITIVES, schema.properties.primitives_seen.items.enum);
  const both = row("both", {question_types: ["noul", "choice"], primitives_seen: ["score", "noul"]});
  assert.deepEqual(primitiveLayers(both), {read: ["choice", "noul"], signalOnly: ["score"]});
  assert.deepEqual(primitiveLayers(row("seen", {primitives_seen: ["noul"]})), {read: [], signalOnly: ["noul"]});
  assert.deepEqual(primitiveLayers(row("none")), {read: [], signalOnly: []});
  // Searching for a primitive finds a reading, not a text match.
  const state = {q: "noul"};
  assert.equal(matchesEntry(row("seen", {primitives_seen: ["noul"]}), state), false);
  assert.equal(matchesEntry(row("read", {question_types: ["noul"]}), state), true);
});

test("an overview project or plugin with code is not yet indexed by pattern until someone reads it", () => {
  assert.deepEqual(UNINDEXED_KINDS, ["project", "plugin"]);
  const unplaced = (extra = {}) => row("p", {patterns: ["overview"], has_code: true, kind: "project", ...extra});
  assert.equal(notIndexedByPattern(unplaced()), true);
  assert.equal(notIndexedByPattern(unplaced({kind: "plugin"})), true);
  // A person's recorded reading ends it; so does any real pattern.
  assert.equal(notIndexedByPattern(unplaced({patterns_reviewed: "2026-09-27"})), false);
  assert.equal(notIndexedByPattern(unplaced({patterns_model_read_on: "2026-10-24"})), false);
  assert.equal(notIndexedByPattern(unplaced({patterns: ["tool-selection"]})), false);
  // Docs, SDKs and rows without code are what overview is for, or cannot be placed by reading code.
  assert.equal(notIndexedByPattern(unplaced({kind: "sdk"})), false);
  assert.equal(notIndexedByPattern(unplaced({kind: "official-docs"})), false);
  assert.equal(notIndexedByPattern(unplaced({has_code: false})), false);
  assert.equal(notIndexedByPattern(row("no-patterns", {has_code: true, kind: "project", patterns: undefined})), false);
});

test("an evidence record without a kind is a call site, and a row without one has none", () => {
  assert.deepEqual(EVIDENCE_KINDS, ["call-site", "wire-shape", "example-only"]);
  assert.equal(evidenceKind(row("none")), null);
  assert.equal(evidenceKind(row("bare", {evidence: {path: "a.py", matched: ["jev"]}})), "call-site");
  for (const kind of EVIDENCE_KINDS) {
    assert.equal(evidenceKind(row(kind, {evidence: {path: "a.py", matched: ["jev"], kind}})), kind);
  }
  // A value the schema does not know reads as the default, like a missing one.
  assert.equal(evidenceKind(row("odd", {evidence: {path: "a.py", matched: ["jev"], kind: "toString"}})), "call-site");
});

test("evidence links preserve repository overrides and encoded file paths", () => {
  assert.equal(evidenceUrl(row("x", {url: "https://github.com/owner/repo/pull/42", evidence: {path: "src/a b.ts"}})), "https://github.com/owner/repo/blob/HEAD/src/a%20b.ts");
  assert.equal(evidenceUrl(row("x", {repo: "https://github.com/other/repo", url: "https://example.com", evidence: {path: "src/main.py"}})), "https://github.com/other/repo/blob/HEAD/src/main.py");
  assert.equal(evidenceUrl(row("x", {url: "https://github.com.evil.example/o/r", evidence: {path: "x"}})), null);
});

test("evidence links agree with scripts/evidence_url.py on the cases both suites read", () => {
  // The READMEs and pattern pages build the same link in Python; this file is
  // the one list of cases both must pass (scripts/tests/test_call_site_links.py).
  const cases = JSON.parse(readFileSync(new URL("./tests/evidence_url_cases.json", import.meta.url)));
  assert.ok(cases.length >= 40);
  for (const { about, entry, url } of cases) assert.equal(evidenceUrl(entry), url, about);
});

test("editorial ranking can surface a useful small project ahead of stars", () => {
  const rows = [row("popular", {stars: 200000}), row("selected", {stars: 1})];
  assert.equal(rows.toSorted(compareEntries("curated", new Map([["selected", 0]])))[0].slug, "selected");
  assert.equal(rows.toSorted(compareEntries("stars"))[0].slug, "popular");
});

test("newest and last link check are separate clocks; missing dates sort last", () => {
  const rows = [row("old", {first_seen: "2026-09-20", checked: "2026-09-24"}), row("new", {first_seen: "2026-09-23", checked: "2026-09-22"}), row("undated")];
  assert.deepEqual(rows.toSorted(compareEntries("newest")).map(x => x.slug), ["new", "old", "undated"]);
  assert.deepEqual(rows.toSorted(compareEntries("checked")).map(x => x.slug), ["old", "new", "undated"]);
});

test("collections, bilingual search, and language filters intersect", () => {
  const entry = row("selected", {summary_zh: "上下文压缩插件", languages: ["typescript"], has_code: true});
  assert.equal(matchesEntry(entry, {q: "压缩", code: true, lang: "typescript"}, new Set(["selected"])), true);
  assert.equal(matchesEntry(entry, {q: "压缩", lang: "python"}, new Set(["selected"])), false);
  assert.equal(matchesEntry(entry, {}, new Set(["different"])), false);
  assert.equal(matchesEntry(entry, {q: "上下文"}, null, "上下文压缩"), true);
});

test("third-party benchmark is a report classification, not a replication certificate", () => {
  assert.equal(isIndependentReport(row("b", {kind: "benchmark", flags: ["unverified-claims"]})), true);
  assert.equal(isIndependentReport(row("b", {kind: "benchmark", flags: ["vendor-reported"]})), false);
  assert.equal(verification(row("b", {kind: "benchmark"})).performance, "not-reproduced");
});

test("short entry permalinks resolve exactly without changing ordinary text search", () => {
  const entries = [row("jev"), row("ai"), row("every"), row("typesafe"), row("jev-router", {summary: "An AI tool using TypeSafe Jev for every request"})];
  for (const slug of ["jev", "ai", "every", "typesafe"]) {
    assert.deepEqual(entries.filter(e => matchesEntry(e, {entry: slug})).map(e => e.slug), [slug]);
  }
  assert.ok(entries.filter(e => matchesEntry(e, {q: "jev"})).length > 1);
});

// ─── Platforms: compat.json's surfaces joined to the values rows record ─────
const PLATFORMS = JSON.parse(readFileSync(new URL("./tests/platform_cases.json", import.meta.url)));

test("a platform filter matches what the MCP server's rule matches, on the cases both suites read", () => {
  // scripts/tests/test_platform_values.py runs the same cases through query.py.
  const {compat, rows, cases} = PLATFORMS;
  assert.ok(cases.length >= 12);
  for (const c of cases) {
    const found = resolvePlatform(compat, rows, c.asked);
    if (c.unknown) {
      assert.equal(found, null, c.asked);
      continue;
    }
    assert.equal(found.surface ? found.surface.id : null, c.surface, c.asked);
    assert.deepEqual(found.values, c.values, c.asked);
    assert.equal(found.coarse, c.coarse, c.asked);
    assert.deepEqual(platformRows(rows, found.values).map(e => e.slug), c.slugs, c.asked);
    const entries = rows.map(e => row(e.slug, e));
    assert.deepEqual(entries.filter(e => matchesEntry(e, {platform: c.asked}, null, "", found.values)).map(e => e.slug), c.slugs, c.asked);
  }
  assert.equal(resolvePlatform(compat, rows, ""), null);
  assert.equal(resolvePlatform(null, rows, "github").values[0], "github", "no compat.json: a recorded value still resolves");
});

test("a coarse match names the other surfaces it may stand for", () => {
  const {compat, rows} = PLATFORMS;
  assert.equal(COARSE, "coarse");
  assert.deepEqual(resolvePlatform(compat, rows, "gw-a").others.map(p => p.id), ["gw-b"]);
  assert.deepEqual(resolvePlatform(compat, rows, "native").others, []);
  assert.deepEqual(resolvePlatform(compat, rows, "gw").others.map(p => p.id), ["gw-a", "gw-b"]);
  assert.deepEqual(resolvePlatform(compat, rows, "github").others, []);
});

test("without a resolved platform the filter matches the value itself, whole", () => {
  const entry = row("r", {platforms: ["vercel-ai-gateway"]});
  assert.equal(matchesEntry(entry, {platform: "vercel-ai-gateway"}), true);
  assert.equal(matchesEntry(entry, {platform: "vercel"}), false, "a fragment never matches");
  assert.equal(matchesEntry(row("none"), {platform: "vercel-ai-gateway"}), false);
  assert.equal(matchesEntry(entry, {platform: "vercel-compat"}, null, "", ["vercel-ai-gateway"]), true);
  // The platform names stay searchable as text, as before.
  assert.equal(matchesEntry(entry, {q: "gateway"}), true);
});

test("the platform choices are the surfaces with rows, then the values no surface lists", () => {
  const {compat, rows} = PLATFORMS;
  assert.deepEqual(platformChoices(compat, rows), {
    surfaces: [
      {id: "native", name: "Native", coarse: true, n: 2},
      {id: "gw-a", name: "Gateway A", coarse: true, n: 2},
      {id: "gw-b", name: "Gateway B", coarse: true, n: 1},
      {id: "edge", name: "Edge", coarse: false, n: 1},
      {id: "self", name: "Self", coarse: false, n: 1},
    ],
    other: [{value: "github", n: 2}],
  });
  assert.deepEqual(platformChoices(null, rows).surfaces, []);
});

test("every surface in the real compat.json lists its values, and every value rows record is joined", () => {
  const compat = JSON.parse(readFileSync(new URL("../compat.json", import.meta.url)));
  const taxonomy = JSON.parse(readFileSync(new URL("../taxonomy.json", import.meta.url)));
  const catalog = JSON.parse(readFileSync(new URL("../catalog.json", import.meta.url)));
  for (const p of compat.platforms) assert.ok(Array.isArray(p.catalog_platforms), p.id);
  const {surfaces, other} = platformChoices(compat, catalog);
  assert.ok(surfaces.length > 0);
  assert.deepEqual(other.map(o => o.value).filter(v => !taxonomy.platforms_without_surface.includes(v)), []);
});

// ─── URL state: every view and filter is a shareable link ─────────────────
const DEFAULTS = {entry: "", collection: "", sort: "curated", pattern: "", kind: "", lang: "", platform: "", q: "", code: false, off: false, indep: false, noflag: false, neg: false};
const OPTIONS = {languages: ["en", "zh"], collections: ["first-call", "build", "measured"]};
const read = (search, hash = "") => stateFromQuery(search, hash, OPTIONS);

test("a default catalogue writes only the language", () => {
  assert.equal(queryFromState(DEFAULTS, "catalog", "en").toString(), "lang=en");
  assert.deepEqual(read("?lang=en"), {lang: "en", view: "catalog", state: DEFAULTS});
});

test("parameter names and order stay what already-shared links use", () => {
  const state = {...DEFAULTS, collection: "build", sort: "stars", pattern: "tool-selection", kind: "project", lang: "python", q: "retry budget", code: true, off: true, indep: true, noflag: true};
  assert.equal(
    queryFromState(state, "prims", "zh").toString(),
    "view=prims&collection=build&sort=stars&p=tool-selection&k=project&lang_f=python&q=retry+budget&code=1&off=1&indep=1&noflag=1&lang=zh",
  );
  // `platform` joined the list on 2026-09-28, after lang_f; a link without it reads as before.
  // docs/compatibility.md links each surface as ?platform=<id>&lang=en.
  assert.equal(
    queryFromState({...state, platform: "cloudflare"}, "catalog", "en").toString(),
    "collection=build&sort=stars&p=tool-selection&k=project&lang_f=python&platform=cloudflare&q=retry+budget&code=1&off=1&indep=1&noflag=1&lang=en",
  );
  assert.deepEqual(read("?platform=vercel-compat&lang=en").state, {...DEFAULTS, platform: "vercel-compat"});
  // `neg` joined the toggles on 2026-09-28, after noflag; a link without it reads as before.
  assert.equal(
    queryFromState({...state, neg: true}, "catalog", "en").toString(),
    "collection=build&sort=stars&p=tool-selection&k=project&lang_f=python&q=retry+budget&code=1&off=1&indep=1&noflag=1&neg=1&lang=en",
  );
  assert.deepEqual(read("?neg=1&lang=en").state, {...DEFAULTS, neg: true});
});

test("every view, sort, toggle and filter survives a round trip", () => {
  for (const view of VIEWS) {
    for (const sort of ["curated", "newest", "checked", "stars", "pattern"]) {
      for (const toggle of TOGGLES) {
        const state = {...DEFAULTS, sort, collection: "measured", pattern: "safety-gating", kind: "benchmark", lang: "go", platform: "typesafe-native", q: "上下文 压缩", [toggle]: true};
        const back = read("?" + queryFromState(state, view, "zh").toString());
        assert.deepEqual(back, {lang: "zh", view, state});
      }
    }
  }
});

test("values the page cannot show fall back instead of reaching the state", () => {
  const back = read("?sort=random&collection=nope&lang=fr&view=graph&code=true&off=0");
  assert.equal(back.lang, null);
  assert.equal(back.view, "catalog");
  assert.deepEqual(back.state, DEFAULTS);
  // Inherited object keys are not languages (a lookup in the strings table would say they were).
  assert.equal(read("?lang=constructor").lang, null);
});

test("the hash names a view only when the query does not", () => {
  assert.equal(read("", "#compat").view, "compat");
  assert.equal(read("?view=prims", "#compat").view, "prims");
  // A bare #slug is an entry permalink: the catalogue, nothing filtered.
  assert.deepEqual(read("", "#jev-router"), {lang: null, view: "catalog", state: DEFAULTS});
});

test("reading the URL always clears the entry being revealed", () => {
  assert.equal(read("?entry=jev-router&q=x").state.entry, "");
});

test("a shared URL keeps the hash only while following its permalink", () => {
  const query = queryFromState({...DEFAULTS, q: "gate"}, "catalog", "en");
  assert.equal(shareUrl(query, {pathname: "/awesome-jev/", hash: "#jev-router"}), "?q=gate&lang=en");
  assert.equal(shareUrl(query, {pathname: "/awesome-jev/", hash: "#jev-router", keepHash: true}), "?q=gate&lang=en#jev-router");
  assert.equal(shareUrl(new URLSearchParams(), {pathname: "/awesome-jev/", hash: "#x", keepHash: true}), "/awesome-jev/#x");
});

test("a sibling-list citation is one fixed shape, and nothing else in sources counts as one", () => {
  // The same cases as scripts/tests/test_sibling_citations.py SHAPES: the two rules must agree.
  const shapes = [
    [{catalog: "heyjunpenn/awesome-jev", url: "https://github.com/heyjunpenn/awesome-jev"}, true],
    [{catalog: "Omrigotlieb/awesome-jev", url: "https://github.com/Omrigotlieb/awesome-jev"}, true],
    [{catalog: "a.b/c-d_e.f", url: "https://github.com/a.b/c-d_e.f"}, true],
    [{catalog: "heyjunpenn/awesome-jev", url: "https://github.com/heyjunpenn/awesome-jev/"}, false],
    [{catalog: "heyjunpenn/Awesome-Jev", url: "https://github.com/heyjunpenn/awesome-jev"}, false],
    [{catalog: "heyjunpenn's list", url: "https://github.com/heyjunpenn/awesome-jev"}, false],
    [{catalog: "maintainer submission", url: "https://github.com/kydlikebtc/awesome-jev"}, false],
    [{catalog: "sibling-list aggregate (docs/sibling-lists.txt)", url: "https://github.com/kydlikebtc/awesome-jev/blob/main/docs/sibling-lists.txt"}, false],
    [{catalog: "a/b/c", url: "https://github.com/a/b/c"}, false],
    [{catalog: "a/..", url: "https://github.com/a/.."}, false],
    [{catalog: "a/b", url: "http://github.com/a/b"}, false],
    [{catalog: "a/b", url: "https://github.com/a/b", note: "x"}, false],
    [{catalog: "a/b"}, false],
  ];
  for (const [source, cited] of shapes) {
    assert.equal(siblingCitations({sources: [source]}).length, cited ? 1 : 0, JSON.stringify(source));
  }
  const entry = row("r", {sources: [
    {catalog: "GitHub code search", url: "https://github.com/search"},
    {catalog: "a/list", url: "https://github.com/a/list"},
    {catalog: "b/list", url: "https://github.com/b/list"},
  ]});
  assert.deepEqual(siblingCitations(entry), [
    {name: "a/list", url: "https://github.com/a/list"},
    {name: "b/list", url: "https://github.com/b/list"},
  ]);
  assert.deepEqual(siblingCitations(row("none")), []);
});

test("a benchmark's measurement is read as recorded, and its directions are the schema's", () => {
  const schema = JSON.parse(readFileSync(new URL("../schema/entry.schema.json", import.meta.url)));
  assert.deepEqual(DIRECTIONS, schema.properties.measurement.properties.direction.enum);
  const taxonomy = JSON.parse(readFileSync(new URL("../taxonomy.json", import.meta.url)));
  assert.deepEqual(taxonomy.measurement_directions.map(x => x.key), DIRECTIONS, "every direction has a label");
  const measured = row("bench", {kind: "benchmark", measurement: {task: "Rerank", direction: "mixed"}});
  assert.deepEqual(measurementOf(measured), {task: "Rerank", direction: "mixed"});
  for (const measurement of [undefined, null, {}, [], "text"]) {
    assert.equal(measurementOf(row("none", {measurement})), null, JSON.stringify(measurement));
  }
});

test("a negative result is the flag or an unfavourable direction, on the cases the server shares", () => {
  const {cases} = JSON.parse(readFileSync(new URL("./tests/negative_cases.json", import.meta.url)));
  assert.ok(cases.length >= 10);
  for (const c of cases) {
    assert.equal(isNegativeResult(c.entry), c.negative, c.name);
    assert.equal(isIndependentReport(c.entry), c.independent, c.name);
  }
  const taxonomy = JSON.parse(readFileSync(new URL("../taxonomy.json", import.meta.url)));
  assert.ok(taxonomy.flags.some(f => f.key === NEGATIVE_FLAG), "the flag has a label");
  assert.ok(DIRECTIONS.includes(NEGATIVE_DIRECTION));
  const neg = row("neg", {kind: "plugin", flags: [NEGATIVE_FLAG]});
  const pos = row("pos", {kind: "benchmark", measurement: {task: "t", direction: "favourable"}});
  assert.equal(matchesEntry(neg, {...DEFAULTS, neg: true}), true);
  assert.equal(matchesEntry(pos, {...DEFAULTS, neg: true}), false);
  assert.equal(matchesEntry(pos, DEFAULTS), true);
});

test("the compatibility view lists the alternatives that record their interface, on the cases the generator shares", () => {
  const {cases} = JSON.parse(readFileSync(new URL("./tests/wire_cases.json", import.meta.url)));
  assert.ok(cases.length >= 8);
  const entries = cases.map(c => c.entry);
  const listed = new Set(wireRows(entries).map(e => e.slug));
  for (const c of cases) {
    assert.equal(listed.has(c.entry.slug), c.wired, c.name);
    assert.equal(wirePersonRead(wireOf(c.entry)), c.person_read, c.name);
    assert.equal(wireEveryFileRead(wireOf(c.entry)), c.every_file_read, c.name);
    assert.equal(wireRepository(c.entry), c.repository, c.name);
  }
  assert.equal(wireRemainder(entries), cases.filter(c => c.unwired).length);
  assert.deepEqual(wireSources(null), []);
  const schema = JSON.parse(readFileSync(new URL("../schema/entry.schema.json", import.meta.url)));
  assert.deepEqual(WIRE_WEIGHTS, schema.properties.wire.properties.weights.enum);
  assert.equal(WIRE_KIND, "alternative");
});

test("every wire record in the real catalogue is on an alternative row the view lists", () => {
  const catalog = JSON.parse(readFileSync(new URL("../catalog.json", import.meta.url)));
  const withWire = catalog.filter(e => "wire" in e);
  assert.deepEqual(wireRows(catalog).map(e => e.slug), withWire.map(e => e.slug));
  for (const e of withWire) assert.match(wireRepository(e), /^[^/]+\/[^/]+$/, e.slug);
  assert.equal(wireRemainder(catalog), catalog.filter(e => e.kind === "alternative").length - withWire.length);
});

test("the primitive picker walks picker.json as scripts/picker.py does", () => {
  const { cases } = JSON.parse(readFileSync(new URL("./tests/picker_cases.json", import.meta.url)));
  assert.ok(cases.length >= 12);
  for (const c of cases) {
    const walked = pickerSteps(c.picker);
    if (c.walk === null) {
      assert.equal(walked, null, c.name);
      continue;
    }
    assert.deepEqual(walked.steps.map(s => [s.node.id, s.yes.id]), c.walk.steps, c.name);
    assert.equal(walked.last.id, c.walk.last, c.name);
  }
  const real = pickerSteps(JSON.parse(readFileSync(new URL("../picker.json", import.meta.url))));
  assert.ok(real && real.steps.length >= 5, "the committed picker is a decision list");
  assert.equal(pickerSteps(null), null);
});

test("a picker leaf is counted from stats.json only when it names a primitive and a pattern", () => {
  const stats = { primitive_layers_by_pattern: { "safety-gating": { noul: { read: 3, signal_only: 4 } } } };
  assert.deepEqual(pickerCounts(stats, { primitive: "noul", pattern_key: "safety-gating" }), { read: 3, signal_only: 4 });
  assert.deepEqual(pickerCounts(stats, { primitive: "choice", pattern_key: "fan-out" }), { read: 0, signal_only: 0 });
  assert.equal(pickerCounts(stats, { pattern_key: "fan-out" }), null);
  assert.equal(pickerCounts(stats, { primitive: "noul" }), null);
});
