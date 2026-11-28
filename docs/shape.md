<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema and history/. Edit those, not this file. -->

# The catalogue's shape

<sub>[awesome-jev](../README.md) · [中文](shape.zh-CN.md)</sub>

Counts that describe this catalogue as a dataset, regenerated from `catalog.json` whenever it changes; the newest link check behind them is dated **2026-11-25**. They describe what the catalogue holds, which is what reached it through the sibling directories, this repository's discovery and its contributors, not the ecosystem at large. A star band is a popularity signal, not a quality verdict, and nothing here was run or reproduced by this repository. `python3 scripts/counts.py` prints the same numbers as text; the headline figures are on [the status page](status.md).

## Evidence by decision pattern

What the catalogue records about the rows filed under each pattern: reports counted, not a verdict. A row counts in every column that applies and under every pattern it is filed under. **Official documentation** is TypeSafe AI's own documentation pages (`kind: official-docs`). **Call site**, **wire shape** and **example only** count rows citing a file, by what `evidence.kind` records it shows: where the project calls Jev; a file speaking Jev's request shape rather than building on Jev; only an example the project ships. **Independent reports** are benchmark rows not flagged `vendor-reported`: their authors' measurements, not reproduced by this repository. **Negative results** are rows whose own author measured Jev for the use and concluded against it (author-stated; [listed on the status page](status.md#negative-results)). **No file cited** counts rows with no `evidence` (`evidence_none` may say why). The MCP server's `list_patterns` and each pattern's page give the same numbers.

| Pattern | Rows | Official documentation | Call site | Wire shape | Example only | Independent reports | Negative results | No file cited |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 311 | 3 | 300 | 7 | 0 | 13 | 1 | 4 |
| [Intent routing](by-pattern/intent-routing.md) | 70 | 3 | 58 | 0 | 1 | 4 | 0 | 11 |
| [Context compaction](by-pattern/context-compaction.md) | 62 | 0 | 62 | 0 | 0 | 2 | 2 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 206 | 2 | 198 | 4 | 0 | 15 | 0 | 4 |
| [Output validation](by-pattern/output-validation.md) | 198 | 2 | 193 | 1 | 0 | 14 | 1 | 4 |
| [Retry control](by-pattern/retry-control.md) | 10 | 0 | 9 | 1 | 0 | 0 | 0 | 0 |
| [Human escalation](by-pattern/human-escalation.md) | 117 | 7 | 102 | 5 | 0 | 11 | 1 | 10 |
| [Model routing](by-pattern/model-routing.md) | 116 | 2 | 106 | 2 | 2 | 0 | 1 | 6 |
| [Speculative fan-out](by-pattern/fan-out.md) | 58 | 3 | 49 | 1 | 1 | 2 | 0 | 7 |
| [Search & ranking](by-pattern/search-ranking.md) | 112 | 3 | 108 | 0 | 0 | 8 | 2 | 4 |
| [Structured extraction](by-pattern/data-extraction.md) | 41 | 4 | 37 | 0 | 0 | 4 | 0 | 4 |
| [Classification](by-pattern/classification.md) | 258 | 4 | 246 | 3 | 0 | 25 | 2 | 9 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 11 | 1 | 10 | 0 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 26 | 0 | 25 | 0 | 0 | 3 | 0 | 1 |
| [Support triage](by-pattern/support-triage.md) | 16 | 1 | 11 | 0 | 0 | 3 | 0 | 5 |
| [Content scoring](by-pattern/content-scoring.md) | 224 | 2 | 215 | 5 | 0 | 14 | 1 | 4 |
| [Recommendation](by-pattern/recommendation.md) | 6 | 0 | 6 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 554 | 6 | 406 | 108 | 0 | 35 | 1 | 40 |

35 independent reports are filed under `overview` and no other pattern, so this table cannot count them for the decision they measured until a person files them under it.

## Languages

Rows recording each language (`languages`; a row may record several). 32 rows record none.

| Language | Rows |
| --- | --- |
| `python` | 703 |
| `typescript` | 530 |
| `javascript` | 190 |
| `rust` | 76 |
| `go` | 72 |
| `swift` | 23 |
| `java` | 18 |
| `csharp` | 13 |
| `kotlin` | 13 |
| `ruby` | 13 |
| `php` | 12 |
| `shell` | 12 |
| `cpp` | 10 |
| `elixir` | 10 |
| `c` | 4 |
| `haskell` | 1 |
| `lua` | 1 |
| `pascal` | 1 |
| `scala` | 1 |

## How rows reach Jev

