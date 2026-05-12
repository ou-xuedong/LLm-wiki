#!/usr/bin/env python3
"""
GBrain 深度分析报告 HTML 渲染器
把 6 份 markdown 渲染成单文件 HTML（暗色主题 + mermaid + 左侧 TOC）

用法：
  cd /Users/ouxuedong/Desktop/AILab/Agent记忆与自进化/Raw/GBrain分析
  python3 _render_html.py

依赖：仅标准库 + 浏览器加载 CDN 的 marked.js / mermaid.js / highlight.js
"""
from pathlib import Path
import html as html_lib
import re
import datetime

base = Path(__file__).parent.resolve()
files = [
    ("00", "00_index.md",        "📚 索引导引",       "⭐⭐⭐"),
    ("01", "01_业务与用户视角.md", "🎯 业务与用户",     "⭐⭐"),
    ("02", "02_功能与流程视角.md", "🔧 功能与流程",     "⭐⭐"),
    ("03", "03_数据与交互视角.md", "💾 数据与交互",     "⭐⭐⭐"),
    ("04", "04_技术落地与运维视角.md", "🛠️ 技术落地与运维", "⭐⭐"),
    ("05", "05_借鉴价值评估.md", "⭐ 借鉴价值评估",   "⭐⭐⭐"),
]

# 读所有 markdown
sections = []
for sid, fname, title, importance in files:
    content = (base / fname).read_text(encoding="utf-8")
    # 转义 </script> 防止破坏 HTML
    content = content.replace("</script>", "<\\/script>")
    sections.append((sid, title, importance, content))

# 生成 markdown <script> 块
md_scripts = "\n".join([
    f'<script type="text/markdown" id="md-{sid}">\n{content}\n</script>'
    for sid, title, importance, content in sections
])

# 生成 TOC nav
toc_items = "\n".join([
    f'    <a href="#view-{sid}" class="toc-item" data-view="{sid}">'
    f'<span class="toc-imp">{importance}</span>'
    f'<span class="toc-title">{title}</span></a>'
    for sid, title, importance, _ in sections
])

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GBrain 深度分析报告 — Agent 记忆与自进化方向设计输入</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-dark.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11/styles/github-dark.min.css">
<style>
* {{ box-sizing: border-box; }}
html, body {{
  margin: 0; padding: 0;
  background: #0d1117;
  color: #c9d1d9;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", "Segoe UI", sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}}

/* 布局 */
.layout {{
  display: flex;
  min-height: 100vh;
}}

/* 左侧 TOC */
#sidebar {{
  width: 280px;
  background: #161b22;
  border-right: 1px solid #30363d;
  padding: 24px 20px;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  flex-shrink: 0;
}}
#sidebar h2 {{
  margin: 0 0 4px 0;
  font-size: 18px;
  color: #f0f6fc;
}}
#sidebar .subtitle {{
  margin: 0 0 24px 0;
  font-size: 12px;
  color: #8b949e;
}}
#sidebar nav {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}
.toc-item {{
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 6px;
  color: #c9d1d9;
  text-decoration: none;
  font-size: 14px;
  border: 1px solid transparent;
}}
.toc-item:hover {{
  background: #1f242c;
  border-color: #30363d;
}}
.toc-item.active {{
  background: #1f6feb22;
  border-color: #1f6feb;
  color: #58a6ff;
}}
.toc-imp {{
  font-size: 10px;
  color: #ffa657;
  flex-shrink: 0;
  width: 50px;
}}
.toc-title {{
  flex: 1;
}}

