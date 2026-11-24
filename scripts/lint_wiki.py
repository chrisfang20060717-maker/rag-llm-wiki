#!/usr/bin/env python3
"""Wiki lint：每次 ingest 後執行。對應 AGENTS.md §3、§5。

檢查項目
  1. 固定區塊：來源頁、概念頁都有規定的 ## 標題
  2. 出處：概念頁「## 重點」的每一條都連到 ../sources/*.md
  3. 數字可追溯：重點裡的數字，必須出現在該條連到的來源頁
  4. 死連結：wiki 內所有相對連結都指到存在的檔案
  5. 孤兒頁：每個 wiki 頁都出現在 wiki/index.md
  6. log：每個來源頁都在 wiki/log.md 有紀錄
用法：python3 scripts/lint_wiki.py           # 每次 ingest 後
      python3 scripts/lint_wiki.py --final   # 全部 ingest 完（加檢查來源數 >= 5）
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SOURCE_HEADINGS = ["## 基本資料", "## 核心主張", "## 關鍵數字", "## 限制", "## 連到的概念"]
CONCEPT_HEADINGS = ["## 一句話", "## 重點", "## 與其他概念的關係", "## 來源"]
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
NUM = re.compile(r"\$?\d+(?:[.,]\d+)*\s?(?:%|M|B|GB|k)?")

errors, passes = [], []


def check(ok, msg):
    (passes if ok else errors).append(msg)
    return ok


def section(text, heading):
    """取出某個 ## 區塊的內容（到下一個 ## 為止）。"""
    m = re.search(rf"^{re.escape(heading)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def numbers(s):
    s = LINK.sub(lambda m: m.group(1), s)          # 連結只留文字，網址裡的數字不算
    s = re.sub(r"`[^`]*`", "", s)                   # 程式碼不算
    out = []
    for n in NUM.findall(s):
        n = n.strip()
        if re.fullmatch(r"\d", n):                  # 單一位數（1 個、3 步）不檢查
            continue
        out.append(n)
    return out


def norm(s):
    return s.replace(" ", "")


def main():
    sources = sorted((WIKI / "sources").glob("*.md"))
    concepts = sorted((WIKI / "concepts").glob("*.md"))
    index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
    log_text = (WIKI / "log.md").read_text(encoding="utf-8") if (WIKI / "log.md").exists() else ""
    if "--final" in sys.argv:
        check(len(sources) >= 5, f"來源頁至少 5 篇（目前 {len(sources)} 篇）")

    for p in sources:
        t = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT)
        missing = [h for h in SOURCE_HEADINGS if h not in t]
        check(not missing, f"{rel}：固定區塊齊全" + (f" → 缺 {missing}" if missing else ""))
        check(p.name in log_text, f"{rel}：wiki/log.md 有 ingest 紀錄")

    for p in concepts:
        t = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT)
        missing = [h for h in CONCEPT_HEADINGS if h not in t]
        check(not missing, f"{rel}：固定區塊齊全" + (f" → 缺 {missing}" if missing else ""))
        bullets = [l for l in section(t, "## 重點").splitlines() if l.strip().startswith("- ")]
        check(len(bullets) >= 2, f"{rel}：重點至少 2 條（{len(bullets)} 條）")
        no_src = [b[:30] for b in bullets if "../sources/" not in b]
        check(not no_src, f"{rel}：每條重點都連回來源頁" + (f" → 沒出處：{no_src}" if no_src else ""))
        bad_nums = []
        for b in bullets:
            # 依引用切段：每段文字裡的數字，只能拿去比對「緊接在這段後面引用的來源」
            pos = 0
            for m in LINK.finditer(b):
                clause, url = b[pos:m.start()], m.group(2)
                pos = m.end()
                if "../sources/" not in url:
                    continue
                src = (p.parent / url).resolve()
                pool = norm(src.read_text(encoding="utf-8")) if src.exists() else ""
                for n in numbers(clause):
                    # 完整數字比對：前後不能接數字或小數點（避免 50 被 150 誤判為找到）
                    if not re.search(rf"(?<![\d.]){re.escape(norm(n))}(?![\d])", pool):
                        bad_nums.append(f"{n}（{src.name}）")
        check(not bad_nums, f"{rel}：重點裡的數字都能在來源頁找到" + (f" → 找不到：{bad_nums}" if bad_nums else ""))

    dead = []
    for p in [WIKI / "index.md", *sources, *concepts]:
        if not p.exists():
            continue
        for _, url in LINK.findall(p.read_text(encoding="utf-8")):
            if url.startswith(("http://", "https://", "#")):
                continue
            if not (p.parent / url.split("#")[0]).resolve().exists():
                dead.append(f"{p.relative_to(ROOT)} → {url}")
    check(not dead, "wiki 內沒有死連結" + (f" → {dead}" if dead else ""))

    linked = {(WIKI / u).resolve() for _, u in LINK.findall(index_text)}
    orphans = [str(p.relative_to(ROOT)) for p in [*sources, *concepts] if p.resolve() not in linked]
    check(not orphans, "沒有孤兒頁（每頁都在 wiki/index.md）" + (f" → {orphans}" if orphans else ""))

    for m in passes:
        print("✅", m)
    for m in errors:
        print("❌", m)
    print(f"\n通過 {len(passes)} 項，失敗 {len(errors)} 項")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
