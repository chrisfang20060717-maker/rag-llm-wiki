# Liu et al. 2023 — Lost in the Middle: How Language Models Use Long Contexts

## 基本資料
- 作者：Nelson F. Liu 等（Stanford、UC Berkeley、Samaya AI）
- 發表：arXiv:2307.03172（2023）；TACL 2024
- 網址：https://arxiv.org/abs/2307.03172
- 類型：實證研究

## 核心主張
- 實驗：多文件問答，context 裡放 10、20 或 30 份文件，只有一份含答案，其餘是用檢索器找來的干擾文件；改變答案文件的位置。
- 發現 U 型曲線：答案在 context 的開頭或結尾時表現最好，在中間時明顯變差（開頭是首因效應 primacy bias，結尾是近因效應 recency bias）。
- 「長上下文版」模型不一定比較會用長上下文。
- 檢索器的召回率會隨檢索數量上升，但模型的答題表現很早就飽和。

## 關鍵數字
- 資料：NaturalQuestions-Open 的 2655 個問題；文件是最多 100 token 的 Wikipedia 段落。
- GPT-3.5-Turbo 不給任何文件（closed-book）的正確率是 56.1%；答案放在中間時，多文件問答表現可能下降超過 20%，在 20 和 30 份文件的設定下甚至低於 closed-book。
- 從檢索 20 份增加到 50 份文件，GPT-3.5-Turbo 只多約 1.5%，Claude-1.3 只多約 1%。

## 限制
- 主要測的是 2023 年的模型；之後的模型可能改善，但「位置會影響表現」仍是設計 RAG 時要測的項目。

## 連到的概念
- [檢索越多越好嗎？長上下文的陷阱](../concepts/long-context.md)
