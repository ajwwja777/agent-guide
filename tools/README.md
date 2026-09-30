# Agent 工具

长期使用的 agent 工具存放在此目录；scratch 仅存下载包和临时缓存。

- GitHub CLI：`bin/gh`，版本 2.101.0，Linux amd64。
- 来源：https://github.com/cli/cli/releases/tag/v2.101.0
- 安装包：gh_2.101.0_linux_amd64.tar.gz，已核对官方 checksums。
- 二进制 SHA-256：ea857a3f0f7d4276cf5848b236542c5048e2eaa7bdd1b6ddec238f8793e74bff。
- 工作位置：/data/LFT-W02_data/jiaan/jiaan/agent-guide/tools。
- 二进制由官方 release 获取，不提交；工具说明和自编脚本可纳入版本管理。

认证由系统用户的 GitHub CLI 凭据存储管理，不复制到项目。

2026-09-26 维护：核对已安装 gh 的版本与 SHA-256，并确认其与安装包内二进制一致后，删除旧临时目录 `/data/LFT-W02_data/jiaan/jiaan/scratch/github-cli/` 中的安装包及空目录。GitHub 与 Gist 的 HTTPS 认证助手均已指向本目录 `bin/gh`，修正了 Gist 遗留的旧临时路径。今后本项目临时下载和缓存放 `/data/LFT-W02_data/jiaan/jiaan/scratch/agent-guide/`，按需创建。来源：本次服务器文件与 Git 配置核验。

2026-09-28：按用户确认，工具归属 agent-guide，迁入本目录随 guide 维护；GitHub／Gist 认证助手已更新。原工具摘要并入本说明，不再作为独立项目登记。顶层 jiaan 的空 Git 元数据已备份到 `/data/LFT-W02_data/jiaan/jiaan/scratch/agent-guide/root-git-backup-20260928-152557`；其他项目 Git 未修改。

2026-09-28 更正：曾通过 `/home/LFT-W02/.zshenv` 限制 Git 向上查找，用户指出账号级配置超出项目范围后，已撤回本次添加的配置。新框架根及 projects 自身没有 `.git`；终端仍会向上识别 `/data/LFT-W02_data/jiaan/` 的旧仓库，该仓库含历史和关联工作区，更上级也有 Git 元数据。外层仓库尚未处理，其他项目 Git 未修改。

## 当前终端的工作区边界

2026-09-28 用户要求所有文件改动限于新框架目录，改用本目录的 `workspace-env.sh`。在使用该工作区的终端执行一次：

```bash
source /data/LFT-W02_data/jiaan/jiaan/agent-guide/tools/workspace-env.sh
```

脚本仅为当前终端及其子进程设置 Git 向上查找边界，保留已有边界设置；重复执行不会重复追加。不修改主目录配置或任何仓库，不移除外层历史。根目录和 projects 容器不再显示外层分支，各项目独立 Git 正常。新开终端需要重新执行；脚本不在其他进程中自动生效。

## 笔记本 Agent Monitor

2026-09-30 安装 `CYUNEO.cyuneo-agent-monitor` 0.7.0（VS Code Marketplace）。用于在底部 Agent Monitor 面板查看本机 Codex 等对话的运行、完成与等待状态；状态不代表任务结果已经验收。

实体目录：`D:\Downloads\VSCodeExtensions\cyuneo.cyuneo-agent-monitor-0.7.0`（约 2.12 MB）。默认扩展位置 `C:\Users\wja\.vscode\extensions\cyuneo.cyuneo-agent-monitor-0.7.0` 是指向该目录的 Windows Junction；其他扩展目录沿用原位置。已核验文件哈希与 VS Code CLI 的版本识别；未重载现有窗口，面板加载需在 VS Code 中确认，未出现时保存工作后执行“Developer: Reload Window”。扩展升级可能新建版本目录，届时核对实际位置。

安装时保留默认本地读取：Codex 监控开启，网络访问与手机推送关闭；后续通知设置以笔记本实际配置为准。来源：[Marketplace](https://marketplace.visualstudio.com/items?itemName=CYUNEO.cyuneo-agent-monitor)、本次 CLI 安装与路径核验。

2026-10-01 按用户指定固定显示九个对话：cobot_rlt、vla-platform、cobot-control、cobot-dagger、rl-platform-部署现场、rl-platform-修改、agent-guide、rl-platform-思路、cobot-web。cobot_rlt 对应用户确认的“rl-总-旧”；按会话 ID 匹配，显示名称只作面板别名，不修改 Codex 对话名称或历史。固定名单后续由用户指定新增，闲置时仍显示；2026-10-01 用户追加：同时显示最近 24 小时活跃过的其他 Codex 对话。

名单：`D:\Downloads\VSCodeExtensions\AgentMonitorConfig\watched-sessions.json`。0.7.0 不原生支持固定名单，采用本地补丁：修改扩展 `lib/monitor.js`，增加 `lib/watched-sessions.js`；原文件与 SHA-256 保存在同级 `AgentMonitorConfig/backups/0.7.0/`。可维护的应用脚本：[agent-monitor-patch.py](agent-monitor-patch.py)，笔记本运行副本在 `AgentMonitorConfig/apply-patch.py`，遇到版本不符停止。扩展升级后需核对补丁；本次未更改用户后续配置的通知设置。

只读使用真实会话验证：配置 9 个、扫描返回 9 个，无缺项、无额外会话、无扫描错误；模拟一年后仍返回同一名单。已保存补丁，现有窗口重载后加载；名单文件的后续修改由补丁读取，无需再修改扩展代码。来源：本次用户名单、cobot_rlt 选择确认与扫描结果。

2026-10-01 后续排障：用户报告面板仍只有 agent-guide。已复现 C 盘 Junction 加载路径导致名单相对路径查找错误；之前直接从 D 盘验证遗漏了该情况。辅助模块与应用脚本改用 `fs.realpathSync(__dirname)` 解析实体路径；同时在 `C:\Users\wja\.vscode\extensions\AgentMonitorConfig` 建立指向 D 盘同名配置目录的 Junction，兼容已载入的旧路径，未复制名单或历史到 C 盘。

经 C 盘入口及 Node `--preserve-symlinks` 验证：固定名单与扫描均为 9 个，无缺项、额外项或扫描错误。实际共享快照仍为 1 个，现有扩展宿主加载了补丁前的扫描代码；已请用户重启当前 VS Code 窗口的扩展宿主，再核验实际共享快照。应区分脚本验证与正在运行窗口的验证，不能仅凭脚本返回就认定面板已生效。

2026-10-01 后续显示范围：笔记本 `agentMonitor.activeWindowMinutes` 改为 1440，补丁保留固定名单，并允许其他 Codex 对话在最近 24 小时内显示。经 C 盘入口验证当前为固定 9 个加校园 VPN，共 10 个，无缺项与超时额外项；模拟时间推进后仍保留固定 9 个。运行中窗口已应用 24 小时设置，但共享扫描仍由补丁前的旧宿主提供；用户报告重启后，实际宿主 PID 未切换，已请其在当前 jiaan_workspace 窗口重新加载窗口，固定名单在真实窗口中的长期保留仍待核验。
