---
title: The Era of Agent
created: 2026-05-16
updated: 2026-05-16
type: concept
tags:
  - #概念
  - #Agent
  - #AGI
  - #投资洞察
confidence: high
source: https://mp.weixin.qq.com/s/-YbLQ2kuolHaXxqkL9mpTw
---

# The Era of Agent（Agent时代）

> 拾象投研 2026年5月AGI投资洞察报告核心摘要

## 核心判断

**AI第一次开始系统性地加速AI自己**——这是进入2026年最重要的结构性变化。
- 模型格局从6个月周期切换→压缩到**以月甚至以周为单位**
- 竞赛窗口压缩：**Coding Agent是科技史上增速最快的新物种**
- AI Coding创造的ARR预计2026年突破**1000亿美元**
- Anthropic凭借Claude Code将在2026年年中有望追平OpenAI的ARR

## 01. 重注Coding是当下最强共识

### 为什么所有AI Labs都要下注Coding

1. **数字世界任务可用Coding表达**：代码能覆盖白领在电脑上的绝大多数操作
2. **AI Labs直接受益**：Coding Agent辅助下，AI Labs产品侧和模型开发都明显加速
3. **内部竞争工具化**：没有领先Coding model = 没有领先GPU，研发和生产力系统将系统性落后
4. **天然飞轮效应**：feedback loop（反馈回路）最短最清晰，每步交互自然产生可用于训练的信号

### "做好Coding没有技术秘密"

做好Coding的难度打分（1-10）：
- **<4分**：任何Lab都能做到，Anthropic领先优势迅速被抹平
- **>8分**：Anthropic形成近似一家独大格局（类似TSMC/NVIDIA）

**真正难度不在技术know-how，而在组织与战略层面**：
- Anthropic核心壁垒：把数据做到极致，首席科学家Jared Kaplan亲自主导数据质量评估
- 极少有AI Lab能组织数百位顶尖研究员做数据这种"dirty work"
- Anthropic两位founder从Day 1把"数据决定一切"写入组织基因

### 下一个OpenAI时刻
随着OpenAI、Gemini在Coding投入加重，"2025年的Google时刻"至少会在OpenAI上重演。交替领先趋势3-5年内不会变。

## 02. AI Labs进入战略与组织文化竞争

### 模型终局：新一代OS

- 今天模型公司的形态（个人助理/工作助理/Chatbot/Agent）本质都在争夺**新一代OS的位置**
- LLM+Agent = 新一代OS，类似Windows 95级别的计算平台
- OS市场典型特征：少数赢家占据核心入口（Android 46%、Windows 30%、iOS 20%）

### 组织文化决定论

> **"模型训练没有secret sauce，组织和战略文化才是。"**

| 公司 | 文化特点 | 执行力 |
|------|----------|--------|
| Anthropic | AGI-native，top-down聚焦，信奉pre-training | 极高（对外承诺几乎全部实现且常超额） |
| OpenAI | 自下而上探索，0→1突破导向 | 分散（300个项目同时推进） |
| Google | 体系化运转能力强，但内部政治复杂决策慢 | 中等（方向确定后可及时跟进） |

### Anthropic制胜关键（All in Coding）

1. **战略聚焦**：放弃C端市场+多模态，避开与OpenAI/Google正面竞争
2. **技术信仰**：对pre-training最坚定，不执着用新架构
3. **产品判断**：IDE是阶段性形态，终端才是终态（→ Claude Code）
4. **组织基因**：全员信奉AGI，人才稳定，Dario每1-2周内部分享最新思考

### OpenAI的问题

- **战略误判**：长期重视ChatGPT C端流量，未及时意识到Coding是主线
- 小模型服务大部分请求，pre-training规模未持续scale
- 内部同时推进项目高达300个
- 基础工作（数据清洗）投入不足
- **最强生命力**：自下而上探索文化，一两位研究员押中正确方向可能带来范式跃迁

### Google定位

- Gemini 3带来C端增长不持续（截止2月增速降至13%）
- 自有TPU极充裕（de-risk集群超头部AI Labs正式训练集群）
- 最稳定追随者但最慢；最可能穿越周期
- Worst case退守英伟达生态角色

## 03. Agent Playbook

### 放弃To B/To C旧地图

新坐标系：**To Human / To Agent** 而非 To B / To C

