from assistant import config
from assistant.llm import get_llm
from assistant.vector_store import load_vector_store, get_retriever, vector_store_exists, create_vector_store, save_vector_store


from assistant.tool import create_tool
from assistant.agent import langchain_agent
from assistant.splitter import split_text
from assistant.embeddings import get_embeddings
from assistant.loader import load_data
from assistant.logger import get_logger

logger = get_logger(__name__)


def build_vector_store(data):
    logger.info("Building vector store...")
    if vector_store_exists(config.vector_store_path):

        logger.info("Loading existing vector store...")
        vector_store = load_vector_store(config.vector_store_path)
        logger.info("Vector store loaded successfully.")
        return vector_store
    
    logger.info("Creating new vector store...")
    data= load_data()
    chunks = split_text(data)
    vector_store = create_vector_store(chunks)
    save_vector_store(vector_store, config.vector_store_path)
    return vector_store

def build_assistant(data):
    logger.info("Building assistant...")

    config.check_api_key()
    config.check_tracing()
    vector_store = build_vector_store(data)
    retriever = get_retriever(vector_store)
    tool = create_tool(retriever)
    llm = get_llm()
    agent = langchain_agent(llm, [tool])
    logger.info("Assistant built successfully.")
    return agent

def ask_question(assistant, question):
        logger.info(f"Asking question: {question}")
        response = assistant.invoke({"messages": [{"role": "user", "content": question}]})
        answer= response['messages'][-1].content
        logger.info(f"Received answer: {answer}")
        return answer
