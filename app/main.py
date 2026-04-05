import streamlit as st
import os
from rag.ingest import load_and_index
from rag.chain import generate_answer
from rag.memory import get_memory

st.title("🔥 Advanced AI RAG System")

api_key = st.text_input("Enter API Key", type="password")
uploaded_file = st.file_uploader("Upload PDF")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

memory = get_memory()

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    db = load_and_index("temp.pdf")

    query = st.text_input("Ask something")

   if query:
    docs = db.similarity_search(query)

    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(streaming=True)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Context:
    {context}

    Question:
    {query}
    """

    response = llm.stream(prompt)

    for chunk in response:
        st.empty(chunk.content, end="")
        with st.expander("📚 View Sources"):
    for i, doc in enumerate(docs):
        st.write(f"Source {i+1}: {doc.metadata.get('source', 'Unknown')}")
