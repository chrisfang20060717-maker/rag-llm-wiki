# RAG LLM Wiki × 教學 HTML 簡報

用「先討論、後生成」建立一個 RAG（檢索增強生成）主題的 LLM Wiki，ingest 6 篇資料，再只用這個 Wiki 當知識來源，透過有檢查關卡的 graph 流程產生一份教學 HTML 簡報。

- 🌐 首頁：https://chrisfang20060717-maker.github.io/rag-llm-wiki/
- 🖥 教學簡報：https://chrisfang20060717-maker.github.io/rag-llm-wiki/slides/deck.html（← → 鍵換頁）
- 📚 Wiki 目錄：[wiki/index.md](wiki/index.md)

| 想看什麼 | 檔案 |
|---|---|
| 需求訪談（先討論、後生成） | [docs/requirements.md](docs/requirements.md) |
| Wiki 規則 | [AGENTS.md](AGENTS.md)（`CLAUDE.md` 以 `@AGENTS.md` 共用） |
| 來源清單（6 篇） | [sources.md](sources.md) |
| Wiki | [wiki/index.md](wiki/index.md)、[ingest 紀錄](wiki/log.md) |
| 簡報大綱＝證據卡 | [slides/outline.md](slides/outline.md) |
| loop / graph 設計 | [docs/workflow.md](docs/workflow.md) |
| 實際執行與檢查紀錄 | [docs/run-report.md](docs/run-report.md) |
| 反思 | [docs/reflection.md](docs/reflection.md) |

## 檢查指令
```bash
python3 scripts/lint_wiki.py --final   # Wiki：出處、數字、孤兒頁、死連結
python3 scripts/check_deck.py          # 簡報：頁數、字數、出處、數字可追溯
python3 scripts/render_check.py        # 簡報：渲染溢出＋截圖（需 playwright）
```
