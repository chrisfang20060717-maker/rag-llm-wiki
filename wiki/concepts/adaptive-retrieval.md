# 什麼時候才需要查？自適應檢索

## 一句話
不是每個問題都該檢索；讓模型先判斷「需不需要查」，查完再檢查「資料相關嗎、答案有被支持嗎」。

## 重點
- 固定檢索的問題：不管需不需要都抓固定幾段，不相關的段落會拉低答案品質（[Asai 2023](../sources/asai-2023-self-rag.md)）。
- Self-RAG 用四種反思標記：Retrieve（要不要查）、IsREL（相關嗎）、IsSUP（有被支持嗎）、IsUSE（有用嗎）（[Asai 2023](../sources/asai-2023-self-rag.md)）。
- 效果：PopQA 上 Self-RAG 13B 達 55.8，ChatGPT 只有 29.3；但在 ARC-Challenge 上 ChatGPT 的 75.3 仍較高，不是每項都贏（[Asai 2023](../sources/asai-2023-self-rag.md)）。
- 以較新的資料為準：RAG 應該「需要時才查」並檢查證據（[Asai 2023](../sources/asai-2023-self-rag.md)）。較舊說法：原始 RAG 每次都檢索固定數量的文件（[Lewis 2020](../sources/lewis-2020-rag.md)）。

## 與其他概念的關係
- 修正的是 [RAG 的三個步驟](rag-pipeline.md) 中「一律檢索」的假設；IsSUP 的想法和 [怎麼評估 RAG](rag-evaluation.md) 的 faithfulness 相同。

## 來源
- [Asai et al. 2023](../sources/asai-2023-self-rag.md)
- [Lewis et al. 2020](../sources/lewis-2020-rag.md)
