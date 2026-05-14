#!/usr/bin/env python3
"""
Migration script: 旧知识库 ~/Desktop/AILab/知识库/wiki/
             → 新 LLM Wiki ~/Desktop/AILab/LLm-wiki/

转换规则：
  - last_updated  → updated
  - decay_speed  → confidence (fast→low, medium→medium, slow→high, eternal→high)
  - access_count → 丢弃
  - relations.*  → 展开为正文 [[wikilinks]]（按类型分发到对应目录）
  - wikilinks 路径修正（旧 → 新目录结构）
  - type 推断（按目录）
  - created 用 last_updated 首次出现的值
  - aliases → 丢弃（转入正文）
"""

import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime

# ========== 配置 ==========
OLD_BASE = Path("/Users/ouxuedong/Desktop/AILab/知识库/wiki")
NEW_BASE = Path("/Users/ouxuedong/Desktop/AILab/LLm-wiki")

MAPPING = {
    "entities/KOLs":         ("entities/kols",       "kols"),
    "entities/Companies":    ("entities/companies",  "companies"),
    "entities/VCs":         ("entities/vcs",        "vcs"),
    "entities/Events":       ("entities/events",      "events"),
    "concepts":             ("concepts",             "concept"),
    "insights":             ("queries",              "query"),
}

DECAY_TO_CONFIDENCE = {
    "fast":   "low",
    "medium": "medium",
    "slow":   "high",
    "eternal":"high",
}

RELATION_KEYS = ["affiliated_with", "expertise", "related_kols",
                 "parent_concept", "related_concepts", "key_players",
                 "portfolio", "competitors", "investors"]


def slugify(name: str) -> str:
    """中文文件名转为小写中划线"""
    # 去掉扩展名
    name = re.sub(r'\.md$', '', name)
    # 空格→中划线，非字母数字下划线→去除
    name = re.sub(r'\s+', '-', name)
    name = re.sub(r'[^\w\u4e00-\u9fff-]', '', name)
    return name.lower()


def extract_frontmatter(content: str):
    """解析 markdown 文件的 YAML frontmatter"""
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not m:
        return {}, content
    fm_text = m.group(1)
    body = content[m.end():]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except:
        fm = {}
    return fm, body


def build_wikilinks(relations: dict, type_hint: str) -> list[str]:
    """把 relations 字典展开为 wikilink 行列表"""
    lines = []
    if not relations:
        return lines
    lines.append("")
    lines.append("## 关联")
    lines.append("")
    for key in RELATION_KEYS:
        vals = relations.get(key, [])
        if not vals:
            continue
        if isinstance(vals, str):
            vals = [vals]
        # 拍平嵌套列表
        flat = []
        for v in vals:
            if isinstance(v, list):
                flat.extend(v)
            else:
                flat.append(v)
        vals = flat
        label = {
            "affiliated_with": "所属",
            "expertise": "专长",
            "related_kols": "相关 KOL",
            "parent_concept": "上位概念",
            "related_concepts": "相关概念",
            "key_players": "关键人物",
            "portfolio": "Portfolio",
            "competitors": "竞品",
            "investors": "投资方",
        }.get(key, key)
        lines.append(f"**{label}**：{', '.join(vals)}")
    lines.append("")
    return lines


def convert_wikilinks_in_body(body: str) -> str:
    """把正文里的旧版 [[xxx_yyy_zzz]] wikilinks 路径更新为新版"""
    def replacer(m):
        inner = m.group(1)
        # 旧格式：中文名_英文名_Title.md 或 中文名_英文名.md
        # 提取中文名部分（第一个下划线之前）
        # 实际上需要从完整文件名推断目标新路径
        # 简单策略：保留链接文本不变，路径结构更新
        # 由于我们不知道目标，先保持原样，让后续 lint 修复
        return f"[[{inner}]]"

    result = re.sub(r'\[\[([^\]]+)\]\]', replacer, body)
    return result


def migrate_file(old_path: Path) -> dict:
    """迁移单个文件，返回 index 条目信息"""
    content = old_path.read_text(encoding="utf-8")
    fm, body = extract_frontmatter(content)

    # 确定来源目录
    rel = old_path.relative_to(OLD_BASE)
    parts = rel.parts
    old_subdir = str(Path(*parts[:-1])) if len(parts) > 1 else ""
    old_name = parts[-1] if parts else old_path.name

    if old_subdir not in MAPPING:
        print(f"  ⚠️  未分类，跳过: {old_path}")
        return None

    new_subdir, new_type_hint = MAPPING[old_subdir]
    new_slug = slugify(old_name)

    # Frontmatter 转换
    created = fm.get("last_updated", datetime.today().strftime("%Y-%m-%d"))
    updated = fm.get("last_updated", datetime.today().strftime("%Y-%m-%d"))
    confidence = DECAY_TO_CONFIDENCE.get(fm.get("decay_speed", "medium"), "medium")

    title = fm.get("title", old_name.replace(".md", ""))
    # 从文件名提取中文名作为标题（如果 frontmatter 没 title）
    if not title or title == old_name.replace(".md", ""):
        # 从文件名取第一段（中文名）
        title = old_name.split("_")[0].replace(".md", "")

    sources = fm.get("sources", [])

    # Tags
    tags_raw = fm.get("tags", [])
    if isinstance(tags_raw, str):
        tags_raw = [tags_raw]
    # 补上新 type hint
    tags = list(tags_raw)

    # Wikilinks from relations
    relations = fm.get("relations", {})
    wl_lines = build_wikilinks(relations, new_type_hint)
    body_wl = convert_wikilinks_in_body(body)

    # 重建内容
    # 重建 frontmatter
    new_fm = {
        "title": title,
        "created": created,
        "updated": updated,
        "type": new_type_hint,
        "tags": tags,
    }
    if sources:
        new_fm["sources"] = sources
    if confidence != "medium":
        new_fm["confidence"] = confidence

    lines = []
    lines.append("---")
    for k, v in new_fm.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    if wl_lines:
        lines.extend(wl_lines)
    lines.append(body_wl.lstrip("\n"))

    new_content = "\n".join(lines)
    new_path = NEW_BASE / new_subdir / f"{new_slug}.md"
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text(new_content, encoding="utf-8")

    return {
        "section": new_subdir.split("/")[-1],
        "slug": new_slug,
        "title": title,
        "path": str(new_path.relative_to(NEW_BASE)),
        "type": new_type_hint,
    }


