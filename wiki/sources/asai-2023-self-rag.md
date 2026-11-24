# Asai et al. 2023 — Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

## 基本資料
- 作者：Akari Asai 等（University of Washington、Allen Institute for AI、IBM Research AI）
- 發表：arXiv:2310.11511（2023 年 10 月）；ICLR 2024
- 網址：https://arxiv.org/abs/2310.11511
- 類型：方法論文

## 核心主張
- 一般 RAG 不管需不需要都固定檢索幾段，不相關的段落反而會降低品質，答案也不保證有被證據支持。
- Self-RAG 讓模型自己決定「要不要查」，並用反思標記（reflection tokens）評論自己：
  - Retrieve：現在需不需要檢索
  - IsREL：這段資料跟問題相關嗎
  - IsSUP：答案有被這段資料支持嗎（完全／部分／沒有）
  - IsUSE：答案有用嗎（1–5 分）
- 訓練：先用 GPT-4 的判斷訓練一個評論模型（critic），把反思標記插進訓練資料，再訓練生成模型；推論時用評論分數挑最好的答案。

## 關鍵數字
- 模型大小：7B 與 13B（以 Llama 2 為基礎）。
- PopQA 正確率：Self-RAG 7B 54.9、13B 55.8；ChatGPT 29.3。
- ARC-Challenge：ChatGPT 75.3 仍高於 Self-RAG 13B 的 73.1。
- 預設檢索門檻：「需要檢索」的機率超過 0.2 才去查。

## 限制
- 仍可能產生沒有被引用完全支持的內容。
- ASQA 的引用召回率仍低於有檢索的 ChatGPT。
- 評論模型依賴 GPT-4 標註，成本與可重現性是問題。

## 連到的概念
- [什麼時候才需要查？自適應檢索](../concepts/adaptive-retrieval.md)
