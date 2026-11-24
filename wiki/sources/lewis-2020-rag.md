# Lewis et al. 2020 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## 基本資料
- 作者：Patrick Lewis 等（Facebook AI Research、UCL、NYU）
- 發表：NeurIPS 2020（arXiv:2005.11401）
- 網址：https://arxiv.org/abs/2005.11401
- 類型：原始論文（RAG 這個名詞的出處）

## 核心主張
- 只靠參數記憶（parametric memory）的語言模型，知識存在權重裡：很難更新、很難檢查它為什麼這樣回答，也可能產生幻覺（hallucination）。
- RAG 把兩種記憶接在一起：預訓練的 seq2seq 生成器（BART）當參數記憶，Wikipedia 的向量索引當非參數記憶（non-parametric memory），用檢索器（DPR）去查。
- 兩種版本：RAG-Sequence 整段答案用同一批檢索到的文件；RAG-Token 每個 token 可以參考不同文件。
- 換掉索引就能更新知識，不用重新訓練模型。

## 關鍵數字
- 知識庫：2018 年 12 月的 Wikipedia，每篇切成 100 字的段落，共 21M 個文件。
- 每次檢索的文件數：訓練時取 5 或 10 份；開放域問答測試時 RAG-Sequence 用 50 份、RAG-Token 用 15 份文件。
- Natural Questions 完全比對（exact match）：RAG-Sequence 44.5、RAG-Token 44.1。
- Jeopardy 出題人工評估：RAG 被判定較符合事實的比例 42.7%，BART 只有 7.1%。
- 換索引實驗（82 位職位有變動的世界領袖）：索引年份對得上時答對 70%（2016）與 68%（2018）；對不上時只剩 12% 與 4%。

## 限制
- 檢索器用 DPR 初始化，而 DPR 本身是用 Natural Questions、TriviaQA 有監督訓練的。
- 在故事生成等任務上，檢索可能「崩塌」成不管輸入都抓同一批文件。
- 索引需要約 100 GB 記憶體（壓縮後 36 GB）。
- Wikipedia 本身不保證完全正確、沒有偏見。

## 連到的概念
- [什麼是 RAG](../concepts/rag.md)
