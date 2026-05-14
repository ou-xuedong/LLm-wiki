---
title: GBrain 深度分析 — 索引导引
type: index
source_repo: garrytan/gbrain
source_commit: master @ 2026-05-12
target_project: Agent记忆与自进化
methodology:
  - borrow-github-module skill 三阶段（理解 → 集成 → 多源冲突）
  - 4 视角全景分析（业务/功能/数据/技术）
  - 第 5 份是借鉴价值总评（超出草稿，为新方向设计打底）
analysis_date: 2026-05-12
analyst: 小昭（subagent × 4 并行 + 主 session 整合）
---

# GBrain 深度分析 — 索引导引

> 给 **Agent 优先读**的导引。主人可以从 §3 直接跳到对应视角；Agent 应当先读这份 index 再按主人提问的指向定位到具体视角。

---

## 1. 这套分析是干什么的

**任务来源**：主人启动新方向项目 `Agent记忆与自进化`，需要彻底搞清楚 garrytan/gbrain 的设计逻辑，作为新方向的设计输入。

**核心目的**：不是 GBrain 百科，是**主人下一步项目设计的弹药库**。

**关键洞察一句话**：

> GBrain 不是 RAG 工具，是一台**"信号 → 大脑 → 自进化"的活体机器**。50 个 skill 围绕一个核心循环：`signal-detector + brain-ops + dream cycle` 是真正的引擎；其他 47 个 skill 都是外围。

---

## 2. 5 份产出物速查

| 文件 | 视角 | 重点 | 重要性 |
|---|---|---|---|
| `01_业务与用户视角.md` | **为什么做** | Garry 的设计哲学 + 商业模式 + 用户旅程 | ⭐⭐ |
| `02_功能与流程视角.md` | **做什么** | 50 skills 全景 + 4 主循环 mermaid 图 | ⭐⭐ |
| `03_数据与交互视角.md` | **信息流** | schema 922 行解剖 + ER 图 + 自连线机制 | ⭐⭐⭐ 主人借鉴核心 |
| `04_技术落地与运维视角.md` | **怎么实现** | 技术栈 + Engine 双轨 + Minions + 评测 | ⭐⭐ |
| `05_借鉴价值评估.md` | **怎么用** | 按 borrow-github-module skill 框架的总评 + 路线图 | ⭐⭐⭐ 本次最核心产出 |

📊 **总规模**：5 份 .md / 2800+ 行 / 17 万字符 / 13 张 mermaid 图

---

## 3. 按需快速导引

### 主人想了解 GBrain 是什么（10 分钟）→
读 `01_业务与用户视角.md` §A（系统边界）+ §E（设计哲学 6 条）

### 主人想看技术栈和架构（10 分钟）→
读 `04_技术落地与运维视角.md` §A（分层架构图）+ §B（技术栈表）

### 主人想看数据模型怎么设计的（15 分钟）⭐ →
读 `03_数据与交互视角.md` §B（ER 图）+ §C（takes vs facts）+ §D（自连线机制）

### 主人想立刻开始设计自己的项目（必读）⭐⭐⭐ →
读 `05_借鉴价值评估.md` §1（TOP 5 必抄）+ §7（v0.1/v0.2/v0.3 路线图）+ §8（核心 DNA）

### 主人想看 50 个 skills 全景（15 分钟）→
读 `02_功能与流程视角.md` §A（功能域分组）+ §D（完整 skills 索引）

### 主人想看自进化机制怎么工作（10 分钟）→
读 `02_功能与流程视角.md` §B.3（Dream Cycle 流程）+ `03_数据与交互视角.md` §F（Dream Cycle 数据流）

---

## 4. Agent 读取协议

如果 Agent 在主人后续会话中需要查阅这套分析：

1. **先读本 index 的 §1-§3**——确认这次分析的范围、目的、5 份产出的分工
2. **按主人提问的指向**——用 §3 的快速导引定位到具体视角的具体章节
3. **避免全文加载**——5 份加起来 17 万字符，会爆 context；按章节定向 read
4. **引用源码时**——所有视角文件都标了 `(参见 src/xxx.ts:line)` 格式的行号，可以回溯到 `/tmp/gbrain-src/`（如已删则需重新 clone）

---

## 5. 关键发现 TOP 12（跨视角合并）

