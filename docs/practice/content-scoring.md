# Content scoring in practice · 内容评分实践综述

<sub>[awesome-jev](../../README.md) · [practice reviews](README.md) · [design notes](../patterns.md#content-scoring) · [every row](../by-pattern/content-scoring.md)</sub>

> **Written by a model on 2026-10-31**, from this catalogue's records and a reading of the three recommended files that day. No person has reviewed it yet; read it the way the site shows a row marked *read by a model*. The tables are generated from `catalog.json` and stay current. · **由模型于 2026-10-31 撰写**，依据本目录的记录和当天对三个推荐文件的阅读，尚无人审阅。表格由 `catalog.json` 生成，会随目录更新。

Content scoring puts a number or a band on something: a passage's relevance, a reply's risk, a page's quality, a headline's threat level, whether a cached answer can be reused. The projects filed here range from linters and graders to caches, feeds and moderation bots. What they share is that the judgement is applied to many items, so its cost per item matters more than in any other pattern.

## What the catalogue holds

<!-- readings:start -->
|  | Rows |
| --- | ---: |
| Filed under this pattern | 167 |
| Citing one file in their repository (`evidence`) | 163 |
| Of those, the file read by a person (`evidence.read_on`) | 158 |
| Of those, read only by a model (`evidence.model_read_on`) | 5 |
| Of those, no reading recorded (a script's match only) | 0 |
<!-- readings:end -->

## How projects ask

**Break the judgement into atomic questions and combine them in code.** [gptcache](https://kydlikebtc.github.io/awesome-jev/?lang=en#gptcache) does not ask "is this cached answer good enough?"; it asks five Nouls (same task, matching context, right format, still fresh, nothing missing) and keeps the lowest, so every condition has to hold. [killmyidea](https://kydlikebtc.github.io/awesome-jev/?lang=en#killmyidea) scores an idea on several dimensions and turns them into kill, fix or ship in code; [jev-seo-agricidaniel](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-seo-agricidaniel) asks a Choice, a Score and Nouls about each page. The combination rule is then something you can read, test and change without touching the questions.

**One question per rule, per item.** Graders and linters run every rule against every unit: [slop-grader](https://kydlikebtc.github.io/awesome-jev/?lang=en#slop-grader) every rule against every line, [jev-lint](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-lint) one sentence-long question per code match, [jev-semgrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-semgrep) a Noul per line on whether it matches a meaning, [jevmeter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmeter) a score for every sentence of a video. This is only affordable because each question is cheap and many fit in one request.

**A rubric written out level by level.** Where a Score is used, the levels carry the meaning: [perch-semantic-linting](https://kydlikebtc.github.io/awesome-jev/?lang=en#perch-semantic-linting) takes a rubric weakest first, and its catalogue entry records that it reads severity as the score's expected value across levels rather than the top band. [agentgateway-guardrail](https://kydlikebtc.github.io/awesome-jev/?lang=en#agentgateway-guardrail), filed under safety gating, puts three Score questions on one shared severity scale so they can be compared.

**Describe situations, not numbers.** [worldmonitor-shadow-mode](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode) restates its threat-level guidelines as described situations because, as its file says, Jev reads literally and does not count: "10+ killed" would be a numeric comparison it is documented to get wrong. Anything that needs counting or arithmetic belongs in code, before the question.

**Rank, rather than cut.** Where only the best few matter, a ranking does the job: [jev-paper-radar](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-paper-radar) surfaces the few new papers worth reading each morning, [jev-skill-gate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-gate) scores every installed skill for relevance and hides the rest, and [dsh-jev-tools](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-tools), filed under context compaction, keeps segments of a long read by rank, not threshold. Ranking needs the probabilities to be ordered correctly, not calibrated to a particular value, which is a weaker and safer assumption.

**Trial it beside what you have.** worldmonitor-shadow-mode wired Jev in but kept it inert: by its authors' own statement nothing it returns reaches a label, a cache row or an alert, and a blind evaluation found it tied the model already in use. That is the one negative result filed under this pattern, and the way it was found is the part worth copying.

## Which primitive

<!-- primitives:start -->
| Primitive | A person read the code calling it | A model read the code calling it | Only the text signal shows it |
| --- | ---: | ---: | ---: |
| `choice` | 14 | 4 | 56 |
| `score` | 12 | 4 | 45 |
| `noul` | 11 | 3 | 65 |

Primitives recorded together on one row (`question_types`, a person's or a model's reading): `choice` + `score` + `noul` 12 · `choice` + `score` 3 · `choice` 2 · `choice` + `noul` 1 · `noul` 1 · `score` 1.
<!-- primitives:end -->

All three primitives appear, and many rows record all three, because scoring projects tend to be toolkits that expose each one: a SQL extension, a set of workflow blocks, a command-line tool. Score is for an ordered scale whose levels you can describe; Noul is for one criterion at a time, when you want to know which rule failed; Choice is for categories with no order, like worldmonitor-shadow-mode's threat category.

## The thresholds they chose

<!-- thresholds:start -->
| Row | Primitive | Compares | Value | What the file does | Read by |
| --- | --- | --- | --- | --- | --- |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) | `choice` | probability | 0.8 | at or above for safe, with the other checks: allow the command | nobody yet |
| [jevgpt](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgpt) | `noul` | probability | 0.9 | at or above, past a minimum length: stop generating | nobody yet |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) | `noul` | probability | 0.9 | at or above on a gating hazard: block the command | nobody yet |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) | `noul` | probability | 0.55 | at or above on a gating hazard: ask a person | nobody yet |
| [jev-trading-command-center](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trading-command-center) | `noul` | probability | 0.5 | below (risk_ok): refuse the simulated entry | a model, 2026-10-28 |
<!-- thresholds:end -->

Few content-scoring rows record a threshold, and the ones shown come from rows also filed under another pattern, so they gate something else the same project decides. That fits what the projects do: many rank and keep the top few, or combine several answers in code, instead of comparing one answer with a line.

## What was measured

<!-- measured:start -->
- [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) · `benchmark` · author's conclusion: mixed: Check whether Jev's probabilities stay calibrated on a rule-based ticket task it cannot have seen, beside three public benchmarks
- [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) · `benchmark` · author's conclusion: mixed: Answer typed finance judgements over trading logs, filings, industry news and central-bank text in a frozen offline suite
- [worldmonitor-shadow-mode](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode) · `benchmark` · author's conclusion: unfavourable · negative result: Label news headlines' threat level, scored on alerts against a blind human judgement
<!-- measured:end -->

jev-ood-calibration asks whether Jev's probabilities stay calibrated on a task it cannot have seen, and smartmoney-cub runs a frozen suite of finance judgements; both authors call the result mixed. The third is worldmonitor-shadow-mode's blind comparison. Read each author's report before borrowing a number; the conclusions are theirs, not reproduced here.

## Call sites worth reading

<!-- read:start -->
1. **[gptcache](https://kydlikebtc.github.io/awesome-jev/?lang=en#gptcache)** · `project` · cited file [`gptcache/similarity_evaluation/jev.py`](https://github.com/zilliztech/GPTCache/blob/HEAD/gptcache/similarity_evaluation/jev.py), read by a person, 2026-09-22 · primitives: none recorded
2. **[worldmonitor-shadow-mode](https://kydlikebtc.github.io/awesome-jev/?lang=en#worldmonitor-shadow-mode)** · `benchmark` · cited file [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js), read by a person, 2026-09-22 · primitives: `choice`
3. **[autogpt-typesafe-blocks](https://kydlikebtc.github.io/awesome-jev/?lang=en#autogpt-typesafe-blocks)** · `project` · cited file [`autogpt_platform/backend/backend/blocks/typesafe/_client.py`](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py), read by a person, 2026-09-22 · primitives: `choice`, `score`, `noul`
<!-- read:end -->

**gptcache, `similarity_evaluation/jev.py`.** A semantic cache deciding whether a stored answer can be reused. Five Noul questions, each with its own criteria for true and false, and the evaluation returns the minimum, so a hit needs every dimension to clear the cache's similarity threshold. The freshness question is the one to study: it is written not to treat a missing date as expiry, and asks only whether elapsed time could materially invalidate reusing this particular answer for this request.

**worldmonitor-shadow-mode, `shared/jev-classify.js`.** Headline classification as two Choices, a threat level and a category, with each option's criteria written as a described situation, and one request labelling a batch of headlines. The file is pure, building the request and parsing the answer while transport stays with the caller. The chance of an alert is read as the probability of *critical* plus *high*, not from the top pick alone. An answer outside the known levels or categories, or a level without a finite probability, is skipped rather than defaulted, and the endpoint must be https unless it is on the same machine, because every call carries the key. The row records how the project trialled it, in shadow mode, before letting it decide anything.

**autogpt-typesafe-blocks, `blocks/typesafe/_client.py`.** The plumbing behind seven AutoGPT blocks (choice, score, yes/no, ask-many, route, pick-best, filter), and the most defensive client found. It fits the state to a byte budget before sending and reports whether it had to truncate; it captures the exact request and response on the wire; it turns each kind of failure into a plain message with the request id; and a pinned model version the API no longer serves falls back to the current alias with one logged error naming the pin to update, instead of failing every call.

## What to copy, what to avoid

- Ask one criterion per question and combine the answers in code; you can then test the combination on its own.
- Write a Score's levels so each describes a situation a reader would recognise; do not hide counting or arithmetic inside a level.
- Prefer ranking to a fixed line when you only need the best few.
- Validate every answer; skip or flag a missing one, never default it.
- Fit the state to a budget you control, and say when you truncated.
- Run it in shadow beside whatever you use today and compare blind before it decides anything. The one negative result here was found exactly that way.

## 要点（中文）

- 把一个判断拆成几个原子问题，在代码里组合：gptcache 问五个 Noul 取最小值，所有条件都得满足。
- 评分类项目常对每一项、每条规则都问一遍，之所以可行，是因为每个问题都便宜，而且一个请求能装很多个。
- 用 Score 时要把每一级写成可辨认的情形；需要计数或算术的部分放在代码里，不要指望模型去数。
- 只需要最好的几个时，排序比设固定阈值更稳。
- 每个答案都要校验，缺失时跳过或标记，不要填默认值。
- 先影子运行，和现有方案盲测对比，再让它做决定；这个模式下唯一的负面结果（worldmonitor-shadow-mode）就是这样发现的。
- 推荐阅读：gptcache 的五维复用判断、worldmonitor-shadow-mode 的纯函数分类与影子试运行、AutoGPT 积木背后的防御式客户端。
