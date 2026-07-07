Multi-PDF Context-Aware Chatbot (Cost-Free Hybrid RAG Stack)
A highly optimized, production-ready Retrieval-Augmented Generation (RAG) application that allows users to upload multiple heavy PDF documents and interact with their content dynamically using natural language.
By shifting the computational footprint of text chunk vectorization locally on-device and leveraging high-performance, free cloud inference endpoints, this system operates at a total infrastructure cost of  RS 0.00.

System Architecture
This project deliberately avoids full reliance on costly third-party cloud data-ingestion systems by splitting tasks between the local CPU wrapper and asymmetric model orchestration.
[ Multi-PDF Uploads ] ──► [ PyPDF2 Text Extraction ]
                                      │
                                      ▼
                        [ Recursive Character Splitter ]
                                      │
                                      ▼
                        [ HuggingFace Embeddings ] (Local Compute)
                                      │
                                      ▼
                        [ FAISS Vector Index Store ] (In-Memory KNN)
                                      ▲
                                      │ (Similarity Retrieval)
  [ User Query ] ─────────────────────┴──► [ Stuffed Context Context Prompt ]
                                                      │
                                                      ▼
                                           [ Google Gemini API ] 
                                            (gemini-3.5-flash)

Key Technical Talking Points:
Decoupled Architecture: Text embeddings are calculated locally on-device via a 384-dimensional lightweight transformer matrix (all-MiniLM-L6-v2), completely eliminating pay-per-token API embedding dependencies.

Reduced Memory Footprint: Using a 384-dimension local index instead of a standard 1536-dimension vector model reduces application memory consumption inside the active running instance thread by 75%.

Frontier Generation: Context vectors are parsed, compiled into stuffed system instructions, and processed through Google Gemini's lightning-fast gemini-3.5-flash engine using its generous free tier.

Core Features
Multi-File Batch Ingestion: Drag and drop multiple complex PDF files simultaneously.

Overlapping Sliding Chunk Matrix: Text segmentation preserves syntactic context over token boundaries using automated mathematical text splitters.

Reactive Session Chat Layout: Interactive conversational visual interface displaying styled chat history balloons with immediate context resolution.

Ultra-Low Latency Index Search: Employs an exact K-Nearest Neighbors (KNN) matrix query algorithm inside RAM for instant vector lookup.

 Tech Stack
Frontend Framework: Streamlit (Dynamic state-driven web framework)

Orchestration: LangChain Ecosystem (langchain-core, langchain-community, langchain-text-splitters)

Local Embedding Engine: Hugging Face Transformers via langchain-huggingface

Foundational LLM Client: Google AI Studio via langchain-google-genai

Vector Database: FAISS (Facebook AI Similarity Search)

File Extractors: PyPDF2

 Installation & Local Setup
1. Clone the Repository
Bash
git clone https://github.com/Varun-Fatepuria/RAG_chatbox.git
cd RAG_chatbox
2. Set Up a Virtual Environment
Bash
# Create the environment
python -m venv venv

# Activate the environment (MacOS/Linux)
source venv/bin/activate

# Activate the environment (Windows)
venv\Scripts\activate
3. Install Required Dependencies
Create a requirements.txt file if you haven't already, then run:

Bash
pip install -r requirements.txt
Note: Ensure your requirements.txt contains the following optimized modern package layout:

Plaintext
streamlit
langchain-core
langchain-community
langchain-text-splitters
langchain-huggingface
langchain-google-genai
faiss-cpu
PyPDF2
python-dotenv
sentence-transformers
4. Configure Environment Secrets
Create a .env file in the root directory of your project and populate it with your Google AI Studio API key:

Code snippet
GOOGLE_API_KEY=your_actual_free_gemini_api_key_here
How to Use
Launch the application from your terminal workspace:

Bash
streamlit run app.py
Open your browser to the local running network address (usually http://localhost:8501).

Locate the sidebar pane and drop your sample target PDF files into the file system drag zone.

Click "Submit & Process" to invoke the text-extraction thread, calculate local structural vectors, and instantiate the FAISS memory index.

Once processing finishes, enter any natural language question inside the main chat input field to see response streaming.

DEPLOYED WEBSITE => https://ragchatbox-5yjdfuefghsei3wycjtlfm.streamlit.app/
