from typing import Optional

import os
import re
import gradio as gr
import yaml
import random

from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

from dotenv import load_dotenv
load_dotenv()

DATA_DIR = "company_documents"
USER = {"role": "guest"}

embedder_model = SentenceTransformer("all-MiniLM-L6-v2")

class SentenceTransformerEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return embedder_model.encode(texts).tolist()

    def embed_query(self, text):
        return embedder_model.encode([text])[0].tolist()

embeddings = SentenceTransformerEmbeddings()

vectorstore = Chroma(
    persist_directory="./chroma_db",
    collection_name="aether_collection",
    embedding_function=embeddings,
)

def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^---\n(.*?)\n---\n?", content, re.DOTALL)
    if fm_match:
        frontmatter = yaml.safe_load(fm_match.group(1)) or {}
        body = content[fm_match.end():]
    else:
        frontmatter = {}
        body = content

    body = re.sub(r"\n---\n", "\n", body)

    if not body.startswith("\n"):
        body = "\n" + body

    sections = re.split(r'\n(?=#{1,6} )', body)

    docs = []

    raw_roles = frontmatter.get("allowed_roles", [])
    roles = raw_roles if isinstance(raw_roles, list) else [raw_roles]

    for section in sections:
        section = section.strip()
        if not section:
            continue

        lines = section.split("\n")
        section_title = lines[0].strip()

        if section_title.strip("-") == "":
            continue

        docs.append(
            Document(
                page_content=(
                    f"DOCUMENT: {frontmatter.get('title', '')}\n"
                    f"SECTION: {section_title}\n"
                    f"CONTENT:\n{section}"
                ),
                metadata={
                    "section": section_title,
                    "allowed_roles": roles,
                    "access_level": frontmatter.get("access_level", ""),
                    "department": frontmatter.get("department", ""),
                    "date": frontmatter.get("date", "")
                }
            )
        )

    return docs

def ingest_documents():
    if vectorstore._collection.count() > 0:
        return

    all_docs = []

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    for file in os.listdir(DATA_DIR):
        if file.endswith(".md"):
            all_docs.extend(parse_markdown(os.path.join(DATA_DIR, file)))

    if all_docs:
        vectorstore.add_documents(all_docs)

def retrieve(query):
    return vectorstore.as_retriever(search_kwargs={"k": 3}).invoke(query)

def filter_docs(docs):
    filtered = []
    for doc in docs:
        roles = doc.metadata.get("allowed_roles", [])
        if USER["role"] in roles:
            filtered.append(doc)

    return filtered

def get_suggested_question(role):
    try:
        data = vectorstore.get()
        metadatas = data.get("metadatas", [])
        if not metadatas:
            return "Could you summarize the main policies?"
            
        valid_docs = []
        for meta in metadatas:
            roles = meta.get("allowed_roles", [])
            if role in roles:
                valid_docs.append(meta)
                
        if valid_docs:
            chosen = random.choice(valid_docs)
            section = chosen.get("section", "").lstrip('#').strip()
            if section:
                return f"{section}{'?' if '?' not in section else ''}"
        
        return "Could you summarize the main policies?"
    except Exception as e:
        print(f"Error generating suggestion: {e}")
        return "Could you summarize the main policies?"

def respond(
    message,
    history: list[dict[str, str]],
    role,
    system_message,
    max_tokens,
    temperature,
    top_p,
    hf_token: Optional[gr.OAuthToken]
):
    USER["role"] = role

    docs = retrieve(message)
    docs = filter_docs(docs)

    pattern = r"^.*\?\n"
    for doc in docs:
        doc.page_content = re.sub(pattern, "", doc.page_content, flags=re.DOTALL).strip()

    if len(message) < 3:
        yield "Your query is too short. Please try again."
        return

    if len(message) > 80:
        yield "Your query is too long. Please try again."
        return

    if not docs:
        yield "I cannot help you with that. Try asking something else!"
        return

    context = ' '.join([d.page_content for d in docs[:2]])

    prompt = f"""Context:
{context}

You are a question-answering assistant. Use the following context to answer the question. If the context does not suggest a reliable answer, say, "I cannot help you with that!" Write detailed, product and proper English answers ONLY.

Question: {message}"""

    token = hf_token.token if (hf_token and hasattr(hf_token, 'token')) else os.getenv("HF_TOKEN")
    client = InferenceClient(token=token, model="openai/gpt-oss-20b")

    messages = [{"role": "system", "content": system_message}]

    if history:
        if isinstance(history[0], dict):
            messages.extend(history)
        else:
            for user_msg, bot_msg in history:
                if user_msg:
                    messages.append({"role": "user", "content": user_msg})
                if bot_msg:
                    messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": prompt})

    response = ""
    try:
        for msg in client.chat_completion(
            messages,
            max_tokens=max_tokens,
            stream=True,
            temperature=temperature,
            top_p=top_p,
        ):
            choices = msg.choices
            token_str = ""
            if len(choices) and choices[0].delta.content:
                token_str = choices[0].delta.content

            response += token_str
            yield response
    except Exception as e:
        yield f"Error generating response. Please check your Hugging Face login or token. Details: {e}"
        return

    suggestion = get_suggested_question(USER["role"])
    yield response + f"\n\n💡 **Suggested next question:** {suggestion}"


print("Initializing system...")
ingest_documents()
print("Ready.\n")

try:
    chatbot = gr.ChatInterface(
        respond,
        type="messages",
        title="Aether Corporations",
        description="Role-Based Access Control / Multi-Document RAG Agent",
        additional_inputs=[
            gr.Dropdown(
                choices=["guest", "engineer", "hr", "finance", "executive"], 
                value="guest", 
                label="Simulated User Role",
                info="Select a role to see how document access control affects responses."
            ),
            gr.Textbox(value="You are a friendly and helpful question-answering assistant for Aether Corporations. Use the provided context to answer questions.", label="System message"),
            gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
            gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
            gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.95,
                step=0.05,
                label="Top-p (nucleus sampling)",
            ),
        ],
    )
except TypeError:
    # Fallback for Gradio < 4.x or environments where type="messages" is invalid
    chatbot = gr.ChatInterface(
        respond,
        title="Aether Corporations",
        description="Role-Based Access Control / Multi-Document RAG Agent",
        additional_inputs=[
            gr.Dropdown(
                choices=["guest", "engineer", "hr", "finance", "executive"], 
                value="guest", 
                label="Simulated User Role",
                info="Select a role to see how document access control affects responses."
            ),
            gr.Textbox(value="You are a friendly and helpful question-answering assistant for Aether Corporations. Use the provided context to answer questions.", label="System message"),
            gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
            gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
            gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.95,
                step=0.05,
                label="Top-p (nucleus sampling)",
            ),
        ],
    )

with gr.Blocks() as demo:
    with gr.Sidebar():
        gr.LoginButton()
    chatbot.render()

if __name__ == "__main__":
    demo.launch()
