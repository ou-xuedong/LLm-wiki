#!/usr/bin/env bash
# slack_post.sh —— 把一条消息发进 Slack 频道（多 Agent 的"汇报总线"）
# 用法：
#   ./slack_post.sh "队长：任务已分解，派出 3 个子 Agent"
#   ./slack_post.sh "子Agent-1" "Mem0 框架要点：……"   # 两个参数 = 加粗标题 + 正文
#
# Webhook 地址从两个地方找（任选其一）：
#   1) 环境变量 SLACK_WEBHOOK_URL
#   2) 同目录下的 .slack_webhook 文件（推荐，第一步会生成）

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 取 Webhook
HOOK="${SLACK_WEBHOOK_URL:-}"
if [[ -z "$HOOK" && -f "$DIR/.slack_webhook" ]]; then
  HOOK="$(tr -d '[:space:]' < "$DIR/.slack_webhook")"
fi
if [[ -z "$HOOK" ]]; then
  echo "❌ 没找到 Webhook。把地址存进 $DIR/.slack_webhook，或 export SLACK_WEBHOOK_URL=" >&2
  exit 1
fi

# 拼消息：1 个参数 = 纯文本；2 个参数 = *标题* + 正文
if [[ $# -ge 2 ]]; then
  TITLE="$1"; shift
  TEXT="*${TITLE}*"$'\n'"$*"
else
  TEXT="${1:-（空消息）}"
fi

# 用 jq 安全转义；没装 jq 就退回简单转义
if command -v jq >/dev/null 2>&1; then
  PAYLOAD="$(jq -n --arg t "$TEXT" '{text:$t}')"
else
  ESC="${TEXT//\\/\\\\}"; ESC="${ESC//\"/\\\"}"; ESC="${ESC//$'\n'/\\n}"
  PAYLOAD="{\"text\":\"${ESC}\"}"
fi

curl -sS -X POST -H 'Content-type: application/json' --data "$PAYLOAD" "$HOOK"
echo   # 换行，curl 返回 ok 后好看