`platforms` records how a row reaches Jev. Discovery does not tag it: `scripts/discover_candidates.py` and the drafts it writes leave the field to the person adding a row, and `typesafe-api` is what a row records when nobody named another route. So the first group below counts that default at least as much as a finding: a row that reaches Jev through a pass-through may record `typesafe-api` alone ([compatibility](compatibility.md)). Each row counts in exactly one group.

| Group | Rows |
| --- | --- |
| `typesafe-api` and nothing else | 1277 |
| At least one value another surface in [the compatibility table](compatibility.md) stands for (a gateway, SDK or framework), and not `self-hosted` | 182 |
| Besides `typesafe-api`, only values no compatibility surface stands for (a host, tool or framework the example runs in, or a route that table does not describe), and not `self-hosted` | 101 |
| `self-hosted`, whatever else is recorded | 117 |
| No value recorded | 26 |

Every value rows record, with the compatibility surfaces that stand for it:

| Value | Compatibility surface | Rows |
| --- | --- | --- |
| `typesafe-api` | `typesafe-native` | 1487 |
| `openrouter` | `openrouter` | 122 |
| `self-hosted` | — | 117 |
| `claude-code` | — | 78 |
| `vercel-ai-gateway` | `vercel-eval`, `vercel-compat` | 62 |
| `mcp` | — | 48 |
| `cloudflare-workers-ai` | `cloudflare` | 14 |
| `opencode-zen` | — | 8 |
| `langchain` | `langchain` | 7 |
| `vercel-ai-sdk` | `vercel-eval`, `ai-sdk-direct` | 5 |
| `github` | — | 4 |
| `jevai-org` | — | 4 |
| `postgresql` | — | 4 |
| `discord` | — | 3 |
| `effect` | — | 2 |
| `litellm` | `litellm` | 2 |
| `pydantic-ai` | `pydantic-ai` | 2 |
| `ruby-llm` | — | 2 |
| `aimlapi` | `aimlapi` | 1 |
| `airflow` | — | 1 |
| `autogpt` | — | 1 |
| `bifrost` | `bifrost` | 1 |
| `composio` | — | 1 |
| `kiln` | — | 1 |
| `lancedb` | — | 1 |
| `langfuse` | — | 1 |
| `netlify` | `netlify` | 1 |
| `opik` | — | 1 |
| `rig` | `rig` | 1 |
| `spring-ai` | — | 1 |

## Licences

