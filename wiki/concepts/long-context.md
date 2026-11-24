# 檢索越多越好嗎？長上下文的陷阱

## 一句話
不是。模型對放在 context「中間」的資訊特別容易忽略，塞更多段落還會增加成本、稀釋重點。

## 重點
- U 型曲線：相關資訊在 context 開頭或結尾時表現最好，在中間時明顯變差（[Liu 2023](../sources/liu-2023-lost-in-the-middle.md)）。
- GPT-3.5-Turbo 不看任何文件的正確率是 56.1%；答案藏在中間時，多文件問答可能下降超過 20%，甚至比不看文件還差（[Liu 2023](../sources/liu-2023-lost-in-the-middle.md)）。
- 檢索 20 份增加到 50 份，GPT-3.5-Turbo 只多約 1.5%：檢索器召回率還在升，模型表現早就飽和（[Liu 2023](../sources/liu-2023-lost-in-the-middle.md)）。
- 實務建議：用 rerank 把最相關的段落移到前面或兩端，並測試答案位置不同時的表現（[Liu 2023](../sources/liu-2023-lost-in-the-middle.md)）。
- 以較新的資料為準：在 5、10、20 段中取 20 段效果最好，加 rerank 時先抓 150 段再篩到 20 段（[Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)）。較舊說法：原始 RAG 在開放域問答用到 50 份文件（[Lewis 2020](../sources/lewis-2020-rag.md)）。

## 與其他概念的關係
- 這是 [RAG 的三個步驟](rag-pipeline.md) 中「生成」階段的問題；解法之一是 [進階 RAG](advanced-rag.md) 的重新排序。

## 來源
- [Liu et al. 2023](../sources/liu-2023-lost-in-the-middle.md)
- [Anthropic 2024](../sources/anthropic-2024-contextual-retrieval.md)
- [Lewis et al. 2020](../sources/lewis-2020-rag.md)
