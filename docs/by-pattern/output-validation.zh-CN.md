# 输出校验

<sub>[awesome-jev](../../README.zh-CN.md) · [English](output-validation.md)</sub>

_在输出到达用户前，按评分标准检查模型产出。_

这个决策的全部已收录例子 —— 共 138 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#输出校验)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#output-validation)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#output-validation)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 2 · 调用点 133 · 接口形态 1 · 仅示例 0 · 独立报告 11 · 负面结果 0 · 未引用文件 4。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) <sub>`官方文档` · `Py` · `noul` · `score`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)** — 面向 AI 智能体的开源可观测性平台，在调用轨迹里标出智能体出错的地方。其中一个影子提供方问 Jev 每个标记维度一个 noul，一次调用最多 11 个；所引文件看不出这些答案是否会改变任何标记，README 也没有提到 Jev。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · latitude-dev · `TS` · 调用点 [`packages/platform/ai-jev/src/jev-shadow-decision-provider.ts`](https://github.com/latitude-dev/latitude-llm/blob/HEAD/packages/platform/ai-jev/src/jev-shadow-decision-provider.ts)，2026-09-22 阅读</sub>

- **[reticle](https://github.com/reticlehq/reticle)** — 通过实际操作正在运行的应用来核实 AI 智能体说的“完成”，给出通过、失败或无法判断。其基准测试框架就采集到的证据用一次调用问 Jev：五个 noul（预期结果是否发生、采集是否干净、应用是否报错等）、一个通过／失败／未知的 choice，以及一个严重程度 score。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★1k+ · reticlehq · `TS` · 调用点 [`bench/harness/jev.mjs`](https://github.com/reticlehq/reticle/blob/HEAD/bench/harness/jev.mjs)，2026-09-24 阅读</sub>

- **[abide](https://github.com/coldteadotai/abide)** — 接入 Claude Code、Codex、OpenCode 和 Pi，在每次编辑或每一轮，就 AGENTS.md 或 CLAUDE.md 中的每条规则问 Jev 一个是非题，只给它看规则和 diff；违反的规则会退回给智能体修改。在 93 个回放的会话中，Jev 标出了 39 次编辑，其中 10 次经审阅者确认。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · coldteadotai · `TS` · 调用点 [`packages/cli/src/lib/jev.ts`](https://github.com/coldteadotai/abide/blob/HEAD/packages/cli/src/lib/jev.ts)，2026-09-24 阅读</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — 编程智能体运行时：工作流是带版本的 TypeScript 阶段，包含可执行检查、评审关卡和人工审批。其 AI 包从 models.dev 收录 Jev，作为 5 家提供方上的 System One 决策模型，与聊天模型分开列出；README 没有说明工作流在哪里调用它。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · bastani-inc · `TS` · 调用点 [`packages/ai/src/decision-models.generated.ts`](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts)，2026-09-24 阅读</sub>

- **[Canny](https://github.com/qkal/Canny)** — 防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。
  <sub>`开源项目` · ★100+ · `TS` · `noul` · `score` · 调用点 [`src/jev.ts`](https://github.com/qkal/Canny/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — 浏览器智能体：每个页面被索引成候选控件，由 Jev 选出下一步，因此不会点击页面上没有的东西；规划和阅读由 Gemini Flash 负责，答案引用页面原文。维护者记录的 46 个任务中成功率为 99.2%，托管版 Browser Use 为 97.8%，而成本不到其十分之一。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · agent-labs-dev · `Py` · 调用点 [`src/fastbrowse/clients/typesafe.py`](https://github.com/agent-labs-dev/fastbrowse/blob/HEAD/src/fastbrowse/clients/typesafe.py)，2026-09-22 阅读</sub>

- **[formanator](https://github.com/timrogers/formanator)** — 从命令行或 MCP 客户端提交 Forma 福利报销。使用 --category-provider jev 时，Jev 用一个 choice 从 Forma 允许的“福利加类别”组合（另加 no_match）中挑一个，只看商家和描述；置信度低于 0.5 或无匹配时，回退到配置好的 LLM。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · timrogers · `Rs` · 调用点 [`src/typesafe.rs`](https://github.com/timrogers/formanator/blob/HEAD/src/typesafe.rs)，2026-09-22 阅读</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — 一个把评测工作通过类型化决策来路由的智能体。
  <sub>`开源项目` · ★100+ · vinilana · `TS` · 调用点 [`agent/lib/jev-router.ts`](https://github.com/vinilana/jev-eval-agent/blob/HEAD/agent/lib/jev-router.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给编程智能体用的安全钩子：每次工具调用前，Jev 判断这次调用可能造成多大危害、是不是用户要求的、是否在执行不可信的文字，再由代码决定拒绝、询问还是放行；调用返回后，Jev 扫描结果中的提示注入。支持 Claude Code、Codex、Cursor 等。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · leepokai · `JS` · 调用点 [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/HEAD/src/jev.js)，2026-09-22 阅读</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — 检查解析器查不出的问题的 lint 工具：由 ast-grep 挑出代码，再就每处匹配向 Jev 提出该规则的一句话问题，例如上方注释是否说了代码里不成立的事，概率超过规则的阈值就报出。随附 99 条规则，出自 48 个问题；被判断的代码会发送到 API。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · mizchi · `TS` · 调用点 [`src/jev.ts`](https://github.com/mizchi/jev-lint/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/provider.ts`](https://github.com/jkudish/jev-mcp/blob/HEAD/src/provider.ts)，2026-09-22 阅读</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — 一个本地优先的 MCP 插件，供编程智能体做持续的代码质量审查。
  <sub>`插件` · ★100+ · niazmorshed2007 · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/NiazMorshed2007/jev-review/blob/HEAD/src/jev/client.ts)，2026-09-22 阅读</sub>

- **[Jevlint (codegirl-007)](https://github.com/codegirl-007/jevlint)** — 按自然语言规则检查代码的 linter：用 Tree-sitter 提取每个代码单元，Jev 对每条规则回答一个 `choice`（通过、失败，可选跳过或弃权），只有置信度达到该规则的下限时才报告失败。也支持 OpenAI、OpenRouter 和 Cloudflare 后端。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · codegirl-007 · `Go` · `choice` · 调用点 [`internal/evaluation/client.go`](https://github.com/codegirl-007/jevlint/blob/HEAD/internal/evaluation/client.go)，2026-10-26 模型阅读</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `score` · `noul` · 调用点 [`src/cli.js`](https://github.com/lakeday-org/perch/blob/HEAD/src/cli.js)，2026-09-22 阅读</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — 给编程智能体用的代码质量与覆盖率判断，Rust 实现。
  <sub>`开源项目` · ★100+ · supercorp-ai · `Rs` · 调用点 [`crates/supercov-cli/src/quality.rs`](https://github.com/supercorp-ai/supercov/blob/HEAD/crates/supercov-cli/src/quality.rs)，2026-09-22 阅读</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — 由 44 个智能体、63 个技能和 79 个钩子组成的工具包，按大白话请求分派。它的 /d 路由器请 Jev 给请求分类，并在派发前确认所选路线不会改变用户要的结果；它的自动压缩插件在上下文超过 60% 后，对每个难以判断的工具调用提三个 noul，并逐字裁剪。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · notque · `Py` · 调用点 [`plugins/jev-auto-compact/hooks/jev-auto-compact.mjs`](https://github.com/notque/vexjoy-agent/blob/HEAD/plugins/jev-auto-compact/hooks/jev-auto-compact.mjs)，2026-09-22 阅读</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · 24601 · `Py` · 调用点 [`.agents/skills/augustus/SKILL.md`](https://github.com/24601/Augustus/blob/HEAD/.agents/skills/augustus/SKILL.md)，2026-09-24 阅读</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — 核查每篇被引论文是否支持引用它的那句话：一个模型证明引文，Jev 打分，人来裁定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · marissafamularo · `JS` · 调用点 [`src/lib/typesafe.js`](https://github.com/MarissaFamularo/citation-verifier/blob/HEAD/src/lib/typesafe.js)，2026-09-22 阅读</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code 与 Pi 插件，把智能体的小判断交给 Jev：一次编辑是否违反 CLAUDE.md 中的规则（违反则拦下并给出 file:line 引用）、压缩时逐字保留哪些上下文块、为每个子智能体选模型档位并用 noul 检查其任务说明，以及为每条提示给出路由提示。所有钩子都失败即放行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · 0x7067 · `Py` · 调用点 [`scripts/jev.py`](https://github.com/0x7067/claude-jev/blob/HEAD/scripts/jev.py)，2026-09-22 阅读</sub>

- **[cmd-mod-jev-nudge](https://github.com/CommandCodeAI/cmd-mod-jev-nudge)** — Command Code 的 mod：当智能体在还有工作未完成时停下，由 Jev 判断后推它继续。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · commandcodeai · `TS` · 调用点 [`src/protocol.ts`](https://github.com/CommandCodeAI/cmd-mod-jev-nudge/blob/HEAD/src/protocol.ts)，2026-09-24 阅读</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — DeepSeek Harness 插件，在工具输出进入上下文之前先问 Jev：长篇读取或抓取结果里哪些段落相关（按排序保留，不卡阈值）；抓回的页面里有没有针对 AI 的指令（概率达到 0.75 时附提醒，内容原样保留）；推荐哪一个技能；以及每条“完成”声明有没有证据。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · horusjiang · `TS` · 调用点 [`src/config.ts`](https://github.com/HorusJiang/dsh-jev-tools/blob/HEAD/src/config.ts)，2026-09-24 阅读</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · keeltrace · `Py` · 调用点 [`hermes_nerve/client.py`](https://github.com/keeltrace/hermes-nerve/blob/HEAD/hermes_nerve/client.py)，2026-09-22 阅读</sub>

- **[hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin)** — 给 Hermes Agent 的 Jev 决策工具：check／route／score／evaluate 四件套。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ajensenwaud · `Py` · 调用点 [`client.py`](https://github.com/ajensenwaud/hermes-jev-plugin/blob/HEAD/client.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[invalidate](https://github.com/chopratejas/invalidate)** — AI 记忆的失效层：每条事实都有租期，新证据会终结它。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · chopratejas · `Py` · 调用点 [`evals/screen_matrix.py`](https://github.com/chopratejas/invalidate/blob/HEAD/evals/screen_matrix.py)，2026-09-22 阅读</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code 的 Stop 钩子：在未经验证的“完成”之前拦下——读取会话记录找证据，只问 Jev 一次，其余情况一律放行。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · valentynkit · `JS` · 调用点 [`belay.mjs`](https://github.com/valentynkit/jev-belay/blob/HEAD/belay.mjs)，2026-09-24 阅读</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — 一个基于 Jev 与 Playwright 的统一内核：带类型的 SDK、常驻 CLI，以及带原生浏览器操作和确定性断言的 MCP 服务器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tontoko · `JS` · 调用点 [`src/decision.ts`](https://github.com/tontoko/jev-browser/blob/HEAD/src/decision.ts)，2026-09-24 阅读</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · francoischastel · `TS` · 调用点 [`integrations/opencode/jev.ts`](https://github.com/FrancoisChastel/jev-code/blob/HEAD/integrations/opencode/jev.ts)，2026-09-22 阅读</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · goodrahstar · `JS` · 调用点 [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/HEAD/lib/racers.mjs)，2026-09-22 阅读</sub>

- **[jev-commit](https://github.com/valentynkit/jev-commit)** — 一个 pre-commit 钩子：一次调用判断提交信息与 diff 是否相符。
  <sub>`开源项目` · ★10+ · valentynkit · `Py` · 调用点 [`jev_commit/jev.py`](https://github.com/valentynkit/jev-commit/blob/HEAD/jev_commit/jev.py)，2026-09-22 阅读</sub>

- **[jev-cua](https://github.com/ronadin2002/jev-cua)** — 用语音和文字控制 macOS：一个悬浮栏，由 Jev 实时选择界面操作，并持续执行“观察—行动—验证”循环。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · ronadin2002 · `Swift` · 调用点 [`Sources/Core.swift`](https://github.com/ronadin2002/jev-cua/blob/HEAD/Sources/Core.swift)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-e2e](https://github.com/perixtar/jev-e2e)** — 为网页应用编写自然语言的端到端测试，由 Jev 与 Playwright 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · perixtar · `TS` · 调用点 [`src/runner.ts`](https://github.com/perixtar/jev-e2e/blob/HEAD/src/runner.ts)，2026-09-24 阅读</sub>

- **[jev-enforce](https://github.com/erkamyaman/jev-enforce)** — 一个 Claude Code 插件，按你的 CLAUDE.md 或 AGENTS.md 检查每次回复和每次文件编辑：每条规则对应一个 Jev noul，全部放在一个请求里；违反的规则会通过 Stop 或 PostToolUse 钩子被引用回去，让 Claude 在同一轮内修正。也提供可用于 CI 的命令行工具。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · erkamyaman · `TS` · `noul` · 调用点 [`dist/src/jev.js`](https://github.com/erkamyaman/jev-enforce/blob/HEAD/dist/src/jev.js)，2026-10-24 模型阅读</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — 把语义决策变成普通 Ruby —— feels?、decide、score，以及 Rails 校验与模式匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · qew7 · `Rb` · 调用点 [`lib/jev/client.rb`](https://github.com/Qew7/jev-feels/blob/HEAD/lib/jev/client.rb)，2026-09-22 阅读</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — 精细的机器人控制，带物理预览与可配置的 LIBERO 任务。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · dimweaker · `Py` · 调用点 [`src/jev_libero/client.py`](https://github.com/Dimweaker/jev-libero/blob/HEAD/src/jev_libero/client.py)，2026-09-22 阅读</sub>

- **[jev-lint](https://github.com/ckorhonen/jev-lint)** — 面向编程 Agent 的模糊 linter：Agent 写完文件后，团队用自然语言写的每条规则都作为一个 Jev noul 来问，约 0.3 秒后 Agent 就能知道自己违反了哪些规则。可以从仓库自动生成规则；也可改用 Cloudflare 或 OpenAI 作为评判。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · ckorhonen · `TS` · `noul` · 调用点 [`src/jev.ts`](https://github.com/ckorhonen/jev-lint/blob/HEAD/src/jev.ts)，2026-10-24 模型阅读</sub>

- **[jev-pref](https://github.com/doeixd/jev-pref)** — 把 AGENTS.md 里的偏好变成一个由 Jev 驱动的快速 AI linter。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · doeixd · `JS` · 调用点 [`packages/jev-pref/src/config.js`](https://github.com/doeixd/jev-pref/blob/HEAD/packages/jev-pref/src/config.js)，2026-09-22 阅读</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — 可复现的基准：衡量 Jev 在 RAG 里的重排质量、延迟与成本。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · erendikmenn · `Py` · 调用点 [`src/jev_rag_benchmark/rerankers.py`](https://github.com/erendikmenn/jev-rag-benchmark/blob/HEAD/src/jev_rag_benchmark/rerankers.py)，2026-09-22 阅读 · 作者结论：有利（作者自述，未经本仓库复现）</sub>

- **[jev-recruiter](https://github.com/skeptrunedev/jev-recruiter)** — 由 Jev 驱动的领英招聘智能体：浏览相关档案并保存链接。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · skeptrunedev · `Py` · 调用点 [`jev_ultrafast/decision_provider.py`](https://github.com/skeptrunedev/jev-recruiter/blob/HEAD/jev_ultrafast/decision_provider.py)，2026-09-22 阅读</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · choxos · `JS` · 调用点 [`docs/jev.js`](https://github.com/choxos/jev-reviewer/blob/HEAD/docs/jev.js)，2026-09-22 阅读</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 的可疑行为，结合静态证据并明确标注覆盖范围。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · win4r · `Py` · 调用点 [`scripts/jev_client.py`](https://github.com/win4r/jev-security-scan/blob/HEAD/scripts/jev_client.py)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** — 每次提交都检查规格漂移：用 Jev 对照你的 Markdown 规格检查代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · nozomi-koborinai · `TS` · 调用点 [`src/evaluator/jev-evaluator.ts`](https://github.com/nozomi-koborinai/jev-spec/blob/HEAD/src/evaluator/jev-evaluator.ts)，2026-09-22 阅读</sub>

- **[jev-subtitle-translator](https://github.com/GeekLinkDev/jev-subtitle-translator)** — 用结构化 LLM 输出翻译 SRT 字幕，并让 Jev 检查每一条译文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · geeklinkdev · `Py` · 调用点 [`src/jev_subtitle_translator/cli.py`](https://github.com/GeekLinkDev/jev-subtitle-translator/blob/HEAD/src/jev_subtitle_translator/cli.py)，2026-09-24 阅读</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — 可配置的语义 lint，带文件级 NOUL 判断与一个「魔法字符串」插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · huntedman · `TS` · 调用点 [`src/jev-client.ts`](https://github.com/iamtoomas/JevLint/blob/HEAD/src/jev-client.ts)，2026-09-22 阅读</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — 由 Jev 自动完成的 PR 风险审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · hexyedev · `Py` · 调用点 [`src/JevPR/providers/jev.py`](https://github.com/HexyeDEV/JevPR/blob/HEAD/src/JevPR/providers/jev.py)，2026-09-24 阅读</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★10+ · kyu1204 · `TS` · `noul` · `choice` · `score` · 调用点 [`src/providers.ts`](https://github.com/kyu1204/jgrep/blob/HEAD/src/providers.ts)，2026-09-23 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[lejudge-jev-jepa](https://github.com/AbdelStark/lejudge-jev-jepa)** — 为 JEPA 世界模型规划写自然语言约束，由决策模型而非 LLM 来判定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · abdelstark · `Py` · 调用点 [`lejudge/judge/jev.py`](https://github.com/AbdelStark/lejudge-jev-jepa/blob/HEAD/lejudge/judge/jev.py)，2026-09-24 阅读</sub>

- **[lintus](https://github.com/virolea/lintus)** — 一个用自然语言写规则的代码检查器。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · virolea · `Rs` · 调用点 [`crates/jev/src/client.rs`](https://github.com/virolea/lintus/blob/HEAD/crates/jev/src/client.rs)，2026-09-24 阅读</sub>

- **[oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev)** — oxlint 插件：一条规则就是针对函数、调用、JSX 元素或整个文件的是非题；每个匹配都交给 Jev，当“是”的概率超过阈值时报错。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · wobsoriano · `TS` · 调用点 [`src/jev.ts`](https://github.com/wobsoriano/oxlint-plugin-jev/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — 用 Jev 做拦截、引导与「模糊 lint」，让智能体遵守你的规则与约定。含 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · tyler-dot-earth · `TS` · 调用点 [`apps/patdown/src/typesafe-judge.ts`](https://github.com/tyler-dot-earth/patdown/blob/HEAD/apps/patdown/src/typesafe-judge.ts)，2026-09-22 阅读</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — 给 pi 编程智能体的运行时约束：每个有副作用的工具调用执行前，先对照你说过的话检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · nyarlathoteppppp · `TS` · 调用点 [`bench/jev-lab.ts`](https://github.com/Nyarlathoteppppp/pi-heed/blob/HEAD/bench/jev-lab.ts)，2026-09-22 阅读</sub>

- **[Sedum (npm: sedum-cli)](https://github.com/sedum-dev/sedum)** — 在 Playwright 代码旁用纯英文句子编写浏览器端到端测试。目标模式下，由 Jev 的 Choice 选出每一步操作（点击、输入、完成或受阻）及其目标；逐句步骤每句用一个 Choice；每条验证断言是两个 Noul（holds、contradicted）。动作由 Playwright 执行，阈值由代码判定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · sedum-dev · `TS` · `choice` · `noul` · 调用点 [`packages/provider-typesafe/src/index.ts`](https://github.com/sedum-dev/sedum/blob/HEAD/packages/provider-typesafe/src/index.ts)，2026-09-30 阅读 · ⚠ `宣称未核实` `作者自荐`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · myc0576 · `Py` · 调用点 [`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/HEAD/src/smartmoney_cub_harness/jev/direct.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — 识别 AI 写作痕迹的文风 linter：零依赖，可计数规则外加一个判断模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · danrwilloughby · `TS` · 调用点 [`src/jev.ts`](https://github.com/DanRWilloughby/snifftest/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[taste-lint](https://github.com/mblode/taste-lint)** — 在发布前拦住 AI 水文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · mblode · `TS` · 调用点 [`src/map/jev.ts`](https://github.com/mblode/taste-lint/blob/HEAD/src/map/jev.ts)，2026-09-22 阅读</sub>

- **[typed_evals](https://github.com/TrustifAI/typed_evals)** — 为 LLM 与智能体输出提供快速、带类型、经校准的评估，由 Jev 驱动，附带简单且与框架无关的 Python API。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · trustifai · `Py` · 调用点 [`typed_evals/backends/jev.py`](https://github.com/TrustifAI/typed_evals/blob/HEAD/typed_evals/backends/jev.py)，2026-09-24 阅读</sub>

- **[vibecheck](https://github.com/RafalWilinski/vibecheck)** — Chrome 扩展：发推之前先用 Jev 给你的帖子做个氛围检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · rafalwilinski · `JS` · 调用点 [`background.js`](https://github.com/RafalWilinski/vibecheck/blob/HEAD/background.js)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · compozy · `TS` · 调用点 [`benchmarks/jev-calibrate.ts`](https://github.com/compozy/yoshi/blob/HEAD/benchmarks/jev-calibrate.ts)，2026-09-22 阅读</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — 可复用的 GitHub Action：由检查、AI 审查者与 Jev 共同把关的智能体修复循环。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ripwords · `TS` · 调用点 [`src/jev.ts`](https://github.com/Ripwords/agent-gate-loop/blob/HEAD/src/jev.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — 面向证据感知的智能体交接与有界工作续跑的实验性协议。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · zsoxi · `Py` · 调用点 [`tools/build_benchmark_prompts.py`](https://github.com/zsoXi/agent-handoff-gate/blob/HEAD/tools/build_benchmark_prompts.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `已归档`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jourdanlabs · `Py` · 调用点 [`harness/run.py`](https://github.com/jourdanlabs/assay-001/blob/HEAD/harness/run.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — 用确定性规则加 Jev 评估代码变更风险的 CLI 与 GitHub Action。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · moezubair · `TS` · 调用点 [`src/jev.ts`](https://github.com/moezubair/check-risk/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop 钩子：核对 AI 助手的声明与它这轮实际读过的内容是否相符。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · vladyslavhontar · `Py` · 调用点 [`stop_verify.py`](https://github.com/VladyslavHontar/clear-head/blob/HEAD/stop_verify.py)，2026-09-22 阅读</sub>

- **[deepseek-harness-jev (luobosibing2)](https://github.com/luobosibing2/dsh-jev-plugin)** — DeepSeek Harness 插件，提供 12 项需手动开启的功能，用 Jev 作为判断模型：技能选择和 glob 结果排序（每个候选一个 `noul`）、完成度与目标检查、偏离提醒、插话路由、工具输出和测试日志过滤，以及对单个工作区操作的审批。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · luobosibing2 · `TS` · `noul` · 调用点 [`packages/jev/src/selection.ts`](https://github.com/luobosibing2/dsh-jev-plugin/blob/HEAD/packages/jev/src/selection.ts)，2026-10-28 模型阅读</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — PR 风险路由器兼代码审查教练。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · raihankhan-rk · `TS` · 调用点 [`src/lib/review.ts`](https://github.com/raihankhan-rk/diffjury/blob/HEAD/src/lib/review.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[dinostomp](https://github.com/collapseindex/dinostomp)** — 面向 AI 评测的验证层：检查的是测量工具本身，而不仅仅是分数——数据、评分器、运行、数字与结论。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · collapseindex · `Py` · 调用点 [`audits/xstest-refusal-guards/compare.py`](https://github.com/collapseindex/dinostomp/blob/HEAD/audits/xstest-refusal-guards/compare.py)，2026-09-24 阅读</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — 给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · xienda · `JS` · 调用点 [`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/HEAD/lib/index.js)，2026-09-22 阅读</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — 经过验证的浏览器智能体：在任意 LLM 浏览器智能体前加一道便宜的 Jev 防护（经证据检查的完成判断、破坏性操作关卡）。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tom-r-main · `Py` · 调用点 [`jevdual/evals/runner.py`](https://github.com/Tom-R-Main/Footwork/blob/HEAD/jevdual/evals/runner.py)，2026-09-24 阅读</sub>

- **[human-compiler](https://github.com/asfarsadewa/human-compiler)** — 人类语言的编译器：粘贴文本，得到诊断，由 Jev 度量。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · asfarsadewa · `TS` · 调用点 [`src/worker/index.ts`](https://github.com/asfarsadewa/human-compiler/blob/HEAD/src/worker/index.ts)，2026-09-22 阅读</sub>

- **[hunch](https://github.com/Kelbie/hunch)** — 用 Jev、大白话规则与 Agent 技能做语义代码审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kelbie · `TS` · 调用点 [`packages/core/src/jev.ts`](https://github.com/Kelbie/hunch/blob/HEAD/packages/core/src/jev.ts)，2026-09-22 阅读</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — 面向编程智能体、并行 Git worktree 与代码审查的桌面工作区。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jackalope-dev · `Rs` · 调用点 [`apps/desktop/src-tauri/src/commands/jev.rs`](https://github.com/Jackalope-Dev/jackalope/blob/HEAD/apps/desktop/src-tauri/src/commands/jev.rs)，2026-09-22 阅读</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · Really Artificial · `JS` · `choice` · `score` · `noul` · 调用点 [`src/client.mjs`](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs)，2026-09-22 阅读 · ⚠ `疑似 AI 生成`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · yuyang2230 · `Py` · 调用点 [`jev.py`](https://github.com/yuyang2230/jev-agent-skill/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-align](https://github.com/caiovicentino/jev-align)** — 面向 LLM 回复与智能体计划的校准对齐验证器，由 Jev 驱动。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · caiovicentino · `JS` · 调用点 [`src/jev.mjs`](https://github.com/caiovicentino/jev-align/blob/HEAD/src/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — 实验性的逐次调用 GPT 模型路由，通过 Jev 与一个本地 Rescue 层为 Codex 服务。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · minilv · `TS` · 调用点 [`src/jev-adapter.ts`](https://github.com/miniLV/Jev-Auto-Router/blob/HEAD/src/jev-adapter.ts)，2026-09-22 阅读</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — 独立的 Jev 1.13.0 行为研究：报告、受控提示实验、原始结果与离线验证。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rinnecoder · `Py` · 调用点 [`behavior_study.py`](https://github.com/RINNECODER/jev-behavior-study/blob/HEAD/behavior_study.py)，2026-09-22 阅读</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)** — 引用的来源真的这么说了吗？一个包含 42 条论断的基准：Jev（TypeSafe System One）对比 GPT 与 Claude 等模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · thewaywithin · `Py` · 调用点 [`run.py`](https://github.com/TheWayWithin/jev-bench/blob/HEAD/run.py)，2026-09-24 阅读</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ufec · `Kt` · 调用点 [`app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt`](https://github.com/ufec/jev-block-android-ad/blob/HEAD/app/src/main/kotlin/me/ethanxu/jevnoisegate/app/ProxyProbe.kt)，2026-09-22 阅读</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — 给浏览器与桌面自动化的有界决策层：只做决策的模型负责选择。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · aidil2105 · `Py` · 调用点 [`src/jev_pilot/providers/jev.py`](https://github.com/aidil2105/jev-browser-pilot/blob/HEAD/src/jev_pilot/providers/jev.py)，2026-09-22 阅读</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)** — 在 Python 代码审查规则上比较 Jev、Gemini Flash 与 Claude Fable：成本、速度、准确率与一致性。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · gemanor · `Py` · 调用点 [`determinest/clients.py`](https://github.com/gemanor/jev-code-review-benchmark/blob/HEAD/determinest/clients.py)，2026-09-24 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-codes](https://github.com/Kushwho/jev-codes)** — 用 TypeSafe Jev 模型对照 YAML 编码规范包审计你的 git diff，可从 CLI 或 AI 智能体的命令中调用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kushwho · `TS` · 调用点 [`src/scorer/jev.ts`](https://github.com/Kushwho/jev-codes/blob/HEAD/src/scorer/jev.ts)，2026-09-24 阅读</sub>

- **[jev-debtgate](https://github.com/smlayero/jev-debtgate)** — 由 Jev 驱动的技术债关卡，面向编码智能体与 CI。自带 TypeSafe API key 即可使用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · smlayero · `TS` · 调用点 [`src/jev.ts`](https://github.com/smlayero/jev-debtgate/blob/HEAD/src/jev.ts)，2026-09-24 阅读</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions-hermes)** — 给 Hermes 及其他智能体的 Jev 决策插件：工具风险审查与人工批准。 <sub>(机翻)</sub>
  <sub>`插件` · bojansandhaus · `Py` · 调用点 [`jev_client.py`](https://github.com/bojansandhaus/jev-decisions-hermes/blob/HEAD/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)** — 让大量语义决策走同一条经过验证的路径的架构，附带标注数据集。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ghubnab99 · `C#` · 调用点 [`src/DecisionFabric.TypeSafe/TypeSafeClientOptions.cs`](https://github.com/ghubnab99/jev-enterprise-decision-fabric/blob/HEAD/src/DecisionFabric.TypeSafe/TypeSafeClientOptions.cs)，2026-09-22 阅读</sub>

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)** — Jev 探索性合集：宣称核查、实时演示与可运行代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · samuelsacco · `Py` · 调用点 [`jevlab/client.py`](https://github.com/SamuelSacco/jev-exploration/blob/HEAD/jevlab/client.py)，2026-09-22 阅读</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · foadsf · `Py` · 调用点 [`jev.py`](https://github.com/Foadsf/jev-for-engineers/blob/HEAD/jev.py)，2026-09-22 阅读</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — 给 Claude Code 的六道校准闸门：规则、范围、意图、完成度等。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · rashedint32 · `JS` · 调用点 [`lib/jev.mjs`](https://github.com/rashedInt32/jev-gates/blob/HEAD/lib/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — 为 Claude Code 提供概率评分的护栏：拒绝违反规则的修改和未经要求的部署，并把文档路由到合适的位置。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · muratcakmak · `TS` · 调用点 [`scripts/jev-lint.ts`](https://github.com/muratcakmak/jev-guard/blob/HEAD/scripts/jev-lint.ts)，2026-09-24 阅读 · ⚠ `仅一次提交`</sub>

- **[jev-labs](https://github.com/copyleftdev/jev-labs)** — 绝不自信地犯错：围绕 Jev 的 TLA+ 验证共识内核。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · copyleftdev · `Py` · 调用点 [`consensus/rust/consensus-kernel/src/jev.rs`](https://github.com/copyleftdev/jev-labs/blob/HEAD/consensus/rust/consensus-kernel/src/jev.rs)，2026-09-22 阅读</sub>

- **[jev-lm](https://github.com/y0usaf/jev-lm)** — 输出层就是 Jev 的词级语言模型：n-gram 起草，Noul 做分块校验。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · y0usaf · `TS` · 调用点 [`python/jev_lm/api.py`](https://github.com/y0usaf/jev-lm/blob/HEAD/python/jev_lm/api.py)，2026-09-22 阅读</sub>

- **[jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** — 用确定性检查加 Jev 语义判断，揪出藏在 OpenAPI 描述文字里的破坏性变更。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · shuhansun · `Py` · 调用点 [`src/jev_oas_sentinel/jev.py`](https://github.com/ShuhanSun/jev-oas-sentinel/blob/HEAD/src/jev_oas_sentinel/jev.py)，2026-09-22 阅读</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — 用 TypeSafe System One（Jev）为拉取请求给出类型化结论：一次并行调用，策略写在代码里，可作为 GitHub Action 使用。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · juanegido · `TS` · 调用点 [`dist/action/index.js`](https://github.com/juanegido/jev-pr-judge/blob/HEAD/dist/action/index.js)，2026-09-24 阅读</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — 给 Claude Code 的有界 Jev 风险检查：八个风险维度、一次请求。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · muse0509 · `Go` · 调用点 [`internal/jev/client.go`](https://github.com/muse0509/jev-preflight/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读</sub>

- **[jev-reasoning-navigator](https://github.com/AndreuVM/praxeon)** — JEV 推理导航器：面向自主 LLM 智能体的认知监督、防止循环与反幻觉引擎。 <sub>(机翻)</sub>
  <sub>`开源项目` · andreuvm · `Py` · 调用点 [`jev_navigator/core/typesafe_client.py`](https://github.com/AndreuVM/praxeon/blob/HEAD/jev_navigator/core/typesafe_client.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-resume-analyzer](https://github.com/awun8191/jev-resume-analyzer)** — 用 Jev、React 与 FastAPI 做简历诊断与岗位匹配。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · awun8191 · `Py` · 调用点 [`backend/app/gateways/typesafe.py`](https://github.com/awun8191/jev-resume-analyzer/blob/HEAD/backend/app/gateways/typesafe.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — 由 Jev 自主完成的拉取请求审查：带类型的决策、校准后的批准关卡，以及升级给可信负责人的机制。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · thiago-ss · `Py` · 调用点 [`jev_review/provider.py`](https://github.com/thiago-ss/jev-review/blob/HEAD/jev_review/provider.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · fatwang2 · `JS` · 调用点 [`src/jev.mjs`](https://github.com/fatwang2/jev-review-action/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[jev-rust-review](https://github.com/kindintelligence/jev-rust-review)** — 给 Claude Code 与编程智能体的 Rust 感知代码审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · kindintelligence · `Rs` · 调用点 [`src/jev.rs`](https://github.com/kindintelligence/jev-rust-review/blob/HEAD/src/jev.rs)，2026-09-22 阅读</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — 给某 lint 工具做的二次评估：用 Jev 评判 linter 的判断。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · blas0 · `JS` · 调用点 [`run-rule-cases.mjs`](https://github.com/blas0/jev-shadcn-lint-eval/blob/HEAD/run-rule-cases.mjs)，2026-09-22 阅读</sub>

- **[jev-suite](https://github.com/klauswg/jev-suite)** — 基于 Jev（TypeSafe System One）的四个决策质量工具：Jev 回答结构化问题，最终决定权留在确定性代码手里。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · klauswg · `Java` · 调用点 [`jev-fidelity/src/main/java/com/jevsuite/fidelity/eval/EvalRunner.java`](https://github.com/klauswg/jev-suite/blob/HEAD/jev-fidelity/src/main/java/com/jevsuite/fidelity/eval/EvalRunner.java)，2026-09-24 阅读</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — 由 Jev 驱动的 Markdown 知识库清洁工：Jev 对每篇笔记投票，你的代码负责归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · kylehovance-ai · `Py` · 调用点 [`janitor/client.py`](https://github.com/kylehovance-ai/jev-the-janitor/blob/HEAD/janitor/client.py)，2026-09-22 阅读</sub>

- **[jev-ui-test](https://github.com/buer2233/jev-ui-test)** — 基于 jev-ultrafast 分支改造的 UI 自动化测试框架：用例以自然语言 YAML 编写并由 pytest 执行，Jev 为每一步选出操作和目标；语义断言对页面上的每条原子陈述问一个 `noul`，通过阈值留在测试代码里。作者报告每次操作决策的中位耗时为 458 毫秒。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · buer2233 · `Py` · `noul` · 调用点 [`jev_ultrafast/framework/judge.py`](https://github.com/buer2233/jev-ui-test/blob/HEAD/jev_ultrafast/framework/judge.py)，2026-10-28 模型阅读 · ⚠ `厂商自报数据`</sub>

- **[jev-verify](https://github.com/stillmarcus24/jev-verify)** — 检查一份公开的 Jev 输出是否真的由 Jev 产生，并标记可疑的发布内容。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · stillmarcus24 · `JS` · 调用点 [`scripts/live_confirm.cjs`](https://github.com/stillmarcus24/jev-verify/blob/HEAD/scripts/live_confirm.cjs)，2026-09-24 阅读</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)** — 开源的自带 key 竞技场，用来评测 Jev 与其他 AI 裁判：找出失败案例，比较质量、成本与延迟。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · chenmingtang830 · `TS` · 调用点 [`jevjudge/providers.py`](https://github.com/chenmingtang830/jevarena/blob/HEAD/jevjudge/providers.py)，2026-09-24 阅读</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — 面向 CI 与编码智能体的代码审查关卡：就函数、文件、测试与依赖向 TypeSafe Jev 提出小而具体的类型化问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tech-byte-frontier · `Rs` · 调用点 [`src/auth/provider.rs`](https://github.com/Tech-Byte-Frontier/jevgate/blob/HEAD/src/auth/provider.rs)，2026-09-24 阅读</sub>

- **[jevguard](https://github.com/Jhonnyr97/JevGuard)** — Claude Code 与 Codex CLI 插件：用 System One 判断校验智能体是否遵守项目规则。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · jhonnyr97 · `TS` · 调用点 [`dist/bin/jevguard-hook.js`](https://github.com/Jhonnyr97/JevGuard/blob/HEAD/dist/bin/jevguard-hook.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jevibe-check](https://github.com/sriganesh/jevibe-check)** — 给 Bluesky 帖子与草稿做实时语气标注。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · sriganesh · `JS` · 调用点 [`extension/background.js`](https://github.com/sriganesh/jevibe-check/blob/HEAD/extension/background.js)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[jevkit](https://github.com/ariel-frischer/jevkit)** — 用 Rust 写的快速 CLI：类型化决策，付费之前先离线 lint。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ariel-frischer · `Rs` · 调用点 [`src/auth.rs`](https://github.com/ariel-frischer/jevkit/blob/HEAD/src/auth.rs)，2026-09-22 阅读</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — 由 Jev 驱动的 ATS 友好简历评审。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · unownone · `TS` · 调用点 [`packages/jev/http.ts`](https://github.com/unownone/jevsume/blob/HEAD/packages/jev/http.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[JevTest](https://github.com/CorieW/JevTest)** — 用 Jev 做有边界的探索式浏览器测试，配合确定性断言和可回放的证据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · coriew · `TS` · 调用点 [`src/jev.ts`](https://github.com/CorieW/JevTest/blob/HEAD/src/jev.ts)，2026-09-24 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[jevtest](https://github.com/realZachi/jevtest)** — 面向 Vitest 与 Jest 的语义测试匹配器，由 TypeSafe Jev 模型驱动。用自然语言写期望。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · realzachi · `TS` · 调用点 [`packages/jevtest/src/types.ts`](https://github.com/realZachi/jevtest/blob/HEAD/packages/jevtest/src/types.ts)，2026-09-24 阅读</sub>

- **[jod](https://github.com/mateonunez/jod)** — 构建在 Jev 之上的语义 schema：先在本地校验状态，再投影出类型化答案。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · mateonunez · `TS` · 调用点 [`e2e/support.ts`](https://github.com/mateonunez/jod/blob/HEAD/e2e/support.ts)，2026-09-22 阅读</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — 一个 Stop 钩子，阻止编程智能体过早收工 —— 用大白话写规则，由 Jev 裁定。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · noplan-inc · `Py` · 调用点 [`limpet.py`](https://github.com/noplan-inc/limpet/blob/HEAD/limpet.py)，2026-09-22 阅读</sub>

- **[lossless-rewrite](https://github.com/dttfrancesco/lossless-rewrite)** — AI 文本改写与文档摘要，由 Jev 检查是否遗漏了观点并自动修复。提供本地编辑器。 <sub>(项目旧自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dttfrancesco · `TS` · 调用点 [`lib/decision/client.ts`](https://github.com/dttfrancesco/lossless-rewrite/blob/HEAD/lib/decision/client.ts)，2026-09-24 阅读</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · khmuhtadin · `TS` · 调用点 [`nodes/JevClassification/JevClassification.node.ts`](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/HEAD/nodes/JevClassification/JevClassification.node.ts)，2026-09-22 阅读</sub>

- **[omp-typesafe](https://github.com/siddicky/omp-typesafe)** — 为 omp 编码智能体提供的 TypeSafe AI（Jev）对抗式审查器与 typesafe_ask 工具。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · siddicky · `TS` · 调用点 [`src/client.ts`](https://github.com/siddicky/omp-typesafe/blob/HEAD/src/client.ts)，2026-09-24 阅读</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — 给 Codex 与 Claude Code 的二值批准闸门：每次被拦截的工具调用都要审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · alexj11324 · `Go` · 引用文件 [`internal/jev/client.go`](https://github.com/alexj11324/open-jev-approvals/blob/HEAD/internal/jev/client.go)，2026-09-22 阅读 · ⚠ `并非 Jev 本身`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — 给 OpenClaw 的可选类型化 Jev 决策，带 SecretRef 凭据与严格的 API 校验。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · olli0103 · `TS` · 调用点 [`src/client.ts`](https://github.com/Olli0103/openclaw-typesafe-ai/blob/HEAD/src/client.ts)，2026-09-22 阅读</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — 单智能体的 Pi 编程协处理器，带 Jev 语义闸门与基线对比 diff 审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · kamilpostrozny · `TS` · 调用点 [`src/index.ts`](https://github.com/KamilPostrozny/pi-jev-code/blob/HEAD/src/index.ts)，2026-09-22 阅读</sub>

- **[plotveil](https://github.com/Dearest/plotveil)** — YouTube 评论的安静剧透拦截器：每条评论一次类型化 Noul 决策。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · dearest · `TS` · 调用点 [`scripts/evaluate-jev.ts`](https://github.com/Dearest/plotveil/blob/HEAD/scripts/evaluate-jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[profanity-checker](https://github.com/4rays/profanity-checker)** — 用 Jev 检查脏话的 Cloudflare Worker。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 4rays · `TS` · 调用点 [`src/endpoints/profanityCheck.ts`](https://github.com/4rays/profanity-checker/blob/HEAD/src/endpoints/profanityCheck.ts)，2026-09-22 阅读</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — 给 pytest 的语义断言：测试 LLM 应用输出的含义，由 Jev 判定。 <sub>(机翻)</sub>
  <sub>`插件` · allebee · `Py` · 调用点 [`src/pytest_jev/judge.py`](https://github.com/allebee/pytest-jev/blob/HEAD/src/pytest_jev/judge.py)，2026-09-22 阅读</sub>

- **[riff](https://github.com/scale-venture-partners/riff)** — 小而快的文风 linter：ruff 式的规则编码，由 Jev 支撑。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · scale-venture-partners · `Py` · 调用点 [`src/riff/jev.py`](https://github.com/scale-venture-partners/riff/blob/HEAD/src/riff/jev.py)，2026-09-22 阅读</sub>

- **[semantic-assert](https://github.com/mondaychen/semantic-assert)** — 用来断言“真实需求”的测试库。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`SDK` · mondaychen · `TS` · 调用点 [`packages/semantic-assert-typesafe/src/client.ts`](https://github.com/mondaychen/semantic-assert/blob/HEAD/packages/semantic-assert-typesafe/src/client.ts)，2026-09-24 阅读</sub>

- **[solvi](https://github.com/solvi-ai/solvi)** — Python 决策运行时，内置 System One API 适配器：由 Jev、LLM 或本地模型给出类型化答案，再由硬性检查、规则和校准阈值决定采纳、弃权或转交人工；每个决策都保存为可重放的哈希链记录。 <sub>(机翻)</sub>
  <sub>`SDK` · mxkuzn · `Py` · `choice` · `noul` · 调用点 [`src/solvi/core/deciders/systemone.py`](https://github.com/solvi-ai/solvi/blob/HEAD/src/solvi/core/deciders/systemone.py)，2026-10-23 阅读 · ⚠ `作者自荐`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — 智能体的每一次工具调用在执行前都过一遍检查的 Claude Code 插件。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · getexcited · `TS` · 调用点 [`lib/jev.ts`](https://github.com/getexcited/stepwarden/blob/HEAD/lib/jev.ts)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

- **[system-one-playground](https://github.com/DonaldMurillo/system-one-playground)** — 可读的脚本、语义代码检查、一个 Go System One 客户端与配套 Studio。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · donaldmurillo · `Go` · 调用点 [`typesafe/client.go`](https://github.com/DonaldMurillo/system-one-playground/blob/HEAD/typesafe/client.go)，2026-09-22 阅读</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server 兼 agent 技能：把一个判断分解成多个类型化问题。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · simota · `TS` · 调用点 [`skills/tenbin/scripts/evaluate.py`](https://github.com/simota/tenbin/blob/HEAD/skills/tenbin/scripts/evaluate.py)，2026-09-22 阅读</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — 在用户看到之前先审判每一条 LLM 响应。提供 AI SDK middleware 与 OpenAI 兼容代理。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · noelzappy · `TS` · 调用点 [`src/judge/jev.ts`](https://github.com/noelzappy/tripwire/blob/HEAD/src/judge/jev.ts)，2026-09-22 阅读</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — 智能体工具调用执行前防火墙的影子模式验证 harness。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · anshchoudhary · `Py` · 调用点 [`firewall/judge.py`](https://github.com/AnshChoudhary/typesafe-ai-firewall/blob/HEAD/firewall/judge.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — 给 Codex 与 Claude Code 的非官方社区 MCP 插件，用 Jev 做有界路由。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · e-fl · `JS` · 调用点 [`server/judge.mjs`](https://github.com/E-FL/typesafe-as-a-judge/blob/HEAD/server/judge.mjs)，2026-09-22 阅读</sub>

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)** — 关于为代码审查校准 Jev 的研究。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · selmar · `Py` · 调用点 [`calibrate.py`](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review/blob/HEAD/calibrate.py)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — 由 Jev 驱动的数据库迁移安全自动审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · opaielsheikh · `TS` · 调用点 [`lib/typesafe.ts`](https://github.com/opaielsheikh/typesafe-migration-guard/blob/HEAD/lib/typesafe.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — 用 Typesafe.AI 生成 diff 审查。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · rbalch · `Py` · 调用点 [`src/typesafe_review/ask.py`](https://github.com/rbalch/typesafeai-review/blob/HEAD/src/typesafe_review/ask.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[zod-jev](https://github.com/jomatsu/zod-jev)** — Zod 校验结构，Jev 校验含义：把 schema 上的语义检查（是否含个人数据、价格是否合理、类别是否匹配）一次性发给 Jev，得到的校准概率再转成 Zod 的校验问题。 <sub>(机翻)</sub>
  <sub>`SDK` · jomatsu · `TS` · 调用点 [`src/types.ts`](https://github.com/jomatsu/zod-jev/blob/HEAD/src/types.ts)，2026-09-24 阅读</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

- **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)** — 汇总了目前已有的第三方评测，并讨论决策模型能在多大程度上顶替 LLM 评判者。
  <sub>`文章` · Laurie Voss</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
