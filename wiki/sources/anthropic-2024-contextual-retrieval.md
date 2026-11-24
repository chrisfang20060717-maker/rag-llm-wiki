# Anthropic 2024 — Introducing Contextual Retrieval

## 基本資料
- 作者：Anthropic（Engineering 部落格）
- 發表：2024 年 9 月 19 日
- 網址：https://www.anthropic.com/engineering/contextual-retrieval
- 類型：業界技術文章（附實驗與 cookbook）

## 核心主張
- 先問需不需要 RAG：知識庫小於 200,000 tokens（約 500 頁）時，可以直接整份放進 prompt；搭配 prompt caching，延遲可降低超過 2 倍、成本最多降低 90%。
- 只用向量嵌入會漏掉精確字詞，例如查「Error code TS-999」可能找到一般的錯誤碼說明；BM25 做字面比對能補上。常見做法是嵌入＋BM25 混合檢索，再用 rank fusion 合併。
- 傳統切塊會丟失上下文：一段寫著「公司營收比上一季成長 3%」的 chunk，沒寫是哪家公司、哪一季，就很難被正確檢索。
- Contextual Retrieval：在嵌入和建 BM25 索引之前，先用 LLM 替每個 chunk 寫一段 50-100 tokens 的說明（是哪份文件、講什麼）加在前面。

## 關鍵數字
- 指標：取前 20 段時的檢索失敗率（1 − recall@20），基準是 5.7%。
- Contextual Embeddings：失敗率 3.7%，減少 35%。
- Contextual Embeddings + Contextual BM25：失敗率 2.9%，減少 49%。
- 再加上 rerank：失敗率 1.9%，減少 67%。
- 測試 5、10、20 段，取 20 段效果最好；加 rerank 時先抓 150 段再篩到 20 段。
- 產生 contextual chunk 的一次性成本：每百萬 document tokens 1.02 美元。

## 限制
- 結果來自 Anthropic 自己的內部評估資料；作者建議一定要用自己的資料跑評估。
- 段落太多也可能讓模型分心。

## 連到的概念
- [混合檢索：嵌入＋BM25](../concepts/hybrid-search.md)
- [進階 RAG：檢索前後的改良](../concepts/advanced-rag.md)
- [RAG、微調還是長 prompt？](../concepts/rag-vs-alternatives.md)
- [檢索越多越好嗎？長上下文的陷阱](../concepts/long-context.md)
