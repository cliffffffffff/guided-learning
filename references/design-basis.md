# 设计来源与证据边界

## 设计来源

参考用户提供的《【AI未来青年说】当AI代替人类承担“思考的阵痛”，它在如何重塑人类认知架构？》，作者 Renx，发布于“启元洞见”，归档标注发布时间为 2026-08-19。

[原文链接](https://mp.weixin.qq.com/s/7_ET-5fNRlcJKxtB4tkYBg)

借鉴其认知预设、学习摩擦、创作留白和耐受适度思考困难的设计动机。本 skill 聚焦陌生领域的知识学习：保留一次独立尝试，通过有条件的推理和新情境应用校准理解。不要把文章所有建议强制施加于每类任务。

当前交互约定是“背景或示范 → 一次有诊断价值的尝试 → 定位缺口与修补 → 按意愿检验应用”。这些环节根据基础、已有回答与用户意愿调整，不宣称这套完整流程已被研究验证。

## 寓言与费曼式讲回

### 寓言作为机制的具体载体

上游叙事参考为“数字生命卡兹克”发布的[《分享一个很实用的寓言故事prompt，5分钟帮你理解任何新概念。》](https://mp.weixin.qq.com/s/L1ISA0FvxY_7OR994RttWw)，文章文末署名为卡兹克、tashi。文中的寓言写作 Prompt 是用户提供的 `fable-writing` 技能的参考来源。

来源关系：**原文的寓言写作 Prompt → `fable-writing` 技能封装 → 本 skill 的教学改编**。技能文件标注作者 Hermes Agent、版本 v1.0.0、许可证 MIT；这是封装文件的元数据，原文仍适用其自身的版权与使用条款。

本仓库保留 [fable-writing 参考原文件](fable-writing/SKILL.md)，按需借鉴叙事写法，保留其原有元数据与正文。它是参考资料，不单独注册为本 skill 的运行依赖；其中的固定输出格式与两道检验问题不覆盖本 skill 的教学节奏。

借鉴的做法是围绕指定概念，让角色的选择、相互影响及后果具体呈现机制，再解释故事与概念的对应关系，并分别检验理解和迁移。文章对快速理解、记住概念的描述属于作者经验与推荐，不作为本 skill 学习效果的实证证据。原文和 `fable-writing` 都不是本 skill 的安装依赖。

本 skill 按教学需要采用短寓言或具体案例。没有移植其意象黑名单、固定篇幅、隐去概念名称的要求，以及同轮输出正文、解析和两道问题的格式。决定性条件、必要事实、一次尝试的空间和用户随时获得解释的选择优先。

### 区分费曼本人表述与流行四步法

费曼在 1966 年演讲《What is Science?》中区分知道名称与知道事物如何发生，并提出用自己的语言重述所学，检验是否只是记住定义。演讲也展示了用观察检验猜测、无法解释时承认不知道的做法。[费曼演讲原文转录](https://feynman.com/science/what-is-science/)

Kansas State University 的学习资源将费曼学习法整理为学习、教给别人、修补缺口、简化四步。本 skill 借鉴这种整理；本次未核实完整四步程序由费曼本人以此形式发布，不将其写成费曼原话，也不要求每轮机械走完。[大学学习指南](https://www.k-state.edu/aac/success-tools/collection/Feynman_Technique.pdf)

“讲给不熟悉的人听”用于暴露遗漏的因果关系和条件，不要求幼儿化表达、角色扮演或删除必要术语。AI 解释得通俗只显示讲解方式；用户自己的解释才能提供当次理解的证据。即使用户讲回流畅，是否能迁移仍需另行观察。

### 相关学习研究的适用边界

| 原始研究 | 能支持的内容 | 不能据此推断 |
|---|---|---|
| Bisra 等，2018，Inducing Self-Explanation: a Meta-Analysis | 自我解释涉及生成因果联系或概念关系；元分析支持提示自我解释具有学习价值。 | 把术语换成简单词就等于理解；本 skill 的完整流程、寓言或多轮 AI 对话已获同样效果验证。 |
| Pan & Rickard，2018，Transfer of test-enhanced learning: Meta-analytic review and synthesis | 检索练习能在一些条件下促进迁移，其效果受任务及练习方式等因素影响。 | 一次正确讲回必然迁移到任何领域；当前可见聊天中的讲回自动等同实验里的检索练习。 |
| Karpicke & Blunt，2011，Retrieval practice produces more learning than elaborative studying with concept mapping | 该研究的科学文本学习任务中，检索与重建所学对理解和推断题有学习收益。 | 要求新手猜未学内容就是检索练习；本 skill 必然优于普通 AI 问答或其他教学方式。 |

核对来源：

- [Bisra 等原研究摘要](https://link.springer.com/article/10.1007/s10648-018-9434-x)
- [Pan & Rickard 原研究全文](https://pdf.retrievalpractice.org/transfer/Pan_Rickard_2018.pdf)
- [Karpicke & Blunt 原研究摘要](https://pubmed.ncbi.nlm.nih.gov/21252317/)

因此反馈优先定位一处会改变判断的机制或条件缺口，必要时修补后再解释；解释、修补后的表现与新情境应用分开记录。此安排是教学设计选择，不是上述研究对本 skill 的直接验证。

### 示范、帮助与检验各自承担什么

[美国教育科学研究院的学习实践指南](https://ies.ed.gov/ncee/wwc/PracticeGuide/1)分别建议交替使用完整示例与自主解题、连接具体和抽象表征、主动检索及深层解释问题。指南针对相应教学场景的建议，不是对本 skill 或 AI 导师的效果认证。

本 skill 据此采用的设计选择是：缺少前提时先展示可理解的解题过程；已有把握时撤去方法提示；用户要求检验时给一处真正改变判断的条件，并等待其依据。提示后的正确回答用于看修补进展，不冒充未提示时的应用能力。返场检验先尝试再反馈，不先重讲答案；没有返场数据就不判断保留效果。

是否优于普通 AI 问答，还需比较学习者的结果。导师是否少泄题、能针对误解修补，可以通过行为测试观察；学习者是否更能独立判断、隔天保留或迁移，需要相同学习材料、相近投入时间及不提示方法的后测。固定的模拟学习者脚本不能证明这些效果。

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
