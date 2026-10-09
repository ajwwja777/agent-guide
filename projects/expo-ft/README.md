# EXPO-FT × Cobot

## 当前本地状态（2026-10-09 后续）

本项目没有笔记本运行需求：本地仅 AGENTS.md，旧仓库、两层 .git、缓存和传输 tar 已从项目目录移除，进入可恢复 Windows 回收站，未清空回收站。完整旧仓库和未提交适配保存在 A6000 scratch/expo-ft/laptop-migration-20261009/repository；重新核验 322 个保留文件，其中 320 个与原归档逐字节一致，两个 Git 索引差异另存 cleanup-original-git-metadata，原始版本未丢弃。额外迁移记录已补存 cleanup-source-extras。

代码/Git 在 A6000，现场部署按需在 Cobot，不在本地保留运行仓库；正常开发仍使用 projects/expo-ft，历史适配不自动合入当前主仓库。此前“暂留本地副本、删除被拒绝”是历史阶段，后续采用回收站完成清理。实际项目 docs/MIGRATION_20261009.md 和 scratch/expo-ft/laptop-migration-20261009/cleanup-result-20261009.json 保留详细结果。来源：2026-10-09 用户本次授权与逐文件、原路径和回收站核验。

## 框架核对（2026-09-29）

主仓库 main 与 OpenPI expo_ft 的 HEAD 均与各自远端一致，仍为下表版本。主仓库保留 `pyproject.toml`、`uv.lock` 两处依赖修正，未代为提交。最新跨项目交付仍将 EXPO-FT 标为待适配：环境与数据读取准备不等于 SFT/replay 适配或训练完成。下一步由算法项目确认 Cobot 数据与动作合同，再验证真实 batch 和专用归一化。

来源：本次只读 Git 核验、已有基础准备记录及 [2026-09-29 跨项目交付](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。历史资产路径可能随迁移变化，使用前核对实际位置；`PREPARATION.md` 合并仍由对应项目对话处理。

实际项目：`/data/LFT-W02_data/jiaan/jiaan/projects/expo-ft/`。

目标：忠实复现原始同步 EXPO-FT，后续用于 Cobot Plug 插入（右臂、三相机）。用户倾向把真机适配放在独立 Cobot 项目，具体接口边界待核对。

## 当前状态

2026-09-26 已在新目录 clone 作者源码，并按用户要求新建 `ajwwja777/expo-ft` 和 `ajwwja777/openpi` 两个独立仓库（已按用户要求设为 public），切换 origin 后完成首次 push。两个远端分支均已核对与下表提交一致；当时两层工作树干净，未加入旧适配代码。随后本轮已完成环境与资产核查（见下文），尚未训练。旧远端由用户另行处理。

| 仓库 | 上游 | 分支 | 当前 commit | 自有 origin |
|---|---|---|---|---|
| EXPO-FT | `pd-perry/expo-ft` | `main` | `803381fc3b4c91a0c47904f1b688fc5e35904f50` | [expo-ft](https://github.com/ajwwja777/expo-ft) |
| OpenPI | `pd-perry/openpi` | `expo_ft` | `46407a41183b037313a383ff679683f2773b766d` | [openpi](https://github.com/ajwwja777/openpi) |

OpenPI 位于主项目的 `expo_ft/agents/vla/openpi/`，是独立仓库，主仓库已忽略该目录。两层均保留作者仓库为 `upstream`，并使用仓库局部 SSH 配置访问自有 `origin`。主仓库只拉取 `main` 分支的完整历史，未使用浅克隆。

[项目 README](../../../projects/expo-ft/README.md) 保留作者原文；新项目的本地状态在本摘要登记。旧 A6000 项目与笔记本工作树保留为历史参考，本次未迁入其代码与配置。

2026-09-26 已完成固定版本 README、scripts/pick/、OpenPI SFT 配置、DROID 数据加载器及 WebSocket 接口的静态源码核对。确认 SFT 与在线 replay 使用不同的数据入口；作者的 DROID 图像映射仅启用两路图像，动作采用笛卡尔速度。Plug 三相机及关节动作仍需训练侧数据/配置适配。该阶段仅做静态阅读；随后完成的环境与数据读取验证见下文。

2026-09-26 基础准备已完成：根目录 .venv（Python 3.11.12）安装205个包，EXPO/OpenPI导入、SFT/RL/归一化入口和最小JAX GPU运算通过。A6000已有Plug V3 LeRobot副本：134条、19,022帧；完整payload哈希匹配，全部Parquet数值检查、9个视频解码、LeRobot实际读取通过。现有π0.5基座路径与参数元数据已登记，尚未做完整权重恢复。

唯一依赖修正：上游TorchCodec 0.13.0与Torch 2.7.1二进制不兼容，已固定为0.3.0并验证默认视频读取；其余包版本保持上游锁定值。主仓库仅pyproject.toml和uv.lock有本轮未提交修改，OpenPI干净；没有训练、启动服务、访问Cobot/HPC、提交或push。

完整交付见 [基础准备结果与适配对照](PREPARATION.md)：环境、资产地址、检查结果、Cobot接口和剩余问题。

下一项待办：与Cobot项目确认动作/夹爪语义、三相机映射及控制频率，再实现SFT/replay数据适配、验证真实batch并生成EXPO专用norm。环境和原始数据读取通过不等同于训练适配完成。

来源：2026-09-26 本项目对话、官方分支、两层仓库的本地与远端核验；同步日期：2026-09-26。
