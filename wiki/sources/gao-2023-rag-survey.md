# Gao et al. 2023 — Retrieval-Augmented Generation for Large Language Models: A Survey

## 基本資料
- 作者：Yunfan Gao 等（同濟大學、復旦大學）
- 發表：arXiv:2312.10997（2023 年 12 月，2024 年 3 月更新至 v5）
- 網址：https://arxiv.org/abs/2312.10997
- 類型：綜述論文

## 核心主張
- LLM 的三個問題：幻覺、知識過時、推理過程不透明無法追溯；RAG 用外部資料庫來補。
- RAG 演進分三個範式：Naive RAG → Advanced RAG → Modular RAG。三者是繼承關係：Naive 是 Advanced 的特例，Advanced 是 Modular 的特例。
- Naive RAG＝「Retrieve-Read」：建索引（清理、切塊 chunk、嵌入 embedding、存成向量）→ 檢索（把問題嵌入，取最相似的 top K 段）→ 生成（問題＋段落組成 prompt 交給 LLM）。
- Naive RAG 的缺點：檢索面（精準度低抓錯段落、召回率低漏掉段落、資料過時）；生成面（幻覺、用到不相關內容）；整合面（段落重複、難以判斷哪段重要、過度依賴檢索內容）。
- Advanced RAG：檢索前（更細的切塊、加 metadata、改寫或擴充查詢、HyDE 先產生假想答案再拿去檢索）；檢索後（重新排序 rerank、把最相關的放在 prompt 兩端、壓縮上下文）。
- Modular RAG：可替換、可重組的模組，例如 Search、Memory、Fusion（多個查詢平行搜尋再合併）、Routing（決定去哪個資料庫查）。
- RAG 與微調（fine-tuning）不互斥：RAG 適合更新知識、可追溯；微調適合改變風格、術語與行為；兩者可以結合。
- 評估：三個品質指標（context relevance、answer faithfulness、answer relevance）與四種能力（noise robustness、negative rejection、information integration、counterfactual robustness）。

## 關鍵數字
- 本篇是綜述，沒有自己的實驗數字；重點在分類架構。
- 三個範式、三個品質指標、四種能力。

## 限制
- 綜述整理的是 2023 年底以前的研究，之後的方法（如 Contextual Retrieval）不在內。

## 連到的概念
- [RAG 的三個步驟](../concepts/rag-pipeline.md)
- [進階 RAG：檢索前後的改良](../concepts/advanced-rag.md)
- [怎麼評估 RAG](../concepts/rag-evaluation.md)
- [RAG、微調還是長 prompt？](../concepts/rag-vs-alternatives.md)
