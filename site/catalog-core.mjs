// Data-only catalogue behavior, shared by the page and its offline tests.
export const SORTS = ["curated", "newest", "checked", "stars", "pattern"];

export function verification(entry) {
  return {
    linkChecked: entry.checked || null,
    linkOk: Boolean(entry.checked && entry.link_status >= 200 && entry.link_status < 300),
    codeRead: entry.evidence?.read_on || null,
    // A model's reading of the call site (since 2026-10-24), kept apart and
    // shown as a model's; only where no person's reading is recorded.
    codeModelRead: (!entry.evidence?.read_on && entry.evidence?.model_read_on) || null,
    // The catalogue records source inspection, not executions or replications.
    runtime: "not-tested",
    performance: "not-reproduced",
  };
}

// What a cited file shows, as evidence.kind records it (schema/entry.schema.json).
// A record without the field is a call site; a row without evidence has none.
export const EVIDENCE_KINDS = ["call-site", "wire-shape", "example-only"];

export function evidenceKind(entry) {
  if (!entry.evidence) return null;
  return EVIDENCE_KINDS.includes(entry.evidence.kind) ? entry.evidence.kind : "call-site";
}

// Whose words a summary is, as summary_source records it (schema/entry.schema.json).
// The two upstream values are the project's own description, and model-written
// a model's text for the catalogue; they are marked wherever the summary is
// shown, as the READMEs mark them. `curated`, a person's text, is not.
export const SUMMARY_SOURCES = ["curated", "upstream-description", "upstream-description-stale", "model-written"];
export const MARKED_SOURCES = ["upstream-description", "upstream-description-stale", "model-written"];

// The provenance marks a card's summary carries in a language, in reading
// order: whose words it is, then, for the Chinese text only, that a model
// translated it (zh_machine describes summary_zh, never the English).
export function summaryMarks(entry, lang) {
  const marks = [];
  if (MARKED_SOURCES.includes(entry.summary_source)) marks.push(entry.summary_source);
  if (lang === "zh" && entry.zh_machine === true) marks.push("zh-machine");
  return marks;
}

// A project or plugin with code whose only pattern is `overview`, and no record
// of anyone reading it against the patterns (a person's `patterns_reviewed`,
// or since 2026-10-24 a model's `patterns_model_read_on`), is not yet indexed
// by pattern: `overview` is also what the keyword rules suggest when nothing
// matches. The overview listing shows these rows last, under their own
// heading, as the READMEs do. scripts/_stats.py not_indexed_by_pattern() is
// the same rule for the generated pages.
export const UNINDEXED_KINDS = ["project", "plugin"];

export function notIndexedByPattern(entry) {
  return Array.isArray(entry.patterns) && entry.patterns.length === 1 && entry.patterns[0] === "overview"
    && Boolean(entry.has_code) && UNINDEXED_KINDS.includes(entry.kind)
    && !entry.patterns_reviewed && !entry.patterns_model_read_on;
}

// The Jev primitives in the schema's order, and the two records of which ones a
// row uses, never merged. question_types is a person's reading of the code
// calling them (a model's where only a model read the call site:
// primitivesReadBy). primitives_seen is a script's text signal: the one file the
// row's evidence cites contains their request or answer shape, which is not a
// call. signalOnly is what the signal adds to the reading. scripts/_stats.py
// signal_only() is the same rule for the generated pages and the figures.
export const PRIMITIVES = ["choice", "score", "noul"];

export function primitiveLayers(entry) {
  const read = PRIMITIVES.filter(p => (entry.question_types || []).includes(p));
  const signalOnly = PRIMITIVES.filter(p => (entry.primitives_seen || []).includes(p) && !read.includes(p));
  return { read, signalOnly };
}

// Whose reading question_types is (since 2026-10-24): a model's when the row's
// call site records only a model's reading (evidence.model_read_on), since no
// person read the code; a person's otherwise; null without question_types.
// The MCP package's query.py primitives_read_by() is the same rule.
export function primitivesReadBy(entry) {
  if (!(entry.question_types || []).length) return null;
  return verification(entry).codeModelRead ? "model" : "person";
}

