# 输出校验

<sub>[awesome-jev](../../README.zh-CN.md) · [English](output-validation.md)</sub>

_在输出到达用户前，按评分标准检查模型产出。_

这个决策的全部已收录例子 —— 共 134 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#输出校验)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐ — 用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)** — 面向 AI 智能体的开源可观测性：定位智能体在哪里失败。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4,672 · latitude-dev · `TS`</sub>

- **[reticle](https://github.com/reticlehq/reticle)** — AI 智能体能生成代码，却仍难以理解自己构建的东西。Reticle 用 TypeSafe Jev 路由验证流程，并由 Jev 驱动对页面的探索。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★830 · reticlehq · `TS`</sub>

- **[atomic](https://github.com/bastani-inc/atomic)** — 可验证的编程智能体运行时：用自然语言定义智能体的流程。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★820 · bastani-inc · `TS`</sub>

- **[vexjoy-agent](https://github.com/notque/vexjoy-agent)** — 带 Jev 智能路由的 AI 智能体：把大白话请求分派给合适的专家智能体。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★425 · notque · `Py`</sub>

- **[jev-mcp](https://github.com/jkudish/jev-mcp)** — 现成的 Agent 判断工具箱：事实核验、内容筛查、语义排序、分类和信息提取，各自独立成工具。
  <sub>`插件` · ★320 · `JS` · `choice` · `score` · `noul`</sub>

- **[JevRev](https://github.com/Alex314618-create/JevRev)** — LLM 身边的决策层：Jev 负责筛选方案、检查进度，把注意力留在值得继续的工作上；LLM 负责广度和具体实现。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★303 · alex314618-create · `TS`</sub>

- **[jev-review](https://github.com/NiazMorshed2007/jev-review)** — 一个本地优先的 MCP 插件，供编程智能体做持续的代码质量审查。
  <sub>`插件` · ★217 · niazmorshed2007 · `TS`</sub>

- **[abide](https://github.com/coldteadotai/abide)** — 让你的编码智能体遵守项目里的所有规则。 <sub>(机翻)</sub>
  <sub>`插件` · ★211 · coldteadotai · `TS`</sub>

- **[perch: semantic code linting](https://github.com/lakeday-org/perch)** — 先用 tree-sitter 找出并排序方法，再把用户自写的 YAML 规则编译成 noul；严重度取评分量表的期望值，而不是概率最高的那一档。
  <sub>`开源项目` · ★173 · `JS` · `choice` · `score` · `noul`</sub>

- **[supercov](https://github.com/supercorp-ai/supercov)** — 给编程智能体用的代码质量与覆盖率判断，Rust 实现。
  <sub>`开源项目` · ★109 · supercorp-ai · `Rs`</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)** — 一个把评测工作通过类型化决策来路由的智能体。
  <sub>`开源项目` · ★105 · vinilana · `TS` · ⚠ `无许可证`</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)** — 快速浏览器智能体：Jev 从页面现有内容里挑动作，LLM 负责阅读与规划。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★100 · agent-labs-dev · `Py`</sub>

- **[formanator](https://github.com/timrogers/formanator)** — 从命令行和 MCP 客户端提交福利报销单。 <sub>(机翻)</sub>
  <sub>`插件` · ★99 · timrogers · `Rs`</sub>

- **[jev-lint](https://github.com/mizchi/jev-lint)** — 用 Jev 打分器给代码中的文本做 lint。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★78 · mizchi · `TS`</sub>

- **[Canny](https://github.com/qkal/Canny)** — 防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。
  <sub>`开源项目` · ★74 · `TS` · `noul` · `score`</sub>

- **[jev-libero](https://github.com/Dimweaker/jev-libero)** — 精细的机器人控制，带物理预览与可配置的 LIBERO 任务。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★64 · dimweaker · `Py`</sub>

- **[oxlint-plugin-jev](https://github.com/wobsoriano/oxlint-plugin-jev)** — oxlint 插件：一条规则就是针对函数、调用、JSX 元素或整个文件的是非题；每个匹配都交给 Jev，当“是”的概率超过阈值时报错。 <sub>(机翻)</sub>
  <sub>`插件` · ★60 · wobsoriano · `TS`</sub>

- **[jev-recruiter](https://github.com/skeptrunedev/jev-recruiter)** — 由 Jev 驱动的领英招聘智能体：浏览相关档案并保存链接。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★47 · skeptrunedev · `Py`</sub>

- **[vibecheck](https://github.com/RafalWilinski/vibecheck)** — Chrome 扩展：发推之前先用 Jev 给你的帖子做个氛围检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★47 · rafalwilinski · `JS` · ⚠ `无许可证`</sub>

- **[jev-suite](https://github.com/klauswg/jev-suite)** — 基于 Jev（TypeSafe System One）的四个决策质量工具：Jev 回答结构化问题，最终决定权留在确定性代码手里。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★36 · klauswg · `Java`</sub>

- **[jev-cua](https://github.com/ronadin2002/jev-cua)** — 用语音和文字控制 macOS：一个悬浮栏，由 Jev 实时选择界面操作，并持续执行“观察—行动—验证”循环。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★34 · ronadin2002 · `Swift` · ⚠ `无许可证`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★33 · choxos · `JS`</sub>

- **[jev-guard](https://github.com/leepokai/jev-guard)** — 给所有编程智能体做的自动模式：结合会话上下文给每次工具调用打风险分（拒绝／询问／放行）。 <sub>(机翻)</sub>
  <sub>`插件` · ★30 · leepokai · `JS`</sub>

- **[snifftest](https://github.com/DanRWilloughby/snifftest)** — 识别 AI 写作痕迹的文风 linter：零依赖，可计数规则外加一个判断模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★29 · danrwilloughby · `TS`</sub>

- **[smartmoney-cub](https://github.com/myc0576/SmartMoney-Cub)** — 只读的交易日志与复盘 harness：Jev 类型化判断、智能体集成，以及一个可复现的金融基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★26 · myc0576 · `Py`</sub>

- **[yoshi](https://github.com/compozy/yoshi)** — 给 Claude Code 和 Codex 做的上下文裁剪代理：由 Jev 判断哪些历史还需要 —— 实测而非宣称。 <sub>(机翻)</sub>
  <sub>`插件` · ★25 · compozy · `TS`</sub>

- **[jgrep (npm: jevgrep)](https://github.com/kyu1204/jgrep)** — 按代码的作用来 grep：对每个代码块、diff 块或 CSV 行问一个 Noul，输出带概率的 file:line 命中。--diff 用一条英文规则在 CI 里为 PR 把关（退出码 0 命中 / 1 干净 / 2 出错）；--tests 列出一次 diff 可能影响的测试文件。
  <sub>`开源项目` · ★24 · kyu1204 · `TS` · `noul` · `choice` · `score` · ⚠ `宣称未核实`</sub>

- **[jev-column-race](https://github.com/goodrahstar/jev-column-race)** — Jev 对比一个轻量 LLM：标注 1000 条应用评论，快 4.1 倍、便宜 7 倍。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★23 · goodrahstar · `JS`</sub>

- **[hermes-jev](https://github.com/keeltrace/hermes-nerve)** — 类型化的 System One 决策、排序、校验，以及可选启用的 Hermes 工具闸门。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★20 · keeltrace · `Py`</sub>

- **[invalidate](https://github.com/chopratejas/invalidate)** — AI 记忆的失效层：每条事实都有租期，新证据会终结它。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★18 · chopratejas · `Py`</sub>

- **[jev-belay](https://github.com/valentynkit/jev-belay)** — Claude Code 的 Stop 钩子：在未经验证的“完成”之前拦下——读取会话记录找证据，只问 Jev 一次，其余情况一律放行。 <sub>(机翻)</sub>
  <sub>`插件` · ★18 · valentynkit · `JS`</sub>

- **[jev-code](https://github.com/FrancoisChastel/jev-code)** — 把 Jev 作为工具接入多个编程智能体。 <sub>(机翻)</sub>
  <sub>`插件` · ★15 · francoischastel · `TS`</sub>

- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark)** — 可复现的基准：衡量 Jev 在 RAG 里的重排质量、延迟与成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★14 · erendikmenn · `Py`</sub>

- **[patdown](https://github.com/tyler-dot-earth/patdown)** — 用 Jev 做拦截、引导与「模糊 lint」，让智能体遵守你的规则与约定。含 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★14 · tyler-dot-earth · `TS`</sub>

- **[cmd-mod-jev-nudge](https://github.com/CommandCodeAI/cmd-mod-jev-nudge)** — Command Code 的 mod：当智能体在还有工作未完成时停下，由 Jev 判断后推它继续。 <sub>(机翻)</sub>
  <sub>`插件` · ★13 · commandcodeai · `TS`</sub>

- **[claude-jev](https://github.com/0x7067/claude-jev)** — Claude Code 插件：Jev 负责规则检查、逐字压缩与提示路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★12 · 0x7067 · `Py`</sub>

- **[lintus](https://github.com/virolea/lintus)** — 一个用自然语言写规则的代码检查器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · virolea · `Rs`</sub>

- **[jev-commit](https://github.com/valentynkit/jev-commit)** — 一个 pre-commit 钩子：一次调用判断提交信息与 diff 是否相符。
  <sub>`开源项目` · ★11 · valentynkit · `Py`</sub>

- **[jevlint](https://github.com/iamtoomas/JevLint)** — 可配置的语义 lint，带文件级 NOUL 判断与一个「魔法字符串」插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★11 · huntedman · `TS`</sub>

- **[jev-feels](https://github.com/Qew7/jev-feels)** — 把语义决策变成普通 Ruby —— feels?、decide、score，以及 Rails 校验与模式匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10 · qew7 · `Rb`</sub>

- **[jev-security-scan](https://github.com/win4r/jev-security-scan)** — 使用 TypeSafe Jev 审查 Skill 与 MCP 的可疑行为，结合静态证据并明确标注覆盖范围。 <sub>(机翻)</sub>
  <sub>`插件` · ★10 · win4r · `Py`</sub>

- **[augustus](https://github.com/24601/Augustus)** — 面向决策模型这一类别的 agent 技能：分类器、编解码器、专用 AR 头、System One。 <sub>(机翻)</sub>
  <sub>`插件` · ★9 · 24601 · `Py`</sub>

- **[JevPR](https://github.com/HexyeDEV/JevPR)** — 由 Jev 自动完成的 PR 风险审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · hexyedev · `Py`</sub>

- **[lejudge-jev-jepa](https://github.com/AbdelStark/lejudge-jev-jepa)** — 为 JEPA 世界模型规划写自然语言约束，由决策模型而非 LLM 来判定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · abdelstark · `Py`</sub>

- **[typed_evals](https://github.com/TrustifAI/typed_evals)** — 为 LLM 与智能体输出提供快速、带类型、经校准的评估，由 Jev 驱动，附带简单且与框架无关的 Python API。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · trustifai · `Py`</sub>

- **[zod-jev](https://github.com/jomatsu/zod-jev)** — Zod 校验结构，Jev 校验含义：把 schema 上的语义检查（是否含个人数据、价格是否合理、类别是否匹配）一次性发给 Jev，得到的校准概率再转成 Zod 的校验问题。 <sub>(机翻)</sub>
  <sub>`SDK` · ★8 · jomatsu · `TS`</sub>

- **[citation-verifier](https://github.com/MarissaFamularo/citation-verifier)** — 核查每篇被引论文是否支持引用它的那句话：一个模型证明引文，Jev 打分，人来裁定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · marissafamularo · `JS`</sub>

- **[diffjury](https://github.com/raihankhan-rk/diffjury)** — PR 风险路由器兼代码审查教练。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · raihankhan-rk · `TS` · ⚠ `无许可证`</sub>

- **[jev-auto-router](https://github.com/miniLV/Jev-Auto-Router)** — 实验性的逐次调用 GPT 模型路由，通过 Jev 与一个本地 Rescue 层为 Codex 服务。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · minilv · `TS`</sub>

- **[jev-browser](https://github.com/tontoko/jev-browser)** — 一个基于 Jev 与 Playwright 的统一内核：带类型的 SDK、常驻 CLI，以及带原生浏览器操作和确定性断言的 MCP 服务器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · tontoko · `JS`</sub>

- **[jev-guard](https://github.com/muratcakmak/jev-guard)** — 为 Claude Code 提供概率评分的护栏：拒绝违反规则的修改和未经要求的部署，并把文档路由到合适的位置。 <sub>(机翻)</sub>
  <sub>`插件` · ★7 · muratcakmak · `TS`</sub>

- **[jev-pref](https://github.com/doeixd/jev-pref)** — 把 AGENTS.md 里的偏好变成一个由 Jev 驱动的快速 AI linter。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · doeixd · `JS`</sub>

- **[pi-heed](https://github.com/Nyarlathoteppppp/pi-heed)** — 给 pi 编程智能体的运行时约束：每个有副作用的工具调用执行前，先对照你说过的话检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · nyarlathoteppppp · `TS`</sub>

- **[dinostomp](https://github.com/collapseindex/dinostomp)** — 面向 AI 评测的验证层：检查的是测量工具本身，而不仅仅是分数——数据、评分器、运行、数字与结论。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · collapseindex · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · ufec · `Kt`</sub>

- **[jev-lm](https://github.com/y0usaf/jev-lm)** — 输出层就是 Jev 的词级语言模型：n-gram 起草，Noul 做分块校验。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · y0usaf · `TS`</sub>

- **[jev-spec](https://github.com/nozomi-koborinai/jev-spec)** — 每次提交都检查规格漂移：用 Jev 对照你的 Markdown 规格检查代码。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · nozomi-koborinai · `TS`</sub>

- **[riff](https://github.com/scale-venture-partners/riff)** — 小而快的文风 linter：ruff 式的规则编码，由 Jev 支撑。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · scale-venture-partners · `Py`</sub>

- **[dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools)** — 用 Jev 做判断而不是生成：修剪过长的工具输出、筛查抓取页面中注入的指令、为“完成”把关。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · horusjiang · `TS`</sub>

- **[hermes-jev-plugin](https://github.com/ajensenwaud/hermes-jev-plugin)** — 给 Hermes Agent 的 Jev 决策工具：check／route／score／evaluate 四件套。 <sub>(机翻)</sub>
  <sub>`插件` · ★5 · ajensenwaud · `Py`</sub>

- **[jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark)** — 在 Python 代码审查规则上比较 Jev、Gemini Flash 与 Claude Fable：成本、速度、准确率与一致性。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · gemanor · `Py`</sub>

- **[jev-e2e](https://github.com/perixtar/jev-e2e)** — 为网页应用编写自然语言的端到端测试，由 Jev 与 Playwright 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · perixtar · `TS`</sub>

- **[hunch](https://github.com/Kelbie/hunch)** — 用 Jev、大白话规则与 Agent 技能做语义代码审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · kelbie · `TS`</sub>

- **[jev-align](https://github.com/caiovicentino/jev-align)** — 面向 LLM 回复与智能体计划的校准对齐验证器，由 Jev 驱动。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · caiovicentino · `JS`</sub>

- **[jev-codes](https://github.com/Kushwho/jev-codes)** — 用 TypeSafe Jev 模型对照 YAML 编码规范包审计你的 git diff，可从 CLI 或 AI 智能体的命令中调用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · kushwho · `TS`</sub>

- **[jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel)** — 用确定性检查加 Jev 语义判断，揪出藏在 OpenAPI 描述文字里的破坏性变更。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · shuhansun · `Py`</sub>

- **[jevarena](https://github.com/chenmingtang830/jevarena)** — 开源的自带 key 竞技场，用来评测 Jev 与其他 AI 裁判：找出失败案例，比较质量、成本与延迟。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★4 · chenmingtang830 · `TS`</sub>

- **[jevgate](https://github.com/Tech-Byte-Frontier/jevgate)** — 面向 CI 与编码智能体的代码审查关卡：就函数、文件、测试与依赖向 TypeSafe Jev 提出小而具体的类型化问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · tech-byte-frontier · `Rs`</sub>

- **[semantic-assert](https://github.com/mondaychen/semantic-assert)** — 用来断言“真实需求”的测试库。 <sub>(机翻)</sub>
  <sub>`SDK` · ★4 · mondaychen · `TS`</sub>

- **[taste-lint](https://github.com/mblode/taste-lint)** — 在发布前拦住 AI 水文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · mblode · `TS`</sub>

- **[jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)** — 独立的 Jev 1.13.0 行为研究：报告、受控提示实验、原始结果与离线验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · rinnecoder · `Py`</sub>

- **[jev-exploration](https://github.com/SamuelSacco/jev-exploration)** — Jev 探索性合集：宣称核查、实时演示与可运行代码。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · samuelsacco · `Py` · ⚠ `无许可证`</sub>

- **[jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)** — 八个最小可运行示例：把 Jev 用在机械与电气工程场景。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · foadsf · `Py`</sub>

- **[jevkit](https://github.com/ariel-frischer/jevkit)** — 用 Rust 写的快速 CLI：类型化决策，付费之前先离线 lint。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · ariel-frischer · `Rs`</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — 由 Jev 驱动的 ATS 友好简历评审。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · unownone · `TS` · ⚠ `无许可证`</sub>

- **[jevtest](https://github.com/realZachi/jevtest)** — 面向 Vitest 与 Jest 的语义测试匹配器，由 TypeSafe Jev 模型驱动。用自然语言写期望。 <sub>(机翻)</sub>
  <sub>`SDK` · ★3 · realzachi · `TS`</sub>

- **[jod](https://github.com/mateonunez/jod)** — 构建在 Jev 之上的语义 schema：先在本地校验状态，再投影出类型化答案。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · mateonunez · `TS`</sub>

- **[limpet](https://github.com/noplan-inc/limpet)** — 一个 Stop 钩子，阻止编程智能体过早收工 —— 用大白话写规则，由 Jev 裁定。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · noplan-inc · `Py`</sub>

- **[open-jev-approvals](https://github.com/alexj11324/open-jev-approvals)** — 给 Codex 与 Claude Code 的二值批准闸门：每次被拦截的工具调用都要审查。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★3 · alexj11324 · `Go` · ⚠ `并非 Jev 本身`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server 兼 agent 技能：把一个判断分解成多个类型化问题。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · simota · `TS`</sub>

- **[tripwire](https://github.com/noelzappy/tripwire)** — 在用户看到之前先审判每一条 LLM 响应。提供 AI SDK middleware 与 OpenAI 兼容代理。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★3 · noelzappy · `TS`</sub>

- **[typesafe-jev-calibrate-for-code-review](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review)** — 关于为代码审查校准 Jev 的研究。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★3 · selmar · `Py` · ⚠ `无许可证`</sub>

- **[clear-head](https://github.com/VladyslavHontar/clear-head)** — Claude Code Stop 钩子：核对 AI 助手的声明与它这轮实际读过的内容是否相符。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · vladyslavhontar · `Py`</sub>

- **[jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot)** — 给浏览器与桌面自动化的有界决策层：只做决策的模型负责选择。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · aidil2105 · `Py`</sub>

- **[jev-decisions](https://github.com/bojansandhaus/jev-decisions)** — 给 Hermes 及其他智能体的 Jev 决策插件：工具风险审查与人工批准。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · bojansandhaus · `Py`</sub>

- **[jev-pr-judge](https://github.com/juanegido/jev-pr-judge)** — 用 TypeSafe System One（Jev）为拉取请求给出类型化结论：一次并行调用，策略写在代码里，可作为 GitHub Action 使用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · juanegido · `TS`</sub>

- **[jev-rust-review](https://github.com/kindintelligence/jev-rust-review)** — 给 Claude Code 与编程智能体的 Rust 感知代码审查。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · kindintelligence · `Rs`</sub>

- **[jev-scout](https://github.com/AkashPriyadarshii/jev-scout)** — 由 Jev 打分驱动的开源仓库与 crate 侦察工具。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · akashpriyadarshii · `Rs`</sub>

- **[jevibe-check](https://github.com/sriganesh/jevibe-check)** — 给 Bluesky 帖子与草稿做实时语气标注。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · sriganesh · `JS`</sub>

- **[n8n-nodes-jev-classification](https://github.com/khmuhtadin/n8n-nodes-jev-classification)** — Jev 的 n8n 社区节点：带校准概率的文本分类、打分与检查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · khmuhtadin · `TS`</sub>

- **[pytest-jev](https://github.com/allebee/pytest-jev)** — 给 pytest 的语义断言：测试 LLM 应用输出的含义，由 Jev 判定。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · allebee · `Py`</sub>

- **[typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall)** — 智能体工具调用执行前防火墙的影子模式验证 harness。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · anshchoudhary · `Py` · ⚠ `无许可证`</sub>

- **[typesafe-as-a-judge](https://github.com/E-FL/typesafe-as-a-judge)** — 给 Codex 与 Claude Code 的非官方社区 MCP 插件，用 Jev 做有界路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · e-fl · `JS`</sub>

- **[typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)** — 由 Jev 驱动的数据库迁移安全自动审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · opaielsheikh · `TS` · ⚠ `无许可证`</sub>

- **[datajev](https://github.com/zzz1YAO/DataJev)** — 用 System-1 控制 System-2：继续／切换／校验／停止。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · zzz1yao · `Py`</sub>

- **[dsh-jev-verify](https://github.com/xienda/dsh-jev-verify)** — 给 DeepSeek Harness 的 Jev 决策工具与实时验证基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · xienda · `JS`</sub>

- **[Footwork](https://github.com/Tom-R-Main/Footwork)** — 经过验证的浏览器智能体：在任意 LLM 浏览器智能体前加一道便宜的 Jev 防护（经证据检查的完成判断、破坏性操作关卡）。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · tom-r-main · `Py`</sub>

- **[human-compiler](https://github.com/asfarsadewa/human-compiler)** — 人类语言的编译器：粘贴文本，得到诊断，由 Jev 度量。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · asfarsadewa · `TS`</sub>

- **[jackalope](https://github.com/Jackalope-Dev/jackalope)** — 面向编程智能体、并行 Git worktree 与代码审查的桌面工作区。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jackalope-dev · `Rs`</sub>

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)** — 十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。
  <sub>`开源项目` · ★1 · Really Artificial · `JS` · `choice` · `score` · `noul` · ⚠ `仅一次提交` `疑似 AI 生成`</sub>

- **[jev-bench](https://github.com/TheWayWithin/jev-bench)** — 引用的来源真的这么说了吗？一个包含 42 条论断的基准：Jev（TypeSafe System One）对比 GPT 与 Claude 等模型。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · thewaywithin · `Py`</sub>

- **[jev-debtgate](https://github.com/smlayero/jev-debtgate)** — 由 Jev 驱动的技术债关卡，面向编码智能体与 CI。自带 TypeSafe API key 即可使用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · smlayero · `TS`</sub>

- **[jev-labs](https://github.com/copyleftdev/jev-labs)** — 绝不自信地犯错：围绕 Jev 的 TLA+ 验证共识内核。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · copyleftdev · `Py`</sub>

- **[jev-preflight](https://github.com/muse0509/jev-preflight)** — 给 Claude Code 的有界 Jev 风险检查：八个风险维度、一次请求。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · muse0509 · `Go`</sub>

- **[jev-reasoning-navigator](https://github.com/AndreuVM/jev-reasoning-navigator)** — JEV 推理导航器：面向自主 LLM 智能体的认知监督、防止循环与反幻觉引擎。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · andreuvm · `Py` · ⚠ `无许可证`</sub>

- **[jev-review-action](https://github.com/fatwang2/jev-review-action)** — 可配置的 GitHub 提交审查与 PR 分类，不使用任何文本生成模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · fatwang2 · `JS`</sub>

- **[jev-subtitle-translator](https://github.com/GeekLinkDev/jev-subtitle-translator)** — 用结构化 LLM 输出翻译 SRT 字幕，并让 Jev 检查每一条译文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · geeklinkdev · `Py`</sub>

- **[jevguard](https://github.com/Jhonnyr97/JevGuard)** — Claude Code 与 Codex CLI 插件：用 System One 判断校验智能体是否遵守项目规则。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · jhonnyr97 · `TS`</sub>

- **[lossless-rewrite](https://github.com/dttfrancesco/lossless-rewrite)** — AI 文本改写与文档摘要，由 Jev 检查是否遗漏了观点并自动修复。提供本地编辑器。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · dttfrancesco · `TS`</sub>

- **[omp-typesafe](https://github.com/siddicky/omp-typesafe)** — 为 omp 编码智能体提供的 TypeSafe AI（Jev）对抗式审查器与 typesafe_ask 工具。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · siddicky · `TS`</sub>

- **[plotveil](https://github.com/Dearest/plotveil)** — YouTube 评论的安静剧透拦截器：每条评论一次类型化 Noul 决策。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · dearest · `TS`</sub>

- **[profanity-checker](https://github.com/4rays/profanity-checker)** — 用 Jev 检查脏话的 Cloudflare Worker。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · 4rays · `TS`</sub>

- **[stepwarden](https://github.com/getexcited/stepwarden)** — 智能体的每一次工具调用在执行前都过一遍检查的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★1 · getexcited · `TS`</sub>

- **[system-one-playground](https://github.com/DonaldMurillo/system-one-playground)** — 可读的脚本、语义代码检查、一个 Go System One 客户端与配套 Studio。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · donaldmurillo · `Go`</sub>

- **[agent-gate-loop](https://github.com/Ripwords/agent-gate-loop)** — 可复用的 GitHub Action：由检查、AI 审查者与 Jev 共同把关的智能体修复循环。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · ripwords · `TS` · ⚠ `无许可证`</sub>

- **[agent-handoff-gate](https://github.com/zsoXi/agent-handoff-gate)** — 面向证据感知的智能体交接与有界工作续跑的实验性协议。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · zsoxi · `Py`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jourdanlabs · `Py` · ⚠ `无许可证`</sub>

- **[check-risk](https://github.com/moezubair/check-risk)** — 用确定性规则加 Jev 评估代码变更风险的 CLI 与 GitHub Action。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · moezubair · `TS`</sub>

- **[jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)** — 给 AI 智能体的免费类型化判断：把分类／筛查／打分／校验卸载给 Jev。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · yuyang2230 · `Py`</sub>

- **[jev-enterprise-decision-fabric](https://github.com/ghubnab99/jev-enterprise-decision-fabric)** — 让大量语义决策走同一条经过验证的路径的架构，附带标注数据集。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · ghubnab99 · `C#`</sub>

- **[jev-gates](https://github.com/rashedInt32/jev-gates)** — 给 Claude Code 的六道校准闸门：规则、范围、意图、完成度等。 <sub>(机翻)</sub>
  <sub>`插件` · ★0 · rashedint32 · `JS`</sub>

- **[jev-resume-analyzer](https://github.com/awun8191/jev-resume-analyzer)** — 用 Jev、React 与 FastAPI 做简历诊断与岗位匹配。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · awun8191 · `Py` · ⚠ `无许可证`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — 由 Jev 自主完成的拉取请求审查：带类型的决策、校准后的批准关卡，以及升级给可信负责人的机制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · thiago-ss · `Py` · ⚠ `无许可证`</sub>

- **[jev-shadcn-lint-eval](https://github.com/blas0/jev-shadcn-lint-eval)** — 给某 lint 工具做的二次评估：用 Jev 评判 linter 的判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · blas0 · `JS`</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — 由 Jev 驱动的 Markdown 知识库清洁工：Jev 对每篇笔记投票，你的代码负责归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kylehovance-ai · `Py`</sub>

- **[jev-verify](https://github.com/stillmarcus24/jev-verify)** — 检查一份公开的 Jev 输出是否真的由 Jev 产生，并标记可疑的发布内容。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · stillmarcus24 · `JS`</sub>

- **[JevTest](https://github.com/CorieW/JevTest)** — 用 Jev 做有边界的探索式浏览器测试，配合确定性断言和可回放的证据。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · coriew · `TS` · ⚠ `无许可证`</sub>

- **[openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai)** — 给 OpenClaw 的可选类型化 Jev 决策，带 SecretRef 凭据与严格的 API 校验。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · olli0103 · `TS`</sub>

- **[pi-jev-code](https://github.com/KamilPostrozny/pi-jev-code)** — 单智能体的 Pi 编程协处理器，带 Jev 语义闸门与基线对比 diff 审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kamilpostrozny · `TS`</sub>

- **[typesafeai-review](https://github.com/rbalch/typesafeai-review)** — 用 Typesafe.AI 生成 diff 审查。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · rbalch · `Py` · ⚠ `无许可证`</sub>

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)** — 找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。
  <sub>`基准测试` · Near Here</sub>

- **[TypeSafe's Jev: Can decision models replace LLM judges?](https://arize.com/blog/typesafe-jev-llm-judge/)** — 汇总了目前已有的第三方评测，并讨论决策模型能在多大程度上顶替 LLM 评判者。
  <sub>`文章` · Laurie Voss</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
