# AI PDF Chatbot (RAG System)

An AI-powered PDF Question Answering application that enables users to upload PDF documents and ask natural language questions about their content. The system uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant document sections and generate context-aware responses.

---

## Features

* Upload and process PDF documents
* Extract and chunk document text
* Generate semantic embeddings for efficient retrieval
* Perform similarity search using FAISS vector database
* Answer questions using a Large Language Model (Groq LLaMA)
* Interactive chat interface built with Streamlit

---

## Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* Groq API (LLaMA)
* PyPDF

---

## System Workflow

```text
PDF Upload
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Database
      ↓
Similarity Search
      ↓
Groq LLM
      ↓
Context-Aware Response
```

---

## Project Structure

```
pdf-chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
└── utils/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── embeddings.py
    ├── vectorstore.py
    └── rag_chain.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/farwaraza/AI-PDF-Chatbot
cd AI-PDF-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## How It Works

1. The user uploads a PDF document.
2. The document text is extracted and divided into smaller chunks.
3. Each chunk is converted into vector embeddings.
4. FAISS indexes the embeddings for semantic similarity search.
5. When a question is asked, the most relevant chunks are retrieved.
6. The retrieved context is sent to the Groq LLM.
7. The model generates a response grounded in the document content.

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Semantic Search
* Vector Databases
* Embedding Generation
* Prompt Engineering
* LangChain Workflows
* Streamlit Application Development

---

## Future Improvements

* Multiple PDF support
* Persistent vector database storage
* Chat history persistence
* Source citation highlighting
* Conversation memory
* File management dashboard

---
