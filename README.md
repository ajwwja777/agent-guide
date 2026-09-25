# Jiaan 工作框架

框架根：`/data/LFT-W02_data/jiaan/jiaan/`。新对话先读本文件，确定项目，再按本次任务读取对应文档。

GitHub：[ajwwja777/agent-guide](https://github.com/ajwwja777/agent-guide)（公开，origin 已关联；默认分支 `main`）。

## 机器职责

| 机器 | 职责 | 工作区 |
|---|---|---|
| MateBook | Codex 对话入口，指向 A6000 对应项目目录 | `D:\Code\jiaan_workspace` |
| A6000 | 主工作区、代码仓库、共享文档与编排 | `/data/LFT-W02_data/jiaan/jiaan/` |
| HPC | 模型训练 | `/data/user/jhe724/jiaan/`（现有项目在 `research-workspace/` 下） |
| Cobot 4090 | 模型部署、真机实验与操作网页 | `/media/agilex/Getea1/jiaan/` |

## 框架结构

```text
jiaan/
├── agent-guide/
│   ├── README.md           # 总览与对话工作流程
│   ├── AGENTS.md           # 对话入口
│   ├── SKILL.md            # 可复用的技能入口
│   ├── projects/           # 各项目摘要与任务进展
│   └── pipelines/
│       ├── project/        # 项目启动与维护，按主题拆分
│       │   ├── README.md   # 项目启动顺序与导航
│       │   └── GIT.md      # Git、GitHub 与仓库地址
│       ├── DATA.md         # 数采
│       ├── TRAINING.md     # 训练
│       └── DEPLOYMENT.md   # 部署
├── projects/               # 实际项目工作区与独立仓库
└── scratch/                # 临时文件
```

## 目录约定

在 A6000 新框架根下，`projects/<项目名>/` 保存实际项目，`agent-guide/projects/<项目名>/` 保存接管摘要，`scratch/<项目名>/` 保存临时文件。`<项目名>` 是占位符；新建前检查是否已存在。

其他机器的具体项目、数据和输出子目录由项目文档记录；上表 HPC、Cobot 路径来自已有登记，使用前核对。

## 一个项目对话如何开始

1. 明确用户指定的项目和本次目标，查看[项目索引](projects/README.md)。已有项目读取其摘要和相关任务记录；索引中没有时先确认实际项目是否已存在。
2. 新建或迁入项目时，按[项目启动流程](pipelines/project/README.md)依次确定工作目录、初始化文档、选择 Git 方式并建立仓库关系；已有项目从当前步骤继续。
3. 结合当前任务读取相关论文、代码或配置，了解项目已有结果和下一步。
4. 按需读[数采](pipelines/DATA.md)、[训练](pipelines/TRAINING.md)或[部署](pipelines/DEPLOYMENT.md)，执行用户要求的部分；无需每次从头走完整条流程。
5. 有进展后更新实际项目记录，并同步指南中的项目摘要：结果、下一步、来源和日期。新项目同时加入索引，方便下个对话接管。

## 如何维护

具体项目参数、路径和进展放在项目文档中；通用流程放在对应 pipeline。项目启动与维护的新主题按需加入 `pipelines/project/`，并在[项目流程总览](pipelines/project/README.md)增加入口。

任意对话均可更新，无需指定管理对话审批。新增或修改 MD 中的流程时，先向用户展示拟写内容、涉及文件及简要原因，供用户学习和审核；用户确认后再写入，完成后列出实际修改文件与要点。用户已明确批准的具体内容可直接落实。

新旧对话恢复工作时重新读取相关文档；具体任务的执行范围和是否逐步确认仍按当前对话要求。

框架维护对话在 `agent-guide/` 开启。技能复用时携带整个目录，迁移环境后更新框架位置与机器职责；当前尚未安装到技能发现目录。
