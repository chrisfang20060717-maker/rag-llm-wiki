# AGENTS.md — RAG LLM Wiki

> 這份規則是依 `docs/requirements.md` 的需求訪談（先討論、後生成）整理出來的。改規則前先改需求摘要。

## 1. 目的與讀者
- 主題：RAG（Retrieval-Augmented Generation，檢索增強生成）。
- 讀者：修過生成式 AI 課的同學，懂 prompt、LLM、token 等詞，不用從頭解釋。
- 產出：`wiki/`（知識庫）→ `slides/deck.html`（教學簡報）。簡報只能用 wiki 裡的內容。
- 語言：正體中文，術語第一次出現附英文，例如「重新排序（rerank）」。

## 2. 資料夾
```
raw/              原始資料（PDF／網頁存檔），不進 git
sources.md        所有來源清單（網址、日期）
wiki/index.md     目錄：每個 wiki 頁都要出現在這裡
wiki/log.md       ingest 紀錄，新紀錄加在最上面
wiki/sources/     一篇資料一頁，檔名 作者-年份-短名.md
wiki/concepts/    一個概念一頁，檔名 英文 kebab-case.md
slides/outline.md 簡報大綱＝證據卡（每頁的說法＋引用的 wiki 頁）
slides/deck.html  教學簡報
scripts/          lint 與檢查腳本
docs/             需求紀錄、流程設計、執行紀錄、反思
```

## 3. Ingest 規則（一次一篇）
1. 一次只處理一篇資料。先寫 `wiki/sources/` 的來源頁，再更新或新增相關概念頁。
2. 來源頁固定區塊：`## 基本資料`、`## 核心主張`、`## 關鍵數字`、`## 限制`、`## 連到的概念`。
3. 概念頁固定區塊：`## 一句話`、`## 重點`、`## 與其他概念的關係`、`## 來源`。
4. **每個重點都要連回來源頁**：`## 重點` 底下的每一條都必須有 `../sources/xxx.md` 的連結。
5. **數字只能寫在來源頁有出現的**：概念頁引用的數字，必須能在它連到的來源頁找到一模一樣的寫法（例如 `49%`）。
6. **說法矛盾時以較新的資料為準**：在概念頁寫較新的說法，並用一行「較舊說法：…（年份）」註明，不要刪掉舊來源。
7. 每 ingest 完一篇：更新 `wiki/index.md`、在 `wiki/log.md` 最上方加一筆、跑 `python3 scripts/lint_wiki.py`，全過才能 ingest 下一篇。

## 4. 簡報規則（graph 流程，詳見 docs/workflow.md）
- 10–14 頁，結構「先問題、再解法」：問題 → 核心想法 → 流程 → 會遇到的坑 → 解法 → 評估 → 何時使用 → 小測驗 → 回顧。
- 先寫 `slides/outline.md`（證據卡），人確認後才寫 `deck.html`。
- 每頁 `<section class="slide" data-sources="wiki 頁路徑,…">`，頁尾顯示來源。
- 每頁正文（不含標題、頁首編號 `.kicker` 與頁尾）最多 160 字；數字必須出現在該頁引用的 wiki 頁裡。
- 用到來源頁才有的細節（例如實驗的題數），`data-sources` 要直接列出那個來源頁。
- 只能改出錯的那一頁，其他頁不動。

## 5. 檢查（完成的定義）
```bash
python3 scripts/lint_wiki.py     # wiki：出處、數字、孤兒頁、死連結、固定區塊
python3 scripts/check_deck.py    # 簡報：頁數、字數、引用存在、數字可追溯
python3 scripts/render_check.py  # 簡報：每頁渲染後沒有溢出（需 playwright）
```
- 任一 ❌：只修報告列出的問題，最多 3 輪；3 輪還沒過就停下來回報。
- 結果寫進 `docs/run-report.md`。

## 6. 不要做
- 不要用 wiki 以外的知識寫簡報；wiki 缺資料就退回 ingest，不要硬湊。
- 不要把 `raw/` 的原始檔或付費內容上傳。
- 不要改檢查腳本讓它通過。
