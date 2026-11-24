# Es et al. 2023 — Ragas: Automated Evaluation of Retrieval Augmented Generation

## 基本資料
- 作者：Shahul Es、Jithin James、Luis Espinosa-Anke、Steven Schockaert
- 發表：arXiv:2309.15217（2023 年 9 月）；EACL 2024 Demo
- 網址：https://arxiv.org/abs/2309.15217
- 類型：評估框架論文（開源工具）

## 核心主張
- 做 RAG 時通常沒有人工標好的標準答案，所以需要「不靠參考答案」（reference-free）的自動評估，只用問題、檢索到的內容和生成的答案。
- 三個指標：
  - Faithfulness：用 LLM 把答案拆成多個陳述，逐一檢查是否被檢索內容支持；分數＝被支持的陳述數 ÷ 全部陳述數。
  - Answer relevance：用 LLM 從答案反推幾個可能的問題，和原問題比相似度；答案不完整或多餘會被扣分。
  - Context relevance：讓 LLM 從檢索內容挑出回答所需的句子；分數＝需要的句子數 ÷ 全部句子數，越高代表越少雜訊。

## 關鍵數字
- WikiEval 資料集：50 個 2022 年之後事件的 Wikipedia 頁面，兩位標註者評分。
- 與人類判斷的一致率：faithfulness 0.95、answer relevance 0.78、context relevance 0.70；都高於 GPT Score 與 GPT Ranking 兩個基準。
- 作者指出 context relevance 是最難評估的一項。

## 限制
- 評估本身用 LLM（gpt-3.5-turbo-16k）判斷，評估結果也可能出錯。

## 連到的概念
- [怎麼評估 RAG](../concepts/rag-evaluation.md)
