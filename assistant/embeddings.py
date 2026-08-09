from langchain_community.embeddings import JinaEmbeddings

from assistant import config
def get_embeddings():
    embeddings = JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME,
                                JINA_API_KEY=config.JINA_API_KEY)
    return embeddings