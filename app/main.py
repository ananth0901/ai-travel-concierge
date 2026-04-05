import streamlit as st
import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from rag.ingest import load_and_index

st.title("AI Travel RAG Assistant")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    # Save file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load and index
    db = load_and_index("temp.pdf")

    # Ask question
    query = st.text_input("Ask something")

  if query:
    docs = db.similarity_search(query)

    st.write("### 🤖 Answer")
    st.write(answer)

    # 👇 PASTE HERE
    unique_sources = set()

    with st.expander("📚 View Sources"):
        for doc in docs:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "Unknown")

            key = f"{source}-page-{page}"

            if key not in unique_sources:
                unique_sources.add(key)
                st.write(f"📄 {source} | Page {page}")
