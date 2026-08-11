from langchain_text_splitters import RecursiveCharacterTextSplitter
from assistant import config
from assistant.logger import get_logger

logger = get_logger(__name__)

def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,

    )
    chunks = text_splitter.split_documents(data)
    logger.info(f'splitted the {data} into {len(chunks)} chunks')
    return chunks