---
title: "不写一行代码，用 AI 做 Python 小工具"
seoDescription: "原来需要你懂英文、懂技术、懂设计……现在只要你会、能用 AI。用白话描述需求，AI 就能帮你做出东西来。AI 渗透进我的生活。"
datePublished: Wed Jun 04 2025 12:34:37 GMT+0000 (Coordinated Universal Time)
cuid: cmbhxjhn2001909ic1t8414lm
slug: 20250604143419
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1749018774371/13db9660-e8c6-426a-9b13-1ba158a30e4b.png

---

这一个多星期的空闲时间，我都在和 Grok 聊需求，讲逻辑，复制粘贴运行 Python 代码。我让 Grok 帮我写一个优化 [Telegram 频道](https://mp.weixin.qq.com/s/u9sg3KBe9k3L3oOUZcRd5w)导出 HTML 文件的小工具——自动合并文件，去掉影响阅读的多余元素，可选隐藏媒体和标签，统计超链接和转发博主等等。

简单说，就是把导出的 HTML 文件从这样：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749018789731/0dd00789-dba1-49db-b48b-fde81e2abfa5.png align="center")

变成了这样：

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749018802339/2803d337-0797-4b01-94fc-ed5d49f8c31a.png align="center")

这个小工具的代码初稿，Grok 花 3 天就写到能用了。后面 7 天，都是我在抠细节。没有编程经验，最花时间的地方，就是等 AI 生成完整代码的过程。因为我不知道新代码改的片段在哪里，复制粘贴又经常弄错，干脆输出完整代码。后期对话上下文太多，每次生成 800 行代码就要花 3 到 5 分钟。好不容易等到生成完毕，粘贴到 PyCharm 运行，又报错。等我把提示复制给 Grok，它说是幻觉，不知道怎么混进去一句中文，我会疯。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749018815778/06272268-a66c-4f05-aac4-77531fec2ea7.png align="center")

