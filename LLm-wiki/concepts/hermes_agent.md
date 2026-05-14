---
title: Hermes
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - #概念
  - #AgentInfra
  - #AI智能体
confidence: low
---

# Hermes


## 关联

**上位概念**：[[Agent|Agent Infra]]
**相关概念**：[[OpenClaw|OpenClaw]], [[gbrain_ai记忆系统|gbrain_ai记忆系统]], [[human-like_memory_类人记忆插件|human-like_memory_类人记忆插件]]
**关键人物**：[[Nous-Research|Nous Research]]

# 🧠 Hermes Agent

## 1. 定义与核心原理
**Hermes Agent** 是由著名开源 AI 研究机构 [Nous Research](https://nousresearch.com/) 开发的一款强调“自我进化（self-improving）”和“学习闭环（learning loop）”的 AI 智能体框架。
与普通一次性响应的 AI 助手不同，Hermes Agent 的设计初衷是成为一个“随用户共同成长的系统”。它可以从日常交互中自动创建和提取技能（Skills），在使用中不断优化这些技能，周期性地提示自己将临时记忆固化到持久层，并通过大模型摘要及 FTS5（SQLite 全文检索）在跨会话中回忆历史对话与用户画像。

## 2. 关键技术路线与变体
- **无缝对接多模型生态**：后端随意切换，支持 Nous Portal、OpenRouter (200+模型)、OpenAI、Hugging Face 或本地端点。
- **无处不在的多端网关 (Messaging Gateway)**：自带丰富的终端适配能力。Agent 的核心进程可以部署在云端闲置服务器（或 5 美元/月的低成本 VPS 上），而用户可通过 Telegram、Discord、Slack、WhatsApp 或 Signal 与其跨平台交流。
- **动态记忆与技能生成 (Procedural Memory & Skills Hub)**：
  - 基于经验自动生成代码或逻辑脚本（Skills）。
  - 使用 Honcho 系统进行辩证式的用户建模（Dialectic User Modeling），随时间推移刻画极深度的用户画像。
- **多范式部署与沙盒隔离**：后端支持 Local、Docker、SSH、Daytona、Modal 等 6 种终端后端，甚至在云端无负载时自动休眠。
- **OpenClaw 生态平移**：原生支持从 OpenClaw 框架的无损一键迁移（`hermes claw migrate`），可以继承 OpenClaw 的 `SOUL.md`、`MEMORY.md`、用户审批白名单以及多平台通讯配置。

## 3. 行业应用场景
- **极客向的全天候个人数字管家**：利用内置的 Cron 调度功能，在无人值守时生成每日简报、夜间备份日志或每周审计。
- **复杂任务流的代理派遣**：支持孵化隔离的子代理（Subagents）进行并行数据抓取或分析，主 Agent 则负责指挥与结果汇总。
- **RL (强化学习) 研究基座**：系统支持批量轨迹生成（Trajectory Generation）与压缩，非常适合研究者为下一代“工具调用（Tool-Calling）模型”制造对齐数据。

## 4. 代表性论文/项目
- **GitHub 官方仓库**: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **Skills Hub**: [agentskills.io](https://agentskills.io/) (支持共享开放技能标准的生态)

## 5. 争议与开放问题
- **学习回环的失控与脏数据**：智能体自我创建的技能和提取的用户偏好，在未经人类强干预时可能产生幻觉固化，形成“偏见飞轮”。
- **多平台安全管控**：将底层沙盒环境通过公共即时通讯软件（如 Telegram/WhatsApp）的网关直接暴露给用户，如果鉴权与指令白名单漏配，容易产生社会工程学或终端被黑客接管的风险。
