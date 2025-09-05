---
title: "极简比特币策略的 107 周持仓体验丨k 线盲测"
seoDescription: "收益率、盈亏比都只是最终你平仓那一瞬间的结果，可是持仓体验，是你拿住仓位无时无刻都要忍耐、等待的煎熬过程。收益再好，如果和你的性子不合，你拿不住，都是虚的。"
datePublished: Fri Sep 05 2025 06:52:59 GMT+0000 (Coordinated Universal Time)
cuid: cmf6hacza000k02ld1moz9m1a
slug: 20250905145213
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1757054840168/7198c1c2-dd3c-4bec-abef-0f19559091f8.jpeg

---

不凑巧，上期视频我们分享了[比特币周 EMA10 策略](https://mp.weixin.qq.com/s/80Z1_c4v-rmdAcavAzbUyw)后，这周一收盘就跌破了 EMA10，如果执行这套策略的话，已经到了清仓点。

所以有读者邮件向我确认，是不是要清仓了。我说，如果你没用过这个策略，不建议马上照搬，优先执行自己原有的系统。因为时间不够，你还没仔细研究过，不可能有信心，做起来容易虎头蛇尾。你现在想清仓，大概率是找了个策略背锅而已。是你想要清仓了。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757054923970/ab930a77-d25b-422a-8541-18d92a167910.png align="center")

我的经验是不要背叛自己的研究成果。我在这上面吃过太多亏了，经常到了策略开平仓位，却不执行，有时候因为害怕，有时候因为固执，有时候是被其他看起来更优秀的策略吸引。这就是我为什么说策略的收益率，并不是最重要的指标，最重要的是交易的心态，敢执行策略，下单不纠结。怎么才能不纠结，胸有成竹，先见而不惑。预见过最好和最坏的情况，自然就不慌了。

还有读者邮件里问我觉得某某大 V 的策略怎么样。我说，不管任何人的任何策略，都需要你亲自做回测，用 K 线验证理论对不对。策略再好，也要适合你才行。比如有的策略盈亏比高，但胜率低，心高气傲、受不了出错的人就做不了这种策略。我们在执行策略的过程中，在每一个明知道该做但没做的瞬间，一步步靠近自己，发现自己的性格适合什么样的策略。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757054916177/680257f6-e9bb-4a73-ad24-63c819d832d4.png align="center")

你可能觉得，心态和情绪问题我用量化交易解决不就行了？问题是你对程序的信心有多少，能多到让它操作你的大仓位账户吗？如果不能下重注，只是玩玩，意义也不大。

好，这是上期视频发出来读者来信的题外话。我们回到周 EMA10 策略，买卖点位和交易日志我们做过了，这次带大家走一遍盲测流程，讨论一下开单的细节和持仓中的心态变化。

先复述一遍周 EMA10 策略的规则：**当比特币周收盘价连续 20K 在 EMA10 下运行直到收上 EMA10，或者收盘价在 EMA10 上出现近 20K 新高，则全仓做多。周收盘价跌破 EMA10 清仓。**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757055021250/e1598506-50e2-4241-a9a6-f0d1c0a9caf3.png align="center")

我们打开币安`BTC/USDT`交易对周线图表,这是我们上一期做的交易记录买卖点位标记。有读者好奇为什么策略用 EMA 不用 MA 呢？只是我的偏好，随你喜欢，选参数之前自己像这样肉眼观察一遍就行。简单说 EMA 和 MA 的区别就在 EMA 测算均线时间越近权重越高，越能影响均线的方向，更敏感。现在开启 TradingView 的 K 线回放功能，模拟真实的盲测环境。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757054931115/249d6779-ecbd-4cce-8c81-ba62b796ed9f.jpeg align="center")

（文字描述不清楚，这里我做了 [17 分钟的 YouTube 视频](https://youtu.be/tnla184OEi4)讲解 🎞️）

我们用 700 多天，107 根周 K 线，走完了比特币一轮牛熊。后面还有 300 多根，碍于时长，暂时不继续了。在这 700 多天的过程中，人性的拷问和情绪波动，在牛熊转换中反复出现。这就是为什么利弗莫尔说「投机像山岳一样古老。」因为人性不变。

同时，我们边测边问的记录了周 EMA10 策略的 5 个问题。这 5 个问题，你有解决方案了吗？有没有你一票否决的策略缺陷。比如 700 天就一买一卖？忍不住，接受不了低频的方案。这些问题只有你亲自盲测，跳进 K 线，才知道你最关心的什么问题。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757055043746/3814cfe0-3435-4d02-9519-4191aabddd59.png align="center")

下一期，我会就这 5 个问题给出我的答案，丰富这套周 EMA10 策略的实战细节和底层哲学。如果你厌倦了复杂和神神叨叨的交易方式，记得去 YouTube 给视频点赞关注，我们下个视频见 👋

---

延伸阅读：

* 《[K 线里的人生：2600 小时的焦虑狂喜和迷茫](https://mp.weixin.qq.com/s/t3SMla9eEJjB9j2tCJooTg?payreadticket=HF3E73WCYRmCcUqqimItfgD3FMBlXq2a1ss8ho19wvucgV12g_LvLodVmwpFOadMM5mmi5w)》
    
* 《[2 个数字 1 条线，获得比特币 20.5 倍收益](https://mp.weixin.qq.com/s/80Z1_c4v-rmdAcavAzbUyw)》
    

💳 支持我并订阅我的[动态和读书笔记](https://mp.weixin.qq.com/s/u9sg3KBe9k3L3oOUZcRd5w)，请[购买](http://atimelogger.mikecrm.com/0SSigrh)我的 Telegram 频道，现价 699 元，我会用这份收入采集更多内容，用创作反哺。

📖 最近我在 YouTube 做交易视频，分享我在用且适合大部分普通人的比特币极简交易策略。如果你有兴趣可以私聊我加内测群。