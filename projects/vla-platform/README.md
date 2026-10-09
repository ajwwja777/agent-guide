# 基于 FluxVLA 的模型训练、部署与评测平台

## 当前摘要（2026-10-09 复核）

π0.5 导入修复、RTC 代际取消和 guided 预热校准已交付；DAgger 和原版完整原始权重恢复到获准 Cobot NVMe 路径，CPU 非有限值为 0、GPU 加载后 SHA 保持。真实 observation 预热暂停加载及无指令影子运行通过，Getea 底层读取故障仍未修复，持续真机动作与效果待操作者验收。早期权重阻碍是历史阶段，恢复后的结论见最新节。来源：所属项目 docs/MIGRATION.md 与 web 恢复回执；本轮未复跑现场。

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

## 2026-10-08：π0.5 导入修复；DAgger 权重阻碍

来源：cobot-web 用户报告及本对话现场核验。VLA 明确包名导入修复已发布 83a49c9c059da661df34f152c617b7d54d3424a5，144 项 CPU 回归及真实环境 8 个导入组合通过。实际 DAgger 3000 的暂停加载在首次普通 baseline 预热失败；只读扫描发现 4 个参数张量共 96 个非有限值，19 个文件中 4 个 SHA 与 9 月 28 日迁移记录不同。旧路径是当前坏权重链接，历史训练机两个登记入口均超时，等待可信同版本权重；部署尚未恢复，不声称 20／50 Hz 真机通过。最终无模型运行、网页及 12 个采样硬件／模型身份保持，未运动／写 Episode／改 Replay／权重，现场拥有权释放。完整证据 cobot-web/outputs/pi05-import-20261008/，详见所属项目 docs/MIGRATION.md，本次文档版本 8053756402a6b6d92144ac948cb60a778caf4760；guide Git 不提交／推送。

### 2026-10-08 追加：更正 π0.5 权重初步归因

用户补充迁移后曾成功且旧训练机已不用；现场 9 月 29 日两次 DAgger ready＋PAUSED 日志支持，同样加载当前 Getea DAgger 路径。用户指定旧部署目录 step_3000 是当前权重链接。直接读取及针对 checkpoint 的缓存 advice 曾使一个文件恢复原 SHA，但其他仍异常，后续恢复又令读取 SHA 改变；CPU 非有限参数由 96 变 127，隔离串行读取 embedding 仍有 26。独立读取样本 395 字节／3 扇区有差异，多数候选未匹配原 SHA，不部署。尚不能确认持久文件损坏；不以旧训练机副本为唯一恢复路径。等待管理员底层只读诊断信息以区分文件系统／缓存／内存／读取路径。15:39 释放现场后，网页已另行加载 RLT，本对话不停止或切换它。源码修复完成，实际 DAgger 恢复仍未完成。详见所属 MIGRATION 追加核验与 cobot-web/outputs/pi05-import-20261008/，文档 c09ec8b6a10bb57f960b3aea833ea8c8bed085cb；guide Git 不提交／推送。

### 2026-10-08：π0.5 原始 DAgger 权重恢复到 NVMe

底层只读读取获得全部 19 文件原始迁移 SHA，CPU 恢复 33.53 亿参数非有限值为 0，恢复后全部 SHA 稳定。两次块设备 O_DIRECT 样本仍出现差异，底层链路故障未定位或修复。用户明确批准永久 NVMe 路径 /home/agilex/jiaan/model/vla-platform/pi05/in_the_pot/dagger_2000plus3000，原 Getea 权重保留；web 主机配置登记仅此模型例外。用户批准接管做暂停加载，接管时模型 offline、无录制/GPU 任务。实际 20／50 Hz＋RTC＋滤波加载结果待追加；不以 CPU 验收代替运行验收。来源：所属 docs/MIGRATION.md、web outputs/pi05-import-20261008/；文档发布 b2e5d900e6b03ea51521b92f6ade39384056635f，guide Git 不提交／推送。

### 2026-10-08：π0.5 DAgger 暂停部署恢复通过

