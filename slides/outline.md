# 簡報大綱＝證據卡

主題：RAG 是什麼？讓 LLM 先查資料再回答
讀者：修過生成式 AI 課的同學　結構：先問題 → 再解法　頁數：13

每一頁只能用「引用」欄列出的 wiki 頁裡的內容；數字必須在那些頁裡找得到。

| # | 標題 | 要講的重點（證據） | 引用的 wiki 頁 |
|---|---|---|---|
| 1 | RAG：讓 LLM 先查資料再回答 | 封面；一句話定義（開書考試） | concepts/rag.md |
| 2 | 問題：LLM 只靠記憶回答 | 知識難更新、難追溯、會幻覺 | concepts/rag.md |
| 3 | 核心想法：開書考試 | 參數記憶＋非參數記憶；原始論文 21M 段 Wikipedia；換索引 70% / 68% vs 12% / 4% | concepts/rag.md |
| 4 | 三個步驟 | 建索引 → 檢索 → 生成（Retrieve-Read） | concepts/rag-pipeline.md |
| 5 | 怎麼「找」：嵌入＋BM25 | 語意 vs 字面；TS-999 例子；rank fusion | concepts/hybrid-search.md |
| 6 | 坑一：塞越多越好？ | U 型曲線；56.1%；20→50 份只多 1.5% | concepts/long-context.md |
| 7 | 坑二：chunk 丟了上下文 | Naive RAG 三類問題；chunk 沒寫是哪家公司 | concepts/rag-pipeline.md、concepts/advanced-rag.md |
| 8 | 解法一：把檢索做好 | 檢索前（改寫查詢、HyDE）／檢索後（rerank、壓縮）；Contextual Retrieval 5.7% → 2.9% → 1.9% | concepts/advanced-rag.md |
| 9 | 解法二：需要時才查 | Self-RAG 四種反思標記；PopQA 55.8 vs 29.3；不是每項都贏 | concepts/adaptive-retrieval.md |
| 10 | 怎麼知道做得好？ | 三個指標；faithfulness 公式；RAGAS 一致率 0.95 / 0.78 / 0.70 | concepts/rag-evaluation.md |
| 11 | 一定要用 RAG 嗎？ | 小於 200,000 tokens 直接放 prompt；RAG 補知識、微調改行為、可結合 | concepts/rag-vs-alternatives.md |
| 12 | 小測驗 | 3 題，點擊看答案 | concepts/long-context.md、concepts/hybrid-search.md、concepts/rag-evaluation.md |
| 13 | 重點回顧 | 一頁總結＋延伸閱讀 | wiki/index.md |

## 確認紀錄
- [x] 2026-11-24 AI 自查：結構符合「先問題再解法」，13 頁在 10–14 頁範圍內，每頁都有引用頁。
- [ ] 人確認：這次因為趕在期限內，大綱自查後直接進入逐頁稿，人工確認改在交件前和簡報一起看（見 docs/reflection.md）。
