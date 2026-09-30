# Decision patterns

<sub>[中文](patterns.zh-CN.md)</sub>

The catalog is indexed by pattern rather than by resource type, because the blog
post you read this week is disposable and the pattern is not. This page defines
each pattern: what decision it makes, why a calibrated decision model suits it,
and when you should reach for something else instead.

## The three primitives

Every pattern below is built out of these. Shapes are from the official API
reference — see [`sources.md`](sources.md) for the exact URLs.

| `type`   | Returns                                             | `criteria`                            | Limits                     |
| -------- | --------------------------------------------------- | ------------------------------------- | -------------------------- |
| `noul`   | `noul`: a 0–1 yes-no probability                    | optional `{true, false}` descriptions | —                          |
| `choice` | `choice` + `probabilities` + `confidence`           | required map of option → description  | **max 255 options**        |
| `score`  | `score` + `legend` + `probabilities` + `confidence` | required ordered array of levels      | **2–10 levels, 0-indexed** |

Three facts that catch people out:

1. **`noul` answers carry no `confidence` field.** The probability _is_ the
   answer. `choice` and `score` carry a separate `confidence`, derived from the
   shape of the probability distribution. A threshold tuned against a `noul`
   probability is not transferable to a `choice` confidence — they are different
   quantities.
2. **A `score` is probability-weighted and lands between levels.** The docs' own
   example returns `1.05` on a three-level scale. Do not assume an integer.
3. **Input is text only.** String, JSON object, or array of text. No image,
   audio or video — pre-process to text first. There is no visual-classification
   pattern in this catalog for that reason.

The property that makes the rest of this page work is **calibration**:
confidence tracks accuracy, so a threshold is a policy lever rather than a
guess. That is what makes the "act above `t`, escalate below `t`" shape possible
at all.

## The test for whether a decision belongs here

A decision is a good fit when **all** of these hold:

1. **The answer space is closed.** You can enumerate the options up front. If the
   answer is prose, you need a generative model.
2. **It runs often.** The inner loop of an agent, one call per message, one call
   per document. A decision made once a day does not need to be cheap.
3. **Being wrong is survivable or detectable.** Either the step is reversible, or
   a confidence threshold can route the doubtful cases to a person.
4. **The context fits.** 64k tokens per request total, and 32k for the `state`
   plus the single longest question.

If any of those fails, keep an LLM in that spot. The practical division of
labour: a generative model for open-ended reasoning and writing, a decision
model for the frequent typed judgements along the way, ordinary code for policy.

The vendor's own [jaggedness doc](https://docs.typesafe.ai/model-jaggedness/jev-1.13)
lists where the current model is weak — literal reading, arithmetic and
counting, date comparison, indirection, large states full of irrelevant detail,
adversarial content. Read it before designing around any of those.

---

## tool-selection

**The decision:** given the conversation so far and the available tools, which
tool should the agent call next — or none?

**Why here:** the most frequent judgement in an agent loop, and a closed choice
over a list you already have. Schema matching removes a failure class: an agent
choosing among four tools cannot invent a fifth.

**Shape:** `choice` over tool names plus a `none` option. Gate on confidence and
fall back to the planning model when the choice is close.

**When not to:** when picking the tool requires composing a plan, or when the
arguments are the hard part. This chooses _which_; something still fills in the
arguments.

<!-- catalogued-tool-selection:start -->
**Tool selection** in the catalogue: 230 rows, [each listed with its caveats](by-pattern/tool-selection.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=en).
<!-- catalogued-tool-selection:end -->

---

## intent-routing

**The decision:** what does this user actually want, and which branch handles it?

**Why here:** classic text classification, the task where the cost and latency
gap against an LLM is widest. Routing sits in front of everything else, so its
latency is added to every request.

**Shape:** `choice` over intents, plus a `score` for urgency when the branch
depends on both — asked in the same request, since questions are evaluated in
parallel against one ingest of the state.

