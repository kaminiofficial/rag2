from langchain_community.embeddings import JinaEmbeddings
from assistant.logger import get_logger

logger = get_logger(__name__)

from assistant import config
def get_embeddings():
    logger.info(f"Initializing Jina embeddings... {config.EMBEDDING_MODEL_NAME}")
    embeddings = JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME,
                                JINA_API_KEY=config.JINA_API_KEY)
    return embeddings