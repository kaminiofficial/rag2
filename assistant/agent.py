from langchain.agents import create_agent
from assistant import config  
from assistant.logger import get_logger 

logger=get_logger(__name__)

def langchain_agent(llm,tools):
    agent = create_agent(model=llm,tools=tools,system_prompt=config.SYSTEM_PROMPT)
    logger.info
    return agent