再就是对话一多，Chrome 网页占用内存就超 2G，很卡。官方网页也会在我上传超过 25 个附件之后，提示我附件太多，Grok 会忘记前文，建议我最好开个新对话。我没听，结果最后想保存聊天记录需要一直往上刷新，翻到浏览器卡死也翻不完，啥导出[插件](https://chromewebstore.google.com/detail/grok-%E8%81%8A%E5%A4%A9%E5%AF%BC%E5%87%BA%E5%99%A8/jnnlkkaidhngedlkogmbhodjlegcdggb?hl=zh-CN&utm_source=ext_sidebar)也不行，漏掉了很多思路和线索。

期间还出现过一次聊天记录没实时保存情况。按理说聊完就有历史记录自动保存在网页的，但有一次我嫌太卡刷新网页换节点之后，最新的十几条记录都没了。而我又没保存最新的版本代码，撤回也被覆盖了，导致我只能重新写需求做功能。修修补补大几个小时就没了。这些，下次都要注意。

代码完成后，我[问 Grok](https://mp.weixin.qq.com/s/pfETlm9E01NoqBnumr6mJg) 有哪些因为我的个人能力不足而导致代码进度缓慢的地方。我只让它说不足，但它还是先说了我的优点，然后才开始说不足，这情商 🤣

不足之处节选：

* 你在提交问题时，未**提供完整的测试用例或运行结果**，导致我需要基于假设进行分析。你可能缺乏系统化的调试经验，无法快速定位问题根源。建议学习基本的调试技巧（如使用 print 或 Python 的 pdb 模块跟踪变量），并在提出问题时提供更多上下文（如日志或错误输出），这能显著提高问题解决效率。
    
* 代码目前是一个长而连续的脚本，缺乏函数或模块划分。你可能对 Python 的模块化编程（如定义函数或类）不够熟练，导致难以拆分代码或复用逻辑。建议学习 Python 函数和模块的基本知识，将代码拆分为独立功能，这将提高代码可维护性和可扩展性。
    

所以后来遇到具体问题的时候，我都打开 F12 审查元素，把出问题的内容块的整段代码复制发给它。然后再说问题具体在哪个类（Class），让它自查逻辑，告诉我原因并修正。一旦出现幻觉，我都会在问题最后加一句「请使用你的 Token 上限，仔细检查错误成因，并给出修正方案。注意，修正方案只解决当前我说的问题，不要产生幻觉额外添加代码影响代码的其他功能。」

有时候，更关键的问题，是我不知道能怎么实现我想要的功能。比如代码里有个鼠标悬停显示图片的功能，一开始我只想到隐藏图片后留一句提示，可以点击提示打开图片链接。后来我把 Grok 的代码发给 Gemini 让它帮我检查，给我些改进建议，它说可以用鼠标悬停展示图片，直接帮我写好代码。所以后来遇到问题，我都会加一句「你有什么想法，有什么更好的实现我想要的效果的方式吗？」AI 的方案比我想得更细致。我想，和优秀的人相处是不是也应该这样？说需求和目的，不定死实现的细节。

再就是合作过程中，观察不同 AI 的风格。我主用免费的 Grok 3，不用高级功能的情况下，每 2 小时能问 20 次。生成代码加学习调试，很少超过限额，超了我刚好遛娃等免费额度刷新。Grok 的回答对新手友好，不吝啬 Token，步骤详尽。除非 Grok 一直解决不了，或者开始频繁出现幻觉，我会复制源代码到 Gemini 2.5 Pro 或 Claude 3.7 让它们帮我检查。Gemini 的特色是灵动、有自己的想法，常常超额完成工作，且输出飞快（Token 如流水，一次代码输出约 ¥1.5）。我提过一嘴优化代码功能模块，跑代码的时候经常会发现一些小惊喜，比如帮我加上了提示词，帮我改了更好的显示模式等等。让我自己问 Grok，需要十几个问题才能改好。Gemini 一次搞定。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749018828664/49e36585-47e6-4acc-a7a0-6df4a741ccc2.png align="center")

接下来，我还要和 AI 学怎么把代码上传到 GitHub 开源，怎么版本控制。你看，不需要从枯燥的书本开始，换成由兴趣和实际项目驱动，把代码跑起来，哪里不会点哪里。

AI 大幅扩展个人的[能力边界](https://superhuang.feishu.cn/wiki/CBBPwvgEuicVhFkx0s7cPmhpn4e)。原来需要你懂英文、懂技术、懂设计……现在只要你会、能用 AI。用白话描述需求，AI 就能帮你做出东西来。比如，原来我需要自己浏览知识星球，现在可以用八爪鱼抓星球的数据，然后喂给 AI 帮我[分类总结](https://mp.weixin.qq.com/s/Mm5JMTfgT3SKrQ5z8pWmmw)生成一句话描述的精华集；原来我要去 TradingView 社区找免费脚本，现在直接让 DeepSeek 帮我[定制](https://weibo.com/5262225303/PbaV43jiz)一个；原来哀叹 iOS 捷径好用但不会用，现在让 AI 手把手教我设置，写个[定时播客](https://weibo.com/5262225303/P8jnBcy3I)和打开 APP 自动计时的捷径不在话下；原来觉得 Telegram 输出的 HTML 太丑，现在用 Grok + Gemini 写 Python 帮我重排版……原来因为不会不懂、怕麻烦怕丢人，问不出口的问题，现在豆包随时待命。AI 渗透进我的生活。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1749018833302/6e4e10d7-ba32-43ea-97b5-de01882d2f7f.jpeg align="center")

现在 AI 爆发的情景就像，你想象有朝一日，等我有钱了，我就去做这个实现那个。现在美梦成真，钱管够，放手去做吧。你还会做吗？觉得还值得做吗？还敢实现愿望吗？

不是钱的问题，也不是 AI 问题。

---

延伸阅读：

* 《[AI 来了，什么技能最值得学](https://mp.weixin.qq.com/s/ifldCMLTSb1Ir-qcyoa5rw?poc_token=HHqgP2ijNlu9itvafU7F3MfAin21ZtY2hMLGKdny)》
    
* 《[AI 给我的 3 条赚钱建议](https://mp.weixin.qq.com/s/pfETlm9E01NoqBnumr6mJg)》
    

💳 支持我并订阅我的[动态和读书笔记](https://mp.weixin.qq.com/s/u9sg3KBe9k3L3oOUZcRd5w)，请购买我的 Telegram 频道，现价 599 元，我会用这份收入采集更多内容，用创作反哺。

📖 最近一个月我都在写 30 岁[自传](https://mp.weixin.qq.com/s?__biz=MzI3MzU5MDA1OQ==&mid=2247488741&idx=1&sn=3aca11b2f15bcb82156b45c8a69ae937&chksm=eb21a6a1dc562fb7bbf6242bc1a68995eba7b560a49627ac031e129b33aa29a624896186a2a3#rd)，预计 10 万字。复制链接打开向我[提问](https://wj.qq.com/s2/15897499/4fe9/)，或者点文章最左下角`阅读原文`，我会优先为你写。