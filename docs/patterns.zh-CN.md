# 决策模式

<sub>[English](patterns.md)</sub>

> 本页由模型根据英文版 [docs/patterns.md](patterns.md) 译写，尚未经人工审校；两者如有出入，以英文版为准。

本目录按决策模式而不是按资源类型建索引：你这周读到的博客文章转眼就过时，模式不会。本页逐个定义每个模式：它做什么决策、为什么适合交给校准过的决策模型，以及什么时候应该改用别的办法。

## 三种原语

下面每个模式都由这三种原语搭成。结构取自官方 API 参考 —— 确切网址见 [`sources.md`](sources.md)。

| `type` | 返回 | `criteria` | 限制 |
| --- | --- | --- | --- |
| `noul` | `noul`：一个 0–1 之间的是/否概率 | 可选的 `{true, false}` 描述 | — |
| `choice` | `choice` + `probabilities` + `confidence` | 必填：选项 → 描述的映射 | **最多 255 个选项** |
| `score` | `score` + `legend` + `probabilities` + `confidence` | 必填：有序的等级数组 | **2–10 级，从 0 开始编号** |

三个容易让人踩坑的事实：

1. **`noul` 的回答不带 `confidence` 字段。** 概率*本身*就是答案。`choice` 和 `score` 另带一个 `confidence`，由概率分布的形状推算而来。针对 `noul` 概率调好的阈值不能挪到 `choice` 的置信度上用 —— 两者是不同的量。
2. **`score` 按概率加权，会落在等级之间。** 文档自己的例子在三级量表上返回 `1.05`。不要假定它是整数。
3. **输入只能是文本。** 字符串、JSON 对象或文本数组。不支持图像、音频或视频 —— 先把它们预处理成文本。正因如此，本目录没有视觉分类这一模式。

让本页其余内容成立的性质是**校准**：置信度与准确率相符，所以阈值是一根政策杠杆，而不是瞎猜。正是这一点，才让「高于 `t` 就执行、低于 `t` 就升级」这种结构成为可能。

## 判断一个决策是否适合放在这里

一个决策适合，需要以下各条**全部**成立：

1. **答案空间是封闭的。** 你能事先列举出所有选项。如果答案是一段文字，你需要的是生成式模型。
2. **它运行得很频繁。** 智能体的内循环、每条消息一次调用、每份文档一次调用。一天才做一次的决策，不需要便宜。
3. **出错可以承受或能被发现。** 要么这一步可以撤销，要么置信度阈值能把拿不准的情况转给人。
4. **上下文放得下。** 每次请求总共 64k token，其中 `state` 加上最长的那一个问题最多 32k token。

只要有一条不成立，那个位置就继续用 LLM。实际的分工是：开放式的推理和写作交给生成式模型，一路上那些频繁的类型化判断交给决策模型，政策交给普通代码。

