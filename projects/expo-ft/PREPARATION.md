# EXPO-FT 基础准备交付（2026-09-26）

状态：**A6000 环境与原始数据读取检查通过；Cobot 适配、训练 batch、完整权重恢复和训练尚未执行。**

用户授权范围为基础环境、已有资产核查、输入输出差异与接口整理、项目进度更新。本轮仅访问 A6000；未访问 Cobot/HPC，未启动机器人或 learner 服务，未训练、提交或 push。

## 已完成与检查结果

| 项目 | 结果 |
|---|---|
| 框架、源码版本与修改归属 | 已核对；原有 guide 与其他对话修改保留 |
| Python 环境 | 项目根 .venv；Python 3.11.12，205 个包 |
| EXPO/OpenPI 导入 | 通过 |
| SFT、归一化、在线 RL 入口 | help 加载通过；RL 的 absl --helpfull 按约定返回1，非训练失败 |
| GPU 最小检查 | A6000 GPU0，128×128 JAX JIT 矩阵乘法，显式 HIGHEST 精度与 NumPy 对照通过；无模型加载 |
| 数据完整性 | 542 文件完整 payload 哈希与原冻结记录一致 |
| Parquet | 全部134条、19,022帧，state/action=7D，finite、帧索引和30Hz时间戳检查通过 |
| 视频 | episode 0/67/133 的三相机共9个视频、1,209帧全部解码；RGB uint8，480×640 |
| LeRobot 实际读取 | 默认 TorchCodec 和 PyAV 都通过；三条轨迹首尾6个样本，三相机 CHW float32、7D状态/动作 |
| 输入输出、Cobot接口 | 已形成下表，尚未实现适配，不等同于训练 batch 验证 |
| 环境收尾 | pip check 通过；uv 严格离线 dry-run 显示无需修改；GPU0 回到检查前50MiB/0% |

