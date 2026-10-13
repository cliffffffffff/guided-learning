# Guided Learning · 安装与兼容性

用背景与具体情境搭桥，通过一次推理或用自己的话讲回发现理解缺口，再解释、修补，并按需换个情境检验应用。随时可以说“我完全不知道，先示范”或“直接讲完，不用提问”。

[核心指令](SKILL.md) · [教学示例](references/teaching-examples.md) · [设计来源](references/design-basis.md) · [MIT 许可证](LICENSE) · [GitHub 图文介绍](https://github.com/cliffffffffff/guided-learning) · [SkillHub](https://skillhub.cn/skills/user_2d01d3cb/guided-learning)

## 通用格式与依赖

- 核心为标准 `SKILL.md`：YAML 中保留通用字段 `name`、`description`、`license` 与字符串形式的 `metadata`；完整触发范围与教学流程在正文中。
- 将目录命名为 `guided-learning`，并保留 `references/` 与 `SKILL.md` 的相对位置。参考文件由宿主的文件或技能资源接口按需读取。
- `agents/openai.yaml` 与 `assets/icon.svg` 为可选的 OpenAI 界面资源；其他 agent 无需解释这些元数据，也无需安装 OpenAI 工具。
- 技能本身无需 Python、Git、MCP 或 API 密钥。下文的 Git 命令是下载方式，发布脚本的 Python 是维护者工具；宿主模型服务与计费仍由所用 agent 决定。
- 基础讲解可在离线、纯文本环境运行。实时事实和拿不准的专业资料仍需查证；没有检索能力时会说明未核验，保留未知。单次或后台任务没有互动入口时，给完整示范，不模拟学习者作答。

## Codex

将技能放入个人目录 `~/.agents/skills/guided-learning/`。

Windows（PowerShell）：

```powershell
$skillRoot = Join-Path $env:USERPROFILE '.agents/skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
git clone https://github.com/cliffffffffff/guided-learning.git (Join-Path $skillRoot 'guided-learning')
```

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/cliffffffffff/guided-learning.git ~/.agents/skills/guided-learning
```

也可以在 Codex 中发送：

```text
用 $skill-installer 安装 https://github.com/cliffffffffff/guided-learning
仓库根目录里的 skill，名称为 guided-learning。
```

如果下载的是 ZIP，将内容解压到上述 `guided-learning` 目录，确保 `guided-learning/SKILL.md` 直接存在。已有安装时先保留本地自定义内容；Git clone 仅适用于目标目录尚不存在的情况。

使用 `$guided-learning` 显式调用，或让 Codex 根据学习请求选择。新安装或更新后未出现时，重启 Codex。目录与调用方式依据 [OpenAI 官方文档](https://learn.chatgpt.com/docs/build-skills)。

## WorkBuddy

在 WorkBuddy 打开“技能 → 添加技能 → 上传技能”，选择本地 ZIP。导入后在“已安装”中确认技能已启用，再发送：

```text
请使用 guided-learning（启发式学习）带我理解数据库索引。
我写过 SQL，但不清楚索引为何能加快查询。
```

也可以从 [SkillHub 技能页](https://skillhub.cn/skills/user_2d01d3cb/guided-learning)下载 ZIP，或使用页面提供的“安装到本地 Agent”WorkBuddy 入口。入口与文件格式以当前页面和产品提示为准，不要求 WorkBuddy 识别 Codex 的 `$guided-learning`。

WorkBuddy 的导入与启用方式依据 [官方技能说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)，自然语言使用方式见 [官方自定义技能案例](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)。CodeBuddy IDE / CLI 与 WorkBuddy 的安装入口不同，不要直接套用 `.codebuddy/skills/` 路径。

## Hermes

将 ZIP 解压为当前 Hermes 配置使用的 `skills/guided-learning/` 目录，或从 GitHub 下载完整仓库。该目录位于当前 Hermes 数据目录下；命名 profile、`HERMES_HOME` 和 Windows 安装方式可能改变它，先通过当前配置或 skills 管理界面确认路径。

macOS / Linux 默认数据目录的 Git 安装示例（目标目录尚不存在时）：

```bash
mkdir -p ~/.hermes/skills
git clone https://github.com/cliffffffffff/guided-learning.git ~/.hermes/skills/guided-learning
```

如果已经维护共享目录，例如 Codex 的 `~/.agents/skills/`，可在当前 Hermes `config.yaml` 中将其加入既有 `skills.external_dirs` 列表，保留其他设置：

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
```

Hermes 可修改有写权限的外部技能；希望各工具独立维护时，使用各自的副本。同名技能按宿主优先级处理，旧的本地副本可能遮蔽外部目录中的更新。

安装后在当前配置中确认技能可见：

```bash
hermes skills list
```

在对话中调用：

```text
/guided-learning 带我理解数据库索引。我是新手，先给背景和例子。
```

若运行中的会话未更新技能命令，使用当前版本提供的刷新入口，例如 `/reload-skills`，或开启新会话。也可使用当前版本的 Skills Hub / GitHub 安装器，具体标识符依据 [Hermes 官方技能文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)。不要把腾讯 SkillHub 的页面标识符直接当成 Hermes 自带 Skills Hub 的标识符。

## SkillHub

本技能页面为 [@user_2d01d3cb/guided-learning](https://skillhub.cn/skills/user_2d01d3cb/guided-learning)。页面提供的安装提示是：

```text
请根据 https://skillhub.cn/install/skillhub.md，安装 @user_2d01d3cb/guided-learning。
```

需要支持安装操作的 agent 才能执行此提示。只希望手动导入时，直接下载页面上的 ZIP。SkillHub 是分发渠道，最终的技能目录、启用和调用方式由接收它的 agent 决定。

仓库更新与 SkillHub 已上传版本分别维护。维护者在仓库根目录运行 `python scripts/package_skill.py` 生成 `dist/guided-learning.zip`，然后在 SkillHub 发布对应版本。脚本不随 ZIP 分发；再次打包时使用新路径，例如 `python scripts/package_skill.py --output dist/guided-learning-1.1.0.zip`，保留既有文件。上传时保留原技能标识符，并让平台版本与 `SKILL.md` 中的 `metadata.version` 一致；生成 ZIP 本身不会更新平台。

发布包根目录包含 `SKILL.md`、两份 `references/`、`LICENSE`、可选的 `agents/openai.yaml` 与图标，以及由本说明生成的 `README.md`。完整介绍图通过 GitHub 查看，教学运行无需下载这些图片。

## 其他 Agent 与纯聊天工具

支持 [Agent Skills 标准](https://agentskills.io/specification)的 agent 可将同一目录放入其官方技能目录或使用导入界面，再通过技能选择器、宿主命令或自然语言调用；不统一规定所有产品的隐藏目录和命令语法。

不支持技能加载时，将 `SKILL.md` 的 Markdown 正文作为本次会话指令提供，再发送学习请求。这只对当前会话有效，不等于已经安装；需要示例或来源时，再附相应参考文件。

## 检查是否可用

1. 技能管理界面或列表能找到 `guided-learning`，且处于启用状态；目录安装时确认没有多套一层文件夹。
2. 发送“请使用 guided-learning 带我理解机会成本。我是新手，先给背景和例子，再留一个问题。”应先得到背景和案例，当轮只留一个核心问题。
3. 接着说“我完全不知道，先示范。”应得到完整思路；说“直接讲完，不用提问。”应立即切换到完整解释。
4. 需要参考内容时，确认宿主能按技能根目录读取 `references/`；没有读取能力时，核心流程仍可运行，但不能声称已看过参考文件。

格式校验与文件完整性检查能验证包的可移植结构；不同 agent、版本及模型是否正确选择并遵循流程，需在实际对话中检查，不能由格式通过推断。
