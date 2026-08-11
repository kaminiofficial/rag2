from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\KAMINI TYAGI\\OneDrive\\Documents\\Desktop\\rag2\\rag2env\\.env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")


MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v3"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


vector_store_path = "C:\\Users\\KAMINI TYAGI\\OneDrive\\Documents\\Desktop\\rag2\\rag2env\\faiss_index"

TOP_K = 5


SYSTEM_PROMPT = """You are a helpful assistant that answers questions based on the context provided.
If you don't know the answer, just say that you don't know, don't try to make up an answer."""

def check_api_key():
    if not GROQ_API_KEY :
        raise ValueError("GROQ_API_KEY is NOT FOUND")
    if not JINA_API_KEY :
        raise ValueError("JINA_API_KEY is NOT FOUND")