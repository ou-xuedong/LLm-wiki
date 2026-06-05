#!/usr/bin/env python3
"""卟卟鸡 VC 外联 · 邮件收发引擎 (Gmail SMTP/IMAP)

用法:
  python3 mailer.py send  --to a@b.com --subject "..." --body-file draft.txt
  python3 mailer.py fetch [--since-days 7] [--from-only known]   # 拉未读, 打印摘要

凭证从同目录 .mail_config 读取 (该文件已 gitignore, 绝不提交):
  EMAIL=you@gmail.com
  APP_PASSWORD=abcdefghijklmnop      # 16位应用专用密码, 去掉空格
"""
import argparse, imaplib, email, smtplib, ssl, sys, os, datetime
from email.header import decode_header, make_header
from email.mime.text import MIMEText
from email.utils import parseaddr, formatdate

CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".mail_config")


def load_config():
    if not os.path.exists(CONFIG):
        sys.exit(f"缺少凭证文件 {CONFIG} — 先填 EMAIL 和 APP_PASSWORD")
    cfg = {}
    with open(CONFIG) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    if not cfg.get("EMAIL") or not cfg.get("APP_PASSWORD"):
        sys.exit("凭证文件里 EMAIL / APP_PASSWORD 不完整")
    return cfg


def send(args):
    cfg = load_config()
    with open(args.body_file, encoding="utf-8") as f:
        body = f.read()
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = str(make_header([(args.subject, "utf-8")]))
    msg["From"] = cfg["EMAIL"]
    msg["To"] = args.to
    msg["Date"] = formatdate(localtime=True)
    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
        s.login(cfg["EMAIL"], cfg["APP_PASSWORD"])
        s.sendmail(cfg["EMAIL"], [args.to], msg.as_string())
    print(f"✅ 已发送 → {args.to} | 主题: {args.subject}")


def _decode(raw):
    try:
        return str(make_header(decode_header(raw or "")))
    except Exception:
        return raw or ""


def _plain_body(m, limit=1500):
    text = ""
    if m.is_multipart():
        for part in m.walk():
            if part.get_content_type() == "text/plain":
                try:
                    text = part.get_payload(decode=True).decode(
                        part.get_content_charset() or "utf-8", "ignore")
                    break
                except Exception:
                    continue
    else:
        try:
            text = m.get_payload(decode=True).decode(
                m.get_content_charset() or "utf-8", "ignore")
        except Exception:
            text = ""
    text = "\n".join(l for l in text.splitlines() if l.strip())
    return text[:limit]


def fetch(args):
    cfg = load_config()
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(cfg["EMAIL"], cfg["APP_PASSWORD"])
    M.select("INBOX")

    # 时间闸: 只看最近 N 天 (邮箱里有上万旧未读, 必须收窄)
    since = datetime.date.today() - datetime.timedelta(days=args.since_days)
    base = ["UNSEEN", "SINCE", since.strftime("%d-%b-%Y")]

    senders = [s.strip() for s in (args.from_addr or "").split(",") if s.strip()]
    ids = []
    if senders:
        # 只看追踪表里这些 VC 发来的回信 (精准过滤, 最省 token)
        for addr in senders:
            typ, data = M.search(None, *base, "FROM", addr)
            ids += data[0].split()
        ids = list(dict.fromkeys(ids))
    else:
        typ, data = M.search(None, *base)
        ids = data[0].split()

    if not ids:
        print(f"📭 最近 {args.since_days} 天没有符合条件的未读邮件")
        M.logout()
        return
    ids = ids[-args.limit:]  # 数量闸: 最多看 limit 封
    print(f"📬 命中 {len(ids)} 封（最近 {args.since_days} 天）：\n")
    for i in ids:
        # BODY.PEEK 不标记已读, 让主人确认前保持未读
        typ, d = M.fetch(i, "(BODY.PEEK[])")
        m = email.message_from_bytes(d[0][1])
        frm = parseaddr(m.get("From"))[1]
        subj = _decode(m.get("Subject"))
        print(f"── from: {frm}")
        print(f"   主题: {subj}")
        print(f"   正文摘要:\n{_plain_body(m)}\n")
    M.logout()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("send")
    s.add_argument("--to", required=True)
    s.add_argument("--subject", required=True)
    s.add_argument("--body-file", required=True)
    s.set_defaults(func=send)
    f = sub.add_parser("fetch")
    f.add_argument("--since-days", type=int, default=7)
    f.add_argument("--from", dest="from_addr", default="",
                   help="只看这些发件人(逗号分隔), 留空则看全部未读")
    f.add_argument("--limit", type=int, default=20, help="最多显示几封")
    f.set_defaults(func=fetch)
    a = p.parse_args()
    a.func(a)
