# graph_builder.py
from langgraph.graph import END, START, StateGraph
from IPython.display import Image, display
from graph_nodes import State

def build_graph(node_a_func, node_b_func, node_c_func):
    """Build and return the workflow graph"""
    builder = StateGraph(State)
    
    # Add nodes
    builder.add_node("a", node_a_func)
    builder.add_node("fetch_data", node_b_func)
    builder.add_node("c", node_c_func)
    
    # Add edges
    builder.add_edge(START, "a")
    builder.add_edge("a", "fetch_data")
    builder.add_edge("fetch_data", "c")
    builder.add_edge("c", END)
    
    return builder.compile()

def display_graph(graph):
    """Display the graph visualization"""
    display(Image(graph.get_graph().draw_mermaid_png()))

def execute_graph(graph, input_state):
    """Execute the graph with given input state"""
    print("Streaming graph execution:")
    for event in graph.stream(input_state):
        print(event)
        print("-" * 50)
    
    print("\nFinal result:")
    return event