1. **GBrain 本质是 Garry 个人生产配置的开源化**——所有数字（17K pages / 21 cron / P@5 49.1%）都来自他本人真实使用。主人无法复制这种"信任叙事"
2. **GStack + GBrain + OpenClaw 铁三角**——GBrain 商业模式不能孤立看，主人不具备这三层支撑（YC 岗位 + 生态绑定 + 真实生产证据），不能盲抄"纯开源"
3. **3 件套引擎**：50 个 skill 看似多，真正核心只有 `signal-detector + brain-ops + dream cycle`，主人起步抄这三件套就够
4. **Skillify（procedural memory）是主人最稀缺的差异化**——市面 90% Agent 记忆系统只做记事实，GBrain 做记"怎么做"。主人若不抓，就跟 RAG-only 项目同质化
5. **Markdown 为真，DB 为索引**——所有真相住在 .md 文件，Postgres 只是派生 cache。主人项目极推荐照搬这条架构契约
6. **自连线 90% 零 LLM**——靠 3 个静态机制叠加（wikilink 正则 + 11 条 frontmatter 规则 + 4 条 verb 正则），精度 70-94%。这是知识图谱可规模化的基础
7. **takes vs facts 二分**——「主人本人说的」必须和「主人引用的别人观点」分开存。`holder` 字段是核心创新，不能省
8. **Hybrid ranking 完整公式**：RRF(K=60) + 0.7 RRF + 0.3 cosine 重排 + 三轴增权（backlink × 0.05·ln / salience × 0.15·ln / recency 按 slug 前缀 halflife）。5 行 Python 直译
9. **Dream cycle 是生产级样板**——两层模型降本（Haiku 过滤 + Sonnet 合成）+ 冷却 + 沙箱白名单 + 隐私正则前置。Letta/MemGPT/Mem0 都没做到这个工程深度
10. **PGLite ↔ Supabase 不是双方言抽象，是同一份 PG WASM**——主人 Python 没有等价物，最接近 DuckDB 但不是 PG 方言；要靠 schema 一致性 + 一行迁移脚本保证
11. **dispatch.ts 是契约优先架构范本**——279 行函数 + 五字段 opts 收口四种 transport。Python 50 行可复刻
12. **Minions 4375 行对个人项目过度工程**——用 Celery / pgmq 即可，**唯一值得偷**：crash-resumable LLM loop（messages + tool_executions 持久化）

---

## 6. 必看踩坑预警（Garry 真金白银教训）

主人项目立项前**必须**逐项确认对策（详见 `05_借鉴价值评估.md` §6）：

- ⚠️ Holder ≠ Subject 混淆
- ⚠️ 大规模 embedding 成本（100K 页 $361）
- ⚠️ 多端并发写入冲突
- ⚠️ LLM 自我消费 loop
- ⚠️ FTS + 向量召回都不够（缺重排器）
- ⚠️ Always-on 用贵模型烧钱
- ⚠️ 同名实体歧义

---

## 7. 主人需要立刻决策的 3 个产品问题

> 这 3 条是 `05_借鉴价值评估.md` §8.3 提出的——v0.1 启动前必须想清楚

🔴 **1. 商业模式**：主人不是 YC 总裁，纯开源活不下来。先想清楚未来变现路径（企业版 / SaaS / 配套硬件 / 知识库撮合）

🔴 **2. 技术栈**：Python 还是 TS？强烈建议 Python，但要面对 PGLite 没有 Python 等价物的现实（最接近 DuckDB 但不是 PG 方言）

🔴 **3. 范围边界**：`Agent记忆与自进化` vs `知识存储与自进化引擎` vs `知识库` 三个项目是合并、上下游、还是各自独立？（AILab 矩阵 §0.1 当前未登记 Agent记忆与自进化）

---

## 8. 后续工作建议

完成本次分析后，主人若要进入新方向项目的 S1 / S2 阶段：

1. **召开"GStack 八问"** 自检会话（gstack skill），把新方向的 8 个问题逐条过一遍
2. **20 条原则交叉检验**（`方向探索/_playbook/AI时代20条基本原则.md`）
3. **设计 v0.1 PRD**——基于 `05_借鉴价值评估.md` §7 的 v0.1 清单
4. **登记 AILab 矩阵 §0.1**——新增 `Agent记忆与自进化` 项目条目（如确认为独立新方向）
5. **建立项目 CLAUDE.md（L2）**——按产品研发型项目流程（`_shared/产品研发型.md`）

---

## 9. 源码留存

- `/tmp/gbrain-src/`：浅 clone 的 gbrain master 分支（系统重启后可能丢失，按需重新 `git clone --depth 1 https://github.com/garrytan/gbrain.git`）
- 分析过程中**未拷贝任何 gbrain 源码到主人仓库**（避免许可证污染）—— 所有引用都是 file:line 形式

---

*由小昭奴婢编排：4 个 subagent 并行通读源码 → 主 session 整合 + 出借鉴评估 + 渲染 HTML。*