The licences the linked repositories declare are counted on [the sources page](sources.md#licences), beside what this repository's own licence covers.

## Stars by kind

Rows of each kind per star band, from GitHub's count at the last weekly refresh; a row without a repository has no count. The median is the band of the middle row (the lower of two). A band is a popularity signal, not a quality verdict, and says nothing about upkeep.

| Kind | Rows | With a star count | under 10 | ★10+ | ★100+ | ★1k+ | ★10k+ | ★100k+ | Median band |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Official docs (`official-docs`) | 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | ★1k+ |
| Integration (`integration`) | 44 | 32 | 12 | 9 | 1 | 4 | 5 | 1 | ★10+ |
| Project (`project`) | 849 | 827 | 441 | 246 | 97 | 22 | 19 | 2 | under 10 |
| Plugin (`plugin`) | 354 | 346 | 189 | 120 | 32 | 4 | 1 | 0 | under 10 |
| SDK (`sdk`) | 132 | 127 | 95 | 24 | 6 | 1 | 1 | 0 | under 10 |
| Snippet (`snippet`) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Tutorial (`tutorial`) | 25 | 22 | 10 | 8 | 2 | 2 | 0 | 0 | ★10+ |
| Article (`article`) | 15 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | under 10 |
| Video (`video`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Benchmark (`benchmark`) | 114 | 109 | 73 | 25 | 7 | 2 | 1 | 1 | under 10 |
| Discussion (`discussion`) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Jev-like alternative (`alternative`) | 130 | 122 | 28 | 48 | 32 | 12 | 2 | 0 | ★10+ |

## Languages by decision pattern

Rows per pattern recording each of the 6 most recorded languages; the rest share one column. A row recording two languages counts in both, and a row filed under two patterns counts in both.

| Pattern | `python` | `typescript` | `javascript` | `rust` | `go` | `swift` | Other languages |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 139 | 108 | 48 | 6 | 4 | 8 | 3 |
| [Intent routing](by-pattern/intent-routing.md) | 34 | 22 | 5 | 0 | 2 | 2 | 5 |
| [Context compaction](by-pattern/context-compaction.md) | 16 | 34 | 7 | 2 | 3 | 0 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 75 | 84 | 28 | 7 | 9 | 1 | 3 |
| [Output validation](by-pattern/output-validation.md) | 75 | 74 | 23 | 11 | 8 | 1 | 5 |
| [Retry control](by-pattern/retry-control.md) | 3 | 3 | 1 | 1 | 0 | 1 | 1 |
| [Human escalation](by-pattern/human-escalation.md) | 59 | 37 | 7 | 4 | 4 | 0 | 3 |
| [Model routing](by-pattern/model-routing.md) | 33 | 55 | 18 | 7 | 3 | 1 | 1 |
| [Speculative fan-out](by-pattern/fan-out.md) | 29 | 19 | 7 | 3 | 1 | 1 | 5 |
| [Search & ranking](by-pattern/search-ranking.md) | 46 | 35 | 8 | 10 | 8 | 1 | 6 |
| [Structured extraction](by-pattern/data-extraction.md) | 23 | 12 | 4 | 0 | 0 | 0 | 2 |
| [Classification](by-pattern/classification.md) | 109 | 76 | 36 | 7 | 5 | 1 | 22 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 5 | 3 | 2 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 9 | 6 | 7 | 2 | 1 | 0 | 0 |
| [Support triage](by-pattern/support-triage.md) | 10 | 4 | 0 | 0 | 1 | 0 | 3 |
| [Content scoring](by-pattern/content-scoring.md) | 99 | 74 | 33 | 6 | 2 | 3 | 11 |
| [Recommendation](by-pattern/recommendation.md) | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 232 | 119 | 46 | 34 | 38 | 9 | 68 |

## Patterns filed together

521 rows are filed under more than one pattern. The 10 pairs most often filed on the same row:

| Patterns | Rows |
| --- | --- |
| [Classification](by-pattern/classification.md) + [Content scoring](by-pattern/content-scoring.md) | 61 |
| [Safety gating](by-pattern/safety-gating.md) + [Output validation](by-pattern/output-validation.md) | 49 |
| [Tool selection](by-pattern/tool-selection.md) + [Safety gating](by-pattern/safety-gating.md) | 42 |
| [Safety gating](by-pattern/safety-gating.md) + [Classification](by-pattern/classification.md) | 42 |
| [Human escalation](by-pattern/human-escalation.md) + [Classification](by-pattern/classification.md) | 33 |
| [Tool selection](by-pattern/tool-selection.md) + [Output validation](by-pattern/output-validation.md) | 32 |
| [Safety gating](by-pattern/safety-gating.md) + [Human escalation](by-pattern/human-escalation.md) | 32 |
| [Safety gating](by-pattern/safety-gating.md) + [Content scoring](by-pattern/content-scoring.md) | 27 |
| [Human escalation](by-pattern/human-escalation.md) + [Content scoring](by-pattern/content-scoring.md) | 27 |
| [Output validation](by-pattern/output-validation.md) + [Classification](by-pattern/classification.md) | 26 |

## Authors

1586 rows name an author; they name 1451 different ones, compared by display name without regard to case. 1346 of them have one row here, 84 two, and 21 three or more; the most any one author has is 6. No author is named on this page: it shows how concentrated the catalogue is, not who contributes to it.

## Over time

The catalogue's counts at each weekly refresh, from the snapshots in `history/` (generated data, never a source): 8 since 2026-09-30, the newest 8 shown. A count is what was catalogued on that day, not how the ecosystem grew; a dash is a count that snapshot did not record. Candidates to read is the discovery queue's "To read" (issue #14), recorded since 2026-10-30: when it grows, drafting is behind discovery.

| Snapshot | Entries | With code | Rows citing a call site | Independent reports | Negative results | Alternatives | No licence declared | Candidates to read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | 1210 | 1182 | 1076 | 71 | 5 | 58 | 198 | — |
| 2026-10-08 | 1214 | 1185 | 1078 | 71 | 5 | 59 | 197 | — |
| 2026-10-14 | 1217 | 1186 | 1079 | 72 | 5 | 59 | 196 | — |
| 2026-10-21 | 1218 | 1187 | 1079 | 72 | 5 | 60 | 194 | — |
| 2026-10-28 | 1265 | 1233 | 1107 | 72 | 5 | 78 | 192 | — |
| 2026-11-04 | 1370 | 1338 | 1192 | 78 | 5 | 97 | 205 | 444 |
| 2026-11-11 | 1483 | 1451 | 1287 | 90 | 5 | 114 | 214 | 443 |
| 2026-11-25 | 1668 | 1636 | 1460 | 105 | 6 | 125 | 226 | 430 |

---

Generated by `scripts/build_shape.py` from `catalog.json`, `compat.json`, `patterns.json`, the entry schema and the snapshots in `history/`; edit those, not this page.
