# 统一 RL 实验平台

## 2026-09-30：项目对话入口与并行协作交接

用户指定 rl-platform 对话负责本领域，允许多个专题及 fork 并行。笔记本 D:\Code\jiaan_workspace\rl-platform\AGENTS.md 指向本项目；职责、当前问题、worktree/任务范围登记与现场单一负责人约定见 /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/AGENTS.md。对话不共享实时上下文，接管重查 Git 和现场，不沿用历史 PID/版本。
MC30 与 async_rtc20/30/40/50 为可选候选。2026-09-30 修复暂停旧时钟误报及录制 HTTP 占用推理预算，保留 Stage1 的现场重建通过；连续真机 50 Hz 与成功率仍待验收。
来源：cobot_rlt 本次用户指示及实际代码/记录核对；仅追加项目事实，guide Git 不提交/推送。


2026-09-30 实际稳定性修复验收：rl3902fa8/web6b84116 已push、13文件SHA同步。
暂停/HIL旧时钟误报已修复，录制HTTP移出RTC推理预算；web新增收尾未标注录制和通用保留模型重启。
现场活动writer的48帧测试文件提交、writer占用释放、runtime重建ready/disarmed，Stage1 PID233064/start_ticks20025113保留，7个采样硬件身份不变。
Replay3917/Learner7000/Actor3500未变，未执行推理/运动；50Hz连续真机与插入成功率仍待验收。
回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/pause-recovery-20260930/；
Cobot对应 /home/agilex/jiaan/project/cobot-web/runtime/verification/pause-recovery-20260930/。
具体恢复按钮、CLI和限制见web docs/WEB_RECOVERY.md与RL docs/RUNBOOK.md；guide Git不提交。

## 当前交接状态（2026-09-29）

固定RLT算法与参数保留；共享采集/评测边界和目录状态归 integrations/cobot_runtime，不再反向import web Python。录制HTTP仍由web同一个recorder提供，领域库归dagger。现场preflight为Learner5000/Actor2500/warmup锚点2567；在线契约78项、恢复Stage1契约35项通过。两冻结环境在A6000独立恢复导入通过。EXPO-FT保留独立仓库/同步训练，登记为待适配。没有启动真实Episode或更新生产Replay。

已push并核验 main：c6b640ead7d1c869dacce65f224f7d49cd18c553；Cobot副本 /home/agilex/jiaan/project/rl-platform 已逐文件SHA复核。A6000主项目 /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform，先读README结构和docs/DEPLOYMENT.md，详细批次见docs/MIGRATION.md。

数据/模型实体保持 /media/agilex/Getea1/jiaan/{data,model}；本批未搬迁或新增其备份。完整跨项目交付：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/HANDOFF_20260929.md。来源为本次实际源码、Git核验及现场只读检查；guide Git不由本会话提交。

框架复核（2026-09-29）：已只读核对 A6000 项目 HEAD 与 origin/main 一致，并对照实际项目 docs/MIGRATION.md 和 [跨项目交付记录](../../../projects/cobot-web/docs/HANDOFF_20260929.md)。上述测试与现场状态来自项目验收记录，本次未连接 Cobot 或重跑测试；实时 PID、模型与采集状态需现场重新查询。