// The primitive picker (picker.json), walked as the README's figure draws it:
// from `start`, each node with the leaf its yes ends at, then the leaf the last
// node's no ends at. null when the file is not that decision list (lint.py
// refuses such a file; the page then leaves the picker out rather than guess).
// scripts/picker.py walk() is the same walk; scripts/tests/picker_cases.json
// holds the two to one answer.
export function pickerSteps(picker) {
  const byId = (items) => new Map((Array.isArray(items) ? items : []).filter(x => x && typeof x.id === "string").map(x => [x.id, x]));
  const nodes = byId(picker?.nodes), leaves = byId(picker?.leaves);
  const branch = (node, answer) => {
    const found = (Array.isArray(node.branches) ? node.branches : []).filter(b => b && b.answer === answer);
    return found.length === 1 ? found[0] : null;
  };
  const keys = (b) => Object.keys(b).sort().join(",");
  const steps = [], seen = new Set();
  let id = picker?.start;
  if (!nodes.has(id)) return null;
  // At most one pass per node, so a malformed file cannot spin.
  for (let pass = 0; pass < nodes.size; pass++) {
    const node = nodes.get(id);
    seen.add(id);
    const yes = branch(node, "yes"), no = branch(node, "no");
    if (!Array.isArray(node.branches) || node.branches.length !== 2 || !yes || !no) return null;
    if (keys(yes) !== "answer,leaf" || !leaves.has(yes.leaf)) return null;
    steps.push({ node, yes: leaves.get(yes.leaf) });
    if (keys(no) === "answer,leaf" && leaves.has(no.leaf)) return { steps, last: leaves.get(no.leaf) };
    if (keys(no) !== "answer,node" || !nodes.has(no.node) || seen.has(no.node)) return null;
    id = no.node;
  }
  return null;
}

// The counts printed beside a picker leaf that names a primitive and a pattern:
// stats.json's primitive_layers_by_pattern (scripts/_stats.py), the figure's own.
export function pickerCounts(stats, leaf) {
  if (!leaf?.primitive || !leaf?.pattern_key) return null;
  return stats?.primitive_layers_by_pattern?.[leaf.pattern_key]?.[leaf.primitive] || { read: 0, signal_only: 0 };
}

// GitHub's own facts about a row's repository, as the weekly refresh records
// them (repo_created_at, repo_pushed_at, repo_commits; scripts/refresh_metadata.py):
// the creation and last-push days in UTC and the default branch's commit count.
// Shown as recorded, never turned into an age or a verdict on upkeep; a value
// not in GitHub's form is shown as absent rather than guessed at.
const GITHUB_TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;

export function repositoryFacts(entry) {
  const day = value => typeof value === "string" && GITHUB_TIMESTAMP.test(value) ? value.slice(0, 10) : null;
  const commits = Number.isInteger(entry.repo_commits) && entry.repo_commits > 0 ? entry.repo_commits : null;
  return { created: day(entry.repo_created_at), pushed: day(entry.repo_pushed_at), commits };
}

// The sibling directories whose README links a row's repository, as the
// weekly run records them at the end of `sources` (scripts/attribute_sources.py):
// an item whose `catalog` is the list's owner/name and whose `url` is
// https://github.com/owner/name, and nothing else. scripts/sibling_lists.py
// is_citation() is the same rule. The lists copy from each other, so the
// number is how widely a project is mentioned, never a check of it.
const LIST_URL = /^https:\/\/github\.com\/([A-Za-z0-9][\w.-]*)\/([\w.-]+)$/;

export function siblingCitations(entry) {
  return (entry.sources || []).filter(source => {
    if (!source || typeof source !== "object" || Object.keys(source).length !== 2) return false;
    const { catalog, url } = source;
    const match = typeof url === "string" && LIST_URL.exec(url);
    return Boolean(match) && ![".", ".."].includes(match[2]) && typeof catalog === "string"
      && url === `https://github.com/${catalog}`;
  }).map(({ catalog, url }) => ({ name: catalog, url }));
}

