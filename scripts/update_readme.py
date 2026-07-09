"""
Tự cập nhật mục "Recent activity" trong README.md và README.vi.md.

Lấy các repo public mới push gần nhất của NgTrgGiang, bỏ fork và repo bootcamp,
rồi thay nội dung giữa <!-- RECENT:START --> và <!-- RECENT:END --> ở cả 2 file.

Chạy tự động bằng GitHub Actions (dùng GITHUB_TOKEN), hoặc chạy tay:
    GITHUB_TOKEN=$(gh auth token) python scripts/update_readme.py
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request

USER = "NgTrgGiang"
COUNT = 5  # số repo hiển thị
FILES = ["README.md", "README.vi.md"]

# Bỏ chính repo profile và các repo bài tập/bootcamp khỏi danh sách hoạt động
SKIP_NAMES = {USER}
BOOTCAMP = re.compile(r"(^|[-_])[Dd]ay[-_ ]?\d|^2A2026|^Batch\d|lab\d", re.IGNORECASE)

MARKER = re.compile(r"<!-- RECENT:START -->.*?<!-- RECENT:END -->", re.DOTALL)


def fetch_repos() -> list[dict]:
    url = f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def pick(repos: list[dict]) -> list[dict]:
    out = []
    for r in repos:
        if r.get("fork") or r.get("archived"):
            continue
        name = r.get("name", "")
        if name in SKIP_NAMES or BOOTCAMP.search(name):
            continue
        out.append(r)
    out.sort(key=lambda r: r.get("pushed_at", ""), reverse=True)
    return out[:COUNT]


def line(r: dict) -> str:
    name = r["name"]
    url = r["html_url"]
    desc = (r.get("description") or "").strip()
    lang = r.get("language")
    if not desc:
        desc = f"{lang} project" if lang else "No description yet"
    date = (r.get("pushed_at") or "")[:10]
    return f"- **[{name}]({url})** &nbsp; {desc} &nbsp; `updated {date}`"


def build_block(repos: list[dict]) -> str:
    body = "\n".join(line(r) for r in repos) if repos else "_No recent public activity._"
    return f"<!-- RECENT:START -->\n{body}\n<!-- RECENT:END -->"


def main() -> int:
    repos = pick(fetch_repos())
    block = build_block(repos)
    changed = False
    for path in FILES:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        new = MARKER.sub(lambda _m: block, content)
        if new != content:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(new)
            changed = True
            print(f"updated {path}")
    print("changed" if changed else "no change")
    return 0


if __name__ == "__main__":
    sys.exit(main())