以下保留此前阶段记录；旧路径、PID与“尚未迁移”描述应按上述最新状态及所属项目迁移记录理解。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform`；先读AGENTS.md与README.md。
- Cobot：`/home/agilex/jiaan/project/rl-platform`。
- 仓库：[ajwwja777/rl-platform](https://github.com/ajwwja777/rl-platform)，独立仓库，main分支。
- 详细记录：`/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/MIGRATION.md`。

目标：按方法组织采样、Replay、学习、模型发布与评测；当前接入RLT，EXPO-FT沿已有独立实现推进。迁移保持原算法、5k warmup、数据比例和动作语义。

## 历史阶段状态（2026-09-28）

- 当前运行代码、模型、Replay、环境和数据均用新根；正式8015共享入口已加载固定5k及最新在线模型到ready/disarmed，再正常释放。
- 基线learner5000/actor2500/Replay2567；无新数据不更新。A6000与Cobot独立副本测试均通过，一条模拟transition驱动5次更新，重启不重复更新；正式权重和Replay不变。
- Stage1现场加载约44秒，首次固定输入编译16.8秒，后续约76ms。31文件/15.43GB跨机SHA一致；不是新真机成功率。
- 11,123数据文件/158.04GB和2内部链接验收后，旧data下rlt/evaluations/cobot-platform/record/test已删除。新数据在/home/agilex/jiaan/data。
- A6000旧proj-20260904-cobot-realworld-rl已完整归档并删除；479条目一致。历史warmup对比1,731文件已归入outputs/rlt/plug_v3_yyshadow/history。
- Cobot旧RLT历史39,001条目/122.21GB在A6000全量SHA通过，模型归models/history、数据归data/history；旧路径隔离冷加载/释放通过后，旧RLT及其别名已删除。7.49GB现场环境备份已在A6000完成SHA校验并保留，现场暂存tar已清理。
- 当前源码918a2bf已push并同步506文件；自有独立upstream ajwwja777/rlt-openpi固定8cef77e，不fork、不向上游提PR。

## 此前阶段的接续

本批迁移/归档/清理已完成。最终模型offline、无活动Session、无GPU计算进程，系统盘约77.6GiB可用；后续网页新启动的臂/相机任务保留，5臂反馈与3相机可用。本会话没有归位或真实Episode。现场需短轮次验证HIL、暂停、终止结果和复位，再连续在线采集。完整回执在outputs/migrations/20260928-retirement/cobot/，汇总在outputs/migrations/20260928-cutover/final-summary.json。

在线入口：采集页选择/home/agilex/jiaan/data/rlt/plug_v3_yyshadow/online和plug_v3-online-latest；加载完成后才开始Session。固定warmup/Reference是对照，评测不写Replay。完整终端与恢复命令见docs/RUNBOOK.md以及cobot-web/docs/COMMAND_LINE.md、WEB_RECOVERY.md。

## 协作

本项目负责Replay、奖励、learner与在线状态；硬件由cobot-control负责，网页/任务/API由cobot-web负责。录制库暂在web，后续单独交接cobot-dagger。历史58次/22次成功是既有37.9%基线，不能与新路径加载测试或单独Reference目录的成绩混用。

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


## 2026-09-29：RLT录制保留模型恢复

来源：cobot_rlt用户要求，不释放已加载模型。先用原Session stop清除无未决Episode的启动故障，保留PID1436537；web新增录制预检/恢复页面与同API CLI、具体503原因，fault可结束Session。dagger修复实时预检clock先取值后等待cache锁的竞态；未修改RL算法/HIL/mask或数据格式。旧503无细节，不能将全部历史错误归因该竞态。

dagger dffc3f1 / web 8dd6983已push并同步，45/198文件SHA一致；254项Python通过、1项既有跳过，45项前端通过。模型保持暂停时连续3次12帧真实录制/放弃清理通过，无新增训练数据；最终模型ready、recorder idle、Session stopped，手动开始下一Session。Learner5090/Actor2545及模型、硬件PID保留。本轮未真实推理或运动，完整HIL仍需现场使用验收。

具体代码/终端步骤/现场回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/WEB_RECOVERY.md、docs/MIGRATION.md、outputs/rlt-recorder-recovery-20260929/；采集领域细节见cobot-dagger/docs/MIGRATION.md。Guide只更新事实，不提交Git。

## 2026-09-29：RLT启动优化，保留当前π0.5

来源：用户指定先优化RLT，in_the_pot π0.5仍在使用。Stage1只建立VLA/encoder抽象结构，避免真实随机初始化后覆盖；Orbax选择性恢复跳过不参与部署的404,338,688个decoder参数，训练checkpoint保持原样。默认取消72%显存预占，增加项目内持久编译缓存和分阶段加载计时；BF16、seed42、去噪步数、动作/HIL/在线算法不变，未改固定上游。

17项相关冻结环境回归、全部保留参数逐值对比、真实encoder输出及完整固定输入动作/RL Token对比通过；再次启动明确命中编译缓存，输出仍逐值一致。A6000 CPU独立进程初始化+加载32.60→19.80秒，第二次20.10秒；这是CPU/cache条件下证据，不能写成Cobot冷启动从9分钟降到20秒。Cobot实际GPU冷读、编译和显存峰值待用户下一次切换RLT测量。

源码8c3cc48、记录7de2fa2已push并同步Cobot528文件SHA一致；π0.5 supervisor2019008/GPU2019058/客户端2025877与硬件PID/start_ticks保留，没有重启/加载模型/发运动。未搬迁、导出或删除数据/权重，也未将CPU缓存复制到Cobot。

主项目 /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform；现场 /home/agilex/jiaan/project/rl-platform。说明与复现：docs/DEPLOYMENT.md、docs/MIGRATION.md、scripts/validate_stage1_loading.py；证据outputs/startup-optimization-20260929，现场runtime/verification/startup-optimization-20260929。Guide只更新事实，不提交/推送Git。

## 2026-09-29：优化后 Cobot 首次加载实测

16:46:18开始至16:51:08启动RL角色约4分50秒；Stage1权重恢复259.279秒，首次编译/固定输入推理21.016秒，后续76.79/72.18ms。仍主要受Getea1恢复限制；不是完整加载20秒。原日志见Cobot rl-platform/outputs/rlt/plug_v3_yyshadow/logs/model-20260929T084619Z.log，详细记录docs/MIGRATION.md，ce6a64e已push并同步528文件。本轮未重载模型或改算法，录制目录旧标签故障由dagger/web修正。

## 2026-09-29：RLT训练与诊断分析页面

来源：cobot_rlt用户要求新增分析板块、训练页整理对齐。web e775308已push并同步202文件，正式8015新增只读/api/analysis/rlt；训练保留进度/发布/参数/主要loss，核心分析归独立页面，历史Warmup图折叠保留。rl-platform 88b3e1c新增轻量聚合和离线Replay PCA/k-means，保留算法；该项目本批只同步3个新增分析文件，未覆盖另一对话的NVMe/probe现场改动。

4项RL测试、24项web Python、47项Node通过；1800/1200/760宽度同左/上边界、无横向溢出、0 JS异常。真实快照3917条transition，前两轴解释31.50%，属于姿态/动作覆盖，不是视觉阶段或失败因果。正式API Learner11750、published11500/Actor5750；日志旧心跳标历史快照，未冒充训练仍运行。只在模型offline/录制idle/无writer时持锁重载网页，9个硬件进程身份保持，未运动或加载模型。

说明：/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/ANALYSIS.md；网页使用与记录：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/COMMAND_LINE.md、docs/MIGRATION.md。Cobot快照在 /home/agilex/jiaan/project/rl-platform/outputs/rlt/plug_v3_yyshadow/analysis/replay_projection.json，手动运行 envs/online/bin/python scripts/analyze_replay.py 重新生成。HTTP回执归web/runtime/verification/rlt-analysis-20260929/。Guide仅追加事实，不提交/推送Git。

## 2026-09-29：Replay 构成、采样实验与图像诊断交付

来源：cobot_rlt 实际代码、离线实验及正式8015只读验收。
rl-platform e20edada 已 push 并选择性同步 Cobot，保留其他对话的现场配置。
3917 transition / 277轮；成功68.14%，新自主成功102条/2.60%。
完成4种成功采样配比×3种子×2000更新、14个发布Actor回看、
checkpoint11000梯度/Q探针、6记录帧三相机306次遮挡前向。
未改生产权重、Replay、loss/reward/UTD，也未产生机器人动作。

真实batch审计从下一次Learner项目入口启动生效；历史身份不能补造。
10项轻量测试及1项真实JAX Learner数值等价回归通过。
--versions-only固定保存的轮次集合，不随新增Replay改验证对象。
Online版本回看不是独立验证；未保留同一步Critic处留空，未实现自动GPU验证任务。
详细结果、复现命令及建议：
/data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/DIAGNOSIS_20260929.md。
Cobot JSON：/home/agilex/jiaan/project/rl-platform/outputs/rlt/plug_v3_yyshadow/analysis/。
仅小报告回传A6000 outputs/rlt-diagnosis-20260929，无新增数据/权重备份。
Guide只更新事实，不提交/推送。

## 2026-09-30: credit-assignment candidate

Source: cobot_rlt dialogue, actual Replay experiments. Seven methods x three seeds x 2,000 updates complete. Terminal-only sampling worsened HIL MAE ~12%; MC30 improved early Q AUC .54 -> .67 with only ~0.55% HIL MAE improvement against matched uniform, so no proven robot success improvement. Registered plug-v3-credit-mc30 has separate resumable weights/logs and shared Replay. Actual candidate restore/5 updates per synthetic transition/publication/exact restart and spawned process startup/ordered stop passed without EnvDriver. Recorded Stage1 RTC reuse is verified, but integrated asynchronous RLT RTC/40 Hz and field success acceptance remain pending. A6000 full record: /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/EXPERIMENTS_20260930.md. Cobot weights: /media/agilex/Getea1/jiaan/model/rl-platform/rlt/plug_insertion/history/candidates/credit_20260930/mc_30/online_candidate. Default original online preserved. Project Git pushed; guide Git left to its owner.

Final release verification (2026-09-30): main/origin ff3ad397b676e088a6df767073e7252c2d1ebefa; A6000 tree clean; selected Cobot files SHA256 match. Formal 8015 read-only verification passed; no robot motion. Guide Git not committed by this dialogue.

## 2026-09-30: Critic action-guidance follow-up

Actual frozen-state audit and three Actor-Q-loss-off ablations completed with no
robot movement or production weight/Replay changes. MC30 partially mitigates Q1
preference conflict (23% -> 36% HIL endpoints preferred), but gripper MAE worsens
~4.5%; early-AUC paired interval includes zero. Accepted Online Replay contains
six autonomous successes vs 23 assisted successes and 44 failures. Q-loss-off
imitation gain exceeds MC30 on this proxy, so autonomous benefit remains unproven.
Details / source / reproduction:
 /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/EXPERIMENTS_20260930.md.
Next: observation/action/HIL alignment and autonomous vs assisted credit diagnosis,
then independent field evaluation. Guide facts only; guide Git not committed.

Follow-up release verified: rl-platform d6548b329b3f571fe8e65e0a7cad446c68a5058c = origin/main, clean A6000 tree, four changed source/docs SHA256 match Cobot. Replay unchanged; model offline and GPU idle. Figure/release receipt in outputs/rlt-diagnosis-20260930. Guide Git untouched.

## 2026-09-30: optional asynchronous RTC execution
A6000 main code now owns RLT7D execution registry/hooks; shared RTC queue/sampler/
physical-time EMA remain in VLA integrations. Original entries synchronous20;
MC30 RTC20/30/40/50 selectable/manual, common candidate branch, no weight copies.
77 related offline contracts and3 pinned Stage1 loading tests passed; real Stage1+
Actor synthetic-GPU7-variant audit passed (original effective17.93Hz/p95 98.19ms;
async20 p95 50.03ms, async40 25.05ms). Native Replay -> two in-memory learner
updates passed. All are non-motion checks; real ROS/RPC/Learner-contention/robot
jitter and autonomous success still pending. Backbone training-time RTC not run;
Stage1 remains frozen. Replay hash unchanged, GPU idle, web offline, no Session.
Usage/rollback/structure: /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/RUNBOOK.md.
Reports: same project outputs/rlt-diagnosis-20260930/execution-gpu-comparison.json
and execution-final-release.json; Cobot same suffix below /home/agilex/jiaan/project/rl-platform.
Code committed/pushed before selective hash-verified sync; local/probe changes in
other dialogues preserved. Guide facts only, no guide Git operation. Source:
actual code/tests/Cobot live8015 catalog and this dialogue, 2026-09-30.

Final publication verification: rl-platform ecaa8aac2507444f1331c8523b8d90d2b6d86374 = origin/main, clean A6000 tree; selected Cobot SHA hashes match. Receipt in RL outputs/rlt-diagnosis-20260930/execution-final-release.json. Guide Git untouched.

Frozen A/B guidance clarified: use existing Warmup5k frozen entry with an execution override; MC30 online entries can learn on load. Documentation release 1afc52b9e359a70c281b798e2cbb1d2430f4499b pushed and RUNBOOK SHA synced. Guide Git untouched.

## 2026-09-30: RTC field timeout and retained-Stage1 recovery

Actual19:50:31 MC30 async_rtc50 EnvDriver failed because queue delay exceeded its
200 ms budget; final supervisor traceback was a consequence. Old inference
latency omitted recorder checks, so full contention cause is not established.
RL now records actual/allowed delay and inference/recorder timing; bounds and
algorithm settings unchanged. Web collection/deployment display root cause,
Stage1 retention and explicit status/output/runtime recovery controls.

Recovery verifies fully exited owned runtime and no pending writer/evaluation,
uses original launcher and refuses implicit Stage1 reload. No automatic inference,
home, label, data deletion or Replay commit. Completed orphan writer can permit
UI shutdown only after local process-group verification. Source/docs release:
rl-platform d4c798f, cobot-web4f5db63;18 Cobot hashes checked. Full backend709/6skip,
DOM56, selected RL40, additional shutdown/CLI32 passed. Formal8015 updated with
Stage1 PID233064 retained and14 hardware identities unchanged; recovery/start
were not invoked. Live restart/RTC contention acceptance still pending.

Usage: /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/WEB_RECOVERY.md
and /data/LFT-W02_data/jiaan/jiaan/projects/rl-platform/docs/RUNBOOK.md.
Evidence: /data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/rtc-runtime-recovery-20260930/;
Cobot /home/agilex/jiaan/project/cobot-web/runtime/verification/rtc-runtime-recovery-20260930/.
Source: actual code/tests/live API and cobot_rlt dialogue. Guide Git untouched.

Final record-only release 0d197b9b0bbb7f5a33f31d8487dedb54b6270ff0 = origin/main; A6000 clean and all18 selected Cobot source/docs hashes verified. Guide Git not committed.

Operator follow-up: retained recovery launched20:33:53, Stage1 still233064; at20:34:15 async_rtc50 then failed execution_clock_late. Recovery works, but50Hz field timing is not accepted. No recovery/start requested by agent. Evidence in web outputs/runtime rtc-runtime-recovery-20260930/operator-followup.json.

2026-09-30 交接发布核验：rl-platform 93b96eececc19fe6c0374e5dbcd59fb26a17f58a = origin/main，A6000工作树干净；本批选中文档/源码已逐文件SHA同步Cobot。详细回执 projects/cobot-web/outputs/pause-recovery-20260930/handoff-release.json；guide Git未提交。

2026-09-30：运行选项、录制暂存与历史补标签已交付。模型详情区分发布频率与逻辑／Replay 步频，支持 Hz／RTC／滤波选择；暂存结束当前 writer，保留文件与模型任务，完整未标注记录可补标签，不隐式提交 Replay。离线网页后端 725 passed／6 skipped、前端 62、采集 78、RL 79 通过；连续真机 50 Hz 和成功率仍未验收。

最终发布回执：web e75d3cbb、dagger bb85a8a6、RL d878bded；网页 PID 866075、模型 offline、录制 idle、ROS readiness ok，采样进程身份保持，未启动模型／动作或改生产数据。此前两段已被写成问号，现依据实际项目 docs/MIGRATION.md 与 cobot-web/outputs/recording-defer-rate-20260930/final-release.json 核对后重写；详细过程仍归所属项目。

## 2026-10-01：精简执行选项发布事实

来源：cobot-web 本次任务。模型步数项去除 Hz，运行 Hz/RTC/滤波独立成一行；历史结果成功/失败/未知自动保存，保留原备注与训练许可，CAS 与丢响应查询确认。VLA 共用执行配置、物理时间发布/滤波及可选 chunk 执行已接入当前暂停适配器，RLT 复用配置合同。

A6000 web af56ffc / VLA a9f87e0 / RL aee49de 已提交 push。Cobot web 209 个运行文件全 SHA 校验，VLA 16/RL 2 个本次文件校验；只重载 8015，新网页 PID 927182，模型 offline、录制 idle、无 writer/active lease。9 个采样硬件/模型进程身份保持。共用模块现场导入与 4 个 VLA 文件启动计划、两项 π0.5 dry-run 通过；未新加载 GPU、未真实 Episode/Replay 改写/动作，连续真机 Hz/效果待验收。

离线前端 67，web 后端 87（另 1 skipped），RLT 21，共用 VLA 27，G05 15，XR1 26 项通过。回执：/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/outputs/execution-compact-20261001/final-release.json；Cobot 对应 runtime/verification/execution-compact-20261001/final-release.json。guide Git 不由本对话提交或推送。

## 2026-10-01：方法／步数、历史结果与 NVMe 路径现场事实

来源：cobot-web 当前任务。原版／MC30 方法与纯数字步数独立，固定 5000 保留，新增在线分支读取真实已发布步数；所选 50 Hz 的详情与实际生效设置分开。历史标签接口与目录迁移一致，普通采集节点历史保留记录结果，成功／失败／未知可修改并同步同目录显示。Stage1 清单和实际 CPU preflight 恢复 NVMe /home/agilex/jiaan/data/rlt/plug_insertion/reference_4999；在线资产按原登记引用，未搬数据／权重。

rl-platform 发布 bf111eb70cb25d3e65de58a0dd8a63c8f8b23cbe；三项目源码／记录 SHA 已核验，正式 8015 只重载网页 PID 970937。模型 offline、recorder idle、无活动 writer；9 个采样硬件／模型身份及固定 5000／历史标签 SHA 不变。离线前端 69、完整 web 734（6 skipped）、末次相关 60（1 skipped）、采集 78、RL 24 通过。8 条实际历史标签 GET 与目录 DOM 通过；未启动 GPU／训练／动作，真实在线分支与 50 Hz 连续运动、浏览器视觉仍待现场。详见实际项目 docs/MIGRATION.md 与 web outputs/catalog-results-20261001/final-release.json；guide Git 未提交或推送。
