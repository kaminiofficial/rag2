import os
from langchain_community.vectorstores import FAISS
from assistant import config
from assistant.embeddings import get_embeddings
from assistant.loggerlogger import get_logger

logger = get_logger(__name__)


def create_vector_store(chunks):

    logger.info("Creating vector store from document chunks...")

    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    logger.info("Vector store created successfully.")
    return vector_store

def save_vector_store(vector_store, path=config.vector_store_path):
    vector_store.save_local(path)

def load_vector_store(path=config.vector_store_path): 
       embeddings = get_embeddings()
       vector_store = FAISS.load_local(path, embeddings,allow_dangerous_deserialization =True)
       logger.info("Vector store loaded successfully.")
       return vector_store

def vector_store_exists(path = config.vector_store_path):
    logger.info(f"Checking if vector store exists at {path}")
    return os.path.exists(path)

def get_retriever(vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": config.TOP_K})
    logger.info("Retriever created successfully.")
    return retriever
