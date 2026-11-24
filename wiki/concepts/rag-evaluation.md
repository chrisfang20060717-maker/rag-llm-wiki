# 怎麼評估 RAG

## 一句話
RAG 有兩個會出錯的地方——檢索和生成——所以評估要分開看：查到的對不對、答案有沒有忠於查到的內容、有沒有回答到問題。

## 重點
- 三個品質指標：context relevance（查到的內容是否精準）、answer faithfulness（答案是否忠於查到的內容）、answer relevance（答案是否回應問題）（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- 四種能力：抗雜訊（noise robustness）、資料不足時拒答（negative rejection）、整合多份文件（information integration）、不被錯誤資料帶偏（counterfactual robustness）（[Gao 2023](../sources/gao-2023-rag-survey.md)）。
- RAGAS 讓這些指標可以自動算、不需要標準答案：例如 faithfulness＝被檢索內容支持的陳述數 ÷ 全部陳述數（[Es 2023](../sources/es-2023-ragas.md)）。
- RAGAS 和人類判斷的一致率：faithfulness 0.95、answer relevance 0.78、context relevance 0.70；context relevance 最難評（[Es 2023](../sources/es-2023-ragas.md)）。

## 與其他概念的關係
- 評估的對象是 [RAG 的三個步驟](rag-pipeline.md) 中的檢索與生成。

## 來源
- [Gao et al. 2023](../sources/gao-2023-rag-survey.md)
- [Es et al. 2023](../sources/es-2023-ragas.md)
