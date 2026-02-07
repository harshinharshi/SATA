from langchain_core.messages import SystemMessage, HumanMessage
import json

def create_query_agent_prompt(system_prompt, user_input):
    """Create messages for query agent"""
    return [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

def parse_user_input(model, system_prompt, user_input):
    """Parse user input into structured JSON using LLM"""
    messages = create_query_agent_prompt(system_prompt, user_input)
    response = model.invoke(messages)
    return response.content