**When not to:** when intents overlap so heavily that a human labeller could not
agree with themselves. Fix the taxonomy first.

<!-- catalogued-intent-routing:start -->
**Intent routing** in the catalogue: 35 rows, [each listed with its caveats](by-pattern/intent-routing.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=en).
<!-- catalogued-intent-routing:end -->

---

## context-compaction

**The decision:** in a long session, which earlier tool calls and results are
still relevant?

**Why here:** the alternative is summarising, which paraphrases and loses exactly
the details — an error string, an ID, a file path — that a later step needs.
Deciding _keep or drop_ per item preserves what is kept **verbatim**.

**Shape:** `noul` per item, or a `score` for relevance when you want to drop the
lowest-ranked items until you are under budget.

**When not to:** when the session fits anyway. Compaction adds a failure mode —
dropping something that turns out to matter — so do not pay for it until context
pressure is real.

<!-- catalogued-context-compaction:start -->
**Context compaction** in the catalogue: 34 rows, [each listed with its caveats](by-pattern/context-compaction.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=en).
<!-- catalogued-context-compaction:end -->

---

## safety-gating

**The decision:** is this action safe to execute?

**Shape:** `noul` for allow/block, or a `score` for a risk band mapped to
allow / confirm / block.

**When not to — read this one carefully:** a probabilistic gate is **defence in
depth, not a security boundary**. Anything genuinely destructive or irreversible
needs a deterministic rule, a permission system, or a human. Use a decision model
to catch the careless, not to contain the adversarial: an attacker chooses the
input, and a model that is right 99% of the time is one an attacker will probe
for the other 1%. The vendor's jaggedness doc names adversarial content as a
known weak spot.

<!-- catalogued-safety-gating:start -->
**Safety gating** in the catalogue: 139 rows, [each listed with its caveats](by-pattern/safety-gating.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=en).
<!-- catalogued-safety-gating:end -->

---

## output-validation

**The decision:** does this generated output meet the bar before a user sees it?

**Why here:** a rubric check is a typed judgement, and running it on every
generation is only affordable if it is cheap. This is the LLM-as-judge job with
the economics fixed.

**Shape:** `score` against a rubric, or `noul` per criterion when you want to
know _which_ rule failed rather than an aggregate.

**When not to:** when the defect needs explaining rather than detecting. A score
says the output is weak; it does not say how to fix it. Pair it with a generative
critique for the cases it rejects.

<!-- catalogued-output-validation:start -->
**Output validation** in the catalogue: 134 rows, [each listed with its caveats](by-pattern/output-validation.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=en).
<!-- catalogued-output-validation:end -->

---

## retry-control

**The decision:** this step failed — retry, change approach, or stop?

**Shape:** `choice` over `retry` / `retry-modified` / `escalate` / `abort`.

**When not to:** when the error is already machine-readable. An HTTP 429 with a
`Retry-After` header does not need a model; it needs you to read the header.
Reach for a decision model for the messy cases, after the deterministic rules.

<!-- catalogued-retry-control:start -->
**Retry control** in the catalogue: 7 rows, [each listed with its caveats](by-pattern/retry-control.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=retry-control&lang=en).
<!-- catalogued-retry-control:end -->

---

## human-escalation

**The decision:** must a person look at this one?

**Why here:** the pattern calibration exists for. With confidence that tracks
accuracy, the threshold becomes a dial between throughput and error rate.

**Shape:** any primitive; the escalation comes from the confidence attached to
the answer — remembering that `noul` gives you a probability rather than a
confidence.

**Note:** picking the threshold is a policy decision, not a modelling one. It
belongs in config, reviewed against measured outcomes. See
[`../examples/README.md`](../examples/README.md).

<!-- catalogued-human-escalation:start -->
**Human escalation** in the catalogue: 69 rows, [each listed with its caveats](by-pattern/human-escalation.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=en).
<!-- catalogued-human-escalation:end -->