GPU 检查最初以默认矩阵乘法精度对比 NumPy，误差超出测试容差；改为测试内显式 HIGHEST 后通过。只修正验证方法，没有修改训练精度或算法配置。[JAX 精度说明](https://docs.jax.dev/en/latest/201/precision.html)

## 环境与本轮唯一依赖修正

环境：
`/data/LFT-W02_data/jiaan/jiaan/projects/expo-ft/.venv`

复用了现有 uv `/data/LFT-W02_data/junfeng/.local/bin/uv`（0.12.1）、Python 3.11.12 和 uv 缓存，没有新装 Conda、系统 CUDA 或驱动，也没有修改全局 uv 配置。OpenPI 与 openpi-client 都从本项目嵌套仓库 editable 安装，共用根 .venv。

关键版本：JAX/JAXlib 0.5.3、Flax 0.10.2、Torch 2.7.1、NumPy 1.26.4、datasets 3.6.0、PyArrow 24.0.0、Orbax 0.11.13、websockets 13.1。LeRobot 为作者固定 commit `0cf864870cf29f4738d3ade893e6fd13fbd7cdb5`。

作者锁文件的 TorchCodec 0.13.0 与 Torch 2.7.1 存在运行时 ABI 不兼容，默认 LeRobot 读视频报 `undefined symbol: torch_from_blob`；pip check 无法发现这个二进制问题。依据[官方版本兼容表](https://github.com/meta-pytorch/torchcodec#compatibility-with-torch-versions)，先在临时目录验证0.3.0，再加入根 pyproject 的 override 并更新锁文件。安装后的默认解码及 PyAV 回退均实测通过。**全部依赖版本只有 TorchCodec 改为0.3.0，其余保持上游锁定版本。**

安装时服务器全局 uv 配置使用清华镜像，与原锁的 PyPI 源不同；直接 --locked 会要求改锁。指定原始源可以通过解析，但下载较慢。本轮通过 `uv export --frozen` 导出精确版本及哈希，再用镜像执行 `uv pip sync`；保留原锁的 registry 地址与其余包记录。修正后的锁文件经 `uv lock --check --offline` 及 `uv sync --locked --dry-run --offline --default-index https://pypi.org/simple` 验证通过。[uv 导出说明](https://docs.astral.sh/uv/concepts/projects/export/)

已验证的环境入口（不触发重新安装）：

```bash
cd /data/LFT-W02_data/jiaan/jiaan/projects/expo-ft
source .venv/bin/activate
python --version
```

当前主仓库仅有 `pyproject.toml`、`uv.lock` 两处未提交环境修正；OpenPI 工作树干净。两个 HEAD 未变，算法源码未改。

## 已核对的资产

| 资产 | A6000 实际路径 | 本轮结论 |
|---|---|---|
| Plug V3 LeRobot | `/data/LFT-W02_data/jiaan/scratch/cobot-realworld-rl/data/rlt/plug_v3_yyshadow/plug_v3_yyshadow_demonstrations` | 542 文件、1,208,081,237 字节；134 Parquet、402 MP4；完整 payload 哈希匹配旧冻结记录 |
| π0.5 基座 | `/data/LFT-W02_data/jiaan/scratch/cobot-realworld-rl/assets/pi05_base/params` | 基座目录共 29 文件、12,441,749,581 字节；参数元数据 51 个叶节点，动作投影维度 32；只检查文件和元数据，尚未恢复完整权重 |
| RLT V3 norm | `/data/LFT-W02_data/jiaan/scratch/cobot-realworld-rl/checkpoints/plug_v3_yyshadow/stage1-faithful-s42/4999/assets/plug_v3_yyshadow_demonstrations/norm_stats.json` | 可作历史参考；尚未证明与 EXPO 的动作变换、频率、采样窗口一致，不直接作为 EXPO norm |
| EXPO SFT checkpoint / 专用 norm | 新 EXPO 项目中尚未生成 | 待数据合同与适配确定后训练、计算 |

Cobot 原始 HDF5 来源（来自记录，本轮未连接核验）：
`/media/agilex/Getea1/jiaan/data/rlt/plug_v3_yyshadow/demonstrations/recording_tmp/`

Cobot 已转换数据来源（来自记录）：
`/media/agilex/Getea1/jiaan/data/rlt/plug_v3_yyshadow/demonstrations/lerobot-validated-v1/`

本轮使用 A6000 已有副本，不重新转换、复制整套数据或修改源数据。当前检查的 A6000 数据目录没有 Plug V3 原始 HDF5。LeRobot payload SHA-256 为 `96e6e2b30016d75fdaf099a256f324398fcd472d0c8326bb2ce033edf49af101`；转换清单 SHA-256 为 `c1c3fd4ad2ca0d1602d611c99f9ad97c4792a17882aca22224c7d375e76f1171`，均与旧项目审计一致。

## 输入输出及适配差异

以下是源码与已有数据的核对结果，尚未实现适配，不能当作已经通过的训练合同。

| 项目 | 现有 Plug V3 | 固定版本官方入口 | 必要适配或待决定事项 |
|---|---|---|---|
| 相机 | `cam_high / cam_left_wrist / cam_right_wrist`，RGB、480×640 | DroidInputs 实际只用 exterior + wrist 两路，第三路补零且 mask=false | 映射到 base_0_rgb / left_wrist_0_rgb / right_wrist_0_rgb，三路 mask=true；critic_camera_keys 同步启用第三路。保留官方 resize/增强逻辑 |
| 状态 | `observation.state` 为右臂六关节＋夹爪，7D | 示例为笛卡尔位姿 6D＋夹爪 | 配置明确使用右臂关节状态；不能用相同维度冒充笛卡尔状态 |
| 原始动作 | `action` 为 7D；转换器直接复制 HDF5 `action[:,7:14]`，未做 delta 变换 | DROID 示例是笛卡尔速度＋夹爪速度 | 明确关节目标、单位和夹爪语义；若用 delta joint，训练时六关节相对 chunk 起始 state 转换，推理时逆变换，夹爪单独处理；不能重复转换或按每步累计 delta |
| 频率 | LeRobot 元信息 30Hz | pick 控制 10Hz；SFT loader 默认按数据 fps 取连续 action | 确定控制频率。若选 10Hz，应同时对齐观测 anchor 和 action 时间偏移（例如源帧 stride=3），而非只改 fps 标签；SFT、replay、部署一致 |
| SFT 入口 | LeRobot v2.1，键为 observation.state / action / observation.images.* | LeRobotDROIDDataConfig 的键映射不同 | Cobot 数据配置与输入/输出 transforms；可复用现有 LeRobot payload |
| replay 入口 | 有原始 HDF5 和已审核 LeRobot；134 成功轨迹可追溯到源文件与裁剪区间 | train_pi_robo.py 只分派 droid；loader 读取数字子目录中的 traj.hdf5、saved_observation、action 子键 | 外部 replay loader 或明确的入口扩展；不能仅把 Cobot HDF5 路径填进去；也不必为了格式相同重新采集 |
| 动作修正维度 | 六关节＋夹爪 | pick 示例 edit_action_xyzg=true，只编辑 xyz＋gripper | 关节动作任务必须重新明确修正 mask；不能沿用 xyz 名称对应的维度 |
| 数据划分 | splits.json 为 120/14，meta/info.json 声明 train:0:134 | 标准 loader 不自动应用外部 splits.json | 当前默认会读全部134。是否保留验证集需明确；旧 RLT 已见过全部134，不能称14条为 RLT 未见测试集 |
| 归一化 | 旧 RLT norm 已存在 | EXPO norm 依赖最终 data transforms | 适配、频率及窗口确定后再生成 EXPO 专用 norm |

固定版本核对入口：
- `expo_ft/env/droid_utils.py`：示范载入、最后一步 reward=1 / done=1、其余 reward=0；num_data 取排序后的前 N 条。
- `expo_ft/agents/vla/openpi/src/openpi/policies/droid_policy.py`：两路图像、状态和输出维度。
- `expo_ft/agents/vla/openpi/src/openpi/training/config.py`、`data_loader.py`、`transforms.py`：SFT 映射、时间偏移与 delta/absolute 变换。
- `expo_ft/agents/alg/batch_utils.py`：critic 相机堆叠顺序。
- 旧项目 `/data/LFT-W02_data/jiaan/projects/proj-20260904-cobot-realworld-rl/methods/openpi_rlt/plug_v3_yyshadow/tools/convert_experts.py`：原始14D切到右臂7D、动作未做 delta 转换。

官方 pick 脚本示例是 H16、执行8步、SFT 4001步、在线入口引用2000步 SFT checkpoint、10条 replay 示范、每 episode 触发3次更新、edit_scale=0.2。这是代码示例事实，不直接作为最终 Plug 或论文插入任务参数。旧项目的 C4 / 25 demos / edit_scale=0.05 等配置不能未经逐项确认迁入。

## 给独立 Cobot 项目的接口摘要

Cobot 端主动连接 learner 的 WebSocket；通信编码是 `openpi_client.msgpack_numpy`，learner 使用 websockets 13.x。源码示例端口 8102 只是配置示例，本轮没有启动监听。HPC 与 Cobot 的连通性尚未验证。

| 请求 operation | 回复中使用的字段 |
|---|---|
| create_env | env_id、task_description；错误用 status=error 和 message |
| reset | observation、done |
| get_observation | observation；同时返回 done、success、reward、mask，减少独立查询 |
| get_info_for_step | done、success、reward、mask（兼容回退入口） |
| step | action（实际执行的动作，必须与请求采用同一坐标和单位）、action_type=policy 或 human |
| render | frame：RGB uint8 图像（评估视频用） |

原算法接到 human 动作会清空剩余 action chunk；replay 应保留实际执行动作与 HIL 标记。成功奖励与人工接管是独立信号。终局时间对齐、暂停/取消/故障与普通失败如何区分，需要在 Cobot 适配合同中明确，不能擅自合并。

独立 Cobot 项目除了现场硬件桥接，还需提供训练端可安装的数据适配模块。当前上游入口包含 DROID 分派与固定配置注册，因此完全外置适配需要薄启动器或显式扩展点；尚未实现和验证，不能声称只接通网络即可使用三相机关节控制。

## 剩余问题与下一步

1. 与 Cobot 项目确认右臂动作单位、夹爪编码、绝对/增量边界、三相机顺序及控制频率。
2. 明确 SFT 训练划分、replay 示范选择，以及论文插入任务对应参数；保留原算法，单独记录必要平台差异。
3. 实现数据配置与 replay 入口后，检查真实 batch、动作变换往返和终局/HIL 对齐，再计算 EXPO norm。
4. 之后恢复基座权重并做小规模 SFT 检查；正式 HPC 访问与训练需当次授权。当前没有 EXPO 训练结果或真机成功率。


## 证据位置与修改文件

本轮原始日志、检查脚本及 JSON 回执：
`/data/LFT-W02_data/jiaan/jiaan/scratch/expo-ft/preparation-20260926-211717/`

关键回执：
- `environment-final.json`：实际205包、源码commit、依赖差异与文件SHA-256。
- `environment-checks.json`：基础导入与入口检查（此文件保留修正前的0.13版本快照，最终版本以 environment-final.json 为准）。
- `gpu-check.json`、`gpu-check-highest.log`：GPU检查；原始低精度对比失败日志保留。
- `dataset-integrity.json`、`dataset-sample-check.json`：完整哈希、全量数值与视频检查。
- `lerobot-reader-final.json`：最终环境两个解码后端及首尾样本检查。失败的原锁环境回执另行保留。
- `assets.json`、`pip-check-final.log`、`lock-dry-run-final.log`：资产与最终环境核验。
- `install-mirror.sh`、`compatible-requirements.txt`、`compat-install.log`：本轮安装证据；临时导出文件不是第二套项目依赖来源，项目以 pyproject.toml / uv.lock 为准。

本轮修改：
- `/data/LFT-W02_data/jiaan/jiaan/projects/expo-ft/pyproject.toml`
- `/data/LFT-W02_data/jiaan/jiaan/projects/expo-ft/uv.lock`
- `/data/LFT-W02_data/jiaan/jiaan/agent-guide/projects/expo-ft/README.md`
- `/data/LFT-W02_data/jiaan/jiaan/agent-guide/projects/expo-ft/PREPARATION.md`

来源：本轮 A6000 实物检查、固定版本源码、旧项目转换代码与冻结清单；2026-09-26。