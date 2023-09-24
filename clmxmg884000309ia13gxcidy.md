---
title: "英语渣无痛阅读英文材料的 3 种方法"
seoDescription: "AI 牛逼，这才两个月啊！"
datePublished: Sun Sep 24 2023 15:35:49 GMT+0000 (Coordinated Universal Time)
cuid: clmxmg884000309ia13gxcidy
slug: 20230924233520
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1695569400570/dff29182-4760-4c34-9dbe-49686736e20f.jpeg

---

距离《[100 个订阅也不乱，如何打造一站式信息中心](https://mp.weixin.qq.com/s?__biz=MzI3MzU5MDA1OQ==&mid=2247487924&idx=1&sn=9a95f510ab113194c52669d1ebba2d63&chksm=eb21a3f0dc562ae6ef1ea79c0dff46863e60729c5f22cbee53295522d6c2a2cbc96575c24320#rd)》写完都快两个月了，我的「下篇」还没写出来，哈哈。动笔之前，我又看了一遍这篇文章，这两个月，很多流程又有了新变化，所以做个增补，然后再写下篇，聊我怎么管理输出的。

主要是「英文播客」这一节，新增了 3 种英文资料阅读方法：

1. TTS 英译中
    
2. Claude 辅助阅读
    
3. 微信读书英转中
    

### TTS 英译中

之前的听英文播客的做法是「借助沉浸式翻译，导出英文播客字幕文件（如果没有字幕，需要使用 Whisper 或者飞书妙记之类的工具先语音转文字），上传到翻译插件双语对照阅读。」但是读始终不如听方便，那些没那么严肃需要一字一句读的播客，为什么不能英转中也「听懂」播客呢？于是研究一下流程，发现虽然麻烦点，但是能跑通。

1. 下载（或[转录](https://www.feishu.cn/product/minutes)）播客字幕文件
    
2. 使用[沉浸式翻译插件](https://immersivetranslate.com/)英转中
    
3. 清洗数据，如去掉时间戳和人声标记
    
4. 使用 [TTSMaker](https://ttsmaker.com/) 免费额朗读
    
5. 用 [Audio Joiner](https://audio-joiner.com/cn/) 把分段语音合并
    

里面有很多细节可以调整，比如不在乎人声机器感强的，可以用 [Balabolka](https://www.52pojie.cn/thread-1830109-1-1.html) 之类的朗读器，不限字符数，就不存在合并 MP3 的步骤了。实测转录一期 Tim Ferriss 的播客，大概要 15 分钟左右。如果能实现自动化，点一下播放键自动中文朗读，甚至分人声的话，就还挺酷的。

后来我加入 [Memo AI](https://memo.ac/) 的测试群，发现他们已经在做这个功能了，牛逼，可以期待一下。

### Claude 辅助阅读

之前看过一些朋友分享用 AI 辅助阅读的方法，我一直觉得阅读不能被替代，所以没尝试。但是今天准备听 Tim Ferriss 播客的时候，觉得一句一句看太费劲了。就想着「不那么重要的内容」能不能让 Claude 辅助，帮我总结，给些列表然后以 QA 的形式带我读。效果还不错，准备再试试。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1695569563952/f19bda53-ef00-402f-8807-86b7f2d47763.jpeg align="center")

后来我又想到，如果是 YouTube 视频的话，还可以借用 [Reccap](https://reccap.it/signup?invite=hz2bsp) 速读，全文文字识别+分段小标题，阅读体验更好。不过现在超过 2 小时的视频要付费了，5 美元/月。

### 微信读书英转中

播客和文章翻译都还好说，文本量不大，但读英文书有点儿麻烦。虽然沉浸式翻译插件也可以做双语电子书，但是排版时常出错，太简陋了，读不下去。这下好了，微信读书 7.4.1 版本上线了「本地导入英文书翻译成中文」的功能，体验很棒，速度快，排版也行，直接把「风声雨声」之类的付费翻译服务干掉了。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1695569612935/0ac758a0-f8a8-44e0-b47d-d25684f71d12.png align="center")

接下来想读英文书，你只需要在 Z-Library 上下载英文电子书，然后同步到微信读书，打开后，等待微信全文翻译完成，美滋滋。

其他文字流程没啥变化，但是数据处理方面，我开始引入 GPT-4 的 Advanced Data Analysis 功能帮忙。它可以说是高级版 Excel 快速填充（Crtl+E），就是那种「只要会一个快捷键，整个 Excel 都明亮了的功能」。往后你只要导入数据，「说出」你的问题，GPT-4 都能完成（如下图就是 GPT-4 做的）。而且原来费时费力，没啥技术含量的数据清洗它也能做，比如数据按顺序重排、时间戳格式化等等，简直小天使。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1695569628149/e04c0d0c-b9d7-4b39-91b3-9057a57a9eab.png align="center")

AI 牛逼，这才两个月啊！

🔗

《[让 AI 帮我做周报](https://mp.weixin.qq.com/s?__biz=MzI3MzU5MDA1OQ==&mid=2247488073&idx=1&sn=6c18d1f9bd799622d32447e1c9f40083&chksm=eb21a00ddc56291b5a2ee43c4b0ca59c756ef29fe06e7677236cd4bd32eb0993f080b41dac31#rd)》

《[AI 来了，什么技能最值得我们学？](https://mp.weixin.qq.com/s?__biz=MzI3MzU5MDA1OQ==&mid=2247487648&idx=1&sn=d86ff126d81bdd53d299a6c7eeb92ec1&chksm=eb21a2e4dc562bf2c71eb5e8f7eb0fa3ef77186a5b4e182d6b51554cd4e41aa5f226400776dc#rd)》