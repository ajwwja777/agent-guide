# Cobot 操作网页

目标：保留现有操作台、统一采集、训练和部署页面，以及相机／输出面板、模型与任务状态交互。

## 入口

- A6000：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web`；先读该项目 `AGENTS.md` 和 `README.md`。
- 迁移清单与验收条件：`/data/LFT-W02_data/jiaan/jiaan/projects/cobot-web/docs/MIGRATION.md`。
- 笔记本：`D:\Code\jiaan_workspace\cobot-web\AGENTS.md`。
- 仓库：[ajwwja777/cobot-web](https://github.com/ajwwja777/cobot-web)，独立仓库，分支 `main`。
- Cobot 运行副本：`/home/agilex/jiaan/project/cobot-web`；正式 8015 已切换，另有只读预览 8018。

## 当前进度

2026-09-27 网页源码、共享 schema、兼容控制代码和 uv 锁定环境已迁入 A6000 主仓库，已 push。源码提交 `1cf4797f4942f2f27d3815943f7e23cab79452df`；启动隔离修复 `117fe141aea17e9081a1db535e557a155fa136f3`。273 个运行文件同步到 Cobot 并逐文件核验；初次迁移时日志／PID 在 ops/runtime；现已实体归入 cobot-web/runtime，见下方收尾记录。

保留原统一采集、HIL、部署与输出成果；补充设备健康、内部系统盘空间、ROS 日志竞争修复、重要日志切换和 Ctrl 框选。Python 主包使用 cobot_console、capture_core、segmented_capture。旧协议保持兼容，源码不重复散落到其他项目。

网页后端 529 passed／11 skipped、前端 28 passed；只读预览 29 个资源和主要 API 通过。真实只读反馈确认前臂／中臂使能与通路就绪。未进行机器人运动、实际示教或浏览器目视验收。扩展的历史 robot 测试仍有 ROS 依赖／测试隔离及夹爪断言分歧，详见迁移记录，不宣称硬件验收完成。

## 下一步与协作

2026-09-27 用户确认停止当前任务并授权切换。正式 8015 已从新目录启动，初次切换 PID 893608；共享模型更新后 PID 916985，运行版本 3b54cf7；机械臂 724550、相机 631028 保持不变。承接有效任务状态和模型设置，672 个评测文件复制到新数据根并逐文件核验。修复 RL 终止时 operator_nodes 请求 schema 缺失引起的 HTTP 503，相关 82 项回归通过。记录详见实际项目 docs/MIGRATION.md。

部署／采集共用模型进程、实际路径展示、加载前即可选目录均已上线。完整后端 545 passed／15 skipped，新增目录回归集合 12 passed，前端 31 passed，原生 RLT 接口验证 4 passed；正式 API 和静态资源通过。当前保留原始 rollout 的实际目录，失败 episode 历史可读；没有自动加载模型或运行真机 Episode。旧目录因硬件／RLT／模型依赖暂不删除；模型权重、RLT 与原始 rollout 数据仍使用登记的真实原路径，后续逐批迁移。

页面／API 编排由本项目负责；robot 兼容验收交 cobot-control，采集内核后续交 cobot-dagger；模型／RL 问题交 vla-platform／rl-platform，网页使用／运行故障由本项目排查，硬件／存储／算法问题直接交相应领域。各项目只有一份主实现，按批次交接。

来源：A6000 实际源码、Git 远端核验、Cobot 只读观察与 HTTP 验证（2026-09-27）。全部证据与切换条件以实际项目 `docs/MIGRATION.md` 为准。

## 终端与故障恢复归并

2026-09-27 用户取消独立 ops 维护层。命令行操作手册、网页恢复工具与测试迁入本项目；完整启动、普通／模型采集、共享模型／Session、评测、归位与退出见实际项目 `docs/COMMAND_LINE.md`，HTTP／PID／磁盘故障见 `docs/WEB_RECOVERY.md`。统一入口 `scripts/console.py` 复用网页 API；`recovery` 子命令不依赖 8015 正常。输出栏增加诊断入口，展示请求错误、状态与建议，不自动重试动作。旧 ops/runtime、uv 和现场硬件进程保持兼容，原脚本仅跳转。验证与发布结果以实际项目迁移记录为准。

发布补充：功能及命令登记版本 `94840c1` 已 push，285 个现场文件校验；完整 Python 571 passed／15 skipped，前端 34 passed，后续相关 30 项回归通过。确认 idle/offline 后仅重启网页至 PID 967289，14 个硬件／ROS 进程身份不变；原故障用例首轮时序失败及复查通过均留在实际项目记录。CLI 可列出 6 模型、65 主 API／20 recorder API；输出栏有 61 条常用命令。未加载模型或做实机运动验收。

## runtime 与旧项目清理收尾

2026-09-27：网页不再依赖 ops。runtime 原软链接已替换为本项目实体目录，tools/uv、缓存、任务状态、日志、事故与恢复证据全部接管；2,819 条逐项核验。配置切换代码 b1190dd 已 push，同步 285 个文件，23 项 CLI／恢复测试通过。现场 uv 离线检查 32 包、11 类 API、37 个页面资源与 6 模型目录可读；8015 重启为 PID 982318、8018 为 982430，14 个硬件／ROS 进程身份保持不变。

已删除：A6000 /data/LFT-W02_data/jiaan/jiaan/projects/cobot-ops、Cobot /home/agilex/jiaan/project/cobot-ops、笔记本 D:\Code\jiaan_workspace\cobot-ops；guide 的原 ops 摘要也已归并。旧 Git 最终 b67e3e0 已 push 且 bundle 留档，A6000 保存两机原件备份和删除清单，不丢失原成果。

当前运行根 /home/agilex/jiaan/project/cobot-web；runtime/ 日志与状态、tools/uv、.venv/ 环境。完整终端流程在实际项目 docs/COMMAND_LINE.md，故障处置在 docs/WEB_RECOVERY.md；旧 ui_up/down/status 等脚本名称保留，统一 console.py 扩充模型／采集／评测操作。

旧 cobot-platform 仍被机械臂／相机／ROS 使用，且含约 22 GiB 未验收历史实验归档，因此本轮未删除；RLT、模型、原始 rollout、已安装 ROS/SDK 和 A6000 旧算法项目也保留。未做模型加载、机器人运动或成功率验收。新目录能启动网页，不代表所有算法／硬件项目都已迁完。

证据：实际项目 outputs/verification/20260927-runtime-cleanup、outputs/migrations/20260927-ops-retirement；逐项清理与备份哈希见实际项目 docs/MIGRATION.md。其他项目本次仅修正 ops 归属文档，未迁移业务代码；源码分别已 push。

最终发布：网页迁移记录与终端说明提交 d5fe47769604d894a85a1e7800d883b75944db82 已 push；Cobot 同步 285 文件并逐项核验。运行代码无需因本次文档更新再次重启。GitHub 历史仓库保留，本地旧 ops 目录已实际清理。

## 2026-09-27 RLT／硬件新路径联动（待上线）

A6000 已准备调用 cobot-control / rl-platform 的轻量入口、新模型／Replay／数据路径和进程识别；576 项后端回归通过，后续路径／输出相关 63 项通过。现场仍为 d5fe477，未同步这批路径变更。Cobot 在模型独立验证期间 SSH/ping 失联，原件保留，硬件重启和新配置切换待恢复连接后验证。用户已确认机械臂安全断电，可重启节点；无归位或运动授权测试。详见三个实际项目的 docs/MIGRATION.md，guide Git 交原负责 agent。

## 2026-09-28 接续进度

正式8015使用新control/rl-platform/数据根；共享模型加载释放、历史视频及首尾图通过。浏览器最近目录随注册前缀迁移，重复硬件代码移除。历史归档仍在执行；新终端流程见项目COMMAND_LINE/WEB_RECOVERY及RL RUNBOOK。

来源：对应项目docs/MIGRATION.md的实测记录。无真实Episode／运动测试；旧目录清理见后续回执。guide Git由原负责agent管理。
