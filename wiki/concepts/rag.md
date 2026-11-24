# 什麼是 RAG（Retrieval-Augmented Generation）

## 一句話
讓 LLM 先去外部知識庫「查資料」，再把查到的內容和問題一起交給模型生成答案——像開書考試。

## 重點
- 只靠參數記憶的模型會有三個問題：知識難以更新、難以檢查來源、可能產生幻覺（[Lewis 2020](../sources/lewis-2020-rag.md)）。
- RAG = 參數記憶（生成模型）＋非參數記憶（可檢索的文件索引）；原始論文用 BART 當生成器、DPR 當檢索器、Wikipedia 當知識庫（[Lewis 2020](../sources/lewis-2020-rag.md)）。
- 原始論文的知識庫是 2018 年的 Wikipedia，切成 100 字段落，共 21M 個文件（[Lewis 2020](../sources/lewis-2020-rag.md)）。
- 知識可以「換索引」來更新：索引年份對得上時答對 70% / 68%，對不上時只剩 12% / 4%（[Lewis 2020](../sources/lewis-2020-rag.md)）。
- 人工評估中，RAG 生成的內容被判定較符合事實的比例是 42.7%，純生成的 BART 只有 7.1%（[Lewis 2020](../sources/lewis-2020-rag.md)）。

## 與其他概念的關係
- 具體流程見 [RAG 的三個步驟](rag-pipeline.md)；何時該用 RAG 見 [RAG、微調還是長 prompt？](rag-vs-alternatives.md)。

## 來源
- [Lewis et al. 2020](../sources/lewis-2020-rag.md)
