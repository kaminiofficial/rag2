from langchain_groq import ChatGroq
from assistant import config
def get_llm():
    model = ChatGroq(
        model_name=config.MODEL_NAME,
        api_key=config.GROQ_API_KEY,
        temperature=0.5,)
    return model