---

## model-routing

**The decision:** which downstream model or tier should handle this request?

**Why here:** routing cheap requests away from expensive models only pays if the
router is far cheaper than the gap it saves.

**Shape:** `choice` over model tiers, or a `score` for difficulty that you map to
tiers in code — the second is easier to re-tune when your tiers change.

**When not to:** when your models differ in capability rather than cost. Verify
the cheap path is genuinely adequate for the easy cases before building a router.

<!-- catalogued-model-routing:start -->
**Model routing** in the catalogue: 44 rows, [each listed with its caveats](by-pattern/model-routing.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=en).
<!-- catalogued-model-routing:end -->

---

## fan-out

**The decision:** not one decision — many at once, including ones you might not
need.

**Why here:** the state is ingested once and every question is evaluated against
it in parallel, so a second question costs roughly its own tokens rather than a
second round trip. That changes the design: ask speculatively, then let code pick
what mattered. The vendor's parallel-questions cookbook reports large cost and
latency wins from batching a briefing into one call rather than many.

**Shape:** many questions of any type in a single request, within the 64k budget.

**When not to:** when a later question's wording depends on an earlier answer.
That needs two round trips.

<!-- catalogued-fan-out:start -->
**Speculative fan-out** in the catalogue: 32 rows, [each listed with its caveats](by-pattern/fan-out.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=en).
<!-- catalogued-fan-out:end -->

---

## search-ranking

**The decision:** which of these candidates actually answers the query, and in
what order?

**Why here:** re-ranking a shortlist is a per-pair judgement, which is only
affordable at shortlist scale if each one is cheap. The vendor's re-ranking
cookbook reports substantial top-1 and top-10 gains over a BM25 shortlist.

**Shape:** `score` per candidate, or one `choice` over line ids for
line-granular search.

**When not to:** as your entire retrieval stack. This re-ranks a shortlist; it
does not replace an index over a large corpus.

<!-- catalogued-search-ranking:start -->
**Search & ranking** in the catalogue: 64 rows, [each listed with its caveats](by-pattern/search-ranking.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=en).
<!-- catalogued-search-ranking:end -->

---

## data-extraction

**The decision:** which span is the value?

**Why here:** the model does not generate text, so extraction here means
_selecting_ — regex or a parser proposes candidates, the model picks the right
one, and your code gets a verbatim value rather than a paraphrase. That is a real
advantage for anything you will store or compare.

**Shape:** `choice` over candidate spans; `noul` per field for presence.

**When not to:** when nothing can enumerate candidates first. And note arithmetic
and date comparison are named weak spots — resolve and validate dates in code
after the model names the parts.

<!-- catalogued-data-extraction:start -->
**Structured extraction** in the catalogue: 17 rows, [each listed with its caveats](by-pattern/data-extraction.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=en).
<!-- catalogued-data-extraction:end -->

---

## classification

**The decision:** where does this item sit in a taxonomy?

**Why here:** a `choice` caps at 255 options, but `probabilities` over a level
lets you walk a deep hierarchy with a beam search, and an answer's own confidence
lets you fall back to a coarser level instead of guessing a fine one.

**Shape:** `choice` per level, read alongside `probabilities` and `confidence`.

**When not to:** when your taxonomy has overlapping leaves. Fix the taxonomy.

<!-- catalogued-classification:start -->
**Classification** in the catalogue: 120 rows, [each listed with its caveats](by-pattern/classification.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=en).
<!-- catalogued-classification:end -->

---

## feature-extraction

**The decision:** turn free text into numbers a classical model can train on.

**Why here:** an unusual and underrated use. The probabilities and scores are
themselves features; a gradient-boosted model downstream can consume them
without any of the model's text ever being shown to a user.

**Shape:** `score` and `noul` probabilities read as continuous features.

**When not to:** when you have enough labelled data to train a supervised model
on the raw text directly.

