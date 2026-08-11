from langchain_groq import ChatGroq
from assistant import config
from assistant.logger import get_logger

logger=get_logger(__name__)

def get_llm():

    logger.info(f"loading the model {config.MOAEL_NAME}")
    model = ChatGroq(
        model_name=config.MODEL_NAME,
        api_key=config.GROQ_API_KEY,
        temperature=0.5,)
    return model