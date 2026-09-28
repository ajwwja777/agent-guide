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

核验补充：上级 `/data/LFT-W02_data/jiaan/` 仍有已有 Git 仓库，终端在工作区根可能继续向上识别其分支。本次未修改该上级仓库或其他项目 Git。