export function evidenceUrl(entry) {
  if (!entry.evidence?.path) return null;
  for (const candidate of [entry.repo, entry.url]) {
    if (!candidate) continue;
    try {
      const url = new URL(candidate);
      // The URL Standard added ^ to the characters a path percent-encodes;
      // engines from before that change (Node 22, older browsers) leave it
      // bare, so one row got a different link on each. Encode it here, so every
      // engine prints the link scripts/evidence_url.py writes into the READMEs.
      const parts = url.pathname.split("/").filter(Boolean).map(part => part.replaceAll("^", "%5E"));
      if (url.protocol !== "https:" || url.hostname !== "github.com" || parts.length < 2) continue;
      const path = entry.evidence.path.split("/").map(encodeURIComponent).join("/");
      return `https://github.com/${parts[0]}/${parts[1]}/blob/HEAD/${path}`;
    } catch (_) { /* A malformed source cannot become an executable link. */ }
  }
  return null;
}

// How compat.json's surfaces meet the catalogue: each surface lists in
// `catalog_platforms` the values rows record in `platforms` for it, and says
// `granularity: "coarse"` when such a value does not tell it apart from
// another route. A platform filter is a surface id, standing for the values it
// lists, or a value rows record, standing for itself; matched whole, ignoring
// case, never as a fragment. src/awesome_jev_mcp/query.py resolve_platform()
// is the same rule for the MCP server and docs/compatibility.md.
export const COARSE = "coarse";

const surfaceValues = surface => surface.catalog_platforms || [];

export function platformRows(entries, values) {
  const wanted = new Set(values);
  return entries.filter(e => (e.platforms || []).some(p => wanted.has(p)));
}

// {surface: the compat.json surface or null, values: what it matches,
// coarse, others: the other surfaces a coarse match may stand for}, or null
// when `asked` names neither a surface nor a value.
export function resolvePlatform(compat, entries, asked) {
  const key = String(asked || "").trim().toLowerCase();
  if (!key) return null;
  const surfaces = compat?.platforms || [];
  const surface = surfaces.find(p => String(p.id || "").toLowerCase() === key);
  if (surface) {
    const values = surfaceValues(surface);
    const others = surfaces.filter(p => p !== surface && surfaceValues(p).some(v => values.includes(v)));
    return { surface, values, coarse: surface.granularity === COARSE, others };
  }
  const known = new Set([...entries.flatMap(e => e.platforms || []), ...surfaces.flatMap(surfaceValues)]);
  const value = [...known].sort().find(v => v.toLowerCase() === key);
  if (!value) return null;
  const listing = surfaces.filter(p => surfaceValues(p).includes(value));
  return { surface: null, values: [value], coarse: listing.some(p => p.granularity === COARSE), others: listing };
}

// The platform filter's choices: compat.json's surfaces in its order with how
// many rows each stands for (those with none left out), then every value rows
// record that no surface lists, alphabetically, with its count.
export function platformChoices(compat, entries) {
  const surfaces = (compat?.platforms || [])
    .map(p => ({ id: p.id, name: p.name, coarse: p.granularity === COARSE, n: platformRows(entries, surfaceValues(p)).length }))
    .filter(s => s.n);
  const claimed = new Set((compat?.platforms || []).flatMap(surfaceValues));
  const other = [...new Set(entries.flatMap(e => e.platforms || []))].filter(v => !claimed.has(v)).sort()
    .map(value => ({ value, n: platformRows(entries, [value]).length }));
  return { surfaces, other };
}

// A kind: benchmark row's `measurement` indexes its own author's report
// (schema/entry.schema.json): the task, named datasets, comparators, kinds of
// metric, n, the model string, when, and the author's `direction`. Nothing in
// it was measured here, and a direction is the author's own conclusion, so
// every surface showing one says it is author-stated and not reproduced here.
// src/awesome_jev_mcp/query.py measurement_of() is the same rule.
export const DIRECTIONS = ["favourable", "mixed", "unfavourable", "inconclusive"];