.sidebar-meta {{
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #30363d;
  font-size: 11px;
  color: #8b949e;
  line-height: 1.8;
}}
.sidebar-meta b {{ color: #c9d1d9; }}

/* 主内容 */
main {{
  flex: 1;
  padding: 32px 48px;
  max-width: calc(100% - 280px);
  overflow-x: hidden;
}}

.report-header {{
  border-bottom: 1px solid #30363d;
  padding-bottom: 24px;
  margin-bottom: 32px;
  background: linear-gradient(135deg, #1f6feb15 0%, #f7816615 100%);
  padding: 24px;
  border-radius: 8px;
  border: 1px solid #30363d;
}}
.report-header h1 {{
  margin: 0 0 8px 0;
  font-size: 28px;
  color: #f0f6fc;
}}
.report-header .meta {{
  color: #8b949e;
  font-size: 13px;
  margin: 4px 0;
}}
.report-header .tag {{
  display: inline-block;
  padding: 2px 10px;
  background: #1f6feb22;
  color: #58a6ff;
  border: 1px solid #1f6feb;
  border-radius: 12px;
  font-size: 12px;
  margin-right: 6px;
  margin-top: 8px;
}}

/* markdown body 覆盖 */
.markdown-body {{
  background: transparent !important;
  color: #c9d1d9 !important;
  font-size: 15px !important;
}}
.markdown-body h1 {{
  border-bottom: 2px solid #f78166;
  padding-bottom: 8px;
  color: #f0f6fc;
}}
.markdown-body h2 {{
  border-bottom: 1px solid #30363d;
  color: #58a6ff;
}}
.markdown-body h3 {{ color: #f0f6fc; }}
.markdown-body table {{
  border-collapse: collapse;
  width: 100%;
  margin: 12px 0;
}}
.markdown-body table th, .markdown-body table td {{
  border: 1px solid #30363d;
  padding: 8px 12px;
}}
.markdown-body table th {{
  background: #161b22;
  color: #f0f6fc;
}}
.markdown-body table tr:nth-child(even) {{
  background: #161b2255;
}}
.markdown-body blockquote {{
  border-left: 4px solid #f78166;
  background: #f7816611;
  padding: 8px 16px;
  margin: 12px 0;
  color: #c9d1d9;
}}
.markdown-body code {{
  background: #1f242c !important;
  color: #ffa657 !important;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
}}
.markdown-body pre {{
  background: #0d1117 !important;
  border: 1px solid #30363d;
  border-radius: 6px;
}}
.markdown-body pre code {{
  background: transparent !important;
  color: #c9d1d9 !important;
}}
.markdown-body a {{
  color: #58a6ff;
}}
.markdown-body hr {{
  border: none;
  border-top: 1px solid #30363d;
  margin: 24px 0;
}}

/* 视角分隔 */
article.view-section {{
  margin-bottom: 64px;
  scroll-margin-top: 20px;
}}
article.view-section:not(:last-child)::after {{
  content: "";
  display: block;
  height: 1px;
  background: linear-gradient(90deg, transparent, #30363d, transparent);
  margin-top: 48px;
}}

/* mermaid */
.mermaid {{
  text-align: center;
  background: #0d1117;
  border: 1px solid #30363d;
  border-radius: 6px;
  padding: 16px;
  margin: 16px 0;
}}

/* 视角徽章 */
.view-badge {{
  display: inline-block;
  padding: 2px 10px;
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 12px;
  font-size: 11px;
  color: #8b949e;
  margin-bottom: 16px;
}}
.view-badge .star {{ color: #ffa657; }}

/* loading */
#loading {{
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: #0d1117;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  color: #58a6ff;
  font-size: 14px;
}}

/* 响应式 */
@media (max-width: 900px) {{
  .layout {{ flex-direction: column; }}
  #sidebar {{
    position: relative;
    width: 100%;
    height: auto;
    border-right: none;
    border-bottom: 1px solid #30363d;
  }}
  main {{
    max-width: 100%;
    padding: 24px 16px;
  }}
}}

/* 印刷 */
@media print {{
  #sidebar {{ display: none; }}
  main {{ max-width: 100%; padding: 0; }}
  body {{ background: white; color: black; }}
  .markdown-body {{ color: black !important; }}
}}
</style>
</head>
<body>
<div id="loading">⏳ 渲染中…</div>

<div class="layout">
  <aside id="sidebar">
    <h2>📊 GBrain 分析</h2>
    <p class="subtitle">主人新方向设计输入</p>
    <nav>
{toc_items}
    </nav>
    <div class="sidebar-meta">
      <b>源仓库</b><br>garrytan/gbrain<br>
      <b>分析时间</b><br>2026-05-12<br>
      <b>目标项目</b><br>Agent 记忆与自进化<br>
      <b>规模</b><br>5 份 .md / 2800+ 行<br>
      <b>方法论</b><br>borrow-github-module skill<br>
      <b>生成时间</b><br>{now}
    </div>
  </aside>

  <main>
    <div class="report-header">
      <h1>🧠 GBrain 深度分析报告</h1>
      <div class="meta">研究对象：<a href="https://github.com/garrytan/gbrain" style="color:#58a6ff">garrytan/gbrain</a> · 4 视角 + 1 借鉴评估 · 4 个 subagent 并行通读源码</div>
      <div class="meta">目标：作为主人「Agent 记忆与自进化」新方向的设计输入</div>
      <div>
        <span class="tag">⭐ 17 万字符</span>
        <span class="tag">📊 13 张 mermaid 图</span>
        <span class="tag">🔍 源码级深度</span>
        <span class="tag">🎯 可执行借鉴路线图</span>
      </div>
    </div>

    <div id="content"></div>
  </main>
</div>

{md_scripts}

<script src="https://cdn.jsdelivr.net/npm/marked@11/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/core.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/typescript.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/python.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/sql.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/yaml.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/json.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/highlight.js@11/lib/languages/bash.min.js"></script>

<script>
// 初始化 mermaid（dark theme）
mermaid.initialize({{
  startOnLoad: false,
  theme: 'dark',
  themeVariables: {{
    primaryColor: '#1f6feb',
    primaryTextColor: '#c9d1d9',
    primaryBorderColor: '#30363d',
    lineColor: '#8b949e',
    secondaryColor: '#161b22',
    tertiaryColor: '#0d1117',
    background: '#0d1117',
    mainBkg: '#1f6feb22',
    secondBkg: '#f7816622',
  }},
  flowchart: {{ htmlLabels: true, curve: 'basis' }},
  sequence: {{ useMaxWidth: true }},
}});

// 配置 marked
marked.setOptions({{
  gfm: true,
  breaks: false,
  headerIds: true,
  mangle: false,
}});

// 自定义 renderer：处理 mermaid 代码块
const renderer = new marked.Renderer();
const origCode = renderer.code.bind(renderer);
renderer.code = function(code, lang) {{
  if (lang === 'mermaid') {{
    return '<div class="mermaid">' + code + '</div>';
  }}
  return origCode(code, lang);
}};
marked.use({{ renderer }});

// 渲染所有 markdown
const views = [
  {{ id: '00', title: '📚 索引导引', importance: '⭐⭐⭐' }},
  {{ id: '01', title: '🎯 业务与用户视角', importance: '⭐⭐' }},
  {{ id: '02', title: '🔧 功能与流程视角', importance: '⭐⭐' }},
  {{ id: '03', title: '💾 数据与交互视角', importance: '⭐⭐⭐' }},
  {{ id: '04', title: '🛠️ 技术落地与运维视角', importance: '⭐⭐' }},
  {{ id: '05', title: '⭐ 借鉴价值评估', importance: '⭐⭐⭐' }},
];

const content = document.getElementById('content');
views.forEach(v => {{
  const mdEl = document.getElementById('md-' + v.id);
  if (!mdEl) return;
  const article = document.createElement('article');
  article.id = 'view-' + v.id;
  article.className = 'view-section markdown-body';

  // 视角徽章
  const badge = document.createElement('div');
  badge.className = 'view-badge';
  badge.innerHTML = '视角 ' + v.id + ' · ' + v.title + ' · <span class="star">' + v.importance + '</span>';
  article.appendChild(badge);

  // 渲染 markdown
  const html = marked.parse(mdEl.textContent);
  const wrapper = document.createElement('div');
  wrapper.innerHTML = html;
  while (wrapper.firstChild) article.appendChild(wrapper.firstChild);

  content.appendChild(article);
}});

// 代码高亮
document.querySelectorAll('pre code').forEach(block => {{
  if (block.classList.length > 0) {{
    try {{ hljs.highlightElement(block); }} catch (e) {{}}
  }}
}});

// 渲染 mermaid
mermaid.run({{ querySelector: '.mermaid' }}).catch(err => console.warn('Mermaid:', err));

// TOC 高亮当前章节
const observer = new IntersectionObserver(entries => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      const id = entry.target.id.replace('view-', '');
      document.querySelectorAll('.toc-item').forEach(el => {{
        el.classList.toggle('active', el.dataset.view === id);
      }});
    }}
  }});
}}, {{ rootMargin: '-20% 0px -70% 0px' }});

document.querySelectorAll('.view-section').forEach(s => observer.observe(s));

// 移除 loading
document.getElementById('loading').style.display = 'none';
</script>
</body>
</html>
"""

out_path = base / "GBrain深度分析报告.html"
out_path.write_text(html, encoding="utf-8")
size_kb = out_path.stat().st_size / 1024
print(f"✅ HTML report rendered: {out_path}")
print(f"   size: {size_kb:.1f} KB")
print(f"   open: open '{out_path}'")
