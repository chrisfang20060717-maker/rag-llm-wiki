# Ingest 紀錄

> 新紀錄加在最上面。每筆：日期、哪一篇、新增/更新了哪些頁、lint 結果。

## 2026-11-24 修正 lewis-2020-rag.md
- lint 改成「依引用切段比對數字」後，抓到 `long-context.md` 的「50 份文件」在 Lewis 來源頁找不到
- 退回 ingest：在 `sources/lewis-2020-rag.md` 補上論文附錄的檢索文件數（50 / 15 份）
- lint：全過

## 2026-11-24 #6 anthropic-2024-contextual-retrieval.md
- 新增來源頁 `sources/anthropic-2024-contextual-retrieval.md`
- 新增概念頁 `concepts/hybrid-search.md`
- 更新 `advanced-rag.md`（Contextual Retrieval）、`rag-vs-alternatives.md`（長 prompt 門檻）、`long-context.md`（top-K）、`rag-pipeline.md`、`index.md`
- 矛盾處理：Lewis 2020 開放域問答用 50 份文件 vs Anthropic 2024 取 20 段最好 → 以較新的為準
- lint：見 docs/run-report.md「Ingest #6」

## 2026-11-24 #5 es-2023-ragas.md
- 新增來源頁 `sources/es-2023-ragas.md`
- 更新概念頁 `concepts/rag-evaluation.md`（補自動評估與一致率）、`index.md`
- lint：見 docs/run-report.md「Ingest #5」

## 2026-11-24 #4 asai-2023-self-rag.md
- 新增來源頁 `sources/asai-2023-self-rag.md`
- 新增概念頁 `concepts/adaptive-retrieval.md`
- 矛盾處理：Lewis 2020「固定檢索」vs Asai 2023「需要時才查」→ 依規則以較新的為準，保留一行較舊說法
- 更新 `index.md`
- lint：見 docs/run-report.md「Ingest #4」

## 2026-11-24 #3 liu-2023-lost-in-the-middle.md
- 新增來源頁 `sources/liu-2023-lost-in-the-middle.md`
- 新增概念頁 `concepts/long-context.md`
- 更新 `concepts/rag-pipeline.md`、`index.md`
- lint：見 docs/run-report.md「Ingest #3」

## 2026-11-24 #2 gao-2023-rag-survey.md
- 新增來源頁 `sources/gao-2023-rag-survey.md`
- 新增概念頁 `concepts/rag-pipeline.md`、`advanced-rag.md`、`rag-evaluation.md`、`rag-vs-alternatives.md`
- 更新 `concepts/rag.md`（補上關係連結）、`index.md`
- lint：見 docs/run-report.md「Ingest #2」

## 2026-11-24 #1 lewis-2020-rag.md
- 新增來源頁 `sources/lewis-2020-rag.md`
- 新增概念頁 `concepts/rag.md`
- 更新 `index.md`
- lint：見 docs/run-report.md「Ingest #1」
