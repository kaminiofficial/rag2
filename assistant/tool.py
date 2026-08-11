from langchain.tools import tool
from assistant.logger import get_logger

logger = get_logger(__name__)

def create_tool(retriever):
     ''' Creates a tool for the agent to use for retrieving information from the vector store.'''
     
     @tool
     def search(query: str):
        ''' Searches the vector store for relevant information based on the query.'''
        logger.info(f'searching for relevent documents with {query}')
        docs = retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])
     return search