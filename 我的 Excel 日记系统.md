---
title: "我的 Excel 日记系统"
seoDescription: "AI 大爆发后，ExcelHome、StackOverflow 这些工具性强的网站，都沦为 AI 的养料了。会不会有一天，人也只是饲料，那我们到底在喂养什么呢。"
datePublished: Fri May 23 2025 14:33:45 GMT+0000 (Coordinated Universal Time)
cuid: cmb0wigq1000409jf33l8ffgj
slug: 20250523223326
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1748010730029/f3045bbf-781d-40b5-8b2a-b31253a705b4.jpeg

---

从 2014 年开始，我就用 Excel 写日记，共计 2 万多条，22 万字。我每 2 年切分一次，以 .txt 的文件形式上传到 Google NotebookLM，让它分析我这些年做了什么，有什么潜在的行为模式和性格特征。效果，emm……

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748010746110/82110467-1231-4dac-bb7c-96f88a3c1826.png)

虽然现在 AI 处理的效果一般，有很多幻觉，输出内容也经常错漏，但只要有原始数据，等风来就行。Excel 作为承载器，胜在稳定。一些简单的需求，也能用 VBA 实现。

比如我的 Excel 日记本有 4 个按钮：

* 去年今日
    
* 往年今日
    
* 随机日记
    
* 清除数据
    

功能如标题，快速跳转到对应日期，主要起回顾的作用。点一下`去年今日`就筛选出所有去年今天我写的日记；点一下`往年今日`就筛选出历年所有今天我写的日记；点一下`随机日记`就从所有日记中随机挑 10 条日记显示。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748010761116/e28bb572-9c90-4105-90d1-674f9ed283a6.png)

第一版本的想法是 2017 年我用 Excel 录制宏做的，只能筛选，鸡肋。2019 年的我做时间记录模板的时候，顺便去 ExcelHome 论坛[发帖](https://club.excelhome.net/thread-1455731-1-1.html)求助，有位热心的大佬 @ivccav 帮我写了 VBA，小修小补后开箱即用，完美解决了我的需求，一直沿用到今天。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748010792655/23fe11d7-1084-4a88-a115-1252b3c3a42e.gif)

今天晚上心血来潮，口述需求让 Grok 帮我写个`随机日记`的功能，5 分钟不到搞定。哎呀，想到 AI 大爆发后，ExcelHome、StackOverflow 这些工具性强的网站，都沦为 AI 的养料了。会不会有一天，人也只是饲料，那我们到底在喂养什么呢。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748010782643/c227cf48-6b17-4230-98f7-12b00909bacb.png)

---

延伸阅读：

* 《[怎么积累写作素材](https://mp.weixin.qq.com/s/FFM219ozjvjRhUe88jfZgw)》
    
* 《[怎样用成功日记找到内心热爱](https://mp.weixin.qq.com/s/VQykFb6Dxb-VjsEhuzXatw)》
    

💳 支持我并订阅我的[动态和读书笔记](https://mp.weixin.qq.com/s/u9sg3KBe9k3L3oOUZcRd5w)，请购买我的 Telegram 频道，现价 599 元，我会用这份收入采集更多内容，用创作反哺。

📖 最近一个月我都在写 30 岁[自传](https://mp.weixin.qq.com/s?__biz=MzI3MzU5MDA1OQ==&mid=2247488741&idx=1&sn=3aca11b2f15bcb82156b45c8a69ae937&chksm=eb21a6a1dc562fb7bbf6242bc1a68995eba7b560a49627ac031e129b33aa29a624896186a2a3#rd)，预计 10 万字。复制链接打开向我[提问](https://wj.qq.com/s2/15897499/4fe9/)，或者点文章最左下角`阅读原文`，我会优先为你写。