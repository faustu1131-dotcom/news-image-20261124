# GPT 版式规范 — 新闻图最终版渲染依据

来源：ChatGPT GPT-6.2（最高思考档）"Infographic layout specification"，2026-11-25。
用途：用确定性渲染（Pillow）按此规范绘制最终图。文字绝不用 AI 生图生成。

## 设计概念
高级国际报纸头版：一个主导性地缘政治头条 + 六条结构清晰的次要新闻。优先编辑可信度、事实精确、视觉层级和可读性，而非装饰复杂度。

## 画布与整体构成
- 尺寸 1024 × 1024 px，1:1，sRGB，现代国际报纸风格，单栏编辑网格
- 外边距 48 px，内容宽 928 px，共 7 条新闻，左对齐，PNG 无损导出
- 单栏优于双栏卡片：缩略图尺寸下字体可以更大、摘要可以不断行

## 网格坐标（左上角为原点，单位 px）
- Header：X 48，Y 32，W 928，H 106
- 01 伊朗/霍尔木兹：X 48，Y 148，W 928，H 188
- 02 华为：X 48，Y 348，W 928，H 100
- 03 塞内加尔：X 48，Y 452，W 928，H 100
- 04 卡塔赫纳：X 48，Y 556，W 928，H 100
- 05 孟加拉：X 48，Y 660，W 928，H 100
- 06 赛诺菲/Insmed：X 48，Y 764，W 928，H 100
- 07 Euclid：X 48，Y 868，W 928，H 100
- 头条约占新闻区块面积 24%，其余六条各约 12.7%，六条之间视觉重要性相等

## 页眉
- Day：TUESDAY；Title：World News — 24 November 2026
- Day：Inter Bold 28 px；Title：Inter Display Bold 50 px
- Day 基线 X 48，Y 54；Title 基线 X 48，Y 113；Day 字距 +2 px；Title 字距 0
- 底线：X 48，Y 135，928 × 3 px
- 日期必须是主标题的一部分，不是次要元数据

## 文案（逐字使用，每条标题和摘要各占一行）
- 01 / TOP STORY / MIDDLE EAST
  - 标题（52 px）："Iran says 4 oil tankers hit mines"
  - 摘要（32 px）："Tankers caught fire in the Strait of Hormuz, Iran says."
  - 视觉权重 2.0×
- 02 / LAW
  - 标题（36 px）："US jury convicts Huawei"
  - 摘要（32 px）："Guilty on 10 of 12 counts; acquitted on racketeering."
- 03 / SPORT
  - 标题（36 px）："CAS restores Senegal's title"
  - 摘要（32 px）："Senegal reinstated as Africa Cup of Nations champions."
- 04 / SECURITY
  - 标题（36 px）："25 hostages in Cartagena"
  - 摘要（32 px）："Gunman takes hostages at a supermarket."
- 05 / LABOUR
  - 标题（36 px）："Bangladesh garment workers protest"
  - 摘要（32 px）："Workers demand higher pay and clash with police."
- 06 / BUSINESS
  - 标题（36 px）："Sanofi to buy Insmed for $40bn"
  - 摘要（32 px）："Sanofi to acquire US biotech Insmed."
- 07 / SCIENCE
  - 标题（36 px）："Euclid finds most distant quasar"
  - 摘要（32 px）："630 million years after the Big Bang; redshift 8.13."

## 头条位置（均为基线坐标）
- 分类标签：X 72，Y 193，27 px
- 标题：X 72，Y 254，52 px
- 摘要：X 72，Y 305，32 px
- 实心午夜 navy 背景，左缘 6 px  muted-gold 竖线

## 次要新闻位置（Y 为该区块顶边）
- 竖线：X 48，Y；标题：X 68，Y+43；分类标签：X 956，Y+38（右对齐）；摘要：X 68，Y+82；底部分隔线：X 48，Y+100
- 标题与摘要左对齐；竖线 4 × 92 px；分隔线 928 × 2 px

## 配色
- 报纸象牙白（画布背景）：#F5F2EB
- 午夜 navy（主文字与头条背景）：#172631
- 石板灰（次要摘要）：#40505B
- 编辑铜色（分类标签与次要竖线）：#91602D
-  muted gold（头条标签与竖线）：#D5AC70
- 纯白（头条标题）：#FFFFFF
- 柔白（头条摘要）：#E9EDF0
- 暖灰（分隔线）：#D0CCC3
- 禁用渐变、饱和警示色、阴影、金属质感、装饰边框

## 字体系统（全程 Inter）
- 主标题：Inter Display 50 px，700
- Day：Inter 28 px，700
- 头条标题：Inter Display 52 px，700
- 头条摘要：Inter 32 px，500
- 头条分类：Inter 27 px，700
- 次要标题：Inter 36 px，700
- 次要摘要：Inter 32 px，500
- 次要分类：Inter 24 px，700
- 启用字距与抗锯齿，禁用自动换行，使用真实字体文件，禁止自动截断或省略号
- 最长次要摘要按 32 px Inter Medium 约 853 px，在 888 px 文本区内放得下

## 间距
- 左右边距 48 px；顶边距 32 px；底边距 56 px
- 页眉到头条 10 px；头条到次要 12 px
- 头条文字左右内边距 24 px；次要文字左右内边距 20 px
- 次要区块间距 4 px；次要标题到摘要基线距离 39 px
- 标题到分类最小水平间距 16 px

## 300 px 可读性（缩放系数约 29.3%）
- 头条标题 52 → 15.2 px；主标题 50 → 14.6 px；次要标题 36 → 10.5 px；摘要 32 → 9.4 px；Day 28 → 8.2 px；次要分类 24 → 7.0 px
- 最小的分类标签在 300 px 下读着会吃力，但其中没有标题和摘要里没有的关键事实

## 渲染验收清单（10 项，全部必须通过）
1. 画布恰好 1024 × 1024 px
2. TUESDAY 和 24 November 2026 可见
3. 七条新闻齐全
4. 伊朗的说法明确归属于伊朗
5. 七条标题与摘要各占一行
6. 所有数字事实与提供的新闻一致
7. 无文字重叠、截断、缺字
8. 无编造的照片、旗帜、引言、统计
9. 字体为确定性渲染，非图像模型生成
10. 导出 PNG 在 1024 px 和 300 px 下都检查过

## 美术指导
- 用确定性 SVG、HTML Canvas、Pillow 或同等排版渲染器出最终图，绝不依赖生成式 AI 渲染字体
- 以字体为主的版式，不用摄影插图：为事实信息留出空间，减少编造视觉细节的风险；代价是少一些图画叙事，换来更强的可读性与编辑准确性
- 核心原则：可识别的事件、准确的信息、清晰的编辑层级，优先于视觉奇观
