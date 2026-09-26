# EXPO-FT × Cobot

实际项目：`/data/LFT-W02_data/jiaan/jiaan/projects/expo-ft/`。

目标：忠实复现原始同步 EXPO-FT，后续用于 Cobot Plug 插入（右臂、三相机）。用户倾向把真机适配放在独立 Cobot 项目，具体接口边界待核对。

## 当前状态

2026-09-26 已在新目录 clone 作者源码，并按用户要求新建 `ajwwja777/expo-ft` 和 `ajwwja777/openpi` 两个独立仓库（已按用户要求设为 public），切换 origin 后完成首次 push。两个远端分支均已核对与下表提交一致；两层工作树干净，未加入旧适配代码。尚未安装运行环境、准备训练资产或开始训练。旧远端由用户另行处理。

| 仓库 | 上游 | 分支 | 当前 commit | 自有 origin |
|---|---|---|---|---|
| EXPO-FT | `pd-perry/expo-ft` | `main` | `803381fc3b4c91a0c47904f1b688fc5e35904f50` | [expo-ft](https://github.com/ajwwja777/expo-ft) |
| OpenPI | `pd-perry/openpi` | `expo_ft` | `46407a41183b037313a383ff679683f2773b766d` | [openpi](https://github.com/ajwwja777/openpi) |

OpenPI 位于主项目的 `expo_ft/agents/vla/openpi/`，是独立仓库，主仓库已忽略该目录。两层均保留作者仓库为 `upstream`，并使用仓库局部 SSH 配置访问自有 `origin`。主仓库只拉取 `main` 分支的完整历史，未使用浅克隆。

[项目 README](../../../projects/expo-ft/README.md) 保留作者原文；新项目的本地状态在本摘要登记。旧 A6000 项目与笔记本工作树保留为历史参考，本次未迁入其代码与配置。

2026-09-26 已完成固定版本 README、scripts/pick/、OpenPI SFT 配置、DROID 数据加载器及 WebSocket 接口的静态源码核对。确认 SFT 与在线 replay 使用不同的数据入口；作者的 DROID 图像映射仅启用两路图像，动作采用笛卡尔速度。Plug 三相机及关节动作仍需训练侧数据/配置适配。以上为源码阅读结论，尚未做环境或运行验证。

下一项待办：确定训练侧数据适配边界与环境准备方案；Cobot 项目由另一对话负责建立，后续按接口配合。

来源：2026-09-26 本项目对话、官方分支、两层仓库的本地与远端核验；同步日期：2026-09-26。
