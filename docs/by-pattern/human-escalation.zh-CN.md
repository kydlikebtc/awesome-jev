# 人工升级

<sub>[awesome-jev](../../README.zh-CN.md) · [English](human-escalation.md)</sub>

_用校准置信度决定哪些情况必须由人来看。_

这个决策的全部已收录例子 —— 共 67 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#人工升级)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐ — 把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐ — 用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐ — 判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐ — 在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐ — 把不确定的概率转人工复核，同时保留底层的 noul 数值本身，而不是压成一个标签了事。
  <sub>`官方文档` · `Py` · `noul`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐ — 把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。
  <sub>`官方文档` · `Py`</sub>

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐ — confidence 如何从概率分布推导出来，以及为什么在一种问题类型上调好的阈值不能挪到另一种上用。
  <sub>`官方文档`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)** — 把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。
  <sub>`平台集成` · ★46,958 · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)** — 把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。
  <sub>`开源项目` · ★30,300 · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)** — 七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。
  <sub>`开源项目` · ★12,328 · `TS` · `choice` · `noul`</sub>

- **[jev-review](https://github.com/devagrawal09/jev-review)** — 代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。
  <sub>`开源项目` · ★582 · `TS` · `choice` · `score` · `noul`</sub>

- **[jev-align](https://github.com/sutro-sh/jev-align)** — 从人类反馈出发，构建经过校准的决策函数。
  <sub>`开源项目` · ★284 · sutro-sh · `Py`</sub>

- **[Probing Jev's behaviour with repeated API calls](https://github.com/ahastudio/til)** — 独立的韩语实测笔记，报告仅仅把选项顺序倒过来，就能让概率移动到足以翻转 0.9 阈值的程度。
  <sub>`基准测试` · ★190 · `Py` · ⚠ `无许可证` `宣称未核实`</sub>

- **[neurolink](https://github.com/juspay/neurolink)** — 用一套 TypeScript 接口对接 40 家 AI 供应商，覆盖生成、流式与决策三种推理形态。 <sub>(机翻)</sub>
  <sub>`插件` · ★139 · juspay · `TS`</sub>

- **[Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)** — 一个 Discord 审核机器人：用 Choice 给每条消息定级、用 Noul 表示封禁紧急度，管理员一旦赦免，该消息会作为「安全先例」注入后续请求。
  <sub>`开源项目` · ★44 · brainstormity · `Py` · `choice` · `noul`</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)** — 面向 Jev 式决策模型的开源训练与推理栈。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★34 · zwlijay · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[jev-calibrate](https://github.com/smkrv/jev-calibrate)** — 用你自己的标注数据校准 Jev 的问题：在标注样本上调 criteria，在留出集上确认。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★31 · smkrv · `TS`</sub>

- **[jevalyn](https://github.com/Ray-Hughes/jevalyn)** — 给 Rails 应用的决策层：对 Jev System One API 的 Rails 原生封装。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★19 · ray-hughes · `Rb`</sub>

- **[jevwire](https://github.com/Brainwires/jevwire)** — 给智能体的 Jev 决策层：MCP server、可嵌入的 DecisionModel 库，以及一个只做升级的 Claude Code 插件。 <sub>(机翻)</sub>
  <sub>`插件` · ★18 · brainwires · `TS`</sub>

- **[jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)** — 类型化、带置信度感知的 agent 技能路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★17 · godsboy · `Py`</sub>

- **[jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)** — 面向类型化决策模型的概率感知评测：校准度、选择性风险、延迟，以及可复现的基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★17 · abdelstark · `Py`</sub>

- **[jeval](https://github.com/rlaope/jeval)** — 衡量 Jev 分类器的置信度究竟值多少，并根据出错的代价设定交给人类处理的分界线。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★16 · rlaope · `Py`</sub>

- **[muse-jev-playbook](https://github.com/Bodila51/muse-jev-playbook)** — 为 Muse 提供的 Jev 决策层：在昂贵的智能体工作之前加一道快速、便宜的 TypeSafe AI 关卡——置信度策略与配方。 <sub>(机翻)</sub>
  <sub>`插件` · ★16 · bodila51 · `Py`</sub>

- **[discern](https://github.com/doeixd/discern)** — 类型安全、感知不确定性的语义模式匹配与控制流。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · doeixd · `TS`</sub>

- **[jev-harness](https://github.com/AntonioCoppe/jev-harness)** — Jev 决策 harness：置信闸门、影子模式、配方与评测。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★12 · antoniocoppe · `TS`</sub>

- **[jevcal](https://github.com/abhixhek/jevcal)** — 对着一个 LLM 教师模型做校准、定阈值和漂移检查 —— 而不是靠猜。
  <sub>`开源项目` · ★10 · abhixhek · `Py`</sub>

- **[jevflow](https://github.com/Mawfyy/jevflow)** — 把概率式 AI 决策做成可组合的后端原语。 <sub>(机翻)</sub>
  <sub>`平台集成` · ★9 · mawfyy · `TS` · ⚠ `无许可证`</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — 编程智能体的记忆：每条事实都是一句逐字引文，由 Jev 的校准置信度评级。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★9 · romiluz13 · `Py`</sub>

- **[typesafe-local](https://github.com/aabolfazl/typesafe-local)** — 受 TypeSafe 启发：向本地 LLM 提类型化问题，拿到校准概率。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★8 · aabolfazl · `Py`</sub>

- **[jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab)** — 在 DSPy 工作流中对 Jev 决策做可复现的校准与选择性风险基准。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★7 · jmanhype · `Py`</sub>

- **[luce](https://github.com/scienthoon/luce)** — Luce：一份校准决策模型的配方 —— 输入一句任务描述，产出一个小模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★7 · scienthoon · `Py`</sub>

- **[poorjev](https://github.com/rupeshpoojary9/poorjev)** — 开源的本地 Jev 替代品：一个有可证校准置信度的 System One 决策层。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★7 · rupeshpoojary9 · `Py` · ⚠ `并非 Jev 本身`</sub>

- **[daf-jev](https://github.com/docxology/daf-jev)** — 可组合的 Python 工具包：问题构造器、置信闸门等。 <sub>(机翻)</sub>
  <sub>`插件` · ★6 · docxology · `Py`</sub>

- **[jev-block-android-ad](https://github.com/ufec/jev-block-android-ad)** — Android 上的通知与短信过滤：不是匹配关键词，而是由模型判断。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★6 · ufec · `Kt`</sub>

- **[jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration)** — 在一个它不可能见过的任务上做独立校准测试：900 条规则生成的支持工单。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★6 · scienthoon · `Py`</sub>

- **[jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench)** — 在 2000 封钓鱼邮件上对比 Jev 与一个轻量 LLM：准确率、校准度、延迟、成本。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★5 · anisselbd · `Py` · ⚠ `无许可证`</sub>

- **[jev-usecases](https://github.com/kenhuangus/jev-usecases)** — 生产级的 Jev 用例 harness，带置信度门控的决策逻辑。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kenhuangus · `Py`</sub>

- **[typed-decisions](https://github.com/kotoba-lang/typed-decisions)** — Jev 形状的类型化决策模型：状态加问题进，校准概率出。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★5 · kotoba-lang · `Py`</sub>

- **[opencode-jev-orchestrator](https://github.com/aaronshaf/opencode-jev-orchestrator)** — 让 OpenCode 粘在便宜模型上以保持缓存热度，由 Jev 把困难的轮次升级给更强的模型。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · aaronshaf · `TS`</sub>

- **[qwen-rlcd](https://github.com/shamazharikh/qwen-rlcd)** — 基于 Qwen3.5-0.8B 的 Jev 风格校准决策模型（Choice／Score／Noul）。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · shamazharikh · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[system-one-gemma](https://github.com/akash-kamat/system-one-gemma)** — 开源的 Jev 式 System One 决策模型：Gemma 3 270M 加一个打分头。 <sub>(机翻)</sub>
  <sub>`Jev 替代实现` · ★4 · akash-kamat · `Py` · ⚠ `并非 Jev 本身` `无许可证`</sub>

- **[tink-route](https://github.com/jon-devlapaz/tink-route)** — 动态的、感知置信度的 Agent 技能路由。 <sub>(机翻)</sub>
  <sub>`插件` · ★4 · jon-devlapaz · `Py`</sub>

- **[jev-flash-router](https://github.com/Ravinder82/jev-flash-router)** — 开源的 jev-flash-router：给 Jev 的 MCP server。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · ravinder82 · `TS`</sub>

- **[jev-ui](https://github.com/etweisberg/jev-ui)** — React 组件：由决策模型决定渲染哪个组件、列表如何排序、是否展示。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · etweisberg · `TS` · ⚠ `无许可证`</sub>

- **[pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)** — 一个 pi 扩展，把 Jev 判断暴露成五个 pi 工具，让模型能做狭义的语义判断。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · legacybridge-tech · `TS`</sub>

- **[tenbin](https://github.com/simota/tenbin)** — MCP server 兼 agent 技能：把一个判断分解成多个类型化问题。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · simota · `TS`</sub>

- **[grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard)** — Grok Bot 的类型化预检与审批层：硬性边界由本地策略掌控，模糊情况交给 Jev 判断，Grok Bot 只在返回的范围内执行。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · 0xwhrari · `Py`</sub>

- **[jev-mcp-server](https://github.com/wangkuangkuang/jev-mcp-server)** — Jev 的 MCP server：提供官方三种问题类型。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · wangkuangkuang · `Py`</sub>

- **[jev-starter](https://github.com/hamakyo/jev-starter)** — 基于 Jev 的类型化、策略驱动决策工作流：置信路由、回退与评测。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · hamakyo · `TS`</sub>

- **[jevbus](https://github.com/zkjoie/jevbus)** — 一个流式事件总线：路由、订阅与消费都由概率决策决定。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · zkjoie · `Rs`</sub>

- **[opencode-jev-guard](https://github.com/CogFlux/opencode-jev-guard)** — OpenCode 2 插件：把每条 shell 命令发给 TypeSafe 的 Jev，看起来有风险时先询问你。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · cogflux · `TS`</sub>

- **[toolgate](https://github.com/RiskAverseTech/toolgate)** — 面向 AI 智能体的开源自动模式：一个校准过的工具调用防火墙。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · riskaversetech · `TS`</sub>

- **[toolgate](https://github.com/ndolinschi/toolgate)** — 智能体工具与 MCP 调用关卡：通过 TypeSafe Jev 决定放行、询问人类或拒绝。 <sub>(机翻)</sub>
  <sub>`插件` · ★2 · ndolinschi · `TS` · ⚠ `无许可证`</sub>

- **[watfile](https://github.com/jexp/watfile)** — 用 Jev 或本地校准决策模型给文本与 PDF 分类归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · jexp · `Py` · ⚠ `无许可证`</sub>

- **[jev-eval](https://github.com/4esv/jev-eval)** — 在你自己的标注分类数据上，把 Jev 与任意 OpenRouter 模型做基准对比：准确率与校准度。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · 4esv · `Py` · ⚠ `无许可证`</sub>

- **[jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)** — 由 Jev 判断一批日志是否值得处理：类型化问题、置信闸门，不执行任何动作。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · jyatesdotdev · `Py`</sub>

- **[padflow-jev-evals](https://github.com/zsavage8/padflow-jev-evals)** — 来自某土地开发 SaaS 的类型化决策基准：schema、匿名标注数据与运行器。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★1 · zsavage8 · `Py`</sub>

- **[qualm](https://github.com/qddegtya/qualm)** — 来自 System One 模型的类型化决策 —— 不确定性是你必须自己处理的东西。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · qddegtya · `TS`</sub>

- **[assay-001](https://github.com/jourdanlabs/assay-001)** — ASSAY-001：对 Jev 校准度与类型安全宣称的独立、预注册验证。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · jourdanlabs · `Py` · ⚠ `无许可证`</sub>

- **[Example: confidence-gated escalation](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/02-confidence-gate/main.py)** — 带「自动执行或转人工」闸门的路由；策略函数刻意留空 —— 阈值该定在哪，是你的决定。
  <sub>`代码片段` · `Py` · `choice` · ⚠ `代码未实测`</sub>

- **[jev-asks-until-sure](https://github.com/mintannn/jev-asks-until-sure)** — 二十个问题猜谜：一直问下去，直到 Jev 的校准置信度越过阈值。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · mintannn · `TS`</sub>

- **[jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit)** — 仅通过 API 对 Jev 做的独立校准审计。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · jujumilk3 · `Py`</sub>

- **[jev-guard](https://github.com/CMaintz/jev-guard)** — 在 LLM 智能体的工具调用执行前，交给 TypeSafe AI 的 Jev 审核——放行、阻止或挂起，不确定时安全失败。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · cmaintz · `TS`</sub>

- **[jev-review](https://github.com/thiago-ss/jev-review)** — 由 Jev 自主完成的拉取请求审查：带类型的决策、校准后的批准关卡，以及升级给可信负责人的机制。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · thiago-ss · `Py` · ⚠ `无许可证`</sub>

- **[jev-the-janitor](https://github.com/kylehovance-ai/jev-the-janitor)** — 由 Jev 驱动的 Markdown 知识库清洁工：Jev 对每篇笔记投票，你的代码负责归档。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · kylehovance-ai · `Py`</sub>

- **[n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai)** — 面向 System One API 的 n8n 社区节点：类型化的是非、选择与打分问题。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · dommonte · `TS`</sub>

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)** — 找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。
  <sub>`基准测试` · Lindfors</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
