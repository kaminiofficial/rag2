from langchain_text_splitters import RecursiveCharacterTextSplitter
from assistant import config
def split_text(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,

    )
    chunks = text_splitter.split_documents(data)
    return chunks