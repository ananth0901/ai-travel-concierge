from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def load_and_index(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        chunks,
        OpenAIEmbeddings(),
        persist_directory="db"
    )
    db.persist()

    return db
