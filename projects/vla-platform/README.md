# 基于 FluxVLA 的模型训练、部署与评测平台

## 2026-09-30：项目对话入口与并行协作交接

用户指定 vla-platform 对话负责本领域，允许多个专题及 fork 并行。笔记本 D:\Code\jiaan_workspace\vla-platform\AGENTS.md 指向本项目；职责、当前问题、worktree/任务范围登记与现场单一负责人约定见 /data/LFT-W02_data/jiaan/jiaan/projects/vla-platform/AGENTS.md。对话不共享实时上下文，接管重查 Git 和现场，不沿用历史 PID/版本。
FluxVLA 主框架保留；历史部署与冻结环境分开登记。RTC 队列/时钟/滤波供 RLT 复用，离线/合成 I/O 通过不等于各模型真机通过。
来源：cobot_rlt 本次用户指示及实际代码/记录核对；仅追加项目事实，guide Git 不提交/推送。


## 当前交接状态（2026-09-29）

保留Flux原生框架；历史部署在 integrations/cobot，统一登记family/task/steps/paths/environment/capabilities与接入程度。同类模型优先配置登记，外部sh先提供进程/日志/完整停止，无协议功能明确禁用。必要外部源码和补丁材料归A6000；Flux冻结环境与基础Python独立恢复、核心库导入通过。其他历史环境包清单不冒充完整重建验收；真实GPU模型加载逐个待验收。

已push并核验 main：052a3c5a8e11d25a54fd6e4df78f77419fb4a5df；Cobot副本 /home/agilex/jiaan/project/vla-platform 已逐文件SHA复核。A6000主项目 /data/LFT-W02_data/jiaan/jiaan/projects/vla-platform，先读README结构和docs/DEPLOYMENT.md，详细批次见docs/MIGRATION.md。

数据/模型实体保持 /media/agilex/Getea1/jiaan/{data,model}；本批未搬迁或新增其备份。完整跨项目交付：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/HANDOFF_20260929.md。来源为本次实际源码、Git核验及现场只读检查；guide Git不由本会话提交。

