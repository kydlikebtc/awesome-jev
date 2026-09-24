// Data-only catalogue behavior, shared by the page and its offline tests.
export const SORTS = ["curated", "newest", "checked", "stars", "pattern"];

export function verification(entry) {
  return {
    linkChecked: entry.checked || null,
    linkOk: Boolean(entry.checked && entry.link_status >= 200 && entry.link_status < 300),
    codeRead: entry.evidence?.read_on || null,
    // The catalogue records source inspection, not executions or replications.
    runtime: "not-tested",
    performance: "not-reproduced",
  };
}

export function evidenceUrl(entry) {
  if (!entry.evidence?.path) return null;
  for (const candidate of [entry.repo, entry.url]) {
    if (!candidate) continue;
    try {
      const url = new URL(candidate);
      const parts = url.pathname.split("/").filter(Boolean);
      if (url.protocol !== "https:" || url.hostname !== "github.com" || parts.length < 2) continue;
      const path = entry.evidence.path.split("/").map(encodeURIComponent).join("/");
      return `https://github.com/${parts[0]}/${parts[1]}/blob/HEAD/${path}`;
    } catch (_) { /* A malformed source cannot become an executable link. */ }
  }
  return null;
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

export function matchesEntry(entry, state, collectionSlugs = null, labels = "") {
  if (state.entry && entry.slug !== state.entry) return false;
  if (collectionSlugs && !collectionSlugs.has(entry.slug)) return false;
  if (state.pattern && !entry.patterns.includes(state.pattern)) return false;
  if (state.kind && entry.kind !== state.kind) return false;
  if (state.lang && !(entry.languages || []).includes(state.lang)) return false;
  if (state.code && !entry.has_code) return false;
  if (state.off && !entry.official) return false;
  if (state.noflag && (entry.flags || []).length) return false;
  if (state.indep && !isIndependentReport(entry)) return false;
  const hay = [entry.title, entry.summary, entry.summary_zh, entry.notes, entry.notes_zh,
    entry.slug, ...(entry.platforms || []), ...(entry.languages || []), ...entry.patterns,
    ...(entry.question_types || []), entry.author?.name, entry.repo_license, entry.url, labels]
    .filter(Boolean).join(" ").toLowerCase();
  return (state.q || "").trim().toLowerCase().split(/\s+/).every(word => hay.includes(word));
}
