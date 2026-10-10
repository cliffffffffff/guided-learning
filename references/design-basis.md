# 设计来源与证据边界

## 设计来源

参考用户提供的《【AI未来青年说】当AI代替人类承担“思考的阵痛”，它在如何重塑人类认知架构？》，作者 Renx，发布于“启元洞见”，归档标注发布时间为 2026-08-19。

[原文链接](https://mp.weixin.qq.com/s/7_ET-5fNRlcJKxtB4tkYBg)

借鉴其认知预设、学习摩擦、创作留白和耐受适度思考困难的设计动机。本 skill 聚焦陌生领域的知识学习：保留一次独立尝试，通过有条件的推理和新情境应用校准理解。不要把文章所有建议强制施加于每类任务。

将“先补背景和例子，再留一个问题让用户尝试”作为本 skill 的默认交互约定。将提示、解释及退出条件作为可调整的教学选择，不宣称这套完整流程已被研究验证。

## 阅读研究时保留的边界

| 原始研究 | 能支持的内容 | 不能据此推断 |
|---|---|---|
| Benge & Scullin, 2025, A meta-analysis of technology use and cognitive aging | 常规数字技术使用与中老年群体较低认知障碍发生指标相关。研究综合横断面与纵向观察数据。 | 使用工具必然造成认知保护；相同效应适用于青年或生成式 AI。 |
| Lee 等, CHI 2025, The Impact of Generative AI on Critical Thinking | 知识工作者自述的 AI 信任、任务自信与批判性思考投入之间存在关联。 | 已通过客观前后测证明 AI 导致能力退化；自信就是客观专业水平。 |
| Shaw & Nave, Thinking—Fast, Slow, and Artificial，所核对版本为 v20260111 预印本 | 特定推理任务中可观察到错误 AI 建议的采纳和自信变化；正确建议也能改善当次表现。 | 所有用户都放弃原本正确的判断；单次任务表现能证明长期能力衰退或脑结构变化。 |

核对来源：

- [Benge & Scullin 原研究摘要](https://pubmed.ncbi.nlm.nih.gov/40229575/)
- [Lee 等原论文，Microsoft Research 官方 PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf)
- [Shaw & Nave 预印本条目](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646)
- [Shaw & Nave 作者上传全文](https://www.researchgate.net/publication/399711077_Thinking-Fast_Slow_and_Artificial_How_AI_is_Reshaping_Human_Reasoning_and_the_Rise_of_Cognitive_Surrender)

这些研究不构成本 skill 能改善长期认知或记忆的效果证明。涉及数字时重新查阅原研究，核对样本、分母、指标、百分比与百分点；不要复用参考文章中的百分比表述。用当次的解释、纠错和迁移表现评价学习进展，不把“神经肌肉”“用进废退”等类比当作实测脑变化。