框架复核（2026-09-29）：已只读核对 A6000 项目 HEAD 与 origin/main 一致，并对照实际项目 docs/MIGRATION.md 和 [跨项目交付记录](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。上述测试与现场状态来自项目验收记录，本次未连接 Cobot 或重跑测试；实时 PID、模型与采集状态需现场重新查询。

以下保留此前阶段记录；旧路径、PID与“尚未迁移”描述应按上述最新状态及所属项目迁移记录理解。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/vla-platform`；先读AGENTS.md与docs/JIAAN.md。
- Cobot：`/home/agilex/jiaan/project/vla-platform`。
- 仓库：[ajwwja777/vla-platform](https://github.com/ajwwja777/vla-platform)，独立仓库，main分支。
- 详细记录：`/data/LFT-W02_data/jiaan/jiaan/projects/vla-platform/docs/MIGRATION.md`。

目标：以FluxVLA为基础，逐步接入模型、Cobot/Franka、数采训练部署、RTC、动作处理及真机/仿真评测。

## 历史阶段状态（2026-09-28）

- FluxVLA上游https://github.com/FluxVLA/FluxVLA.git，固定6c94e73139d51fca9650fa76265c468378020558；clone后push自有独立仓库，fork=false。
- 2026-09-28接管旧cobot-platform历史归档：9,457文件+172链接/23.17GB完整SHA与链接验证通过。
- DM0-5 step4000与Xiaomi DAgger step4000实体在models/history；索引configs/assets/legacy_cobot_models.json。原归档的内部链接重定位，provenance保留。
- 旧cobot-platform在新web/control脱离旧路径启动验证后已删除，回执归cobot-web；本项目仍保存完整归档。当前4ee1443已push。
- 这只是源码初始化和历史资产接管，尚未安装/验收FluxVLA运行环境、推理或RTC适配；Cobot仅有入口目录，未同步完整VLA平台。
- 网页两个π0.5入口仍用task3/task5共享部署目录；A6000其他旧VLA/Franka/ZR-0/LiLaWAM资产仍按迁移记录登记，不能据此批量删除。

## 此前阶段的接续与协作

先取现有FluxVLA π0.5固定配置做输入/输出对照，再分批接入Cobot、Franka、其他模型及仿真资产。模型加载、RTC、归一化、动作解释与评测由本项目负责；采集/HIL协作cobot-dagger、RL算法协作rl-platform、硬件协作cobot-control。历史RLT链接指向rl-platform归档，该归档已全量SHA通过；171个重定位链接可访问，原DM05外部基础模型链接保留登记。

来源：cobot_rlt迁移会话，2026-09-28；对应项目迁移记录、现场测试与Git核验。历史阶段细节以实际项目MIGRATION为准；本会话只维护guide摘要，不提交或推送guide Git。

2026-09-28补充：用户确认数据/checkpoint按用途单机单份保存；原始采集与当前部署归Cobot，训练中间/历史模型归A6000。存放盘点及路径/占用见实际cobot-web/docs/STORAGE.md，各领域实际入口已注明相关资产。当前仍有重复副本待收尾，场景目录尚未改名；本次未删除数据或权重。


## 2026-09-28 存储方案更新

Cobot 数据与模型统一在 /media/agilex/Getea1/jiaan/data/ 和 /media/agilex/Getea1/jiaan/model/。数据按场景分、模型按项目/模型分；本轮不新增 A6000 权重备份。代码、安装环境、运行日志与 PID 留在 /home/agilex/jiaan/project/<项目>/。完整路径与批次状态见相邻 cobot-web/docs/STORAGE.md。
当前批次正在复制/验证及切换。以上旧 /home/agilex/jiaan/data、项目内 models 路径属于迁移前状态；最终完成结论以所属项目 docs/MIGRATION.md 最新批次为准。Guide 本轮只更新记录，由其负责 agent 提交。

## 2026-09-28 Getea1 迁移当前状态

主体数据/权重已迁移到 /media/agilex/Getea1/jiaan/{data,model}，新路径网页历史及 RLT 加载验收后清理了主体旧副本。20:00 Getea1 USB 掉线，FluxVLA 环境/暂存副本的验收和清理未完成；网页已正常停止，迁移进程已退出。恢复识别后先核对文件系统和资产校验，再续迁移，不要直接开始在线训练。详细证据见实际 cobot-web/docs/STORAGE.md 和所属项目 docs/MIGRATION.md。来源：cobot_rlt 迁移会话；未新增 A6000 数据/权重备份，guide Git 不由本会话提交。

## 2026-09-28 20:56：Getea1 存储迁移完成

本批已完成复制、哈希与运行验收、切换和对应旧文件清理。Getea1/jiaan 只保留 data、model；旧系统盘数据/模型目录移除。数据按场景/用途/方法归类，位姿与动作回放归 data/motion；模型按项目/模型/场景/版本归类。代码/环境/日志/PID 留在 /home/agilex/jiaan/project/<项目>。

USB 掉线重连后已完成已迁移资产的全量收据复核；尚不能据此认定硬件链路根因已消除。RLT 新路径暂停加载、在线状态恢复与历史媒体通过；FluxVLA 固定版本离线 baseline/prefix-RTC 通过；π0.5 两入口只做 dry-run。本批未启动真实 Episode 或机器人动作。

完整路径、占用、各项验证边界及回执见实际 cobot-web/docs/STORAGE.md。证据位于 rl-platform/outputs/migrations/20260928-getea-storage/cobot/（Cobot 去掉末尾 cobot/）。同批源码与项目记录已按各自仓库发布；guide Git 保持由其他会话管理。


## 2026-09-28：历史模型部署入口复用

用户要求迁入以前的 .sh 部署成果。vla-platform 现登记 12 个历史版本入口；FluxVLA π0.5、G05 两版本、XR1 原版接入原有暂停服务，其他直接运动脚本保留终端入口；DM0.5/XR1 DAgger 本机缺权重。web 列表补模型/场景/步骤/状态，区分终端可用、缺文件、基础依赖；RLT learner 与 actor 不混为同一步数。

代码、测试与实际部署以所属项目 docs/MIGRATION.md 为准。旧已安装 runtime 明确登记为依赖，尚未全量迁移；本轮无机器人运动或新模型成功率测试，不删除待现场验收的旧入口。Guide Git 仍由维护对话提交。

现场发布验收：web 82ced64、vla-platform fd7ee52 已 push 并同步，分别 217 / 280 个运行文件 SHA 一致。模型 offline、采集 idle 时只重启正式 8015，硬件节点未操作。实际目录为 26 项、11 个网页加载入口、6 个保留终端入口、2 个本机缺权重条目，以及历史 RLT/基础依赖；默认 plug_v3-online-latest 未改变。只读回执：cobot-web/outputs/deployments/20260928-legacy-model-entries.json；Cobot 为 cobot-web/runtime/migrations/20260928-legacy-model-entries.json。此数目表示入口与文件预检，新增 4 个网页入口尚未逐个加载 GPU 或验收现场动作。

## 2026-09-30: RTC reuse by RLT

Source: cobot_rlt dialogue. Existing dagger RTC sampler accepts an optional prefix cache; pure action interpolation/bounded-noise helpers live in its existing execution_methods package. FluxVLA native framework and 14D adapter remain unchanged. RLT owns the 7D bridge; three actual recorded-frame tests passed without robot publishers. No live RTC/publication-frequency/noise changes. A6000 details: projects/vla-platform/docs/JIAAN.md and projects/rl-platform/docs/EXPERIMENTS_20260930.md. Code pushed and selected files synced; guide Git not submitted.

Final release verification (2026-09-30): main/origin d252d9b309b80a7df3e3ab649a0436f062e52cc1; A6000 tree clean; selected Cobot files SHA256 match. Formal 8015 read-only verification passed; no robot motion. Guide Git not committed by this dialogue.

## 2026-09-30: reusable publication/filter layer
VLA bda74ad adds pure regular publication timing and causal time-constant EMA,
plus remaining-actions snapshot on the existing RTC queue. Flux core/default
models unchanged; RLT owns its independent7D scheduler. Selective SHA sync to
Cobot after push; RLT real-policy synthetic7-variant GPU audit passed, real robot
acceptance not performed. docs/JIAAN.md and sibling RL EXPERIMENTS_20260930.md
record scope/results; no project/environment/asset migration, no guide Git.

Final publication verification: vla-platform fe9901f7e1561c1804abda14152a66e1d9c4e894 = origin/main, clean A6000 tree; selected Cobot SHA hashes match. Receipt in RL outputs/rlt-diagnosis-20260930/execution-final-release.json. Guide Git untouched.

2026-09-30 交接发布核验：vla-platform 5e3a1ae58c7919e027a74edb63387e4c1752253c = origin/main，A6000工作树干净；本批选中文档/源码已逐文件SHA同步Cobot。详细回执 projects/cobot-web/outputs/pause-recovery-20260930/handoff-release.json；guide Git未提交。

## 2026-10-01：精简执行选项发布事实

来源：cobot-web 本次任务。模型步数项去除 Hz，运行 Hz/RTC/滤波独立成一行；历史结果成功/失败/未知自动保存，保留原备注与训练许可，CAS 与丢响应查询确认。VLA 共用执行配置、物理时间发布/滤波及可选 chunk 执行已接入当前暂停适配器，RLT 复用配置合同。

A6000 web af56ffc / VLA a9f87e0 / RL aee49de 已提交 push。Cobot web 209 个运行文件全 SHA 校验，VLA 16/RL 2 个本次文件校验；只重载 8015，新网页 PID 927182，模型 offline、录制 idle、无 writer/active lease。9 个采样硬件/模型进程身份保持。共用模块现场导入与 4 个 VLA 文件启动计划、两项 π0.5 dry-run 通过；未新加载 GPU、未真实 Episode/Replay 改写/动作，连续真机 Hz/效果待验收。

离线前端 67，web 后端 87（另 1 skipped），RLT 21，共用 VLA 27，G05 15，XR1 26 项通过。回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/execution-compact-20261001/final-release.json；Cobot 对应 runtime/verification/execution-compact-20261001/final-release.json。guide Git 不由本对话提交或推送。
