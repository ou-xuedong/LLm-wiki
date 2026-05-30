#!/bin/bash
# AILab 位置感知同步脚本 v2
# 用法: sync.sh [pull|push|both]   默认 both
# 行为:
#   - 在 AILab 根目录或 $HOME 运行 → 同步 meta 仓 + 5 个子项目
#   - 在某子项目内运行              → 仅同步该子项目
#   - 其他位置                      → 报错退出

set -e
unset HTTP_PROXY HTTPS_PROXY ALL_PROXY http_proxy https_proxy all_proxy
export GIT_TERMINAL_PROMPT=0   # 禁止 git 弹出交互式凭证提示，避免钩子挂起
ACTION="${1:-both}"
AILAB="$HOME/Desktop/AILab"
PWD_NOW="$(pwd -P)"
GIT_NET_TIMEOUT="${GIT_NET_TIMEOUT:-20}"   # 单个网络操作最长等待秒数

# 选择可用的 timeout 命令（GNU coreutils）
if command -v timeout >/dev/null 2>&1; then
    TIMEOUT_BIN="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
    TIMEOUT_BIN="gtimeout"
else
    TIMEOUT_BIN=""
fi

# 包装网络型 git 操作：套超时、缩进输出、失败/超时仅警告不中断
run_git_net() {
    if [[ -n "$TIMEOUT_BIN" ]]; then
        "$TIMEOUT_BIN" "$GIT_NET_TIMEOUT" git "$@" 2>&1 | sed "s/^/  /"
    else
        git "$@" 2>&1 | sed "s/^/  /"
    fi
    local rc=${PIPESTATUS[0]}
    if [[ "$rc" -eq 124 ]]; then
        echo "  ⚠️ 超时 ${GIT_NET_TIMEOUT}s 跳过（远程无响应，变更已存本地，下次再推）"
    elif [[ "$rc" -ne 0 ]]; then
        echo "  ⚠️ 失败跳过（退出码 $rc，变更已存本地）"
    fi
    return 0
}

# ── 决定同步范围 ──
if [[ "$PWD_NOW" == "$AILAB" || "$PWD_NOW" == "$HOME" ]]; then
    SCOPE=("." "LLm-wiki" "方向探索" "卟卟鸡投资决策" "投资决策" "投流决策助手" "知识存储与自进化引擎" "autoResearch实验室")
    LABEL_DOT="meta"
    if [[ "$PWD_NOW" == "$HOME" ]]; then
        echo "📍 在家目录（视同 AILab 根）→ 同步 meta + 7 子项目"
    else
        echo "📍 在 AILab 根 → 同步 meta + 7 子项目"
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
        run_git_net pull --rebase
    fi

    # push（修复旧 bug：检查 ahead 而不仅是 dirty）
    if [[ "$ACTION" == "push" || "$ACTION" == "both" ]]; then
        if [[ -n "$(git status --porcelain)" ]]; then
            echo "[$label] 提交本地变更..."
            git add -A
            git commit -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" 2>&1 | sed "s/^/  /"
            run_git_net push
        elif [[ "$(git rev-list @{u}..HEAD 2>/dev/null | wc -l)" -gt 0 ]]; then
            echo "[$label] 推送已提交的本地变更..."
            run_git_net push
        else
            echo "[$label] 无变更"
        fi
    fi
}

for project in "${SCOPE[@]}"; do
    sync_one "$project"
done

echo "✓ 同步完成"
