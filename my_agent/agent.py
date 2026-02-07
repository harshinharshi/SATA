# agent.py
from langgraph.graph import END, START, StateGraph
from my_agent.utils.state import State
from my_agent.utils.nodes import node_a, node_b, node_c
from llm_setup import llm
from prompts import SYSTEM_PROMPT_QUERY_CREATION_AGENT


def build_graph():
    """Build and return the workflow graph"""
    builder = StateGraph(State)
    
    # Create custom node functions with dependencies
    def custom_node_a(state):
        return node_a(state, llm, SYSTEM_PROMPT_QUERY_CREATION_AGENT)
    
    def custom_node_b(state):
        return node_b(state)
    
    def custom_node_c(state):
        return node_c(state)
    
    # Add nodes
    builder.add_node("a", custom_node_a)
    builder.add_node("fetch_data", custom_node_b)
    builder.add_node("c", custom_node_c)
    
    # Add edges
    builder.add_edge(START, "a")
    builder.add_edge("a", "fetch_data")
    builder.add_edge("fetch_data", "c")
    builder.add_edge("c", END)
    
    return builder.compile()


# Create the graph instance
graph = build_graph()