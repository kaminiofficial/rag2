from langchain.agents import create_agent
from assistant import config    

def langchain_agent(llm,tools):
    agent = create_agent(model=llm,tools=tools,system_prompt=config.SYSTEM_PROMPT)
    return agent