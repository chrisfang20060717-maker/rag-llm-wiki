#!/usr/bin/env python3
"""渲染檢查：每一頁在 1280×720 下，內容不能超出頁面，也不能壓到頁尾的來源列。
需要 playwright（pip install playwright && playwright install chromium）。
同時輸出每頁截圖到 slides/shots/，方便人工檢查。
用法：python3 scripts/render_check.py
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DECK = ROOT / "slides" / "deck.html"
SHOTS = ROOT / "slides" / "shots"

JS = """(i) => {
  goSlide(i);
  const s = document.querySelectorAll('.slide')[i];
  s.style.transform = 'none';
  const box = s.getBoundingClientRect();
  const footer = s.querySelector('.src').getBoundingClientRect();
  let worst = null;
  s.querySelectorAll('*').forEach(el => {
    if (el.closest('.src') || el.closest('details:not([open])') && el.tagName !== 'SUMMARY' && el.tagName !== 'DETAILS') return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    const over = Math.max(r.right - box.right, r.bottom - footer.top + 2);
    if (over > 0 && (!worst || over > worst.over)) worst = {over: Math.round(over), tag: el.tagName, text: (el.innerText || '').slice(0, 20)};
  });
  return {scrollOverflow: s.scrollHeight > s.clientHeight || s.scrollWidth > s.clientWidth, worst};
}"""


def main():
    SHOTS.mkdir(exist_ok=True)
    errors = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(DECK.as_uri())
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        for i in range(n):
            r = pg.evaluate(JS, i)
            pg.screenshot(path=str(SHOTS / f"slide-{i + 1:02d}.png"))
            bad = r["scrollOverflow"] or r["worst"]
            errors += bool(bad)
            msg = f"第 {i + 1} 頁：" + ("渲染後沒有溢出" if not bad else f"溢出 → {r}")
            print(("❌ " if bad else "✅ ") + msg)
        b.close()
    print(f"\n通過 {n - errors} 頁，失敗 {errors} 頁")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
