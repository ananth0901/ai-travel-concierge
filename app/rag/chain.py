from langchain.chat_models import ChatOpenAI

def generate_answer(query, docs, memory):
    llm = ChatOpenAI(temperature=0)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an intelligent assistant.
    
    Context:
    {context}
    
    Question:
    {query}
    
    Answer clearly with sources.
    """

    response = llm.predict(prompt)

    return response
