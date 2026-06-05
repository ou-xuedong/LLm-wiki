#!/usr/bin/env python3
"""把 对外说明_CN.md / 对外说明_EN.md 渲染成单页 对外说明.html (中英切换)。

零依赖, 只认本目录两份一页纸用到的 markdown 构件。
用法:  python3 build_html.py   →  生成/刷新 对外说明.html
"""
import os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))


def md_to_html(md):
    out, in_ul = [], False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def inline(t):
        t = html.escape(t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
        return t

    for raw in md.splitlines():
        line = raw.rstrip()
        # HTML 注释 = 待补充占位, 渲染成醒目徽章
        m = re.search(r"<!--\s*(.*?)\s*-->", line)
        if m:
            close_ul()
            out.append(f'<div class="todo">⚠ 待补充：{html.escape(m.group(1))}</div>')
            continue
        if not line.strip():
            close_ul()
            continue
        if line.startswith("### "):
            close_ul(); out.append(f"<h3>{inline(line[4:])}</h3>"); continue
        if line.startswith("## "):
            close_ul(); out.append(f"<h2>{inline(line[3:])}</h2>"); continue
        if line.startswith("# "):
            close_ul(); out.append(f"<h1>{inline(line[2:])}</h1>"); continue
        if line.startswith("> "):
            close_ul(); out.append(f"<blockquote>{inline(line[2:])}</blockquote>"); continue
        if line.strip() == "---":
            close_ul(); out.append("<hr>"); continue
        if line.lstrip().startswith("- "):
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(line.lstrip()[2:])}</li>"); continue
        close_ul(); out.append(f"<p>{inline(line)}</p>")
    close_ul()
    return "\n".join(out)


def read(name):
    p = os.path.join(HERE, name)
    if not os.path.exists(p):
        return f"<p>缺少 {name}</p>"
    with open(p, encoding="utf-8") as f:
        return md_to_html(f.read())


PAGE = """<!doctype html>
<html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>卟卟鸡 · 对外说明</title>
<style>
:root{{--ink:#1a1a2e;--mut:#6b7280;--line:#e5e7eb;--accent:#c2410c;--bg:#faf8f5}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.7 -apple-system,"PingFang SC","Microsoft YaHei",sans-serif}}
.wrap{{max-width:760px;margin:0 auto;padding:32px 22px 80px}}
.tabs{{position:sticky;top:0;background:var(--bg);padding:14px 0;
  display:flex;gap:8px;border-bottom:1px solid var(--line);margin-bottom:8px}}
.tab{{flex:1;padding:10px;border:1px solid var(--line);background:#fff;border-radius:10px;
  text-align:center;cursor:pointer;font-weight:600;color:var(--mut)}}
.tab.on{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.doc{{display:none}} .doc.on{{display:block}}
h1{{font-size:1.7rem;margin:.8em 0 .3em;line-height:1.3}}
h2{{font-size:1.25rem;margin:1.6em 0 .4em;padding-top:.4em;border-top:1px solid var(--line)}}
h3{{font-size:1.05rem;margin:1.1em 0 .3em}}
blockquote{{color:var(--mut);font-size:.9rem;border-left:3px solid var(--accent);
  margin:1em 0;padding:.4em 0 .4em 14px;background:#fff}}
ul{{padding-left:1.3em}} li{{margin:.25em 0}}
code{{background:#f0ede8;padding:1px 6px;border-radius:5px;font-size:.9em}}
strong{{color:var(--accent)}}
hr{{border:0;border-top:1px solid var(--line);margin:1.4em 0}}
.todo{{background:#fff7ed;border:1px dashed var(--accent);color:var(--accent);
  border-radius:10px;padding:10px 14px;margin:.8em 0;font-size:.9rem}}
.foot{{margin-top:40px;color:var(--mut);font-size:.8rem;text-align:center}}
</style></head><body><div class="wrap">
<div class="tabs">
  <div class="tab on" onclick="sw('cn')">中文</div>
  <div class="tab" onclick="sw('en')">English</div>
</div>
<div id="cn" class="doc on">{cn}</div>
<div id="en" class="doc">{en}</div>
<div class="foot">由 build_html.py 从 md 源渲染 · 改完 md 重跑脚本即刷新</div>
</div>
<script>
function sw(x){{for(const d of document.querySelectorAll('.doc'))d.classList.toggle('on',d.id===x);
const t=document.querySelectorAll('.tab');t[0].classList.toggle('on',x==='cn');t[1].classList.toggle('on',x==='en');}}
</script></body></html>"""


def main():
    out = PAGE.format(cn=read("对外说明_CN.md"), en=read("对外说明_EN.md"))
    dst = os.path.join(HERE, "对外说明.html")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"✅ 已生成 {dst}")


if __name__ == "__main__":
    main()
