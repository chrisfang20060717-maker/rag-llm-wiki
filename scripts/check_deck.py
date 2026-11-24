#!/usr/bin/env python3
"""簡報檢查：對應 AGENTS.md §4、§5。

  1. 頁數在 10–14 頁
  2. 每頁有 data-sources，且引用的 wiki 頁都存在
  3. 每頁正文（不含標題）最多 160 字（不計空白）
  4. 每頁正文裡的數字，必須出現在該頁引用的 wiki 頁
  5. 頁數和 slides/outline.md 的大綱一致
用法：python3 scripts/check_deck.py
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "slides" / "deck.html"
OUTLINE = ROOT / "slides" / "outline.md"
MIN_SLIDES, MAX_SLIDES, MAX_CHARS = 10, 14, 160
NUM = re.compile(r"\$?\d+(?:[.,]\d+)*\s?(?:%|M|B|GB|k)?")


class Deck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []      # {"sources": [...], "title": str, "body": str}
        self._depth = 0       # 目前在 slide 裡的巢狀深度
        self._in_title = False
        self._skip = 0        # 在 <script>/<style>/.kicker 裡

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if tag == "section" and "slide" in cls:
            self.slides.append({"sources": [s.strip() for s in a.get("data-sources", "").split(",") if s.strip()],
                                "title": "", "body": ""})
            self._depth = 1
            return
        if self._depth:
            self._depth += 1
            if tag in ("h1", "h2"):
                self._in_title = True
        if tag in ("script", "style") or "kicker" in cls:
            self._skip += 1
            self._skip_tag = tag

    def handle_endtag(self, tag):
        if self._skip and tag == getattr(self, "_skip_tag", None):
            self._skip -= 1
        if self._depth:
            if tag in ("h1", "h2"):
                self._in_title = False
            self._depth -= 1

    def handle_data(self, data):
        if not self._depth or self._skip:
            return
        key = "title" if self._in_title else "body"
        self.slides[-1][key] += data + " "   # 加空白：避免相鄰元素的數字黏在一起


def main():
    errors, passes = [], []
    check = lambda ok, msg: (passes if ok else errors).append(msg)

    d = Deck()
    d.feed(DECK.read_text(encoding="utf-8"))
    n = len(d.slides)
    check(MIN_SLIDES <= n <= MAX_SLIDES, f"頁數 {n}（規定 {MIN_SLIDES}–{MAX_SLIDES}）")
    outline_rows = len(re.findall(r"^\|\s*\d+\s*\|", OUTLINE.read_text(encoding="utf-8"), re.M))
    check(outline_rows == n, f"頁數與大綱一致（大綱 {outline_rows} 頁、簡報 {n} 頁）")

    for i, s in enumerate(d.slides, 1):
        tag = f"第 {i} 頁「{s['title'].strip()[:14]}」"
        srcs = s["sources"]
        missing = [x for x in srcs if not (ROOT / "wiki" / x).exists()]
        check(bool(srcs) and not missing, f"{tag}：有標出處且引用的 wiki 頁存在" +
              ("" if srcs else " → 沒有 data-sources") + (f" → 不存在：{missing}" if missing else ""))
        body = re.sub(r"\s+", "", s["body"])
        check(len(body) <= MAX_CHARS, f"{tag}：正文 {len(body)} 字（上限 {MAX_CHARS}）")
        pool = "".join(re.sub(r"\s+", "", (ROOT / "wiki" / x).read_text(encoding="utf-8"))
                       for x in srcs if (ROOT / "wiki" / x).exists())
        bad = []
        for num in NUM.findall(s["body"]):
            num = re.sub(r"\s+", "", num)
            if re.fullmatch(r"\d", num):
                continue
            if not re.search(rf"(?<![\d.]){re.escape(num)}(?![\d])", pool):
                bad.append(num)
        check(not bad, f"{tag}：數字都能在引用的 wiki 頁找到" + (f" → 找不到：{bad}" if bad else ""))

    for m in passes:
        print("✅", m)
    for m in errors:
        print("❌", m)
    print(f"\n通過 {len(passes)} 項，失敗 {len(errors)} 項")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
