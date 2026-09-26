# Git 与 GitHub 仓库

先按[项目启动流程](README.md)确定项目和工作位置，再选择新建、clone 或 fork。以下是用户已确定的默认设置，后续对话直接使用。

## 默认设置

| 项目 | 默认值 |
|---|---|
| GitHub 所有者 | `ajwwja777` |
| Git 提交署名（user.name） | `ajwwja777` |
| Git 提交邮箱（user.email） | `139873756+ajwwja777@users.noreply.github.com`（GitHub 隐私邮箱） |
| 新建仓库可见性 | 公开（public） |
| 新建仓库名称 | 根据项目用途自动选取简短明确的英文名，小写、连字符分词；通常与项目目录名一致 |
| 新建本地默认分支 | `main` |
| 执行范围 | 以用户本次要求为准，按需执行初始化、clone、fork、建仓关联或提交推送 |

本流程由具体项目对话在当前任务范围内执行。进入相应 Git 步骤时，直接复用上述默认设置，不重复询问固定账号、公开设置或常规命名；用户另有要求时以其为准。仅要求建目录或写记录时，不自动初始化 Git 或创建远端。需要浏览器登录、设备授权或权限确认时，给出链接或操作让用户完成，然后继续。

新项目按[项目启动流程](README.md)，先确认基本框架与任务，再按文件审阅和暂存基础内容，完成首次提交、push 和远端核验，随后开展具体任务。仅创建目录、初始化 Git 或关联 origin 都不代表基础已发布；用户只要求部分步骤时，按本次范围执行。

## 执行前检查

- 优先使用 `gh`。A6000 固定入口为 `/data/LFT-W02_data/jiaan/jiaan/projects/agent-tools/bin/gh`；长期工具存放在 agent-tools，scratch 只作下载与缓存。
- 用 `gh api user --jq .login` 核对账号。已有正确认证直接复用；缺少认证时用 GitHub CLI 的设备/浏览器登录流程，不让用户在聊天或仓库提供 token。
- 提交身份默认使用上表的署名与邮箱，在目标仓库用 `git config --local user.name ajwwja777` 和 `git config --local user.email 139873756+ajwwja777@users.noreply.github.com` 设置；提交前核对生效身份。GitHub 登录账号仍为 `ajwwja777`。
- 查看目标目录、仓库根和 origin。已有正确仓库与关联时直接复用，不重复初始化。
- 查询拟用仓库名是否存在；只有认证正常且明确返回 404 才按不存在处理。已有仓库需确认属于本项目；不覆盖无关 origin，不将已有私有仓库自动改为公开。

## A. 新建自己的项目

1. 在选定机器工作区创建项目目录和基础文档，保留已有内容。
2. 在项目目录执行 `git init`，新仓库设为 main，并用 `git rev-parse --show-toplevel` 确认根目录。配置适合项目的忽略项；嵌套在其他仓库内时从外层本地排除，避免重复纳入。
3. 在目标目录执行以下建仓和关联命令。`<仓库名>` 是占位符，由 agent 根据项目自动选取：

   `gh repo create ajwwja777/<仓库名> --public --source=. --remote=origin`

4. 用 `git remote -v` 和 GitHub API 核对仓库所有者、公开状态和写入权限。若建仓成功但关联失败，下次只补齐关联，不重复创建。
5. 写回实际路径、仓库链接、分支和完成状态；向用户报告。

新远端保持空仓库，不同时添加另一份 README。已有且确定属于当前项目的空远端，可以通过 `git remote add origin <仓库URL>` 关联；若远端已有提交，先检查历史，不强制推送。

## B. 直接 clone 已有项目

确认来源与目标路径，clone 到新目录或空目录；无需再 init。保留 origin 指向原仓库，记录复现的 commit/tag。直接 clone 不意味着有向原仓库 push 的权限，也不自动为其创建另一个空仓库。

## C. fork 后维护适配

需要自己维护上游副本时，优先在 `ajwwja777` 下创建或复用对应 fork，再 clone。通常 origin 指向自己的 fork，upstream 指向原仓库；记录固定上游版本和适配分支。权限、许可或私有上游限制不通过公开复制绕过。

## 基于上游启动项目的经验

1. **从上游开始**：clone 到空目录，自带 Git 初始化和历史，无需先 `git init`；已有说明文件先妥善安置。
2. **只取所需分支**：确定分支与 commit；可用 `git clone --single-branch --branch <分支> <地址>`，避免下载无关分支的大量历史。
3. **关联自己的仓库**：明确是新建还是复用；作者仓库保留为 `upstream`，自有仓库设为 `origin`，push 后核验远端提交。
4. **配套依赖单独管理**：按作者指定版本和目录分别 clone；普通嵌套仓库由主仓库忽略，分别关联和推送，一个项目可以包含多个仓库。
5. **保持复现基线清晰**：先保留原始源码，平台适配可放独立项目，实际需要改动原实现时再明确接口边界。

来源：2026-09-26 EXPO-FT 项目重新启动经验；具体仓库地址和状态见项目摘要。

## 服务器连接 GitHub 的经验

GitHub 登记服务器的公钥，服务器保存私钥，之后 push 时用密钥证明身份，不必每次网页登录。`user.name/email` 只决定提交署名，不负责登录。

1. 新服务器生成一对专用 SSH 密钥，私钥留在服务器，把 `.pub` 公钥添加到自己的 GitHub「SSH and GPG keys」。
2. 添加公钥可通过网页，也可在已登录的电脑上使用 `gh ssh-key add <公钥文件>`；需要时先完成一次 `gh auth login --web` 授权。若提示缺少上传公钥权限，用 `gh auth refresh -h github.com -s admin:public_key` 补充授权后重试。见 [GitHub CLI 官方说明](https://cli.github.com/manual/gh_ssh-key_add)。
3. 在目标仓库设置自己的提交署名，把 `origin` 设为 SSH 地址，再指定专用密钥：

   ```bash
   git config --local core.sshCommand "ssh -i <私钥绝对路径> -o IdentitiesOnly=yes"
   ```

4. 用 `ssh -i <私钥绝对路径> -o IdentitiesOnly=yes -T git@github.com` 核对返回的 GitHub 用户名，再用 `git push --dry-run origin <分支>` 验证。之后正常 commit、push 即可。
5. 设备授权码过期就重新发起登录；`gh` 登录失效就重新授权。SSH 密钥与 `gh` 登录凭据是两套认证，某一套失效不代表另一套也失效。
6. 换服务器通常新建密钥并登记；其他人照做时使用自己的账号、署名和密钥。仓库局部配置决定使用哪个密钥，但共用同一 Linux 账号的人仍可访问该账号下的凭据。

来源：2026-09-24 A6000 GitHub SSH 配置经验；2026-09-25 核对并整理。

## 提交与同步

需要发布时，审阅具体文件，按文件暂存、提交，再用 `git push -u origin <分支名>` 发布；不使用 `git add .` 或强制推送。验证远端分支后记录已发布状态。

新建、clone、fork 各自扩展实际需要的流程；每次更新向用户说明改了哪些文件，以及创建、关联、提交和推送分别完成到哪一步。