export function measurementOf(entry) {
  const m = entry.measurement;
  return m && typeof m === "object" && !Array.isArray(m) && Object.keys(m).length ? m : null;
}

// A negative result: a row whose own author measured Jev for its use and
// concluded against it. A benchmark says so in its measurement's direction
// (unfavourable); any other row carries the negative-result flag. The page
// derives "negative" from either, as src/awesome_jev_mcp/query.py
// is_negative_result() does for the server and the generated pages; both are
// held to the cases in scripts/tests/negative_cases.json.
export const NEGATIVE_FLAG = "negative-result";
export const NEGATIVE_DIRECTION = "unfavourable";

export function isNegativeResult(entry) {
  if ((entry.flags || []).includes(NEGATIVE_FLAG)) return true;
  return (measurementOf(entry) || {}).direction === NEGATIVE_DIRECTION;
}

// An alternative row's `wire`: what the project's own files show about the
// interface it offers in place of Jev (scripts/wire.py, schema/entry.schema.json).
// The Compatibility view lists the alternative rows that record one and counts
// those that do not, as docs/compatibility.md does; both suites read the cases
// in scripts/tests/wire_cases.json.
export const WIRE_KIND = "alternative";
export const WIRE_WEIGHTS = ["open", "closed", "proxy"];

export function wireOf(entry) {
  const w = entry.wire;
  return w && typeof w === "object" && !Array.isArray(w) ? w : null;
}

// The well-formed items of wire.source (lint reports the rest).
export function wireSources(wire) {
  const items = wire && Array.isArray(wire.source) ? wire.source : [];
  return items.filter(i => i && typeof i === "object" && !Array.isArray(i) && typeof i.path === "string" && Array.isArray(i.matched));
}

// Every cited file carries a person's reading date.
export function wirePersonRead(wire) {
  const items = wireSources(wire);
  return items.length > 0 && items.every(i => "read_on" in i);
}

// Every cited file carries a reading date, a person's or (since 2026-10-24) a
// model's. scripts/wire.py every_file_read() is the same rule.
export function wireEveryFileRead(wire) {
  const items = wireSources(wire);
  return items.length > 0 && items.every(i => "read_on" in i || "model_read_on" in i);
}

export function wireRows(entries) {
  return entries.filter(e => e.kind === WIRE_KIND && wireOf(e));
}

export function wireRemainder(entries) {
  return entries.filter(e => e.kind === WIRE_KIND && !wireOf(e)).length;
}

// owner/name of the GitHub repository the cited files are read in, as
// evidenceUrl() spells it in their links; null off GitHub. Alternatives'
// titles repeat (openjev, OpenJev, open-jev, Open-Jev), so the view prints it
// beside each title, as docs/compatibility.md does.
export function wireRepository(entry) {
  const url = evidenceUrl({ ...entry, evidence: { path: "x" } });
  return url ? url.split("/").slice(3, 5).join("/") : null;
}

export function isIndependentReport(entry) {
  return entry.kind === "benchmark" && !(entry.flags || []).includes("vendor-reported");
}

const originalOrder = (a, b) =>
  Number(Boolean(b.official)) - Number(Boolean(a.official)) ||
  Number(Boolean(b.has_code)) - Number(Boolean(a.has_code)) ||
  (b.stars || 0) - (a.stars || 0) ||
  a.title.localeCompare(b.title) || a.slug.localeCompare(b.slug);

export function compareEntries(sort, ranks = new Map()) {
  return (a, b) => {
    if (sort === "curated") {
      const diff = (ranks.get(a.slug) ?? Infinity) - (ranks.get(b.slug) ?? Infinity);
      if (diff) return diff;
    }
    if (sort === "newest") {
      const diff = (b.first_seen || "").localeCompare(a.first_seen || "");
      if (diff) return diff;
    }
    if (sort === "checked") {
      const diff = (b.checked || "").localeCompare(a.checked || "");
      if (diff) return diff;
    }
    if (sort === "stars" && (b.stars || 0) !== (a.stars || 0)) return (b.stars || 0) - (a.stars || 0);
    return originalOrder(a, b);
  };
}

