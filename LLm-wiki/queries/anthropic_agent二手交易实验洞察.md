---
title: Anthropic
created: 2026-04-30
updated: 2026-04-30
type: query
tags:
  - #洞察
  - #Agent
  - #AI经济
  - #Anthropic
  - #模型能力
  - #组织模式
confidence: low
---

# Anthropic


## 关联

**相关概念**：[[Agent协商层]], [[零点击消费]], [[Service_as_a_Software]], [[Anthropic自举飞轮_Claude Code开发Claude Code]]

# 💡 Anthropic Agent 二手交易实验洞察（Project Deal）

## 核心结论

Anthropic 内部实验证明：AI agent 已能独立完成二手市场全流程交易（挂牌→报价→还价→成交→线下交割），且强模型（Opus）相比弱模型（Haiku）在议价中具有系统性优势——当 agent 开始替人谈判，模型能力将直接转化为议价能力。

**同期重要背景**：Anthropic 在 2026 年 2-3 月的 52 天内推出 74 项功能（平均每天 1.4 个），Claude Code 团队将产品功能交付周期从六个月缩短到一天。这种速度源于其独特的**自举飞轮**和组织机制（见关联概念）。

## 详细分析

### 实验设计

69 名 Anthropic 员工参与，每人给 Claude 100 美元名义预算寄售物品。实验分四轮：
- **Run A/D**：全部用 Opus 4.5
- **Run B/C**：Opus/Haiku 混合（50% 概率分到 Haiku）
- A/B 在公开 Slack 频道，C/D 在私下研究频道
- 只有 Run A 最后要求实物线下交割（参与者事先不知情）

### 核心数据

| 指标 | Opus | Haiku | 差异 |
|---|---|---|---|
| 混合市场额外成交数 | — | — | +2.07 笔/人 |
| 物品售出概率 | — | — | +6.63% |
| 同物品多卖价格 | — | — | +$3.64 |
| 公平性评分 | 4.053 | 4.045 | ≈ |

**最高价实例**：实验室培育红宝石，Opus 卖 $65，Haiku 卖 $35；坏折叠自行车，同一买卖方，Opus 卖 $65，Haiku 卖 $38。

**模型差距定价效应**：Opus seller × Haiku buyer 均成交价 $24.18；Opus seller × Opus buyer 均成交价 $18.63。强弱模型组合会系统性推高价格。

### 关键洞察

1. **主观体验与客观结果脱节**：尽管 Opus 客观数据显著优于 Haiku，但用户满意度几乎无差异（5.14 vs 4.82），且 61 名参与者中只有 17 人偏好 Opus 轮，11 人偏好 Haiku。**最危险的不平等，是你不知道自己少拿了。**

2. **强硬提示词对交易结果影响有限**：强硬卖家的额外收益主要来自一开始就把要价报得更高，而非谈判策略本身。模型能力 > 提示词技巧。

3. **agent 处理非价格维度**：滑雪板重复购买、买 19 个乒乓球送自己、卖出「和狗相处一天」体验——agent 捕捉并放大了人类的审美、社交和临时偏好。

4. **实验边界**：仅 Anthropic 内部，金额低，同事信任背书，无真实支付/物流/售后。尚不能推论到开放市场。

### 组织背景补充（2026-04-30 新增）

Cat Wu 在 Lenny's Podcast（2026-04-23）披露的数据：
- Claude Code 团队将产品功能交付周期从 **六个月缩短到一天**
- 2026年2-3月：**52天内推出74项功能**，平均每天1.4个
- 速度机制：研究预览模式 + 常青发布室 + 全员技术背景 + Side Quest 机制
- 这种速度的本质是**自举飞轮**：Claude Code 开发 Claude Code，工程师59%日常工作由其完成，平均生产力提升50%

## 数据与证据

- 186 笔真实成交，$4010 总交易额（Run A）
- 四轮合计 782 笔成交，均价 $20.05，中位数 $12
- 公平性评分（1-7 量表）：Opus 4.053，Haiku 4.045
- 用户满意度（1-7）：Opus 5.14，Haiku 4.82

## 行动建议

1. **AI 消费决策赛道**：若做 AI shopping agent/比价 agent，需正视模型能力差距带来的议价不对称，头部模型厂商可能形成定价优势
2. **平台机会**：类似「Agent 版闲鱼」的平台，如果接入强模型 agent 和弱模型 agent 混合市场，需要设计机制防止模型质量差距被价格机制放大
3. **企业采购/广告竞价**：强模型 agent 替企业谈判的系统性优势会催生「谁用更强模型谁多赚」的商业逻辑
4. **AI 投流 Agent**：主人方向的投流决策 Agent，其核心价值将高度依赖于模型在广告投放场景下的真实 ROI 差距——参考 Project Deal 揭示的"模型能力→议价能力"系统性转化

## 信息来源

- 文章原文（HR私董会）：「超级干货！值得收藏！Anthropic的组织密码：从6个月到1天，这家AI公司如何重新定义"快"？」2026-04-30
- Project Deal 官方页面：https://www.anthropic.com/features/project-deal
- Project Deal 研究论文：https://cdn.sanity.io/files/4zrzovbb/website/85767420dd844c74fbbaaeb929ee9a399a9691bb.pdf
- Project Vend：https://www.anthropic.com/research/project-vend-1
- Cat Wu 引用来源：Lenny's Podcast（2026-04-23）