- AI工具普及顺序：个人先付费→公司IT预算随后追入
- To B与To C传统边界已模糊，统一为**to Prosumer**（知识工作者）

### Agent = Model + Harness

**Harness** = 除模型本身外的所有工程封装

Claude Code核心运行机制（Agent Loop）：
- 仅几十行代码，可拆解为11步
- 重点在第5-8步：判断需要什么→调用工具→判断任务是否完成
- 机制简单，但让agent从处理1分钟任务→20分钟/2小时/更长时间任务

### Agent设计哲学根本转变

| 旧范式（LangChain等） | 新范式（Anthropic） |
|----------------------|---------------------|
| 大量rule-based逻辑控制 | 充分信任模型 |
| 用规则兜底模型能力 | 把Harness做到极简 |
| 不信任模型 | 模型能力决定一切 |

**Managed Agents**：Anthropic第一次把Harness做成托管型产品
- 从API公司→**Agent云/Agent OS**进化
- 用户既可以让Claude Code在本地跑，也可以在云端环境中运行
- Session管理与状态留在Anthropic，用户粘性远高于单纯API调用

### Agent作为经济系统新主体

- Cloudflare宣布允许Agent直接创建账号、开通订阅、注册域名、部署代码
- Agent第一次以独立客户身份进入云服务商客户体系
- Agent既是**付费客户**也是**被独立计费的流量主体**

## 04. 硅谷前沿趋势

### Robotics：2026是机器人数据Scaling大年

**机器人数据金字塔**（对应LLM训练不同阶段）：

| 数据类型 | 对应LLM阶段 | 特点 |
|----------|-------------|------|
| Egocentric data | Pre-training | 成本最低、最易规模化；第一人称视角视频学物理 |
| UMI数据 | SFT | 成本/规模适中，但硬件构型必须与部署机器人一致 |
| Teleop真机数据 | SFT | 历史最久，直接绑定具体硬件 |
| World Model | RL | 无限复杂度与多样性，极度消耗算力 |

**NVIDIA EgoScale发现**：20,854小时action-labeled第一人称视频预训练VLA模型，灵巧操作的人→机器人迁移中观察到log-linear scaling law。

**Hardware is All You Need**：
- 硬件不只是部署载体，更直接决定能否高质量规模化产生数据
- 美国公司在硬件环节短板明显（核心零部件选型/系统架构/供应链响应）
- **华人创业者结构性机会**：依托中国供应链理解+美国机器人需求，打造机器人领域TSMC
- 灵巧手数据至今无公司实现规模化采集——硬件不成熟是根本原因

### 技术趋势：VLA → World Action Model（WAM）

| 维度 | VLA | WAM |
|------|-----|-----|
| Backbone | 语言 | 世界模型 |
| 数据依赖 | action-labeled data（采集成本高） | 直接学习视频数据 |
| 泛化 | 语义泛化强，物理泛化弱 | 物理泛化强（不同材质/位置/遮挡） |
| 决策方式 | Single-turn | 想象未来状态再选动作 |
| 跨场景迁移 | 较弱 | 2倍以上提升 |

**为什么WAM是正确方向**：
1. 灵巧运动不需要语言，physical intelligence才是本质需求
2. 视频作为世界演化监督信号，不绑定action-labeled data
3. 解决VLA物理泛化弱点
4. 适合long-horizon task（多步路径选择+失败恢复）

### Neo Labs两条路线

**路线1：追寻下一范式**
- 代表：Core Automation（Jerry Tworek，OpenAI前reasoning负责人，2026年1月创立）
- 技术路线：Continual Learning
- 目标：开发超越pre-training和RL路线的新算法+比Transformer更具扩展性的新架构
- 风险：创新窗口是否还打开

**路线2：高价值垂直领域**（硅谷基金更偏好）
- 芯片设计、AI for Science、高温超导材料
- 与头部三家形成清晰差异化
- 潜在回报可能远高于大众场景

> 边际变化：Anthropic与OpenAI大量精力投入Coding竞争，下一范式资源投入受挤压，客观为创业公司留出空间。

## 相关概念

[[Agent]], [[Anthropic自举飞轮-Claude-Code开发Claude-Code|Anthropic自举飞轮]], [[harness_工程|Harness工程]], [[cursor_ai编程智能体|Cursor]], [[Claude-Code|Claude Code]], [[具身智能|具身智能]], [[下一代智能系统|下一代智能系统]]
