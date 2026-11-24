# RAG 的三個步驟（Naive RAG）

## 一句話
建索引 → 檢索 → 生成；最基本的版本叫 Naive RAG，也就是「Retrieve-Read」。

## 重點
- 建索引（離線做一次）：把文件清理成純文字、切成段落（chunk）、用嵌入模型（embedding）轉成向量、存進向量資料庫（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 檢索：用同一個嵌入模型把問題轉成向量，找出最相似的 top K 段（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 生成：把問題和檢索到的段落組成 prompt，交給 LLM 回答（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- Naive RAG 有三類問題：檢索不準（抓錯或漏抓）、生成時仍有幻覺、多段內容整合時重複或抓不到重點（[Gao 2023](../sources/gao-2023-rag-survey.md)）。

## 與其他概念的關係
- 這是 [什麼是 RAG](rag.md) 的具體做法。
- 針對這些問題的改良見 [進階 RAG](advanced-rag.md)；檢索段落太多的問題見 [長上下文的陷阱](long-context.md)；檢索方式的強化見 [混合檢索](hybrid-search.md)。

## 來源
- [Gao et al. 2023](../sources/gao-2023-rag-survey.md)
