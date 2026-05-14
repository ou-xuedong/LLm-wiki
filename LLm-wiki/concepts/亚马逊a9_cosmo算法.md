---
title: 亚马逊A9
created: 2026-04-22
updated: 2026-04-22
type: concept
tags:
  - #概念
  - #电商
  - #算法
  - #亚马逊
---

# 亚马逊A9


## 关联

**上位概念**：[[亚马逊投流决策助手_跨境电商AI决策]]
**相关概念**：[[EBM消费决策模型]], [[Cialdini影响力六原则]], [[Agent引擎优化_AEO]], [[跨境电商AI决策助手破局洞察]]

# 🧠 亚马逊A9_COSMO算法

## 1. 定义与核心原理

**A9** 是亚马逊自有的商品搜索排序算法名（源于 A9.com 子公司），决定关键词搜索结果页（SERP）的商品排位。**COSMO** 是亚马逊于 2024 年公开（KDD 2024）的新一代常识知识图谱排序框架，从"关键词匹配"升级为"意图-属性-场景"三元组预测。

**A9 核心排序因子（乘积模型）**：
```
Rank ∝ CTR × CVR × 转化金额 × 相关性(词×Listing) × 历史表现 × 库存 × 履约 × 评论权重
```

**COSMO 的关键升级**：
- 从"关键词-商品"二元匹配 → `user intent × product attribute × scenario` 三元推理
- 使用 LLM 生成常识知识图谱（如"露营 → 需要便携 → 可折叠"）
- 对长尾+场景化查询显著提升相关性

## 2. 关键技术路线与变体

**三大广告产品与算法耦合**：

| 广告类型 | 英文 | 触发场景 | 算法耦合点 |
|---|---|---|---|
| 搜索结果广告 | SP (Sponsored Products) | 关键词搜索/ASIN 定位 | CTR/CVR 直接反馈 A9 自然排位 |
| 品牌广告 | SB / SBV (Sponsored Brands Video) | 搜索页顶部品牌位 | 拉品牌词搜索量、导流品牌店铺 |
| 展示广告 | SD (Sponsored Display) | 站内+站外受众再营销 | 竞品 ASIN 定位、兴趣人群 |

**心理学-算法映射**：
- 主图/标题优化 CTR ← System 1 直觉触发
- 五点/评论/A+ 优化 CVR ← System 2 理性验证
- 飞轮效应：广告出单 → 评论累积 → CVR 提升 → 自然排位上升 → ACOS 下降

## 3. 行业应用场景

**三漏斗战术分层**：
- **TOFU**：大词/品类词（SB Video / SD）— 激活需求，对应 EBM"问题识别"
- **MOFU**：长尾/属性词（SP 宽泛）— 支持比较，对应"方案评估"
- **BOFU**：品牌词/竞品 ASIN（SP 精准/防御）— 拦截收割，对应"购买决策"

**运营高手的隐性知识** = 心理触发点识别 + 飞轮节点判断 + 竞价博弈（正是 [[亚马逊投流决策助手_跨境电商AI决策]] 的核心捕获对象）

## 4. 代表性论文/项目

- **COSMO 论文**：*COSMO: A Large-Scale E-commerce Common Sense Knowledge Generation and Serving System at Amazon* (KDD 2024)
- **官方 SDK**：`amazon-ads-api`、`python-amazon-ads`
- **开源生态**：`helium10` 关键词反查、`amazon-scraper` 评论 NLP
- **竞价优化**：Thompson Sampling / Multi-armed Bandit 在开源社区的应用
- **代表玩家**：Linkfox、Helium 10、Jungle Scout、Pacvue、Perpetua

## 5. 争议与开放问题

- **黑盒性**：亚马逊从未公开权重，运营依靠经验与 A/B 反推
- **广告权重挤占自然流量**：SP 广告位扩张压缩自然排名价值
- **AI Agent 时代的算法意义**：买方为 Agent 时，官方排序权重下降，Agent 可能重排甚至忽略
- **COSMO 对长尾卖家的门槛**：结构化数据能力不足的卖家被边缘化
- **与 [[Agent引擎优化_AEO]] 的长期替代关系**：A9/COSMO 是"人类注意力排序"，AEO 是"Agent 证据排序"，后者可能反向重塑前者
