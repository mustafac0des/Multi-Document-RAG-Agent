# Aether Corporations Multi-Document RAG Agent

## Overview
A Retrieval-Augmented Generation (RAG) system built with Gradio to securely query internal company documents. The system uses a multi-document approach with Role-Based Access Control (RBAC) to ensure users only receive information they are authorized to access.

## Features
* **Role-Based Access Control (RBAC)**: Documents are filtered based on the user's role (e.g., guest, engineer, hr, finance, executive).
* **Multi-Document Ingestion**: Parses Markdown files containing YAML frontmatter to extract metadata (allowed roles, title, etc.) and chunks the content by headers.
* **Vector Database**: Uses ChromaDB to store and retrieve document embeddings efficiently.
* **Local LLM & Embeddings**: Utilizes open-source models (`google/flan-t5-base` for generation and `all-MiniLM-L6-v2` for embeddings).
* **Gradio Interface**: Provides an easy-to-use web chat interface to interact with the agent.

## Tech Stack
* **UI Framework:** Gradio
* **Vector Store:** Chroma (Langchain Integration)
* **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)
* **LLM:** HuggingFace Transformers (`google/flan-t5-base`)
* **Orchestration:** Langchain Core

## Project Structure
* `app.py`: Main application script running the RAG pipeline, document ingestion, and Gradio UI.
* `company_documents/`: Directory containing internal company knowledge base in Markdown format with YAML frontmatter.
* `chroma_db/`: Persistent local vector database storage generated upon initial ingestion.

## Setup and Installation

1. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install gradio transformers sentence-transformers langchain-core langchain-chroma pyyaml python-dotenv torch
   ```
2. **Set up Environment Variables**:
   Create or modify the `.env` file in the root directory if any specific environment variables are needed.

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```
2. **Access the Web UI**:
   The terminal will output a local URL (typically `http://127.0.0.1:7860`). Open this in your web browser.
3. **Interact with the Agent**:
   * Select a simulated user role from the dropdown (e.g., hr, executive, engineer).
   * Ask questions related to the company documents.
   * The responses will be generated dynamically but are constrained to the documents the chosen role has permission to access.
