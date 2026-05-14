# Wiki Log

> 所有 wiki 操作的时序记录。Append-only。
> 格式：`## [YYYY-MM-DD] action | subject`
> 操作类型：init、ingest、update、query、lint、create、archive、delete
> 文件超过 500 条时轮换：renamed to log-YYYY.md, start fresh.

## [2026-05-14] ingest | 机智流《从SFT到继续预训练》
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
- 更新：index.md、SCHEMA.md、raw/articles/机智流-从SFT到继续预训练-2026.md

