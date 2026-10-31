# Tool selection in practice · 工具选择实践综述

<sub>[awesome-jev](../../README.md) · [practice reviews](README.md) · [design notes](../patterns.md#tool-selection) · [every row](../by-pattern/tool-selection.md)</sub>

> **Written by a model on 2026-10-31**, from this catalogue's records and a reading of the three recommended files that day. No person has reviewed it yet; read it the way the site shows a row marked *read by a model*. The tables are generated from `catalog.json` and stay current. · **由模型于 2026-10-31 撰写**，依据本目录的记录和当天对三个推荐文件的阅读，尚无人审阅。表格由 `catalog.json` 生成，会随目录更新。

Apart from `overview`, tool selection has the most rows whose cited file a person has read. It covers more than picking an MCP tool: computer-use and browser agents picking the next element to click, robots and game agents picking the next move, trading bots picking long, short or hold. In every case the options are known before the question is asked, which is what makes it a Choice.

## What the catalogue holds

<!-- readings:start -->
|  | Rows |
| --- | ---: |
| Filed under this pattern | 241 |
| Citing one file in their repository (`evidence`) | 237 |
| Of those, the file read by a person (`evidence.read_on`) | 222 |
| Of those, read only by a model (`evidence.model_read_on`) | 15 |
| Of those, no reading recorded (a script's match only) | 0 |
<!-- readings:end -->

## How projects ask

**The options are the tools, the state is the request.** [fastmcp-jev-search](https://kydlikebtc.github.io/awesome-jev/?lang=en#fastmcp-jev-search) and [composio-typesafe-provider](https://kydlikebtc.github.io/awesome-jev/?lang=en#composio-typesafe-provider) turn a tool catalogue into a Choice whose options are tool names and whose criteria are the tools' descriptions. Computer-use agents do the same with what is on screen: [cua-jev-use](https://kydlikebtc.github.io/awesome-jev/?lang=en#cua-jev-use), [agent-desktop](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-desktop) and [jev-cu](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cu) offer the accessibility tree's elements or the detected controls as options, rebuilt for every step.

**Leave a way to say "none of these".** A Choice always picks something, so careful projects add an option that is not an action. [jev-voice-browser](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice-browser) always includes a none option, [jev-webmcp-extension](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-webmcp-extension) a "none of these", [macbrow](https://kydlikebtc.github.io/awesome-jev/?lang=en#macbrow) "chat" and "new action" beside the tools, and cua-jev-use reserves options to look again or abstain. fastmcp-jev-search goes further: one Noul per candidate asks whether it does the job at all, so a request no tool serves comes back empty instead of returning the least wrong tool.

**Wide, then close.** With many tools, fastmcp-jev-search first ranks the whole catalogue on one-line summaries, then re-reads a shortlist with full descriptions and parameters. This follows TypeSafe's skill-suggestion cookbook, and it keeps each request small.

**Jev picks, something else writes.** A Choice can pick an action but cannot write its free-text argument. [jev-ultrafast](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ultrafast) calls a small LLM only when text must be typed; [jev-browser-use](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser-use) lets Jev click while a reasoning model thinks and verifies; [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) has an LLM write arguments for the actions Jev chooses. composio-typesafe-provider asks a question per argument it can, and returns a *partial* call naming what is still missing when it cannot.

**Act only when sure, otherwise step aside.** [jev-gateway](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-gateway) steers the LLM to a tool only when Jev is confident and otherwise passes the request through unchanged; [jev-social](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-social) refuses below a confidence floor and asks for a narrower request. Stepping aside is cheap here because the fallback, the agent's own LLM, already exists.

**Do not ask what you already know.** [jevpilot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevpilot) answers single-option questions locally instead of paying to send them, and composio-typesafe-provider asks no question for an argument the caller already supplied.

## Which primitive

<!-- primitives:start -->
| Primitive | A person read the code calling it | A model read the code calling it | Only the text signal shows it |
| --- | ---: | ---: | ---: |
| `choice` | 26 | 10 | 105 |
| `score` | 6 | 1 | 31 |
| `noul` | 16 | 6 | 82 |

Primitives recorded together on one row (`question_types`, a person's or a model's reading): `choice` 16 · `choice` + `noul` 13 · `choice` + `score` + `noul` 6 · `noul` 3 · `choice` + `score` 1.
<!-- primitives:end -->

Choice dominates, as the pattern's design notes expect. Noul appears beside it for two separate questions: whether any candidate fits at all, and whether the chosen action needs the user's confirmation (jev-cu). Score is rare here; where it appears it usually rides beside the choice, such as the conviction [beebots](https://kydlikebtc.github.io/awesome-jev/?lang=en#beebots) asks for alongside each trading move.

## The thresholds they chose

<!-- thresholds:start -->
| Row | Primitive | Compares | Value | What the file does | Read by |
| --- | --- | --- | --- | --- | --- |
| [jev-in-codex](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-in-codex) | `choice` | confidence | 0.8 | below: list the record for human review | nobody yet |
| [jevcumber](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevcumber) | `choice` | confidence | 0.75 | at or above: accept a pick sourced from the page | nobody yet |
| [llm-debugger-vscode](https://kydlikebtc.github.io/awesome-jev/?lang=en#llm-debugger-vscode) | `choice` | confidence | 0.75 | at or above, when the chosen action is finish: finish the hunt | a model, 2026-10-28 |
| [macbrow](https://kydlikebtc.github.io/awesome-jev/?lang=en#macbrow) | `choice` | confidence | 0.6 | at or above: reuse the existing tool instead of adding a duplicate | nobody yet |
| [jev-social](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-social) | `choice` | confidence | 0.35 | below: refuse the operation and ask for a narrower request | nobody yet |
| [jev-voice-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice-control) | `choice` | confidence | 0.3 | below: return an uncertain turn | nobody yet |
| [neo4jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#neo4jev) | `choice` | probability | 0.05 | at or above (default): follow the relationship in the beam search | nobody yet |
| [jev-tetris-machinelearning-nerd](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tetris-machinelearning-nerd) | `score` | confidence | 0.55 | below: send the run to human review | nobody yet |
| [jev-tetris-machinelearning-nerd](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tetris-machinelearning-nerd) | `score` | score | 2 | at or above: send the run to human review | nobody yet |
| [jev-robotics-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robotics-demo) | `noul` | probability | 0.9 | above: end the run as done | nobody yet |
| [jevgpt](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgpt) | `noul` | probability | 0.9 | at or above, past a minimum length: stop generating | nobody yet |
| [browser-use-olympics](https://kydlikebtc.github.io/awesome-jev/?lang=en#browser-use-olympics) | `noul` | probability | 0.85 | above: end the task as done | nobody yet |
| [jev-tetris-machinelearning-nerd](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-tetris-machinelearning-nerd) | `noul` | probability | 0.75 | at or above: page the on-call person | nobody yet |
| [browser-use-olympics](https://kydlikebtc.github.io/awesome-jev/?lang=en#browser-use-olympics) | `noul` | probability | 0.7 | above: escalate the step as blocked | nobody yet |
| [jev-voice-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice-control) | `noul` | probability | 0.7 | at or above: treat the screen as the wrong one and back out | nobody yet |
| [llm-debugger-vscode](https://kydlikebtc.github.io/awesome-jev/?lang=en#llm-debugger-vscode) | `noul` | probability | 0.7 | at or above (readyForFix): finish the hunt without asking the LLM | a model, 2026-10-28 |
| [jev-mobile-xinwang-nwpu](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mobile-xinwang-nwpu) | `noul` | probability | 0.5 | at or above: accept the goal as achieved | nobody yet |
| [neo4jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#neo4jev) | `noul` | probability | 0.5 | at or above (default): stop at the node as the goal | nobody yet |
| [jev-skill-scout](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-scout) | `noul` | probability | 0.3 | below (default): suggest no skill | nobody yet |
<!-- thresholds:end -->

Each value is one project's own choice, written in its file, not a recommendation. Two kinds dominate: a floor on a Choice's confidence below which the project refuses, asks or hands the step back, and a line on a Noul that ends a task as done or blocked. A confidence floor is a policy about how much a wrong pick costs; a project whose wrong click is cheap sets it low, one that acts on a person's behalf sets it higher. A row filed under several patterns brings every threshold it records, so a few belong to another decision the same project makes.

## What was measured

<!-- measured:start -->
- [hermes-jev-skills](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-jev-skills) · `plugin` · negative result: Nine agent skills plus a CLI covering model routing, memory filtering, turn retention, one-of-many skill selection and next-action choice.
- [jev-robot-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-robot-control) · `benchmark` · author's conclusion: inconclusive: Pick up an apple and place it on a plate with a simulated xArm7, choosing intent, motion direction and gripper each cycle
- [smartmoney-cub](https://kydlikebtc.github.io/awesome-jev/?lang=en#smartmoney-cub) · `benchmark` · author's conclusion: mixed: Answer typed finance judgements over trading logs, filings, industry news and central-bank text in a frozen offline suite
- [windtunnel](https://kydlikebtc.github.io/awesome-jev/?lang=en#windtunnel) · `benchmark`: Complete browser tasks on eight self-hosted web apps, Jev choosing each action while Mercury 2.5 writes arguments and answers
<!-- measured:end -->

The measurements filed here test whole agents (a simulated robot arm, browser tasks on self-hosted apps, finance judgements), not tool choice on its own. The negative result is about a use beside tool choice: [hermes-jev-skills](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-jev-skills) dropped Jev-summarised handoffs after they recalled less than raw transcripts. Read each author's report before borrowing a number.

## Call sites worth reading

<!-- read:start -->
1. **[fastmcp-jev-search](https://kydlikebtc.github.io/awesome-jev/?lang=en#fastmcp-jev-search)** · `project` · cited file [`fastmcp_slim/fastmcp/experimental/transforms/jev_search.py`](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py), read by a person, 2026-09-22 · primitives: `choice`, `noul`
2. **[cua-jev-use](https://kydlikebtc.github.io/awesome-jev/?lang=en#cua-jev-use)** · `project` · cited file [`libs/cua-driver/examples/jev-use/python/jev_adapter.py`](https://github.com/trycua/cua/blob/HEAD/libs/cua-driver/examples/jev-use/python/jev_adapter.py), read by a person, 2026-09-22 · primitives: `choice`
3. **[composio-typesafe-provider](https://kydlikebtc.github.io/awesome-jev/?lang=en#composio-typesafe-provider)** · `project` · cited file [`python/providers/typesafe/composio_typesafe/provider.py`](https://github.com/ComposioHQ/composio/blob/HEAD/python/providers/typesafe/composio_typesafe/provider.py), read by a person, 2026-09-22 · primitives: `choice`
<!-- read:end -->

**fastmcp-jev-search, `jev_search.py`.** The clearest two-stage selector. The wide pass ranks each chunk of the catalogue with a Choice over one-line summaries and keeps a shortlist; the close read asks a Choice over the shortlist with full descriptions and parameters, plus one fit Noul per candidate ("does this tool do the specific thing the request asks for?"). A candidate whose fit falls below a configurable line, which the docstring says to tune against your own users' queries, is dropped, so the answer can be empty. With the close read switched off, the fit question rides along in the wide pass and a search is a single round trip. Because probabilities from separate chunks are not comparable, each chunk's shortlist goes forward whole instead of through one merged cut; the constructor rejects settings that would break that (a shortlist more than half a chunk, a chunk larger than one Choice allows).

**cua-jev-use, `jev_adapter.py`.** Small and rigorous. One Choice over a candidate set built from the observation; the adapter rejects a selected id outside that set, a probability for a candidate it never offered, and any confidence or probability that is not finite and between 0 and 1. The same examples ship a mock that runs the loop with no key and no network, so the plumbing can be tested before anything is paid for.

**composio-typesafe-provider, `provider.py`.** What a full tool-calling layer looks like when the model cannot call tools. It compiles tools into questions and turns the answers into exactly one of a *call*, a *partial* call or an *abstain*, with separate thresholds for routing, the action gate and arguments. Its docstring states what its confidence is not: the score of the least certain judgement the call depends on, not a calibrated probability that the whole call is right. A destructive tool needs explicit confirmation to run, and API failures raise typed errors instead of masquerading as an abstention.

## What to copy, what to avoid

- Build the options from what actually exists at that moment, and check the answer is one of them.
- Always leave a way out: a none option, an abstain, or a Noul per candidate that lets the answer be empty.
- Keep requests small with a wide pass on summaries and a close read of a shortlist.
- Let Jev pick and something else write; do not ask a Choice to produce text.
- When unsure, hand the step back to the path that existed before. Do not force a pick.
- Do not treat a Choice's confidence as the probability that the whole action is right; it is about one question.
- Test with a mock and in shadow first, and measure on your own tasks; the benchmarks here measure whole agents.

## 要点（中文）

- 选项就是此刻真实存在的工具、界面元素或动作，状态就是请求；拿到答案后要检查它确实在选项里。
- Choice 总会选一个，所以要留“都不是”的出口：none 选项、弃权，或像 fastmcp-jev-search 那样给每个候选一个 Noul，让结果可以为空。
- 工具多时先用简短描述做一轮宽筛，再对候选短名单细读。
- Jev 负责选，写参数和文本交给别的模型；composio-typesafe-provider 在缺参数时返回“部分调用”。
- 不确定时退回原有路径（交给智能体自己的 LLM），不要硬选。
- Choice 的置信度只针对这一个问题，不等于整个动作正确的概率。
- 推荐阅读：fastmcp-jev-search 的两段式选择、cua-jev-use 的严格校验和离线 mock、composio-typesafe-provider 的 call / partial / abstain 设计。
