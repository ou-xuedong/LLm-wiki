# AILab 项目规则

> 本文件为 AILab 目录的项目级规则，与 `~/CLAUDE.md`（人格 + 工作准则）叠加生效。
> 优先级：当下指示 > 本文件 > `~/CLAUDE.md` > 系统默认。

---

## 规则一：HTML 报告的「术语悬停注释」（强制）

凡是生成 **HTML 格式的报告**，对读者可能不懂的词，一律加**悬停/点击即显的注释**，目标是「小白一眼看明白，不打断阅读」。

### 1. 哪些词要注释

只要"需要上下文才能理解"，就注释。常见类型：

- **专业术语**：如 强化学习、向量数据库、过拟合
- **专有名词**：产品名、项目名、公司/机构、关键人物（如 Transformer、MoE、Boris）
- **英文缩写 / 简称**：如 RAG、LLM、RLHF、SOTA、API、QPS
- **数学公式 / 符号**：如 ∇、Σ、softmax、L2 正则
- **行业黑话 / 隐喻**：如 涌现、对齐、蒸馏、幻觉
- **数值 / 单位的言外之意**：如 7B（70 亿参数）、128K 上下文

判断标准：**一个非本领域的聪明人，看到这个词会不会卡一下？** 会，就注释。

### 2. 注释怎么写

- **一句话讲清**，控制在 30 字内，白话优先，不用术语解释术语
- 缩写先给**全称**，再给**一句人话**：`RAG = 检索增强生成，先查资料再回答，减少瞎编`
- 公式给**直觉含义**，不堆推导：`softmax = 把一组数变成加起来等于 1 的概率`
- **同一术语在同一篇里只注释首次出现**，后续不重复，避免啰嗦

### 3. 怎么实现（默认标准）

- **纯 HTML + CSS 自包含**，不依赖外部 JS 库 / CDN，保证离线和断网可看
- 被注释的词加**虚线下划线 + 问号/浅色**等视觉提示，让读者知道"这里能点/能悬停"
- ⚠️ **必须兼容手机**：手机没有鼠标悬停 → 注释要能**点击 / 轻触触发**，不能只靠 `:hover`
- 注释气泡不要遮住正文关键内容，超出屏幕要自动换行、不横向溢出

### 4. 推荐写法（可直接复用）

用 `<abbr>` 语义标签 + 自定义 tooltip，桌面悬停、手机点击都生效：

```html
<style>
  .term {
    border-bottom: 1px dashed #888;
    cursor: help;
    position: relative;
  }
  .term::after {
    content: attr(data-tip);
    position: absolute;
    left: 0; top: 130%;
    width: max-content; max-width: 260px;
    padding: 8px 10px;
    background: #222; color: #fff;
    font-size: 13px; line-height: 1.5;
    border-radius: 6px;
    white-space: normal;
    opacity: 0; pointer-events: none;
    transition: opacity .15s;
    z-index: 10;
  }
  /* 桌面：悬停显示；手机：点击聚焦显示 */
  .term:hover::after,
  .term:focus::after { opacity: 1; }
</style>

<!-- tabindex 让手机点击也能触发 -->
<span class="term" tabindex="0"
      data-tip="RAG = 检索增强生成，先查资料再回答，减少模型瞎编">RAG</span>
```

> 报告较长时，可统一在 `<head>` 放一份上述样式，正文只写 `<span class="term">` 即可。

---

## 规则二：HTML 报告的「护眼视觉」（强制）

凡是生成 **HTML 格式的报告**，视觉上一律白色底、护眼舒服，目标是「长时间看不累、手机桌面都顺眼」。

### 1. 底色与文字

- **白色或接近白的浅底**（如 `#fff` / `#fafafa`），不用纯黑底、不用刺眼高饱和背景
- 正文文字用**深灰而非纯黑**（如 `#222` / `#333`），降低对比刺激
- 正文字号**不小于 16px**，行高 **1.6~1.8**，段落留白充足

### 2. 排版与配色

- 正文宽度控制在 **680~760px**，两侧留白，不顶满屏幕
- 配色克制，强调色少量点缀，不用大面积高饱和色块
- 字体优先系统无衬线（`-apple-system, "PingFang SC", "Microsoft YaHei", sans-serif`）

### 3. 推荐基样式（可直接复用）

```html
<style>
  body {
    background: #fafafa;
    color: #333;
    font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 16px;
    line-height: 1.7;
    max-width: 720px;
    margin: 0 auto;
    padding: 24px 18px;
  }
  h1, h2, h3 { color: #222; line-height: 1.3; }
  p { margin: 0.8em 0; }
</style>
```
