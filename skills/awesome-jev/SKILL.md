---
name: awesome-jev
description: Use when writing code that calls Jev, TypeSafe AI's System One decision model — choosing a model string, picking between choice/score/noul, designing a confidence threshold, or looking for a worked example of a specific decision such as tool selection, safety gating or context compaction. Also use when porting Jev code between gateways (Vercel, Cloudflare, OpenRouter, LiteLLM), because the model string, field names and request shape all differ per platform.
---

# Building with Jev

A source-attributed catalogue of public Jev examples, indexed by the decision each one
makes. Use it to find how someone already solved the decision you are wiring up,
and to avoid the mistakes that recur in this ecosystem.

## Get the facts right first

These are the errors that show up most often in generated Jev code.

**The yes/no primitive is `noul`.** Not "binary", not "boolean". One SDK — the
Vercel AI SDK evaluation API — spells it `boolean` and reads `.probability`;
everywhere else it is `noul` and `.noul`. Much of the press coverage got this
wrong, so training data is contaminated.

**`noul` answers carry no `confidence` field.** The probability _is_ the answer.
`choice` and `score` do carry one. A helper that reads `.confidence` uniformly
across all three returns nothing for a third of the questions.

**There is no portable model string.** `jev-latest` on the native API,
`typesafe-ai/jev` on Vercel, `typesafe/jev` on Cloudflare, `typesafe/jev-1.13`
on OpenRouter. **`typesafe/jev-1` exists nowhere** and is the most repeated
fabrication about this model — check before writing one.

**Input is text only.** String, JSON object, or array of text. No images, no
audio. Pre-process to text or typed fields.

**It cannot be run locally.** No weights are published. Anything claiming to run
Jev locally is a different model with a compatible wire format, and a compatible
API implies nothing about compatible calibration — thresholds do not transfer.

## Hard limits

|                  |                                                                 |
| ---------------- | --------------------------------------------------------------- |
| `choice` options | max 255                                                         |
| `score` levels   | 2 to 10, 0-indexed, ordered low to high                         |
| Context          | 64k tokens per request; 32k for state plus the longest question |
| Output tokens    | free — the model generates no text                              |
| Streaming        | not supported on any surface                                    |

A `score` is probability-weighted and lands _between_ levels — the official
example returns `1.05` on a three-level scale. Do not assume an integer.

## Querying the catalogue

If the MCP server is available, prefer it over guessing:

- `search_examples(pattern=…, language=…, question_type=…)` — worked examples of
  a specific decision
- `check_model_string(model)` — before writing any model string
- `compatibility(surface=…)` — before porting between gateways
- `list_patterns()` — the taxonomy, including which decisions nobody has
  published an example of

Every result carries a `data` line saying where the catalogue came from and how
current it is. If it begins `STALE`, the server could not reach GitHub and is
answering from a cache or from the snapshot it was installed with — say so when
you rely on it, the same way you would pass on a row's caveat flags.

The Claude Code plugin for this repository starts the server for you. Elsewhere,
`pip install awesome-jev-mcp` and run `awesome-jev-mcp`.

Without it, read
[`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json)
and
[`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json)
directly, or [the searchable site](https://kydlikebtc.github.io/awesome-jev/).

## Design rules worth following

**Always give a closed choice an escape hatch.** A `choice` must return one of
its options, so an agent with no suitable tool returns the least wrong tool
rather than declining. Add a `none` option, and consider a separate `noul` for
"is a tool needed at all" — those are different questions, one relative and one
absolute.

**Ask everything in one request.** The state is read once and every question is
evaluated against it in parallel, so a second question costs roughly its own
tokens rather than a round trip. Ask speculatively and let code pick what
mattered.

**Thresholds are policy, not modelling.** They depend on what being wrong costs.
One catalogued production system uses seven different thresholds for seven email
decisions, ranging from 0.3 to 0.9. A threshold tuned on a `noul` probability is
not a `choice` confidence, and one tuned against a model version does not
survive an alias moving — pin the version once you have tuned anything.

**A probabilistic gate is not a security boundary.** It is useful defence in
depth in front of a shell command, a write or a spend. It is not a permission
system: an attacker chooses the input, and the vendor's own documentation names
adversarial content as a known weak spot. Anything destructive or irreversible
needs a deterministic rule or a human.

**Keep deterministic work in code.** Arithmetic, counting, date comparison and
indirection are documented weak spots. Have the model name the parts and let
code do the maths.

## Before believing a benchmark

Nearly every performance figure circulating about this model is the vendor's
own, produced with reference answers derived from other models' judgements
rather than human ground truth. The catalogue flags those `vendor-reported`.
The handful of independent measurements are mostly _negative_ results — one
large agent framework ported the compaction approach, measured it, and published
the conclusion not to adopt it. Read those first.
