# RAG、微調還是長 prompt？

## 一句話
RAG 不是唯一選項：要補「知識」用 RAG，要改「行為與風格」用微調，兩者可以一起用。

## 重點
- RAG 的優點：換資料庫就能更新知識、答案可追溯、比較不會幻覺；缺點是延遲較高、要維護檢索系統（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 微調（fine-tuning）的優點：可以改變模型的行為、寫作風格與領域術語，回答時不用檢索；缺點是知識是靜態的，要更新就得重新訓練（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 兩者不互斥，結合使用可能效果最好（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 知識庫小於 200,000 tokens（約 500 頁）時，可以不用 RAG，直接整份放進 prompt，再用 prompt caching 降低成本（[Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)）。

## 與其他概念的關係
- 為什麼要用 RAG，見 [什麼是 RAG](rag.md)。

## 來源
- [Gao et al. 2023](../sources/gao-2023-rag-survey.md)
- [Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)
