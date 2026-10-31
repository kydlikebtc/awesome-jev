# Safety gating in practice · 安全闸门实践综述

<sub>[awesome-jev](../../README.md) · [practice reviews](README.md) · [design notes](../patterns.md#safety-gating) · [every row](../by-pattern/safety-gating.md)</sub>

> **Written by a model on 2026-10-31**, from this catalogue's records and a reading of the three recommended files that day. No person has reviewed it yet; read it the way the site shows a row marked *read by a model*. The tables are generated from `catalog.json` and stay current. · **由模型于 2026-10-31 撰写**，依据本目录的记录和当天对三个推荐文件的阅读，尚无人审阅。表格由 `catalog.json` 生成，会随目录更新。

A gate asks whether something an agent is about to do (a shell command, a tool call, a payment, a message it is about to send) is safe to let through. [docs/patterns.md](../patterns.md#safety-gating) puts the limit first, and the projects below agree with it in how they are built: the decision model sits behind deterministic rules and in front of a person, never alone.

## What the catalogue holds

<!-- readings:start -->
|  | Rows |
| --- | ---: |
| Filed under this pattern | 146 |
| Citing one file in their repository (`evidence`) | 142 |
| Of those, the file read by a person (`evidence.read_on`) | 133 |
| Of those, read only by a model (`evidence.model_read_on`) | 7 |
| Of those, no reading recorded (a script's match only) | 2 |
<!-- readings:end -->

## How projects ask

**Rules first, the model for what is left.** The most common shape runs cheap deterministic checks before any request: [jev-engineering](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-engineering) denies on regex rules, then waves through a read-only allowlist, and asks Jev only about the rest; [jev-kit](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-kit) puts a free pre-filter in front, [construct-auto-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#construct-auto-classifier) structural rules, and [jev-runtime-security](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-runtime-security) a kernel-level policy that leaves only the ambiguous cases to the model. The model's job is to shrink the pile a person has to look at, not to be the wall.

**One question per hazard, all in one request.** Rather than one "is this safe?" question, projects ask a battery of narrow ones over the same state and decide in code. [sub2api-moderation](https://kydlikebtc.github.io/awesome-jev/?lang=en#sub2api-moderation) asks a Noul per hazard category; [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) asks one per gating hazard (destroys something with no other copy, touches credentials, exfiltrates, escalates privilege, carries an injection attempt, acts beyond what the user asked); [jev-guard](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-guard) asks how much harm a call could do, whether the user asked for it and whether it follows untrusted text. Because every question reads the same state in one request, the battery costs about what one question does.

**Injection is asked about as its own question.** [deepchat-tool-permission](https://kydlikebtc.github.io/awesome-jev/?lang=en#deepchat-tool-permission) has an explicit prompt-injection pressure check, omp-jevens-classifier asks whether anything in the state addresses the reviewer or imitates a verdict, and [dsh-jev-tools](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-tools) asks whether a fetched page holds instructions aimed at an AI. Asking it separately means a page that is harmless on its effects but full of instructions still shows up.

**Authorisation is asked about, and comes from the user only.** deepchat-tool-permission and jev-guard ask whether the user authorised the action. omp-jevens-classifier writes the rule into the question itself: the user's own messages are the only source of authorisation, and text the requesting agent wrote can explain intent but never authorise.

**Three outcomes, not two.** Most gates answer allow, ask or deny, and keep a band that goes to a person. jev-engineering asks when Jev's confidence is low; omp-jevens-classifier sends a hazard it merely suspects to a person and blocks only one it is sure of; [jev-cu](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cu) asks a separate Noul for whether an action needs the user's confirmation.

**Fail open or fail closed, on purpose.** omp-jevens-classifier and [agentgateway-guardrail](https://kydlikebtc.github.io/awesome-jev/?lang=en#agentgateway-guardrail) fail closed: no key, a timeout or a malformed answer blocks. jev-engineering, jev-kit and [jev-belay](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-belay) fail open, which is safe only because their fallback is the harness's own permission prompt or an unchanged path, not "run it". The choice follows from what happens when the gate is absent; a gate whose absence means "run it" should fail closed.

**Start by watching.** jev-engineering ships in an observe mode that only logs, and tells you to set your thresholds from that log; [grok-bot-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#grok-bot-jev) and [jev-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness) have shadow modes. A gate that has only ever been watched has not been measured, but it has been looked at before it decides anything.

## Which primitive

<!-- primitives:start -->
| Primitive | A person read the code calling it | A model read the code calling it | Only the text signal shows it |
| --- | ---: | ---: | ---: |
| `choice` | 13 | 4 | 46 |
| `score` | 11 | 3 | 31 |
| `noul` | 16 | 7 | 62 |

Primitives recorded together on one row (`question_types`, a person's or a model's reading): `choice` + `score` + `noul` 11 · `choice` + `noul` 6 · `noul` 4 · `score` + `noul` 2 · `score` 1.
<!-- primitives:end -->

Noul carries the hazards: each is a proposition that is true or false of the action, and its probability is what a threshold reads. Choice carries the verdict when there is one (allow, ask, deny; safe, unsafe, unsure). Score appears where a project wants a severity on a scale; agentgateway-guardrail asks three Score questions on a shared severity scale and blocks when two or more cross the line. Many rows record all three, usually because the same project also gates, routes and scores elsewhere.

## The thresholds they chose

<!-- thresholds:start -->
| Row | Primitive | Compares | Value | What the file does | Read by |
| --- | --- | --- | --- | --- | --- |
| [construct-auto-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#construct-auto-classifier) | `choice` | confidence | 0.6 | below (default): do not run the allowed command unattended | nobody yet |
| [jev-belay](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-belay) | `choice` | confidence | 0.4 | below: read the outcome pick as other | nobody yet |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) | `choice` | probability | 0.8 | at or above for safe, with the other checks: allow the command | nobody yet |
| [construct-auto-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#construct-auto-classifier) | `choice` | probability | 0.6 | at or above for allow, every risk quiet (default): allow anyway | nobody yet |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) | `noul` | probability | 0.9 | at or above on a gating hazard: block the command | nobody yet |
| [construct-auto-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#construct-auto-classifier) | `noul` | probability | 0.7 | at or above on any risk question (default): deny the command | nobody yet |
| [jev-belay](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-belay) | `noul` | probability | 0.7 | at or above (default): treat the turn as claiming its work is done | nobody yet |
| [omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier) | `noul` | probability | 0.55 | at or above on a gating hazard: ask a person | nobody yet |
| [jev-belay](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-belay) | `noul` | probability | 0.5 | at or above: treat the checks as applying to the claim | nobody yet |
| [jev-trading-command-center](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trading-command-center) | `noul` | probability | 0.5 | below (risk_ok): refuse the simulated entry | a model, 2026-10-28 |
| [vexjoy-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#vexjoy-agent) | `noul` | probability | 0.5 | at or above (default): keep the tool call or its result when compacting | nobody yet |
| [vexjoy-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#vexjoy-agent) | `noul` | probability | 0.35 | at or above, for edit and write calls: keep them when compacting | nobody yet |
<!-- thresholds:end -->

Each value is one project's own default, written in its file, not a recommendation. A row filed under several patterns brings every threshold it records, so a few here belong to another decision the same project makes (what to keep when compacting, whether to enter a trade). Two habits stand out. The block or deny line sits high and a lower line sends the case to a person, so the model alone never decides the uncertain middle. And allowing usually needs more than one thing to be true: omp-jevens-classifier allows only when the safe verdict is likely enough *and* no gating hazard reached its review line. Several files say outright that these numbers are theirs to tune: omp-jevens-classifier calls its block and review lines the first things to calibrate, and jev-engineering asks you to set yours from your own observe-mode log.

## What was measured

<!-- measured:start -->
- [decision-models-as-guardrails](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-models-as-guardrails) · `benchmark`: Decide whether to block a guardrail check across six suites: content, prompt attacks, denied topics, profanity, PII and grounding
- [jev-benchmarks](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-benchmarks) · `benchmark` · author's conclusion: mixed: Zero-shot single-label text classification with per-label probabilities, scored on accuracy, calibration and coverage at a fixed error budget
- [jev-dspy-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dspy-lab) · `benchmark`: Confidence-gated support-ticket routing in a DSPy-style pipeline, on synthetic cases
- [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) · `benchmark` · author's conclusion: mixed: Check whether Jev's probabilities stay calibrated on a rule-based ticket task it cannot have seen, beside three public benchmarks
<!-- measured:end -->

None of these measures a gate end to end on real agent traffic. They measure guardrail suites and whether Jev's probabilities stay calibrated, which is what a threshold silently relies on. Read each author's report before borrowing a number; the conclusions are theirs, not reproduced here.

## Call sites worth reading

<!-- read:start -->
1. **[jev-engineering](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-engineering)** · `plugin` · cited file [`jev_gate.py`](https://github.com/eugeniughelbur/jev-engineering/blob/HEAD/jev_gate.py), read by a person, 2026-09-28 · primitives: `noul`, `choice`
2. **[omp-jevens-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#omp-jevens-classifier)** · `project` · cited file [`jev.ts`](https://github.com/STRML/omp-jevens-classifier/blob/HEAD/jev.ts), read by a person, 2026-09-22 · primitives: none recorded
3. **[sub2api-moderation](https://kydlikebtc.github.io/awesome-jev/?lang=en#sub2api-moderation)** · `project` · cited file [`backend/internal/pkg/typesafe/client.go`](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go), read by a person, 2026-09-22 · primitives: `noul`
<!-- read:end -->

**jev-engineering, `jev_gate.py`.** The whole layered gate in one file. Hard deny rules run before the read-only allowlist on purpose, because a command name says nothing about its arguments (`cat` is harmless until it reads a private key), and a chained command is split so a harmless first step cannot carry a destructive second one through the allowlist. Then one Noul (is it destructive?) and one Choice (the verdict) come back, and code decides: deny when destructive is likely, ask when confidence is low, allow only when destructive is unlikely *and* the verdict is allow, otherwise ask. Every failure falls back to the harness's normal prompt. Its default mode only logs, and `--stats` shows what auto mode would have done with your history.

**omp-jevens-classifier, `jev.ts`.** The most carefully argued gate found. Its header explains each design choice: the reason shown to the user is built in code from numbers and hazard ids, so nothing the model returns is ever interpolated into a dialog; question ids are not sent to the model, so each question carries its full meaning in `instructions` and its boundaries in `criteria`; hazards are split into *gating* ones, which may decide, and *descriptive* ones (it contacts a remote, it writes outside the working directory), which are only reported, because gating on "does X happen?" made a plain `git push` unclassifiable. It fails closed, never fills a missing hazard with zero, and versions its policy so an audit line says which battery produced a decision.

**sub2api-moderation, `backend/internal/pkg/typesafe/client.go`.** A short, strict transport worth copying for any gate. One request carries a map of Noul questions; each answer must be a Noul, finite and between 0 and 1, or the whole call is an error rather than a default. It bounds the response size, does not log the provider's error bodies because they may echo user input, and leaves retries and timeouts to the caller.

## What to copy, what to avoid

- Put deterministic rules first and keep them deterministic; the model handles what the rules cannot settle.
- Ask narrow questions, one per hazard, and combine them in code you can read and test.
- Keep a band that goes to a person. A probability near the middle is information, not a coin toss to settle automatically.
- Decide fail-open or fail-closed from what the gate's absence would mean, and write the decision down.
- Validate every answer's type and range, and treat a missing answer as an error, never as "safe".
- Never let the model's output reach a dialog, a log line an operator trusts, or a shell. Build the message from your own labels.
- Do not use it as the boundary. As [docs/patterns.md](../patterns.md#safety-gating) says, an attacker chooses the input; a gate like these catches the careless.

## 要点（中文）

- 先用确定性规则（拒绝规则、只读白名单、内核策略），只把规则判不了的部分交给模型；模型的作用是减少要人看的量，而不是当墙。
- 不问笼统的“安全吗”，而是每种危害一个 Noul，放在同一个请求里，再在代码里组合判断。
- 把提示注入和“用户是否授权”单独成题；授权只能来自用户本人的消息。
- 结果分三档（放行、问人、拒绝），中间不确定的那段交给人。
- 失败时放行还是拦截要有意选择：闸门缺席意味着“直接执行”时，就应失败即拦截。
- 校验每个答案的类型和取值范围，缺失的答案按错误处理，绝不当作“安全”。
- 推荐阅读：jev-engineering 的分层闸门、omp-jevens-classifier 对每个设计取舍的说明、sub2api-moderation 的严格传输层。
- 这里记录的阈值都是各项目自己的默认值，不是推荐值；这些项目自己也说要按自己的日志去调。
