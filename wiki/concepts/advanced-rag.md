# 進階 RAG：檢索前後的改良

## 一句話
Naive RAG 的問題多半出在「查得準不準」，所以改良集中在檢索前（把查詢和索引弄好）與檢索後（把結果排好、壓短）。

## 重點
- 檢索前：切更細的段落、加 metadata 方便過濾、改寫或擴充查詢；HyDE 會先讓模型寫一個假想答案，再用它去檢索（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 檢索後：重新排序（rerank）把最相關的段落排到前面，或把最相關的放在 prompt 兩端；也可以壓縮上下文、去掉雜訊（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- Modular RAG 把流程拆成可替換的模組，例如 Routing 決定要去哪個資料庫查、Fusion 用多個查詢平行搜尋再合併（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- Contextual Retrieval：先替每個 chunk 加上 50-100 tokens 的說明再建索引；檢索失敗率從 5.7% 降到 2.9%（減少 49%），加上 rerank 降到 1.9%（減少 67%）（[Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)）。

## 與其他概念的關係
- 改良的是 [RAG 的三個步驟](rag-pipeline.md) 裡的「檢索」那一步。

## 來源
- [Gao et al. 2023](../sources/gao-2023-rag-survey.md)
- [Anthropic 2024 — Contextual Retrieval](../sources/anthropic-2024-contextual-retrieval.md)
