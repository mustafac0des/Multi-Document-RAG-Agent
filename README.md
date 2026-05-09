---
title: Multi Document RAG Agent
emoji: ⚡
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 6.14.0
python_version: '3.13'
app_file: app.py
pinned: false
license: apache-2.0
short_description: Multi-Document RAG Agent
---

# 👥 Role-Based Access Control RAG Agent

A powerful and secure AI chatbot that allows employees to query internal company documents with strict role-based access control.

## ✨ Features

- 🔐 **Role-Based Access Control (RBAC)** - Users only see information they are authorized to access based on their simulated role
- 📚 **Multi-Document Ingestion** - Processes Markdown files and extracts valuable metadata for precise querying
- 🧠 **Local LLM & Embeddings** - Fully local generation and embeddings using open-source HuggingFace models for data privacy
- 🗃️ **Vector Database** - Utilizes ChromaDB for fast, efficient, and persistent document retrieval
- 💬 **Gradio Interface** - An easy-to-use, interactive web UI for chatting with the AI

## 🚀 Getting Started

### Installation
1. Clone the repository
2. Install the required dependencies: `pip install gradio transformers sentence-transformers langchain-core langchain-chroma pyyaml python-dotenv torch`
3. Create or configure your `.env` file in the root directory

### Running the App
1. Open your terminal in the project folder
2. Run the application: `python app.py`
3. Access the web interface via the local URL provided (usually `http://127.0.0.1:7860`)

## 🎯 Quick Tips

- Use the role dropdown to test how different roles (e.g., HR, Executive, Engineer) affect the AI's responses
- Ensure your Markdown documents in the `company_documents` folder have correct YAML frontmatter for roles
- Ask specific, detailed questions for the best response from the LLM
- If the AI says "I cannot help you with that!", try changing your simulated role to one with higher clearance

## ❓ Questions?

- **Can I add new documents?** - Yes, place new Markdown files in the `company_documents` folder and restart the app
- **How do I change roles?** - Select a different role from the dropdown menu in the Gradio UI
- **Is my data sent to the cloud?** - No, the app uses local embeddings and a local LLM (`google/flan-t5-base`) to keep data secure
- **Why is the AI not answering my question?** - You either lack the required role to view the source document, or the answer isn't in the knowledge base

## 🛠️ Tech Stack

- **UI Framework**: Gradio
- **Vector Store**: ChromaDB
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
- **LLM**: HuggingFace Transformers (`google/flan-t5-base`)
- **Orchestration**: Langchain Core