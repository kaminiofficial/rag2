from assistant import config
from assistant.llm import get_llm
from assistant.vector_store import load_vector_store, get_retriever, vector_store_exists, create_vector_store, save_vector_store


from assistant.tool import create_tool
from assistant.agent import langchain_agent
from assistant.splitter import split_text
from assistant.embeddings import get_embeddings
from assistant.loader import load_data

def build_vector_store(data):
    if vector_store_exists(config.vector_store_path):

        print("Loading existing vector store...")
        vector_store = load_vector_store(config.vector_store_path)
        return vector_store
    
    print("Creating new vector store...")
    data= load_data()
    chunks = split_text(data)
    vector_store = create_vector_store(chunks)
    save_vector_store(vector_store, config.vector_store_path)
    return vector_store

def build_assistant(data):
    vector_store = build_vector_store(data)
    retriever = get_retriever(vector_store)
    tool = create_tool(retriever)
    llm = get_llm()
    agent = langchain_agent(llm, [tool])
    return agent

def ask_question(assistant, question):
        response = assistant.invoke({"messages": [{"role": "user", "content": question}]})
        answer= response['messages'][-1].content
        print('answer:', answer)
        print("------------------------------")
        return answer