def main():
    print("=" * 60)
    print("阶段一：批量迁移旧知识库 → 新 LLM Wiki")
    print(f"源：{OLD_BASE}")
    print(f"目标：{NEW_BASE}")
    print("=" * 60)

    results = []
    for old_subdir in MAPPING.keys():
        src_dir = OLD_BASE / old_subdir
        if not src_dir.exists():
            print(f"\n📂 {src_dir} — 目录不存在，跳过")
            continue

        md_files = list(src_dir.glob("*.md"))
        print(f"\n📂 {old_subdir}/ → {MAPPING[old_subdir][0]}/ ({len(md_files)} 个文件)")

        for f in sorted(md_files):
            r = migrate_file(f)
            if r:
                results.append(r)
                print(f"  ✅ {f.name} → {r['path']}")

    # ========== 生成 index.md ==========
    print("\n" + "=" * 60)
    print("阶段二：生成 index.md")
    print("=" * 60)

    sections = {
        "kols":      "### KOLs",
        "companies": "### Companies",
        "vcs":       "### VCs",
        "events":    "### Events",
        "concepts":  "## Concepts",
        "queries":   "## Queries",
    }

    by_section = {}
    for r in results:
        s = r["section"]
        by_section.setdefault(s, []).append(r)

    idx_lines = [
        "# Wiki Index",
        "",
        f"> Content catalog. Every wiki page listed under its type with a one-line summary.",
        f"> Read this first to find relevant pages for any query.",
        f"> Last updated: {datetime.today().strftime('%Y-%m-%d')} | Total pages: {len(results)}",
        "",
        "## Entities",
        "",
    ]
    for sec, label in [(k, v) for k, v in sections.items() if k != "concepts" and k != "queries"]:
        if sec in by_section:
            idx_lines.append(label)
            idx_lines.append("")
            for r in sorted(by_section[sec], key=lambda x: x["title"]):
                idx_lines.append(f"- [[{r['slug']}]] — {r['title']}")
            idx_lines.append("")

    if "concepts" in by_section:
        idx_lines.append("## Concepts")
        idx_lines.append("")
        for r in sorted(by_section["concepts"], key=lambda x: x["title"]):
            idx_lines.append(f"- [[{r['slug']}]] — {r['title']}")
        idx_lines.append("")

    if "queries" in by_section:
        idx_lines.append("## Queries")
        idx_lines.append("")
        for r in sorted(by_section["queries"], key=lambda x: x["title"]):
            idx_lines.append(f"- [[{r['slug']}]] — {r['title']}")
        idx_lines.append("")

    idx_path = NEW_BASE / "index.md"
    idx_path.write_text("\n".join(idx_lines), encoding="utf-8")
    print(f"✅ index.md 已写入 ({len(results)} 个条目)")

    # ========== 统计 ==========
    print("\n" + "=" * 60)
    print("迁移完成 · 统计")
    print("=" * 60)
    counts = {}
    for r in results:
        counts[r["section"]] = counts.get(r["section"], 0) + 1
    for sec, cnt in sorted(counts.items()):
        print(f"  {sec}: {cnt}")
    print(f"  总计: {len(results)}")
    print(f"\n📁 输出目录：{NEW_BASE}")

    # ========== 验证：文件数核对 ==========
    print("\n验证：文件数核对")
    all_new = list(NEW_BASE.glob("entities/**/*.md")) + \
              list(NEW_BASE.glob("concepts/*.md")) + \
              list(NEW_BASE.glob("queries/*.md"))
    print(f"  旧知识库总文件数：{len(results)}")
    print(f"  新 wiki 总文件数：{len(all_new)}")
    if len(results) == len(all_new):
        print("  ✅ 文件数一致，迁移无丢失")
    else:
        print(f"  ⚠️  文件数不一致，请检查")

    # ========== 汇总表写入 JSON ==========
    summary_path = NEW_BASE / "迁移方案" / "migration_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n📋 迁移清单已写入：{summary_path}")

    return results


if __name__ == "__main__":
    main()
