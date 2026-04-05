import streamlit as st
import os
api_key = os.getenv("OPENAI_API_KEY")
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

        # Show answer (temporary)
        st.write("### 🤖 Answer")
        st.write("Answer will come here")

        # Show sources
        st.write("### 📚 Sources:")
        for doc in docs:
            st.write(doc.metadata)
