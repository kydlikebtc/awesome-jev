<!-- Written by scripts/zh_audit.py from catalog.json. Edit those, not this file. -->

# Translation queue · 翻译队列

<sub>The Chinese on this page is model-written and has not been reviewed by a person. · 本页中文由模型撰写（机翻），未经人工审校。</sub>

Chinese summaries a model translated (`zh_machine: true`), for a person to replace with a translation of their own. 1016 of the catalogue's 1211 rows have one; 195 have a Chinese summary a person wrote. Rows more readers see come first: every machine translation on a row at ★100+, then the others at least one signal flags, most-starred band first. A signal is a text comparison a script makes between a translation and its English, not a verdict on the translation: the table below counts how often each also fires on a summary a person wrote, and a translation none of them flags can still be wrong. No README row, pattern page or site card shows the signals; they show only the `(机翻)` mark. To take some rows, see [Claim a translation](../CONTRIBUTING.md#claim-a-translation). A row leaves this page when a translation a person wrote replaces its Chinese and `zh_machine` comes off.

由模型翻译的中文摘要（`zh_machine: true`），等待有人换成自己的译文。目录 1211 行中有 1016 行是机翻，195 行的中文摘要由人撰写。看到的读者越多越靠前：先列出 ★100+ 各行的全部机翻，再按星标区间从高到低列出至少被一项信号标出的其他机翻。信号是脚本把译文与英文对照得出的文本比较，不是对译文的结论：下表列出每项信号在人写摘要上同样触发的次数，而没有被任何信号标出的译文也可能有错。README 各行、模式页面和站点卡片都不显示这些信号，只显示 `(机翻)` 标记。认领方法见[认领翻译](../CONTRIBUTING.md#claim-a-translation)。当一行的中文换成人写的译文、并去掉 `zh_machine` 后，它就会离开本页。

| Signal · 信号 | Rule · 规则 | Machine translations · 机翻 | Written by a person · 人写 |
| --- | --- | --- | --- |
| `short` | The Chinese has fewer than 30% as many characters as the English. · 中文的字符数不到英文的 30%。 | 284 of 1016 | 14 of 195 |
| `numbers` | A number the English gives does not appear in the Chinese. Digit groups are joined first, so 2 000, 2,000 and 2000 are one number; a number written out in words is not read. · 英文给出的某个数字在中文里找不到。比较前先合并数字分组，所以 2 000、2,000 与 2000 算同一个数；用文字写出的数不计。 | 91 of 1016 | 1 of 195 |
| `ascii` | More than 60% of the Chinese is ASCII (Latin letters, digits, spaces and ASCII punctuation): mostly left untranslated. · 中文摘要里超过 60% 的字符是 ASCII（拉丁字母、数字、空格与 ASCII 标点），大部分没有翻译。 | 152 of 1016 | 16 of 195 |
| any · 任一 | At least one of the three. · 三项中至少一项。 | 457 of 1016 | 31 of 195 |

<a id="most-starred"></a>

## Every machine translation at ★100+ · ★100+ 的全部机翻

98 rows, most-starred band first, then the rows more signals flag. A dash means no signal fires, not that the translation is right. · 共 98 行，按星标区间从高到低，再按命中信号的多少排列。破折号表示没有信号触发，不代表译文无误。

| Row · 行 | Stars · 星标 | Signals · 信号 |
| --- | --- | --- |
| [langchain](https://kydlikebtc.github.io/awesome-jev/?lang=en#langchain) | ★100k+ | `short` 0.25 |
| [litellm](https://kydlikebtc.github.io/awesome-jev/?lang=en#litellm) | ★10k+ | `short` 0.24 · `numbers` `100` · `ascii` 0.63 |
| [ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai) | ★10k+ | `short` 0.24 · `ascii` 0.67 |
| [openwork](https://kydlikebtc.github.io/awesome-jev/?lang=en#openwork) | ★10k+ | `short` 0.18 |
| [pydantic-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#pydantic-ai) | ★10k+ | `short` 0.27 |
| [ai-hedge-fund](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai-hedge-fund) | ★10k+ | — |
| [eliza](https://kydlikebtc.github.io/awesome-jev/?lang=en#eliza) | ★10k+ | — |
| [laya-nandhakishorm](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-nandhakishorm) | ★10k+ | — |
| [oh-my-pi](https://kydlikebtc.github.io/awesome-jev/?lang=en#oh-my-pi) | ★10k+ | — |
| [vellum-assistant](https://kydlikebtc.github.io/awesome-jev/?lang=en#vellum-assistant) | ★1k+ | `short` 0.23 · `numbers` `24` `7` |
| [ax](https://kydlikebtc.github.io/awesome-jev/?lang=en#ax) | ★1k+ | `ascii` 0.78 |
| [deep-searcher](https://kydlikebtc.github.io/awesome-jev/?lang=en#deep-searcher) | ★1k+ | `short` 0.25 |
| [latitude-llm](https://kydlikebtc.github.io/awesome-jev/?lang=en#latitude-llm) | ★1k+ | `short` 0.19 |
| [laya-mlx](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-mlx) | ★1k+ | `numbers` `3` |
| [memsearch](https://kydlikebtc.github.io/awesome-jev/?lang=en#memsearch) | ★1k+ | `short` 0.19 |
| [nimble](https://kydlikebtc.github.io/awesome-jev/?lang=en#nimble) | ★1k+ | `short` 0.29 |
| [gptcache](https://kydlikebtc.github.io/awesome-jev/?lang=en#gptcache) | ★1k+ | — |
| [reticle](https://kydlikebtc.github.io/awesome-jev/?lang=en#reticle) | ★1k+ | — |
| [agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent) | ★100+ | `short` 0.09 · `numbers` `21` |
| [openwhisper](https://kydlikebtc.github.io/awesome-jev/?lang=en#openwhisper) | ★100+ | `short` 0.16 · `numbers` `64` `3` |
| [atomic](https://kydlikebtc.github.io/awesome-jev/?lang=en#atomic) | ★100+ | `short` 0.15 |
| [celesto](https://kydlikebtc.github.io/awesome-jev/?lang=en#celesto) | ★100+ | `short` 0.23 |
| [dasheng](https://kydlikebtc.github.io/awesome-jev/?lang=en#dasheng) | ★100+ | `numbers` `2` |
| [djev](https://kydlikebtc.github.io/awesome-jev/?lang=en#djev) | ★100+ | `numbers` `57250` |
| [djev-spark](https://kydlikebtc.github.io/awesome-jev/?lang=en#djev-spark) | ★100+ | `ascii` 0.71 |
| [docjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#docjev) | ★100+ | `short` 0.26 |
| [embodied-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#embodied-jev) | ★100+ | `numbers` `5` `2` |
| [fastbrowse](https://kydlikebtc.github.io/awesome-jev/?lang=en#fastbrowse) | ★100+ | `short` 0.24 |
| [formanator](https://kydlikebtc.github.io/awesome-jev/?lang=en#formanator) | ★100+ | `short` 0.11 |
| [hippo-memory](https://kydlikebtc.github.io/awesome-jev/?lang=en#hippo-memory) | ★100+ | `short` 0.21 |
| [interlinked-cli](https://kydlikebtc.github.io/awesome-jev/?lang=en#interlinked-cli) | ★100+ | `short` 0.26 |
| [jegrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jegrep) | ★100+ | `short` 0.20 |
| [jev-cobusgreyling](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cobusgreyling) | ★100+ | `ascii` 0.61 |
| [jev-chat-windows](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-windows) | ★100+ | `numbers` `4` `3` |
| [jev-dsh-decision](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-dsh-decision) | ★100+ | `ascii` 0.66 |
| [jev-mem](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mem) | ★100+ | `ascii` 0.64 |
| [jev-voice](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-voice) | ★100+ | `ascii` 0.63 |
| [jgrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jgrep) | ★100+ | `short` 0.28 |
| [kody](https://kydlikebtc.github.io/awesome-jev/?lang=en#kody) | ★100+ | `short` 0.19 |
| [laya](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya) | ★100+ | `ascii` 0.75 |
| [laya-ultrafast](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-ultrafast) | ★100+ | `ascii` 0.72 |
| [neurolink](https://kydlikebtc.github.io/awesome-jev/?lang=en#neurolink) | ★100+ | `short` 0.19 |
| [omg-dev](https://kydlikebtc.github.io/awesome-jev/?lang=en#omg-dev) | ★100+ | `short` 0.15 |
| [orchestkit](https://kydlikebtc.github.io/awesome-jev/?lang=en#orchestkit) | ★100+ | `numbers` `9` `10` |
| [quackd](https://kydlikebtc.github.io/awesome-jev/?lang=en#quackd) | ★100+ | `short` 0.13 |
| [req-llm](https://kydlikebtc.github.io/awesome-jev/?lang=en#req-llm) | ★100+ | `ascii` 0.69 |
| [smithers](https://kydlikebtc.github.io/awesome-jev/?lang=en#smithers) | ★100+ | `short` 0.26 |
| [systemoneharness](https://kydlikebtc.github.io/awesome-jev/?lang=en#systemoneharness) | ★100+ | `ascii` 0.77 |
| [taskuary](https://kydlikebtc.github.io/awesome-jev/?lang=en#taskuary) | ★100+ | `short` 0.22 |
| [tax-doc-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#tax-doc-classifier) | ★100+ | `numbers` `100` |
| [tiptour-macos](https://kydlikebtc.github.io/awesome-jev/?lang=en#tiptour-macos) | ★100+ | `ascii` 0.62 |
| [vexjoy-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#vexjoy-agent) | ★100+ | `short` 0.21 |
| [wrongstack](https://kydlikebtc.github.io/awesome-jev/?lang=en#wrongstack) | ★100+ | `short` 0.15 |
| [332-lab-jev-chat](https://kydlikebtc.github.io/awesome-jev/?lang=en#332-lab-jev-chat) | ★100+ | — |
| [abide](https://kydlikebtc.github.io/awesome-jev/?lang=en#abide) | ★100+ | — |
| [aiavatarkit](https://kydlikebtc.github.io/awesome-jev/?lang=en#aiavatarkit) | ★100+ | — |
| [astra-ares](https://kydlikebtc.github.io/awesome-jev/?lang=en#astra-ares) | ★100+ | — |
| [classifier-dev](https://kydlikebtc.github.io/awesome-jev/?lang=en#classifier-dev) | ★100+ | — |
| [compact-adviser](https://kydlikebtc.github.io/awesome-jev/?lang=en#compact-adviser) | ★100+ | — |
| [crush-monitor](https://kydlikebtc.github.io/awesome-jev/?lang=en#crush-monitor) | ★100+ | — |
| [distill](https://kydlikebtc.github.io/awesome-jev/?lang=en#distill) | ★100+ | — |
| [jeff](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeff) | ★100+ | — |
| [jev-browser-openqa-cn](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser-openqa-cn) | ★100+ | — |
| [jev-chat-jarvis-mac](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-jarvis-mac) | ★100+ | — |
| [jev-experiments](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-experiments) | ★100+ | — |
| [jev-gateway](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-gateway) | ★100+ | — |
| [jev-lint](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-lint) | ★100+ | — |
| [jev-semgrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-semgrep) | ★100+ | — |
| [jev-seo-agricidaniel](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-seo-agricidaniel) | ★100+ | — |
| [jev-social](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-social) | ★100+ | — |
| [jev-trade](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trade) | ★100+ | — |
| [jev-use-savka777](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-use-savka777) | ★100+ | — |
| [jev-webmcp-extension](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-webmcp-extension) | ★100+ | — |
| [jev-x-sentiment-analysis](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-x-sentiment-analysis) | ★100+ | — |
| [jevbench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevbench) | ★100+ | — |
| [jevharness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevharness) | ★100+ | — |
| [jevk5](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevk5) | ★100+ | — |
| [jevmem](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmem) | ★100+ | — |
| [jevmind](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmind) | ★100+ | — |
| [jevrev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevrev) | ★100+ | — |
| [laya-vs-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-vs-jev) | ★100+ | — |
| [llm2jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#llm2jev) | ★100+ | — |
| [localjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#localjev) | ★100+ | — |
| [macbrow](https://kydlikebtc.github.io/awesome-jev/?lang=en#macbrow) | ★100+ | — |
| [open-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-jev) | ★100+ | — |
| [open-jev-zefan-cai](https://kydlikebtc.github.io/awesome-jev/?lang=en#open-jev-zefan-cai) | ★100+ | — |
| [openjev-siliconlabai](https://kydlikebtc.github.io/awesome-jev/?lang=en#openjev-siliconlabai) | ★100+ | — |
| [pi-fabric](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-fabric) | ★100+ | — |
| [rizzo-flow](https://kydlikebtc.github.io/awesome-jev/?lang=en#rizzo-flow) | ★100+ | — |
| [runline](https://kydlikebtc.github.io/awesome-jev/?lang=en#runline) | ★100+ | — |
| [shapeshift](https://kydlikebtc.github.io/awesome-jev/?lang=en#shapeshift) | ★100+ | — |
| [stanley-code](https://kydlikebtc.github.io/awesome-jev/?lang=en#stanley-code) | ★100+ | — |
| [system1-agents](https://kydlikebtc.github.io/awesome-jev/?lang=en#system1-agents) | ★100+ | — |
| [third-hand](https://kydlikebtc.github.io/awesome-jev/?lang=en#third-hand) | ★100+ | — |
| [vector-graph-rag](https://kydlikebtc.github.io/awesome-jev/?lang=en#vector-graph-rag) | ★100+ | — |
| [von](https://kydlikebtc.github.io/awesome-jev/?lang=en#von) | ★100+ | — |
| [webctl](https://kydlikebtc.github.io/awesome-jev/?lang=en#webctl) | ★100+ | — |
| [youtube-sponsor-detection](https://kydlikebtc.github.io/awesome-jev/?lang=en#youtube-sponsor-detection) | ★100+ | — |

<a id="flagged"></a>

## Other machine translations a signal flags · 被信号标出的其他机翻

410 rows below ★100+, in the same order. · 共 410 行，低于 ★100+，顺序同上。

| Row · 行 | Stars · 星标 | Signals · 信号 |
| --- | --- | --- |
| [jev-seo](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-seo) | ★10+ | `short` 0.24 · `numbers` `100` `0` · `ascii` 0.81 |
| [jev-autopilot](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-autopilot) | ★10+ | `short` 0.22 · `numbers` `0.01` |
| [jev-canvas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-canvas) | ★10+ | `short` 0.24 · `numbers` `350` |
| [jev-harness](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-harness) | ★10+ | `short` 0.21 · `numbers` `48.9` `1.3` |
| [jev-macos-loop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-macos-loop) | ★10+ | `short` 0.26 · `ascii` 0.66 |
| [jev-reviewer](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-reviewer) | ★10+ | `short` 0.13 · `numbers` `2` |
| [jev-rs](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-rs) | ★10+ | `numbers` `1` · `ascii` 0.67 |
| [laya-jev-graphrag](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-jev-graphrag) | ★10+ | `short` 0.19 · `numbers` `4` |
| [laya-jev-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-jev-lab) | ★10+ | `short` 0.18 · `numbers` `1.8` |
| [openthai-systemone](https://kydlikebtc.github.io/awesome-jev/?lang=en#openthai-systemone) | ★10+ | `numbers` `0.8` `256` `2.0` · `ascii` 0.69 |
| [pdf-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#pdf-race) | ★10+ | `numbers` `3.8` · `ascii` 0.66 |
| [poorjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#poorjev) | ★10+ | `short` 0.23 · `numbers` `0.170` `0.071` |
| [typesafe-skill-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-skill-router) | ★10+ | `short` 0.28 · `numbers` `0.001` |
| [a3m-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#a3m-router) | ★10+ | `short` 0.28 |
| [agent-chaperone](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-chaperone) | ★10+ | `short` 0.16 |
| [agent-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-router) | ★10+ | `short` 0.25 |
| [anydecisionmodel](https://kydlikebtc.github.io/awesome-jev/?lang=en#anydecisionmodel) | ★10+ | `short` 0.22 |
| [augustus](https://kydlikebtc.github.io/awesome-jev/?lang=en#augustus) | ★10+ | `short` 0.23 |
| [bluenoise](https://kydlikebtc.github.io/awesome-jev/?lang=en#bluenoise) | ★10+ | `short` 0.10 |
| [browserclaw](https://kydlikebtc.github.io/awesome-jev/?lang=en#browserclaw) | ★10+ | `ascii` 0.64 |
| [captaincore](https://kydlikebtc.github.io/awesome-jev/?lang=en#captaincore) | ★10+ | `short` 0.27 |
| [cheshi](https://kydlikebtc.github.io/awesome-jev/?lang=en#cheshi) | ★10+ | `short` 0.19 |
| [clash-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#clash-jev) | ★10+ | `short` 0.27 |
| [cultivar](https://kydlikebtc.github.io/awesome-jev/?lang=en#cultivar) | ★10+ | `short` 0.22 |
| [dejevu](https://kydlikebtc.github.io/awesome-jev/?lang=en#dejevu) | ★10+ | `short` 0.27 |
| [discern](https://kydlikebtc.github.io/awesome-jev/?lang=en#discern) | ★10+ | `short` 0.17 |
| [dsh-jev-buberlo](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-buberlo) | ★10+ | `ascii` 0.64 |
| [ego-jev-zephyrdeng](https://kydlikebtc.github.io/awesome-jev/?lang=en#ego-jev-zephyrdeng) | ★10+ | `ascii` 0.61 |
| [eutrya](https://kydlikebtc.github.io/awesome-jev/?lang=en#eutrya) | ★10+ | `short` 0.25 |
| [evoke](https://kydlikebtc.github.io/awesome-jev/?lang=en#evoke) | ★10+ | `short` 0.10 |
| [flue-jev-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#flue-jev-demo) | ★10+ | `ascii` 0.78 |
| [hunch-carldaws](https://kydlikebtc.github.io/awesome-jev/?lang=en#hunch-carldaws) | ★10+ | `ascii` 0.65 |
| [invalidate](https://kydlikebtc.github.io/awesome-jev/?lang=en#invalidate) | ★10+ | `short` 0.25 |
| [james-library](https://kydlikebtc.github.io/awesome-jev/?lang=en#james-library) | ★10+ | `short` 0.19 |
| [jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev) | ★10+ | `ascii` 0.75 |
| [jev-okooo5km](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-okooo5km) | ★10+ | `short` 0.26 |
| [jev-agent-browser](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-agent-browser) | ★10+ | `short` 0.28 |
| [jev-agent-design-with-topk-logits-choices](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-agent-design-with-topk-logits-choices) | ★10+ | `short` 0.24 |
| [jev-as-policy](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-as-policy) | ★10+ | `short` 0.17 |
| [jev-calibrate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-calibrate) | ★10+ | `short` 0.29 |
| [jev-chat-windows-deepseek-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-chat-windows-deepseek-jev) | ★10+ | `numbers` `3` |
| [jev-cli-shaharia-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-cli-shaharia-lab) | ★10+ | `short` 0.22 |
| [jev-code](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-code) | ★10+ | `short` 0.12 |
| [jev-column-race](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-column-race) | ★10+ | `numbers` `3.8` |
| [jev-desktop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-desktop) | ★10+ | `ascii` 0.69 |
| [jev-docs-zh](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-docs-zh) | ★10+ | `short` 0.14 |
| [jev-doom-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-doom-agent) | ★10+ | `short` 0.21 |
| [jev-for-chrome](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-for-chrome) | ★10+ | `short` 0.20 |
| [jev-forge](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-forge) | ★10+ | `short` 0.09 |
| [jev-foundation-models](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-foundation-models) | ★10+ | `ascii` 0.75 |
| [jev-guard](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-guard) | ★10+ | `short` 0.18 |
| [jev-judge-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-judge-mcp) | ★10+ | `ascii` 0.69 |
| [jev-mail-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mail-classifier) | ★10+ | `short` 0.29 |
| [jev-mcp-burnigtm](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-burnigtm) | ★10+ | `ascii` 0.67 |
| [jev-pref](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-pref) | ★10+ | `ascii` 0.62 |
| [jev-recruiter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-recruiter) | ★10+ | `short` 0.21 |
| [jev-skill-suggester](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-suggester) | ★10+ | `short` 0.21 |
| [jev-spring-boot-starter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-spring-boot-starter) | ★10+ | `ascii` 0.85 |
| [jev-superpowers](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-superpowers) | ★10+ | `short` 0.24 |
| [jev-test-filter](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-test-filter) | ★10+ | `short` 0.27 |
| [jev-trades](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trades) | ★10+ | `short` 0.19 |
| [jev-trip](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trip) | ★10+ | `short` 0.20 |
| [jev4k](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev4k) | ★10+ | `ascii` 0.73 |
| [jev-stock](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-stock) | ★10+ | `short` 0.20 |
| [jevals](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevals) | ★10+ | `short` 0.28 |
| [jevalyn](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevalyn) | ★10+ | `ascii` 0.70 |
| [jevflow](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevflow) | ★10+ | `short` 0.10 |
| [jevgpt](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgpt) | ★10+ | `short` 0.27 |
| [jeview](https://kydlikebtc.github.io/awesome-jev/?lang=en#jeview) | ★10+ | `short` 0.26 |
| [jevloop](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevloop) | ★10+ | `short` 0.24 |
| [jevmory](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevmory) | ★10+ | `short` 0.24 |
| [jevql](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevql) | ★10+ | `ascii` 0.66 |
| [jevtown](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevtown) | ★10+ | `numbers` `10000` |
| [jevwire](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevwire) | ★10+ | `ascii` 0.61 |
| [jevyoumean](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevyoumean) | ★10+ | `short` 0.25 |
| [laya-browser-agent](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-browser-agent) | ★10+ | `short` 0.18 |
| [laya-vs-jev-arena](https://kydlikebtc.github.io/awesome-jev/?lang=en#laya-vs-jev-arena) | ★10+ | `short` 0.20 |
| [local-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#local-jev) | ★10+ | `short` 0.28 |
| [midscene-jev-runner](https://kydlikebtc.github.io/awesome-jev/?lang=en#midscene-jev-runner) | ★10+ | `ascii` 0.64 |
| [omnijev](https://kydlikebtc.github.io/awesome-jev/?lang=en#omnijev) | ★10+ | `numbers` `60` |
| [openjev-gpt-agi](https://kydlikebtc.github.io/awesome-jev/?lang=en#openjev-gpt-agi) | ★10+ | `ascii` 0.74 |
| [pg-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#pg-typesafe) | ★10+ | `ascii` 0.64 |
| [pi-heed](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-heed) | ★10+ | `short` 0.29 |
| [pi-jev-auto-mode](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-jev-auto-mode) | ★10+ | `short` 0.24 |
| [pi-jev-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#pi-jev-router) | ★10+ | `ascii` 0.68 |
| [public-browser](https://kydlikebtc.github.io/awesome-jev/?lang=en#public-browser) | ★10+ | `numbers` `30` `25` `41` `34` `40` `11` |
| [robojev](https://kydlikebtc.github.io/awesome-jev/?lang=en#robojev) | ★10+ | `ascii` 0.73 |
| [sift](https://kydlikebtc.github.io/awesome-jev/?lang=en#sift) | ★10+ | `short` 0.28 |
| [slop-grader](https://kydlikebtc.github.io/awesome-jev/?lang=en#slop-grader) | ★10+ | `short` 0.25 |
| [snap](https://kydlikebtc.github.io/awesome-jev/?lang=en#snap) | ★10+ | `short` 0.28 |
| [swift-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#swift-typesafe) | ★10+ | `ascii` 0.72 |
| [sys1](https://kydlikebtc.github.io/awesome-jev/?lang=en#sys1) | ★10+ | `ascii` 0.61 |
| [system-one-iamaamir](https://kydlikebtc.github.io/awesome-jev/?lang=en#system-one-iamaamir) | ★10+ | `ascii` 0.64 |
| [trade-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#trade-jev) | ★10+ | `numbers` `10` |
| [typed-decision-bert](https://kydlikebtc.github.io/awesome-jev/?lang=en#typed-decision-bert) | ★10+ | `short` 0.20 |
| [typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe) | ★10+ | `ascii` 0.91 |
| [typesafe-playground](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-playground) | ★10+ | `short` 0.28 |
| [typesafe-sdk-go](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-sdk-go) | ★10+ | `short` 0.27 |
| [typesafeai-dotnet-sdk](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafeai-dotnet-sdk) | ★10+ | `short` 0.25 |
| [warrenduffer](https://kydlikebtc.github.io/awesome-jev/?lang=en#warrenduffer) | ★10+ | `short` 0.24 |
| [jev-skills-wanlanglin](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skills-wanlanglin) |  | `short` 0.22 · `numbers` `256` `0.0005` `0.72` `360` `5` `4995` · `ascii` 0.83 |
| [agi-jev-containment](https://kydlikebtc.github.io/awesome-jev/?lang=en#agi-jev-containment) |  | `short` 0.11 · `numbers` `1` `5` `4` `2026` |
| [aside-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#aside-jev) |  | `short` 0.28 · `ascii` 0.68 |
| [ask-jev-ai](https://kydlikebtc.github.io/awesome-jev/?lang=en#ask-jev-ai) |  | `short` 0.10 · `numbers` `100` |
| [browser-use-olympics](https://kydlikebtc.github.io/awesome-jev/?lang=en#browser-use-olympics) |  | `short` 0.15 · `numbers` `200` |
| [dsh-jev-verify](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-verify) |  | `short` 0.23 · `ascii` 0.63 |
| [ego-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ego-jev) |  | `short` 0.17 · `numbers` `2` |
| [financialpredictionjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#financialpredictionjev) |  | `short` 0.15 · `numbers` `2026` |
| [gg-friggin-ez](https://kydlikebtc.github.io/awesome-jev/?lang=en#gg-friggin-ez) |  | `short` 0.08 · `numbers` `1` `50` `500` |
| [github-issue-classification-using-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#github-issue-classification-using-jev) |  | `short` 0.08 · `ascii` 0.74 |
| [instruct-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#instruct-jev) |  | `numbers` `119` · `ascii` 0.78 |
| [jev-anotacao-sentencas](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-anotacao-sentencas) |  | `short` 0.23 · `numbers` `3.8` `5.6` |
| [jev-as-quant](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-as-quant) |  | `short` 0.18 · `numbers` `2` |
| [jev-browser-control](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-browser-control) |  | `short` 0.16 · `numbers` `0.5` |
| [jev-bun1](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-bun1) |  | `numbers` `1` · `ascii` 0.64 |
| [jev-certify](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-certify) |  | `short` 0.11 · `numbers` `2412` `150` `0.23` |
| [jev-engineering](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-engineering) |  | `short` 0.23 · `numbers` `300` |
| [jev-enterprise-decision-fabric](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-enterprise-decision-fabric) |  | `short` 0.12 · `numbers` `111` |
| [jev-evaluation](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-evaluation) |  | `short` 0.16 · `numbers` `123805` `12.69` |
| [jev-flash-router](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-flash-router) |  | `short` 0.13 · `ascii` 0.83 |
| [jev-gate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-gate) |  | `short` 0.20 · `numbers` `3` `4` |
| [jev-labs](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-labs) |  | `short` 0.15 · `numbers` `1680` |
| [jev-mcp-server](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mcp-server) |  | `short` 0.16 · `numbers` `0.5` `0.001` |
| [jev-measured](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-measured) |  | `short` 0.25 · `numbers` `8` |
| [jev-mode](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-mode) |  | `short` 0.14 · `numbers` `600` `78` `16` `96.1` `93.7` |
| [jev-no-enem](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-no-enem) |  | `short` 0.22 · `ascii` 0.63 |
| [jev-ood-calibration](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-ood-calibration) |  | `short` 0.12 · `numbers` `3` |
| [jev-orderby-bench](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-orderby-bench) |  | `short` 0.18 · `numbers` `360` |
| [jev-organize](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-organize) |  | `short` 0.13 · `numbers` `17` `1000` |
| [jev-resume-disqualifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-resume-disqualifier) |  | `short` 0.07 · `numbers` `80` |
| [jev-skill-gate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-skill-gate) |  | `short` 0.24 · `numbers` `12750` `3185` `217` `0.0009` |
| [jev-trace-classifier](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-trace-classifier) |  | `short` 0.17 · `numbers` `3.8` |
| [jevaluate](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevaluate) |  | `short` 0.12 · `numbers` `5.1` |
| [jevgrep](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevgrep) |  | `short` 0.20 · `numbers` `0.004` `1000` |
| [jevshield](https://kydlikebtc.github.io/awesome-jev/?lang=en#jevshield) |  | `short` 0.07 · `numbers` `1` |
| [jit-context](https://kydlikebtc.github.io/awesome-jev/?lang=en#jit-context) |  | `short` 0.27 · `numbers` `0` `3` `10` `10.5281` `22649542` |
| [lcc](https://kydlikebtc.github.io/awesome-jev/?lang=en#lcc) |  | `short` 0.16 · `numbers` `1` |
| [search-function-test](https://kydlikebtc.github.io/awesome-jev/?lang=en#search-function-test) |  | `short` 0.10 · `numbers` `100` |
| [shade-arena-jev-monitor](https://kydlikebtc.github.io/awesome-jev/?lang=en#shade-arena-jev-monitor) |  | `short` 0.20 · `numbers` `2.5` |
| [siege](https://kydlikebtc.github.io/awesome-jev/?lang=en#siege) |  | `short` 0.16 · `numbers` `2026` |
| [system-one-chess](https://kydlikebtc.github.io/awesome-jev/?lang=en#system-one-chess) |  | `short` 0.25 · `ascii` 0.66 |
| [system-one-gemma](https://kydlikebtc.github.io/awesome-jev/?lang=en#system-one-gemma) |  | `short` 0.24 · `ascii` 0.66 |
| [tempo-jev-demo](https://kydlikebtc.github.io/awesome-jev/?lang=en#tempo-jev-demo) |  | `short` 0.20 · `numbers` `5.6` `3.8` |
| [typesafe-ai-jev-example](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-ai-jev-example) |  | `short` 0.13 · `numbers` `1.13.0` |
| [typesafe-go](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-go) |  | `short` 0.27 · `ascii` 0.64 |
| [typesafe-jev-bridge](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-jev-bridge) |  | `short` 0.13 · `numbers` `9` |
| [typesafe-sdk-go-valksor](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-sdk-go-valksor) |  | `numbers` `1` · `ascii` 0.78 |
| [typesafe-sdk-php-valksor](https://kydlikebtc.github.io/awesome-jev/?lang=en#typesafe-sdk-php-valksor) |  | `numbers` `1` · `ascii` 0.79 |
| [zerosweep](https://kydlikebtc.github.io/awesome-jev/?lang=en#zerosweep) |  | `short` 0.21 · `numbers` `0` |
| [actiongate-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#actiongate-jev) |  | `short` 0.17 |
| [agent-fastpath](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-fastpath) |  | `short` 0.10 |
| [agent-handoff-gate](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-handoff-gate) |  | `short` 0.17 |
| [agent-jev-tetris](https://kydlikebtc.github.io/awesome-jev/?lang=en#agent-jev-tetris) |  | `short` 0.27 |
| [ai-provider-for-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#ai-provider-for-jev) |  | `short` 0.27 |
| [antigravity-mcp-semantic-search-with-typesafeai](https://kydlikebtc.github.io/awesome-jev/?lang=en#antigravity-mcp-semantic-search-with-typesafeai) |  | `short` 0.22 |
| [askjev](https://kydlikebtc.github.io/awesome-jev/?lang=en#askjev) |  | `ascii` 0.75 |
| [askjev-mcp](https://kydlikebtc.github.io/awesome-jev/?lang=en#askjev-mcp) |  | `ascii` 0.73 |
| [assay-001](https://kydlikebtc.github.io/awesome-jev/?lang=en#assay-001) |  | `short` 0.25 |
| [auto-mode-for-paseo](https://kydlikebtc.github.io/awesome-jev/?lang=en#auto-mode-for-paseo) |  | `ascii` 0.72 |
| [bes-kelime-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#bes-kelime-jev) |  | `short` 0.25 |
| [cairn-jev-lab](https://kydlikebtc.github.io/awesome-jev/?lang=en#cairn-jev-lab) |  | `short` 0.21 |
| [casse-brique-typesafe](https://kydlikebtc.github.io/awesome-jev/?lang=en#casse-brique-typesafe) |  | `short` 0.26 |
| [chat2jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#chat2jev) |  | `ascii` 0.77 |
| [check-risk](https://kydlikebtc.github.io/awesome-jev/?lang=en#check-risk) |  | `short` 0.28 |
| [claude-jev-plugin](https://kydlikebtc.github.io/awesome-jev/?lang=en#claude-jev-plugin) |  | `ascii` 0.72 |
| [computer-use-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#computer-use-jev) |  | `ascii` 0.78 |
| [cyber-breach-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#cyber-breach-jev) |  | `short` 0.16 |
| [daf-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#daf-jev) |  | `short` 0.16 |
| [dbt-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#dbt-jev) |  | `ascii` 0.65 |
| [decido](https://kydlikebtc.github.io/awesome-jev/?lang=en#decido) |  | `ascii` 0.63 |
| [decision-circuits](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-circuits) |  | `short` 0.24 |
| [decision-first](https://kydlikebtc.github.io/awesome-jev/?lang=en#decision-first) |  | `short` 0.29 |
| [deepseek-harness-jev-pre-compaction](https://kydlikebtc.github.io/awesome-jev/?lang=en#deepseek-harness-jev-pre-compaction) |  | `short` 0.12 |
| [diffjury](https://kydlikebtc.github.io/awesome-jev/?lang=en#diffjury) |  | `short` 0.27 |
| [diffusion-jev-sglang](https://kydlikebtc.github.io/awesome-jev/?lang=en#diffusion-jev-sglang) |  | `ascii` 0.63 |
| [discoprint](https://kydlikebtc.github.io/awesome-jev/?lang=en#discoprint) |  | `short` 0.27 |
| [draftpulse](https://kydlikebtc.github.io/awesome-jev/?lang=en#draftpulse) |  | `short` 0.26 |
| [dsh-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev) |  | `ascii` 0.69 |
| [dsh-jev-zhangxaochen](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-zhangxaochen) |  | `ascii` 0.69 |
| [dsh-jev-decide](https://kydlikebtc.github.io/awesome-jev/?lang=en#dsh-jev-decide) |  | `short` 0.10 |
| [duckdb-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#duckdb-jev) |  | `short` 0.23 |
| [ego-jev-ultrafast](https://kydlikebtc.github.io/awesome-jev/?lang=en#ego-jev-ultrafast) |  | `short` 0.17 |
| [emoji-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#emoji-jev) |  | `short` 0.21 |
| [everything-about-jev](https://kydlikebtc.github.io/awesome-jev/?lang=en#everything-about-jev) |  | `short` 0.27 |
| [extremely-specific-council](https://kydlikebtc.github.io/awesome-jev/?lang=en#extremely-specific-council) |  | `short` 0.20 |
| [fast-compaction-dsh](https://kydlikebtc.github.io/awesome-jev/?lang=en#fast-compaction-dsh) |  | `short` 0.19 |
| [footwork](https://kydlikebtc.github.io/awesome-jev/?lang=en#footwork) |  | `short` 0.24 |
| [frost](https://kydlikebtc.github.io/awesome-jev/?lang=en#frost) |  | `short` 0.26 |
| [functions](https://kydlikebtc.github.io/awesome-jev/?lang=en#functions) |  | `ascii` 0.69 |
| [hearth-jev-rental-search](https://kydlikebtc.github.io/awesome-jev/?lang=en#hearth-jev-rental-search) |  | `short` 0.29 |
| [hermes-jev-plugin](https://kydlikebtc.github.io/awesome-jev/?lang=en#hermes-jev-plugin) |  | `ascii` 0.76 |
| [himalaya-jev-mail-classify](https://kydlikebtc.github.io/awesome-jev/?lang=en#himalaya-jev-mail-classify) |  | `short` 0.27 |
| [hunch-js](https://kydlikebtc.github.io/awesome-jev/?lang=en#hunch-js) |  | `ascii` 0.72 |
| [jev-anilsenay](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-anilsenay) |  | `ascii` 0.74 |
| [jev-kataras](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-kataras) |  | `ascii` 0.80 |
| [jev-2048](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-2048) |  | `short` 0.19 |
| [jev-acp](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-acp) |  | `ascii` 0.67 |
| [jev-agent-failure-benchmark](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-agent-failure-benchmark) |  | `short` 0.28 |
| [jev-agent-skill](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-agent-skill) |  | `short` 0.22 |
| [jev-android](https://kydlikebtc.github.io/awesome-jev/?lang=en#jev-android) |  | `ascii` 0.64 |

…and 210 more, in the same order; `python3 scripts/zh_audit.py --json` lists every machine translation. · 另有 210 行未列出，顺序相同；`python3 scripts/zh_audit.py --json` 会列出全部机翻。
