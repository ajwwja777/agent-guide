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