<!-- catalogued-feature-extraction:start -->
**ML feature extraction** in the catalogue: 8 rows, [each listed with its caveats](by-pattern/feature-extraction.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=en).
<!-- catalogued-feature-extraction:end -->

---

## document-triage

**The decision:** what is this document, and where does it go?

**Shape:** `choice` for type and destination, `score` for confidence-driven
review queues, `noul` per compliance check.

**Note:** for invoices and financial paperwork, treat the model as a sorter that
fills a review queue, not as an approver. Approval stays with a person or a
deterministic rule.

<!-- catalogued-document-triage:start -->
**Document triage** in the catalogue: 20 rows, [each listed with its caveats](by-pattern/document-triage.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=document-triage&lang=en).
<!-- catalogued-document-triage:end -->

---

## support-triage

**The decision:** which queue, which priority, which macro?

**Shape:** `choice` for queue and `score` for urgency in the same request.

**Note:** this is the example the vendor's own quickstart uses, so it is the
best-documented starting point.

<!-- catalogued-support-triage:start -->
**Support triage** in the catalogue: 8 rows, [each listed with its caveats](by-pattern/support-triage.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=en).
<!-- catalogued-support-triage:end -->

---

## content-scoring

**The decision:** how good, how risky, how relevant — on an ordered scale?

**Shape:** `score`. Use it when the scale is genuinely ordered; use `choice` when
your "scale" is really unordered categories wearing a number.

**Note:** 2–10 levels only. An ordered scale with calibrated confidence is
rankable, which makes this the pattern for populating review queues worst-first.

<!-- catalogued-content-scoring:start -->
**Content scoring** in the catalogue: 166 rows, [each listed with its caveats](by-pattern/content-scoring.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=en).
<!-- catalogued-content-scoring:end -->

---

## recommendation

**The decision:** what to surface next, fast enough that a live conversation does
not stall.

**Shape:** `choice` over a shortlist, or `score` over candidates from a cheaper
retrieval step.

**When not to:** as your entire ranking stack — see `search-ranking`.

<!-- catalogued-recommendation:start -->
**Recommendation** in the catalogue: 1 row, [listed with its caveats](by-pattern/recommendation.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=en).
<!-- catalogued-recommendation:end -->

---

## overview

Not a pattern. The label for entries that survey the model or the space instead
of demonstrating one decision — launch coverage, explainers, "what is Jev" posts.
Kept separate so the pattern indexes stay honest: an overview is not an example
of doing anything.

It has also been where the keyword rules that suggest patterns
(`scripts/classify.py`) put a description they could not place, and the bulk
passes took their suggestion. So a project or plugin with code whose only
pattern is `overview`, and whose row records no `patterns_reviewed`, counts as
not yet indexed by pattern rather than as an overview. There are
currently <!--n:overview_unindexed-->252<!--/n--> such rows. The READMEs, the
Overview page and the site list them apart under that heading, and the
[review queue](review-queue.md#unsorted-overview) lists them with the rules'
suggestion. Read one against the patterns above, give it the ones it shows or
keep `overview`, and set `patterns_reviewed` to the date you read it.

<!-- catalogued-overview:start -->
**Overview** in the catalogue: 451 rows, [each listed with its caveats](by-pattern/overview.md) · [the site's filter](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=en).
<!-- catalogued-overview:end -->

---

## Adding a pattern

A new pattern earns a heading when there are at least two independent real
examples of it. Until then it goes under the closest existing one, because a
taxonomy with empty branches is harder to use than a coarse one. Adding one means
editing four places — the schema enum, the pattern's entry in
[`../patterns.json`](../patterns.json) (its labels, blurbs and place in the
order), this page, and its Chinese rendering
[`patterns.zh-CN.md`](patterns.zh-CN.md). On both pages its `## key` section
ends with a pair of `catalogued-<key>` markers that `scripts/build_docs.py`
fills with the count and the links, and the build fails loudly if you miss the
labels, a section or the markers. See [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