// `platformValues` is what state.platform resolved to (resolvePlatform()); without
// it the filter matches the value itself, whole.
export function matchesEntry(entry, state, collectionSlugs = null, labels = "", platformValues = null) {
  if (state.entry && entry.slug !== state.entry) return false;
  if (collectionSlugs && !collectionSlugs.has(entry.slug)) return false;
  if (state.pattern && !entry.patterns.includes(state.pattern)) return false;
  if (state.kind && entry.kind !== state.kind) return false;
  if (state.lang && !(entry.languages || []).includes(state.lang)) return false;
  if (state.platform && !(entry.platforms || []).some(p => (platformValues || [state.platform]).includes(p))) return false;
  if (state.code && !entry.has_code) return false;
  if (state.off && !entry.official) return false;
  if (state.noflag && (entry.flags || []).length) return false;
  if (state.indep && !isIndependentReport(entry)) return false;
  if (state.neg && !isNegativeResult(entry)) return false;
  // question_types and not primitives_seen: a search for a primitive finds the
  // rows a person read calling it, never rows a text match alone suggests.
  const hay = [entry.title, entry.summary, entry.summary_zh, entry.notes, entry.notes_zh,
    entry.slug, ...(entry.platforms || []), ...(entry.languages || []), ...entry.patterns,
    ...(entry.question_types || []), entry.author?.name, entry.repo_license, entry.url, labels]
    .filter(Boolean).join(" ").toLowerCase();
  return (state.q || "").trim().toLowerCase().split(/\s+/).every(word => hay.includes(word));
}

// ─── URL state ────────────────────────────────────────────────
// Every view and filter round-trips through the query string, so any state
// is a shareable link. Pure: the page passes `location` in and applies what
// comes back. The parameter names are public — links in READMEs, pattern
// pages and elsewhere already use them — so rename none of them.
export const VIEWS = ["catalog", "prims", "compat"];
export const TOGGLES = ["code", "off", "indep", "noflag", "neg"];

export function queryFromState(state, view, lang) {
  const q = new URLSearchParams();
  if (view !== "catalog") q.set("view", view);
  if (state.collection) q.set("collection", state.collection);
  if (state.sort !== "curated") q.set("sort", state.sort);
  if (state.pattern) q.set("p", state.pattern);
  if (state.kind) q.set("k", state.kind);
  if (state.lang) q.set("lang_f", state.lang);
  if (state.platform) q.set("platform", state.platform);
  if (state.q) q.set("q", state.q);
  for (const t of TOGGLES) if (state[t]) q.set(t, "1");
  q.set("lang", lang);
  return q;
}

// Only retain a hash while following its permalink. A later filter or view
// selection is new intent and must not restore the old entry.
export function shareUrl(query, { pathname, hash, keepHash = false }) {
  return (query.toString() ? "?" + query.toString() : pathname) + (keepHash ? hash : "");
}

// `lang` is null when the URL names no language the page has; the caller then
// keeps the one it chose. A bare #slug (no query) is an entry permalink: it
// yields the catalogue with every filter at its default, and the page reveals
// the entry itself.
export function stateFromQuery(search, hash, { languages, collections }) {
  const q = new URLSearchParams(search);
  const view = q.get("view") || (hash || "").replace("#", "");
  return {
    lang: languages.includes(q.get("lang")) ? q.get("lang") : null,
    view: VIEWS.includes(view) ? view : "catalog",
    state: {
      entry: "",
      collection: collections.includes(q.get("collection")) ? q.get("collection") : "",
      sort: SORTS.includes(q.get("sort")) ? q.get("sort") : "curated",
      pattern: q.get("p") || "",
      kind: q.get("k") || "",
      lang: q.get("lang_f") || "",
      platform: q.get("platform") || "",
      q: q.get("q") || "",
      ...Object.fromEntries(TOGGLES.map(t => [t, q.get(t) === "1"])),
    },
  };
}
