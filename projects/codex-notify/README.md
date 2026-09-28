# codex-notify

## 当前状态（2026-09-29 核对）

首版 `v0.1.0` 已按 MIT 公开发布；主仓库 HEAD 与远端 main 均为 `52fe0b3`。Windows 客户端、CLI／插件通知实收、托盘开关和旧 CLI 重启恢复均有 2026-09-28 验收记录。通知范围为每轮回复结束，不判断任务结果是否正确。下一步按实际使用反馈维护，Codex 升级后复核完成回调兼容性。

来源：本次只读 Git 核验及 [项目 README](../../../projects/codex-notify/README.md)。本次没有发送测试通知或改动笔记本部署。

实际项目：`/data/LFT-W02_data/jiaan/jiaan/projects/codex-notify/`；详细记录见该目录 README.md。

仓库：https://github.com/ajwwja777/codex-notify （public，main）。

2026-09-28，来源：codex-notify 项目对话。用户批准笔记本 CLI、VS Code 插件每轮回复结束通过 pushplus App 通知荣耀 Android 手机，手机无需 VPN。发送器作为客户端 App 部署到用户指定的 `D:\Downloads\CodexNotify`；主代码、Git、正式文档在 A6000，笔记本仅保留运行组件。令牌只在笔记本 DPAPI 加密保存。

已完成基础发布、发送器与测试、CLI/插件后端完成事件验证、Windows 部署及原 Codex 回调保留。Windows 15 项测试通过。用户已完成本地令牌配置并确认 App 测试通知实收。安装后的 CLI、插件 App Server 后端自动通知均获服务端 accepted，用户已进一步确认这两条自动通知实收，并在最终验收步骤确认 VS Code 插件新对话“只回复 OK，不调用工具”也能自动通知。首版部署与实收验收完成（手机状态由用户操作确认，未通过工具独立观测）。

2026-09-28 后续：按用户要求增加 Windows 托盘开关，关闭窗口收起；右键开启/暂停推送、打开设置或暂停并退出。绿色开启、灰色暂停；暂停时取消待发送队列，恢复不补发，开关不消耗推送额度。D 盘应用已更新，17 项 Windows 离线测试和实际托盘交互验证通过；主代码及依赖版本记录仍在 A6000 项目。

2026-09-28：安装前启动的本项目旧 CLI 会话未触发发送器，其他对话正常；时间与事件证据指向旧进程未加载新 notify。用户已于同日明确确认：退出并恢复原会话后，仅回复 OK 的轮次成功通知，排查验收闭环。

2026-09-28：用户要求公开发布供他人使用，并明确选择 MIT。项目 README 改为公共安装、使用、排查与卸载说明，保留版本与验收记录；个人部署详细历史归档在实际项目 .local/deployment-history.md（忽略，不发布；旧版本仍在 Git 历史）。已发布 v0.1.0 源码版本，不变更笔记本运行文件。

发布核验：main 与 v0.1.0 均对应 52fe0b3b1041dafc61d7bee8b4672ec00cac9808；GitHub 为 PUBLIC、识别 MIT，Release 非草稿。下载并检查源码 ZIP，包含代码、安装脚本、固定依赖、测试和文档，无运行数据。Git 历史 21 个 blob 扫描只命中测试示例令牌，未发现真实凭据。本次 A6000 测试 13 项通过、4 项跳过；Windows 17 项与托盘验证沿用同日代码验收。发布页：https://github.com/ajwwja777/codex-notify/releases/tag/v0.1.0 。guide Git 留给框架维护对话。
