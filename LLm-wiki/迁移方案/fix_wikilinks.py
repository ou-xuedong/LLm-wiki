#!/usr/bin/env python3
"""
Fix wikilinks in migrated wiki:
旧格式 [[Name_Name]] (case-sensitive) → 新 slug 精确匹配
只修 body 里的 wikilinks，不动 frontmatter。
"""
import os, re, pathlib

NEW_WIKI = pathlib.Path("/Users/ouxuedong/Desktop/AILab/LLm-wiki")
SUBDIRS = ["entities/kols","entities/companies","entities/vcs","entities/events","concepts","queries"]

# Build lookup: lowercase → original_slug
slug_lookup = {}
for subdir in SUBDIRS:
    for f in (NEW_WIKI / subdir).glob("*.md"):
        slug = f.with_suffix("").name
        slug_lookup[slug.lower()] = slug

UNMAPPABLE = {"人物", "活动", "ai创业十三条军规_核心评估准则"}

def resolve_link(link_text):
    """Resolve old wikilink to actual new slug."""
    lower = link_text.lower().strip()
    if lower in slug_lookup:
        return slug_lookup[lower]
    candidates = [s for s in slug_lookup if lower in s]
    if len(candidates) == 1:
        return slug_lookup[candidates[0]]
    if len(candidates) > 1:
        return slug_lookup[min(candidates, key=len)]
    return None

def fix_file(f):
    content = f.read_text(encoding="utf-8")
    new_content = content

    def replacer(m):
        display_text = m.group(2) if m.group(2) else ""
        link_text = m.group(1).strip()
        resolved = resolve_link(link_text)
        if resolved:
            if display_text:
                return f"[[{resolved}|{display_text}]]"
            return f"[[{resolved}]]"
        # Unmapped - leave as-is
        return m.group(0)

    # Fix body wikilinks: [[text|display]] or [[text]]
    # Don't touch frontmatter
    fm_end_idx = content.find("---", 4)
    if fm_end_idx < 0:
        return 0, 0
    fm_end_idx = content.find("---", fm_end_idx + 3)
    if fm_end_idx < 0:
        return 0, 0

    fm = content[:fm_end_idx + 3]
    body = content[fm_end_idx + 3:]

    fixed_links = 0
    kept_links = 0

    def body_replacer(m):
        nonlocal fixed_links, kept_links
        display = m.group(2) if m.group(2) else ""
        link = m.group(1).strip()
        resolved = resolve_link(link)
        if resolved:
            fixed_links += 1
            if display:
                return f"[[{resolved}|{display}]]"
            return f"[[{resolved}]]"
        else:
            kept_links += 1
            return m.group(0)

    new_body = re.sub(r'\[\[([^\]|]+?)(\|[^\]]+?)?\]\]', body_replacer, body)
    new_content = fm + new_body

    if new_content != content:
        f.write_text(new_content, encoding="utf-8")

    return fixed_links, kept_links

total_fixed = 0
total_kept = 0
for subdir in SUBDIRS:
    for f in (NEW_WIKI / subdir).glob("*.md"):
        fixed, kept = fix_file(f)
        if fixed:
            total_fixed += fixed
            total_kept += kept

print(f"✅ Wikilinks fixed: {total_fixed} links")
print(f"   Kept as-is (unresolved): {total_kept} links")
