import test from "node:test";
import assert from "node:assert/strict";
import { compareEntries, evidenceUrl, matchesEntry, verification, isIndependentReport } from "../site/catalog-core.mjs";

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

test("evidence links preserve repository overrides and encoded file paths", () => {
  assert.equal(evidenceUrl(row("x", {url: "https://github.com/owner/repo/pull/42", evidence: {path: "src/a b.ts"}})), "https://github.com/owner/repo/blob/HEAD/src/a%20b.ts");
  assert.equal(evidenceUrl(row("x", {repo: "https://github.com/other/repo", url: "https://example.com", evidence: {path: "src/main.py"}})), "https://github.com/other/repo/blob/HEAD/src/main.py");
  assert.equal(evidenceUrl(row("x", {url: "https://github.com.evil.example/o/r", evidence: {path: "x"}})), null);
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
