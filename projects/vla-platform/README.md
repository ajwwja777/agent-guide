# 基于 FluxVLA 的模型训练、部署与评测平台

目标：以 FluxVLA 为代码基础，逐步纳入现有模型、Cobot／Franka 适配、数采训练部署范式、RTC、动作处理和真机／仿真评测。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/vla-platform`；先读该项目 `AGENTS.md` 和 `docs/JIAAN.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/vla-platform/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\vla-platform\AGENTS.md`。
- 仓库：[ajwwja777/vla-platform](https://github.com/ajwwja777/vla-platform)，独立仓库，分支 `main`。
- Cobot 目标：`/home/agilex/jiaan/project/vla-platform`，本轮未部署或切换。

## 已完成

2026-09-27 已按“目录 → Git push → 记录”建立基础。首次发布 `0204dd99193966efd34ed7471f29c7c10c0d50e2`；补充发布记录后提交 `71d82239f435077f6793e1ab22386389c4358ba7`，均已核验远端 main 与当时本地一致。笔记本入口已创建。业务资产迁移、环境准备和新位置运行验收尚未开始。

## 下一步与协作

先接入现有 FluxVLA π0.5 的一份固定配置和离线输入／输出校验，确认旧模型语义；再分批适配 Cobot、Franka、其他模型与仿真。

模型加载、RTC、归一化、动作解释与评测由本项目负责；记录问题交 cobot-dagger；RL 学习逻辑交 rl-platform；硬件执行问题交 cobot-control。

来源：本项目维护入口、迁移记录与本次 GitHub／Git 核验（2026-09-27）。初始化完成不代表业务已迁移。框架只保留接管摘要，具体证据与进度在实际项目内维护。

FluxVLA 来源：`https://github.com/FluxVLA/FluxVLA.git`，本次固定提交 `6c94e73139d51fca9650fa76265c468378020558`。clone 后推送到自有独立仓库，`fork=false`；没有使用 GitHub fork。

## 2026-09-28 历史资产接管

A6000本项目已承接旧cobot-platform归档：9,629个文件／链接条目、23.17GB，SHA与链接校验通过。DM0-5 step4000和Xiaomi DAgger step4000实体归models/history，索引configs/assets/legacy_cobot_models.json。内部归档链接按新布局重定位，实验provenance保留。

仅资产归档和目录整理，未完成FluxVLA运行适配；当前网页两个π0.5共享部署目录另批迁移。源目录是否已删除以实际项目docs/MIGRATION.md和删除回执为准。guide Git不由迁移会话提交。
