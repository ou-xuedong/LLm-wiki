#!/bin/bash
# AILab 位置感知同步脚本 v2
# 用法: sync.sh [pull|push|both]   默认 both
# 行为:
#   - 在 AILab 根目录或 $HOME 运行 → 同步 meta 仓 + 5 个子项目
#   - 在某子项目内运行              → 仅同步该子项目
#   - 其他位置                      → 报错退出

set -e
ACTION="${1:-both}"
AILAB="$HOME/Desktop/AILab"
PWD_NOW="$(pwd -P)"

# ── 决定同步范围 ──
if [[ "$PWD_NOW" == "$AILAB" || "$PWD_NOW" == "$HOME" ]]; then
    SCOPE=("." "知识库" "方向探索" "卟卟鸡投资决策" "亚马逊投流决策助手" "知识存储与自进化引擎" "autoResearch实验室")
    LABEL_DOT="meta"
    if [[ "$PWD_NOW" == "$HOME" ]]; then
        echo "📍 在家目录（视同 AILab 根）→ 同步 meta + 6 子项目"
    else
        echo "📍 在 AILab 根 → 同步 meta + 6 子项目"
    fi
elif [[ "$PWD_NOW" == "$AILAB"/* ]]; then
    PROJECT="${PWD_NOW#$AILAB/}"
    PROJECT="${PROJECT%%/*}"
    SCOPE=("$PROJECT")
    LABEL_DOT=""
    echo "📍 在 $PROJECT → 仅同步该项目"
else
    echo "❌ 必须在 ~/Desktop/AILab/ 或 \$HOME 内运行（当前: $PWD_NOW）"
    exit 1
fi

sync_one() {
    local project="$1"
    local dir
    local label
    if [[ "$project" == "." ]]; then
        dir="$AILAB"
        label="$LABEL_DOT"
    else
        dir="$AILAB/$project"
        label="$project"
    fi

    if [[ ! -d "$dir/.git" ]]; then
        echo "[$label] 跳过 - 非 git 项目"
        return
    fi

    cd "$dir"

    # pull
    if [[ "$ACTION" == "pull" || "$ACTION" == "both" ]]; then
        echo "[$label] 拉取..."
        git pull --rebase 2>&1 | sed "s/^/  /"
    fi

    # push（修复旧 bug：检查 ahead 而不仅是 dirty）
    if [[ "$ACTION" == "push" || "$ACTION" == "both" ]]; then
        if [[ -n "$(git status --porcelain)" ]]; then
            echo "[$label] 提交本地变更..."
            git add -A
            git commit -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" 2>&1 | sed "s/^/  /"
            git push 2>&1 | sed "s/^/  /"
        elif [[ "$(git rev-list @{u}..HEAD 2>/dev/null | wc -l)" -gt 0 ]]; then
            echo "[$label] 推送已提交的本地变更..."
            git push 2>&1 | sed "s/^/  /"
        else
            echo "[$label] 无变更"
        fi
    fi
}

for project in "${SCOPE[@]}"; do
    sync_one "$project"
done

echo "✓ 同步完成"
