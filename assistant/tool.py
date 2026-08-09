from langchain.tools import tool

def create_tool(retriever):
    ''' Creates a tool for the agent to use for retrieving information from the vector store.'''
    @tool
    def search(query: str):
        ''' Searches the vector store for relevant information based on the query.'''
        docs = retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])
    return search