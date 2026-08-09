

from langchain_community.document_loaders import WebBaseLoader

def load_data():
 loader = WebBaseLoader(["https://docs.langchain.com//oss//python//langchain//overview" , "https://docs.langchain.com//oss//python//langchain//short-term-memory"])
 data = loader.load()
 return data
