# Wiki Log

> 所有 wiki 操作的时序记录。Append-only。
> 格式：`## [YYYY-MM-DD] action | subject`
> 操作类型：init、ingest、update、query、lint、create、archive、delete
> 文件超过 500 条时轮换：renamed to log-YYYY.md, start fresh.

## [2026-06-04] cron_refresh | 资本对接洞察自动刷新：新建 3（Agent访问控制成为Agent基础设施新需求、AI在法律领域超越法学教授、AI蠕虫可攻击任意联网设备）；更新 0。跳过 12 条（GitHub repo handle ×7、信息不足 ×5：DDR5硬件新闻/Piramidal招聘帖/Roku非AI/Franz低信息/WallieV2信息不足）。
## [2026-05-22] cron_refresh | 资本对接洞察自动刷新：新建 6（阶跃星辰_大模型创业公司、NanoCo_企业级AI代理、Sentinel_AI副驾驶应用、酷哇科技具身智能机器人规模化落地、新石器NeoClaw无人车管理效率跃升、36氪xPureblueAI_GEO品牌推荐力名册）；更新 1（首届人工智能邀请赛颁奖暨2026_OPC创业大赛启动）。跳过 18 条（RSS标题切片/GitHub repo handle/无具体机构名/信息不足/假阳性.git匹配）。
## [2026-05-19] cron_refresh | 资本对接洞察自动刷新：新建 3（第四届中国AIGC产业峰会_2026、首届人工智能邀请赛颁奖暨2026_OPC创业大赛启动、番茄小说推动AI动漫上院线）；更新 1（Sierra_对话式AI客服支持）。跳过 22 条（RSS标题切片/GitHub repo handle/信息不足/假阳性.git匹配）。
- 新增 raw：`raw/articles/机智流-从SFT到继续预训练-2026.md`
- 新增 entity：`entities/kols/李剑锋_机智流_大模型微调讲师.md`
- 新增 concept：`concepts/继续预训练_continued-pretraining.md`
- 更新：index.md
- Domain: 个人全量知识库
- Structure: SCHEMA.md, index.md, log.md, raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/, summaries/
- 标签体系：投资、创业、技术、健康、生活、人物、组织、概念、记录

## [2026-05-14] lint | 首次全量维护
- 执行：坏链修复(255→0)、stub补页(115)、index重建(428页)、sha256修复、taxonomy扩展
- 孤儿页: 182（预期，迁移后遗症，无需处理）
- 超长页面: 5个（需人工拆分，见lint报告）

## [2026-05-15] ingest | 全自动开发！一战封神！GLM5.1（数字游牧人/B站）
- 新增 raw：`raw/transcripts/数字游牧人-glm5.1全自动开发-2026-04-08.md`（字幕全文）
- 更新 entity：`entities/vcs/智谱_ai_z基金_大模型生态cvc.md`（GLM-5.1产品信息）

## [2026-05-15] ingest | 数字游牧人·GLM5全自动开发系统（BV1zZcYz1EMy）
- 新增 raw：`raw/transcripts/数字游牧人-glm5全自动开发系统-2026-02-12.md`（字幕全文）
- 主题：10小时全自动开发，task.json+progress.txt+cloud.md三文件循环

## [2026-05-15] ingest | 数字游牧人·ClaudeCode保姆级速成（BV1kX546QEjG）
- 新增 raw：`raw/transcripts/数字游牧人-保姆级ClaudeCode速成-2026-05-11.md`（字幕全文）
- 主题：Claude Code=Harness层，Kimi K2.6性价比最优，MCP/Skills/Context管理

## [2026-05-15] ingest | 数字游牧人·如何用AI深度学会任何领域（BV1Sh516SEx1）
- 新增 raw：`raw/transcripts/数字游牧人-如何用AI深度学会任何领域-2026-05-13.md`（字幕全文）
- 主题：豆包专家模式五步调研法，Harness思维，任务切分替代长提示词

## [2026-05-15] ingest | 锦秋基金·AI的1万亿美元账单
- 更新 entity：`entities/vcs/锦秋基金_字节系极客ai基金.md`（投资框架扩充：智力工业化+四层系统级机会）
- 新增 entity：`entities/vcs/锦秋基金.md`（完整条目镜像）
- 主题：1万亿美元买"智力的工业化"，下一代智能系统四层框架（算力/消费电子/具身智能/AI应用）