厂商自己的[能力参差文档](https://docs.typesafe.ai/model-jaggedness/jev-1.13)列出了当前模型的弱项 —— 字面阅读、算术与计数、日期比较、间接引用、塞满无关细节的大型 state、对抗性内容。围绕其中任何一项做设计之前，先读它。

---

## tool-selection

**决策：** 根据到目前为止的对话和可用的工具，智能体下一步该调用哪个工具 —— 还是一个都不调用？

**为什么适合：** 这是智能体循环里最频繁的判断，而且是在你手头已有的列表上做封闭式选择。答案必须匹配 schema，这就消除了一类失败：在四个工具之间做选择的智能体，不可能凭空造出第五个。

**形态：** 在工具名上加一个 `none` 选项，做 `choice`。按置信度设闸门，选择很接近时回退到规划模型。

**何时不该用：** 挑工具需要先拟定计划时，或者难点在于参数时。这里只选择*用哪个*；参数仍需别的东西来填。

<!-- catalogued-tool-selection:start -->
目录中的**工具选择**：共 230 条，[逐条列出并附警示](by-pattern/tool-selection.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=zh)。
<!-- catalogued-tool-selection:end -->

---

## intent-routing

**决策：** 这位用户到底想要什么，该由哪个分支来处理？

**为什么适合：** 经典的文本分类 —— 在这类任务上，它相对 LLM 的成本与延迟优势最大。路由位于其他一切之前，所以它的延迟会加到每一个请求上。

**形态：** 在意图上做 `choice`；当分支同时取决于紧急度时，再加一个衡量紧急度的 `score` —— 放在同一次请求里问，因为各个问题是针对同一次摄入的 state 并行评估的。

**何时不该用：** 意图之间重叠得太厉害，连人工标注者都无法与自己保持一致时。先修好分类体系。

<!-- catalogued-intent-routing:start -->
目录中的**意图路由**：共 35 条，[逐条列出并附警示](by-pattern/intent-routing.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=zh)。
<!-- catalogued-intent-routing:end -->

---

## context-compaction

**决策：** 在一个长会话里，前面哪些工具调用和结果仍然相关？

**为什么适合：** 另一种做法是摘要，而摘要会改写原文，恰恰丢掉后面某一步需要的细节 —— 一条错误信息、一个 ID、一个文件路径。对每一项决定*留还是丢*，留下来的内容就能**原样**保留。

**形态：** 每一项一个 `noul`；或者，当你想不断丢掉排名最低的项、直到回到预算以内时，用一个衡量相关性的 `score`。

**何时不该用：** 会话本来就放得下时。压缩会带来一种新的失败方式 —— 丢掉了后来才发现很重要的东西 —— 所以在上下文压力真正出现之前，别为它付出代价。

<!-- catalogued-context-compaction:start -->
目录中的**上下文压缩**：共 34 条，[逐条列出并附警示](by-pattern/context-compaction.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=zh)。
<!-- catalogued-context-compaction:end -->

---

## safety-gating

**决策：** 这个动作执行起来安全吗？

**形态：** 用 `noul` 做放行/拦截；或者用 `score` 给出风险档位，再映射为放行 / 确认 / 拦截。

**何时不该用 —— 这一条请仔细读：** 概率性的闸门是**纵深防御，不是安全边界**。任何真正具有破坏性或不可逆的操作，都需要确定性的规则、权限系统或人。用决策模型去拦住粗心，而不是去围堵对抗：输入由攻击者挑选，一个 99% 的情况下都正确的模型，正是攻击者会去试探剩下那 1% 的模型。厂商的能力参差文档把对抗性内容列为已知弱项。

<!-- catalogued-safety-gating:start -->
目录中的**安全闸门**：共 139 条，[逐条列出并附警示](by-pattern/safety-gating.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=zh)。
<!-- catalogued-safety-gating:end -->

---

## output-validation

**决策：** 这段生成的输出在给用户看之前达标了吗？

**为什么适合：** 按评分标准检查是一种类型化判断，而只有足够便宜，才负担得起对每一次生成都跑一遍。这就是「LLM 当评审」（LLM-as-judge）的活儿，只是把经济账算对了。

**形态：** 按评分标准给一个 `score`；如果你想知道*是哪一条*规则没通过，而不是一个总分，就每条标准一个 `noul`。

**何时不该用：** 当缺陷需要被解释、而不只是被发现时。分数说明输出不好，却不说明怎么改。对被它拒掉的情况，配上一段生成式的点评。

<!-- catalogued-output-validation:start -->
目录中的**输出校验**：共 134 条，[逐条列出并附警示](by-pattern/output-validation.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=zh)。
<!-- catalogued-output-validation:end -->

---

## retry-control

**决策：** 这一步失败了 —— 重试、换个做法，还是停下？

**形态：** 在 `retry` / `retry-modified` / `escalate` / `abort` 上做 `choice`。

**何时不该用：** 错误本身已经是机器可读的时候。一个带 `Retry-After` 头的 HTTP 429 不需要模型；它需要你去读那个头。先走确定性规则，再把那些说不清的情况交给决策模型。

<!-- catalogued-retry-control:start -->
目录中的**重试控制**：共 7 条，[逐条列出并附警示](by-pattern/retry-control.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=retry-control&lang=zh)。
<!-- catalogued-retry-control:end -->

---

## human-escalation

**决策：** 这一条必须有人来看吗？

**为什么适合：** 校准正是为这个模式而存在的。置信度与准确率相符，阈值就成了在吞吐量和错误率之间调节的一个旋钮。

**形态：** 任何一种原语都行；升级依据的是回答所附带的置信度 —— 记住 `noul` 给你的是概率，而不是置信度。

**注：** 挑选阈值是政策决定，不是建模决定。它应该放在配置里，并对照实测结果来复核。见 [`../examples/README.md`](../examples/README.md)。

<!-- catalogued-human-escalation:start -->
目录中的**人工升级**：共 69 条，[逐条列出并附警示](by-pattern/human-escalation.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=zh)。
<!-- catalogued-human-escalation:end -->

---

## model-routing

**决策：** 这个请求该交给哪个下游模型或档位处理？

**为什么适合：** 把便宜的请求从昂贵模型那里分流出去，只有当路由器本身比它省下的差价便宜得多时才划算。

**形态：** 在模型档位上做 `choice`；或者用一个衡量难度的 `score`，在代码里映射到档位 —— 后者在你的档位变化时更容易重新调整。

**何时不该用：** 当你的几个模型区别在于能力而不是成本时。在搭路由器之前，先确认便宜的那条路对简单的请求确实够用。

<!-- catalogued-model-routing:start -->
目录中的**模型路由**：共 44 条，[逐条列出并附警示](by-pattern/model-routing.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=zh)。
<!-- catalogued-model-routing:end -->

---

## fan-out

**决策：** 不是一个决策 —— 而是一次做很多个，包括那些你可能用不上的。

**为什么适合：** state 只摄入一次，每个问题都针对它并行评估，所以多问一个问题的成本大致只是它自己的 token，而不是再来一次往返。这改变了设计思路：先投机性地多问，再让代码挑出真正重要的。厂商的并行提问 cookbook 报告称，把一份简报的所有问题批量放进一次调用而不是分成多次，成本和延迟都大幅下降。

**形态：** 在一次请求里放很多个任意类型的问题，总量在 64k token 的预算之内。

**何时不该用：** 当后一个问题的措辞取决于前一个问题的答案时。那需要两次往返。

<!-- catalogued-fan-out:start -->
目录中的**并行扇出**：共 32 条，[逐条列出并附警示](by-pattern/fan-out.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=zh)。
<!-- catalogued-fan-out:end -->

---

## search-ranking

**决策：** 这些候选里哪些真正回答了查询，按什么顺序排列？

**为什么适合：** 对短名单重排序是逐对的判断，只有每一次都很便宜，才负担得起在短名单的规模上这么做。厂商的重排序 cookbook 报告称，相对 BM25 给出的短名单，top-1 和 top-10 都有显著提升。

**形态：** 每个候选一个 `score`；或者，做按行粒度的检索时，在行 ID 上做一个 `choice`。

**何时不该用：** 把它当作你整个检索栈的时候。它重排的是短名单；它不能替代针对大型语料的索引。

<!-- catalogued-search-ranking:start -->
目录中的**检索与排序**：共 64 条，[逐条列出并附警示](by-pattern/search-ranking.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=zh)。
<!-- catalogued-search-ranking:end -->

---

## data-extraction

**决策：** 哪一段文字才是那个值？

**为什么适合：** 这个模型不生成文本，所以这里的抽取意味着*选择* —— 由正则或解析器提出候选，模型挑出正确的那个，你的代码拿到的是原文照录的值，而不是改写过的。对任何你要存储或比较的东西，这都是实打实的优势。

**形态：** 在候选文本片段上做 `choice`；每个字段一个 `noul`，判断它是否存在。

**何时不该用：** 没有任何东西能先列举出候选时。另外请注意，算术和日期比较是明确列出的弱项 —— 让模型先认出各个部分，再在代码里解析和校验日期。

<!-- catalogued-data-extraction:start -->
目录中的**结构化抽取**：共 17 条，[逐条列出并附警示](by-pattern/data-extraction.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=zh)。
<!-- catalogued-data-extraction:end -->

---

## classification

**决策：** 这个条目在分类体系里属于哪里？

**为什么适合：** 一个 `choice` 最多 255 个选项，但某一层级上的 `probabilities` 让你可以用束搜索（beam search）遍历很深的层级，而答案自身的置信度让你可以退回到更粗的一层，而不是去猜一个更细的。

**形态：** 每一层一个 `choice`，与 `probabilities` 和 `confidence` 一起读。

**何时不该用：** 当你的分类体系里有互相重叠的叶子节点时。先修好分类体系。

<!-- catalogued-classification:start -->
目录中的**分类**：共 120 条，[逐条列出并附警示](by-pattern/classification.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)。
<!-- catalogued-classification:end -->

---

## feature-extraction

**决策：** 把自由文本变成传统模型可以用来训练的数字。

**为什么适合：** 一种少见而被低估的用法。概率和分数本身就是特征；下游的梯度提升模型可以直接消费它们，而模型的任何文本都不必展示给用户。

**形态：** 把 `score` 和 `noul` 的概率当作连续特征来读。

**何时不该用：** 当你有足够的标注数据，可以直接在原始文本上训练一个监督模型时。

<!-- catalogued-feature-extraction:start -->
目录中的**机器学习特征抽取**：共 8 条，[逐条列出并附警示](by-pattern/feature-extraction.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=zh)。
<!-- catalogued-feature-extraction:end -->

---

## document-triage

**决策：** 这是一份什么文档，该送到哪里？

**形态：** 用 `choice` 判定类型和去向，用 `score` 驱动基于置信度的复核队列，每项合规检查一个 `noul`。

**注：** 对发票和财务文书，把模型当作填充复核队列的分拣员，而不是审批人。审批仍归人或确定性规则。

<!-- catalogued-document-triage:start -->
目录中的**文档分拣**：共 20 条，[逐条列出并附警示](by-pattern/document-triage.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=document-triage&lang=zh)。
<!-- catalogued-document-triage:end -->

---

## support-triage

**决策：** 哪个队列、哪个优先级、哪个预设回复（macro）？

**形态：** 在同一次请求里，用 `choice` 定队列，用 `score` 定紧急度。

**注：** 厂商自己的 quickstart 用的就是这个例子，所以它是文档最齐全的起点。

<!-- catalogued-support-triage:start -->
目录中的**工单分拣**：共 8 条，[逐条列出并附警示](by-pattern/support-triage.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=zh)。
<!-- catalogued-support-triage:end -->

---

## content-scoring

**决策：** 在一个有序量表上，有多好、多危险、多相关？

**形态：** `score`。量表真正有序时用它；如果你的「量表」其实是套着数字的无序类别，就用 `choice`。

**注：** 只支持 2–10 级。带校准置信度的有序量表可以排序，这让它成为按最差优先填充复核队列的那个模式。

<!-- catalogued-content-scoring:start -->
目录中的**内容评分**：共 166 条，[逐条列出并附警示](by-pattern/content-scoring.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=zh)。
<!-- catalogued-content-scoring:end -->

---

## recommendation

**决策：** 接下来呈现什么，而且要快到不会让实时对话卡住。

**形态：** 在短名单上做 `choice`；或者对来自更便宜的检索步骤的候选做 `score`。

**何时不该用：** 把它当作你整个排序栈的时候 —— 见 `search-ranking`。

<!-- catalogued-recommendation:start -->
目录中的**实时推荐**：共 1 条，[逐条列出并附警示](by-pattern/recommendation.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=zh)。
<!-- catalogued-recommendation:end -->

---

## overview

不是一种模式。这个标签给那些介绍模型或整个领域、而不是演示某一个决策的条目 —— 发布报道、讲解文章、「Jev 是什么」之类的帖子。把它单独分开，是为了让各模式的索引保持诚实：一篇总览不是做任何事情的例子。

它也一直是那些给出模式建议的关键词规则（`scripts/classify.py`）安放无法归类的描述的地方，而几轮批量整理都采纳了规则的建议。所以，一个唯一模式是 `overview`、且其行没有记录 `patterns_reviewed` 的带代码项目或插件，算作尚未按模式索引，而不算作总览。目前有 <!--n:overview_unindexed-->252<!--/n--> 行是这样。两份 README、Overview 页面和站点都把它们单独列在这个标题下，[复核队列](review-queue.md#unsorted-overview)则连同规则的建议一起列出它们。对照上面的模式阅读其中一行，给它指定它体现的模式，或者保留 `overview`，然后把阅读的日期写入 `patterns_reviewed`。

<!-- catalogued-overview:start -->
目录中的**总览**：共 451 条，[逐条列出并附警示](by-pattern/overview.zh-CN.md) · [站点筛选](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)。
<!-- catalogued-overview:end -->

---

## 添加一个模式

一个新模式要有至少两个彼此独立的真实例子，才配拥有自己的标题。在那之前，它先归到最接近的已有模式下，因为一个带着空枝杈的分类体系，比一个粗一点的分类体系更难用。添加一个模式要改四处 —— schema 的枚举、[`../patterns.json`](../patterns.json) 里该模式的条目（它的标签、简介和在顺序中的位置）、英文页面 [`patterns.md`](patterns.md)，以及本页。两页里它的 `## key` 一节都以一对 `catalogued-<key>` 标记结尾，由 `scripts/build_docs.py` 填入条数和链接。漏了标签、某一节或标记，构建都会明确报错。见 [`../CONTRIBUTING.md`](../CONTRIBUTING.md)。