来源：所属项目 MIGRATION 最终验收与 web outputs/pi05-import-20261008/。完整原始 19 文件恢复到用户批准的 NVMe 路径，CPU 参数非有限值为 0，GPU 加载后 SHA 仍全匹配。20 Hz 无 RTC／滤波及 50 Hz＋RTC＋滤波两次真实 observation＋baseline／guided RTC 预热 ready and PAUSED；最终保留 50 Hz 手动暂停，3 秒只读监测无 policy 动作消息，无运动、录制或 Replay 编辑。只重载网页生效路径；重载当时硬件 12 身份保持，加载后另有 cameras_up 使三路相机 PID 改变，本任务没有发硬件启停，最终其余 9 身份保持。Getea 底层读取链路故障尚未定位／修复；不要误称整机存储健康或运动／50 Hz 连续发布已验收。文档 adee890e7735b59cf8ae2af3d65306616f6ce03f；guide Git 不提交／推送。

### 2026-10-08：π0.5 运动后退出修复，保持暂停待操作者复测

用户运动后退出；无发布器影子诊断确认首次 guided RTC 延迟超过 baseline 初始化预测，异步停止又与 50 Hz 发布 reset 竞争产生 NoneType。已修复代际取消竞争，Task2 异常保护性手动暂停并保留模型／原始原因；网页显示 fault。guided 预热后两次往返校准＋2 逻辑步余量，严格超时／过期动作检查保留，逻辑 20 Hz／发布 50 Hz 不变。VLA f4f1f6b／29cbbb6，web 803d797，48＋50 项测试通过／1 既有跳过，SHA 与两套 RTC manifest 同步核验。中断 eval 保留为 unknown，三个 start JPEG 字节保持。真实相机／关节／NVMe DAgger 的无机器人指令发布器影子运行 300 步／750 次／15.76 秒无错误；最终模型 3727953 保持 ready／手动暂停、无活动轮次／writer。只重载网页，12 采样硬件身份保持；没有实际运动验收，拥有权交还用户。详细事实与证据在所属 docs/MIGRATION.md 和 cobot-web/outputs/pi05-publication-race-20261008/；Getea 底层读取问题未修复。guide Git 不提交／推送。

### 2026-10-08：原版 π0.5 step2000 恢复到工控机 NVMe

来源：cobot-web 用户错误截图及原版现场核验。首次 baseline 预热返回非有限动作，尚未进入 RTC／滤波发布；Getea 原版副本 4/28 SHA 异常、两个 MLP 张量共 30 非有限值。文件／块设备只读恢复获得全部原始 SHA；末个文件两次块设备读有 136 字节／1 扇区变化，底层故障仍未定位／修复。完整原版 28 文件、33.53 亿参数 CPU 非有限值为 0，复制到 /home/agilex/jiaan/model/vla-platform/pi05/in_the_pot/baseline_2000 并登记单键 pi05_checkpoint（web cac047a），Getea 原文件保留。20 Hz 无 RTC／滤波与 50 Hz＋RTC＋滤波真实预热均暂停就绪，GPU restore 约 5 秒，GPU 加载后全部 SHA 仍匹配。无指令发布器影子运行 300 步／750 次／15.60 秒无错误；最终原版模型 3902257 手动暂停，12 采样硬件身份保持，未实际运动或写数据／Replay。现场拥有权交还用户，实际运动复测仍待操作者完成。详见所属 docs/MIGRATION.md 与 cobot-web/outputs/pi05-baseline-finite-20261008/；guide Git 不提交／推送。


## 2026-10-09：Franka 上传材料整理

来源：Franka 项目对话。笔记本 human_upload/franka 四份历史 Word（采集部署速记、目录说明、旧交接提示、训练 pipeline）归入实际 vla-platform/outputs/franka/uploads/20261009/，共 30,844 字节，大小与 SHA256 4/4 核验一致；原件含历史登录信息，限制访问并留在 Git 忽略目录。本地无运行依赖；删除旧副本被自动审批拒绝，改将四份副本归位至 D:\Code\jiaan_workspace\franka\uploads\并再次验 SHA，human_upload/franka 已空。根层保留 AGENTS.md 和 uploads/，未创建 franka/franka/；四份上传副本目前按需保留在合规的 uploads/；此前永久删除被拒绝为历史结果，本地目录归位已完成。历史地址和操作步骤不作为当前状态；未访问真机或提交/push。详情见实际项目 docs/MIGRATION.md 及上述目录 migration-receipt.json。
