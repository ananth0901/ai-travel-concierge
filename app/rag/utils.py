import os
import time

def load_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found!")
    return api_key

def save_uploaded_file(uploaded_file):
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

def clean_text(text):
    return text.replace("\n", " ").strip()

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

def extract_sources(docs):
    sources = []
    for doc in docs:
        if "source" in doc.metadata:
            sources.append(doc.metadata["source"])
    return list(set(sources))

def handle_error(e):
    return f"Error: {str(e)}"

def log(message):
    print(f"[{time.strftime('%H:%M:%S')}] {message}")
