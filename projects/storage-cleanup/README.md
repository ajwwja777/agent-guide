# 各机器空间清理

项目：`storage-cleanup`。来源：2026-09-26 项目对话中确认的框架、机器分工及首次 push 授权。

- A6000 主项目：`/data/LFT-W02_data/jiaan/jiaan/projects/storage-cleanup/`。
- 正式机器记录：`/data/LFT-W02_data/jiaan/jiaan/projects/storage-cleanup/reports/project-state.md`；公开 README 仅保留通用说明。
- 笔记本对话及执行副本：`D:\Code\jiaan_workspace\storage-cleanup\`。
- 仓库：[ajwwja777/storage-cleanup](https://github.com/ajwwja777/storage-cleanup)，公开，分支 `main`。

2026-09-26：精简框架已确认，基础已提交并推送。提交 `d786d0bccce59f26f03fdd8fc8703d781fc3dfa4`，已核验本地、Git 远端和 GitHub API 一致。发布包括 Windows 只读盘点、文件占用核验、配置示例、使用说明、清理项说明和回归检查；完整报告、实际配置及一次性删除脚本留在私有目录。A6000 维护主代码，各目标机器本机执行；其他 Windows 笔记本可独立使用。

已有进展：笔记本 C 盘只读盘点完成；经用户确认的 20 个安装副本/旧转储已删除，约 1.46 GiB，应用保持运行。10 个华为旧转储共 63.07 MiB 因权限拒绝保留。当次清理结束 C 盘可用约 3.61 GiB。详细证据保存在主项目 reports/。

下一步：按用户选择继续 Windows 候选核验，按实际需要扩展 Linux 工具。A6000、Cobot 和 HPC 尚未盘点；HPC 操作仍需具体任务授权。基础发布不会扩大任何删除授权。
