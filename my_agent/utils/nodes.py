# nodes.py
from langchain_core.messages import SystemMessage, HumanMessage
import json
from my_agent.utils.state import State
from my_agent.utils.tools import fetch_data_required


def node_a(state: State, llm, system_prompt) -> State:
    """Node A: Parse user input into structured JSON"""
    print("Node A received input:", state['output'][-1])
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=state['output'][-1])
    ]
    result = llm.invoke(messages)
    return State(output=[result.content])


def node_b(state: State) -> State:
    """Node B: Fetch data from database"""
    print("Node B processing...")
    try:
        input_string = state['output'][-1]
        filter_data = json.loads(input_string)
        
        result = fetch_data_required(filter_data)
        
        if result:
            json_result = json.dumps(result, ensure_ascii=False)
            return State(output=[json_result])
        else:
            return state
            
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return state
    except Exception as e:
        print(f"Unexpected error in node_b: {e}")
        return state


def node_c(state: State) -> State:
    """Node C: Process final result"""
    print("Node C received input:", state['output'][-1])
    # Additional processing can be added here
    return state