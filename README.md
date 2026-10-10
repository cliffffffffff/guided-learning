# Guided Learning · 启发式学习

一个帮助你理解陌生专业知识的 Agent Skill：先补必要背景和具体例子，再留一个问题让你尝试，随后解释、纠错，并在有价值时换个情境检验理解。

An Agent Skill for learning unfamiliar concepts through brief context, concrete examples, one reasoning question, and adaptive feedback. It follows the learner's language and switches to a complete explanation whenever requested.

[Skill 指令](SKILL.md) · [教学示例](references/teaching-examples.md) · [设计来源](references/design-basis.md) · [MIT License](LICENSE)

## 它如何帮助你 / How it helps

默认节奏：**背景与例子 → 一个问题与独立尝试 → 反馈与解释 → 必要时迁移**。

- **初次接触一个领域**：先解释必要术语，给出能想象的例子，再提出一个有依据可推理的问题。
- **已经有自己的判断**：直接检验你的依据与推理。
- **完全不知道或卡住了**：补充背景、示范完整思路；同一学习点默认最多追加一次提示后的尝试。
- **需要直接答案或实际交付物**：立即满足请求，可以随时退出提问模式。

适合希望理解概念、原理、机制和判断条件的学习请求。只查事实、赶时间或需要完成工作时，不强制进入教学流程。

## 安装到 Codex / Install in Codex

此 skill 仅包含指令、示例与图标，无需安装运行依赖或填写 API 密钥。使用 Git 将仓库放入个人 skills 目录即可。

### Windows（PowerShell）

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
git clone https://github.com/cliffffffffff/guided-learning.git (Join-Path $skillRoot 'guided-learning')
```

### macOS / Linux

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/cliffffffffff/guided-learning.git ~/.agents/skills/guided-learning
```

也可以在 Codex 中让内置安装器处理：

```text
用 $skill-installer 安装 https://github.com/cliffffffffff/guided-learning
仓库根目录里的 skill，名称为 guided-learning。
```

安装后用 `$guided-learning` 显式调用，也可由 Codex 根据你的学习请求自动选择。若新安装的 skill 未出现，重启 Codex。安装目录与发现方式见 [OpenAI 官方 skills 文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用示例 / Try it

```text
用 $guided-learning 带我理解：为什么输电要提高电压？
我是新手，先给必要背景和例子，再提出一个问题让我尝试。
```

```text
用 $guided-learning 带我理解数据库索引。我写过 SQL，但不清楚索引为何能加快查询。
```

```text
Use $guided-learning to help me understand HTTP caching.
I'm new to it. Give me a concrete example, then one question to reason through.
```

随时可以说“我完全不知道，先示范”或“我赶时间，直接讲完，不用提问”。

## 仓库内容 / Files

```text
guided-learning/
├── SKILL.md                         核心指令与触发范围
├── agents/openai.yaml               界面元数据与调用策略
├── assets/icon.svg                  图标
├── references/
│   ├── teaching-examples.md          讲解、纠错和模式切换示例
│   └── design-basis.md               设计来源与研究证据边界
├── README.md
└── LICENSE
```

## 设计依据与贡献 / Design and contributions

这是可调整的教学流程；没有实证证明此 skill 能改善长期记忆或认知能力。相关来源及各项研究能支持的结论见 [设计来源与证据边界](references/design-basis.md)。

欢迎通过 [Issues](https://github.com/cliffffffffff/guided-learning/issues) 反馈具体学习情境，也欢迎提交 PR 改进指令和示例。请说明原有行为、期望行为与具体例子，并保留用户随时获得直接答案的选择。

The instructions and examples are written in Chinese; the skill asks the agent to use the learner's language. Share concrete learning scenarios in Issues or PRs. This is an instructional design, with no claim of proven long-term cognitive or memory benefits.

## 许可证 / License

[MIT](LICENSE) — Copyright (c) 2026 cliffffffffff. 外部链接所指文章和论文仍适用各自的版权与使用条款。
