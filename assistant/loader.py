

from langchain_community.document_loaders import WebBaseLoader
from assistant.logger import get_logger

logger = get_logger(__name__)

def load_data():
 logger.info("Loading data from web pages...")
 loader = WebBaseLoader(["https://docs.langchain.com//oss//python//langchain//overview" , "https://docs.langchain.com//oss//python//langchain//short-term-memory"])
 data = loader.load()
 logger.info(f"Loaded {len(data)} documents from web pages.")
 return data
