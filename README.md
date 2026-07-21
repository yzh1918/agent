# RAG 论文问答平台

基于 **LangChain 1.x + FastAPI + Vue 3** 的多轮对话 RAG 系统，支持 PDF 论文上传、多论文管理、多轮问答与会话记忆。

## 核心特性

- **端到端 RAG**：PDF 解析 → 切分 → 向量嵌入 → FAISS 检索 → LLM 生成
- **多轮对话记忆**：`RunnableWithMessageHistory` + session_id 实现会话隔离
- **代词消解**：历史感知检索器将"他/它"等代词重写为独立问题再检索
- **LCEL 链式组合**：`|` 管道符组合 Retriever / Prompt / LLM
- **多论文管理**：按论文名分目录存储 FAISS 索引，动态加载

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + Vite + Axios |
| 后端 | FastAPI + Uvicorn |
| RAG | LangChain 1.x（LCEL、Runnable、MessageHistory） |
| 嵌入 | BGE-M3（本地，1024 维） |
| 向量库 | FAISS |
| 生成模型 | DeepSeek API |

## 项目结构

```
paper_agent/
├── app.py                  # FastAPI 入口（/chat /upload /papers）
├── config.py               # DeepSeek API Key
├── agent/                  # 问答核心
│   ├── agent.py            # run()：路由 → 检索 → 生成
│   ├── llm.py              # LCEL RAG 链 + 历史记忆
│   ├── router.py            # 规则路由（qa / summary）
│   └── memory.py           # session 会话存储
├── knowledge/              # RAG 知识库层
│   ├── pdf_parser.py        # PyPDFLoader
│   ├── text_splitter.py    # RecursiveCharacterTextSplitter
│   ├── embedding.py         # HuggingFaceEmbeddings
│   ├── vector_store.py     # FAISS 创建/保存/加载
│   ├── retriever.py        # as_retriever 封装
│   └── knowledge_base.py   # build / list
└── frontend/               # Vue 3 前端
    └── src/
        ├── App.vue
        ├── api/             # chat / paper / upload
        └── components/      # Sidebar / Chatwindow
```

## 快速开始

**后端**（http://127.0.0.1:8000）

```bash
pip install -r requirements.txt
python app.py
```

**前端**（http://localhost:5173）

```bash
cd frontend
npm install
npm run dev
```

打开浏览器 → 上传 PDF → 选中论文 → 提问。

## 配置

- **API Key**：[config.py](config.py) 中的 `DEEPSEEK_API_KEY`，建议改用环境变量
- **嵌入模型路径**：[knowledge/embedding.py](knowledge/embedding.py) 中的 `model_name`，按实际路径修改

## License

MIT
