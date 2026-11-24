# 混合檢索：嵌入＋BM25

## 一句話
向量嵌入找「意思相近」，BM25 找「字面一樣」；兩個一起用，再合併排序。

## 重點
- 嵌入（embedding）擅長語意相似，但可能漏掉精確字詞：查「Error code TS-999」可能只找到一般錯誤碼說明（[Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)）。
- BM25 是字面比對，可以精確找到 TS-999 那一段；混合檢索把兩邊結果用 rank fusion 合併去重（[Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)）。
- 綜述把這類做法歸在 Advanced RAG 的「混合檢索」與索引優化（[Gao 2023](../sources/gao-2023-rag-survey.md)）。

## 與其他概念的關係
- 是 [RAG 的三個步驟](rag-pipeline.md) 中「檢索」的強化版；再加上 [進階 RAG](advanced-rag.md) 的 Contextual Retrieval 效果更好。

## 來源
- [Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)
- [Gao et al. 2023](../sources/gao-2023-rag-survey.md)
