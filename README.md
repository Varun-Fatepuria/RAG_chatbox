ARCHITECTURE 
[ User Interface ]  🌐 Streamlit Web UI (Session State Management)
          │
          ▼
  [ Orchestrator ]     ⛓️ LangChain / LangChain-Classic / Text-Splitters
          │
   ───────┴──────────────────────────
   |                                 |
   ▼ (Local CPU / App Instance)      ▼ (External Cloud API)
┌──────────────────────────────┐   ┌──────────────────────────────┐
│  📄 PyPDF2 Text Extraction   │   │                              │
│              │               │   │                              │
│              ▼               │   │                              │
│  ✂️ Recursive Chunking      │   │   🤖 Google Gemini API        │
│              │               │   │      (gemini-3.5-flash)      │
│              ▼               │   │   Generates final semantic   │
│  🤗 Hugging Face Embeddings  │   │   responses with 1M context  │
│     (all-MiniLM-L6-v2)       │   │                              │
│              │               │   │                              │
│              ▼               │   │                              │
│  🗄️ FAISS Vector Database   │   │                              │
└──────────────────────────────┘   └──────────────────────────────┘
