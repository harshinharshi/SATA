# main.py
import sys
import os

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import load_environment
from llm_setup import llm, model
from prompts import SYSTEM_PROMPT_QUERY_CREATION_AGENT
from query_agent import parse_user_input
from graph_nodes import State, node_a, node_b, node_c
from graph_builder import build_graph, display_graph, execute_graph

def main():
    """Main execution function"""
    # Load environment variables
    load_environment()
    
    # Test LLM translation
    print("Testing LLM translation...")
    test_translation()
    
    # Test query creation agent
    print("\nTesting query creation agent...")
    test_query_agent()
    
    # Build and execute graph
    print("\nBuilding and executing workflow graph...")
    
    # Create custom node functions with dependencies
    def custom_node_a(state):
        return node_a(state, llm, SYSTEM_PROMPT_QUERY_CREATION_AGENT)
    
    def custom_node_b(state):
        return node_b(state)
    
    def custom_node_c(state):
        return node_c(state)
    
    # Build graph
    graph = build_graph(custom_node_a, custom_node_b, custom_node_c)
    
    # Display graph
    display_graph(graph)
    
    # Execute graph
    input_state = State(output=["Module is Ordering, Application is Manage Central Purchase Contract, Process is GR Contract Change"])
    final_result = execute_graph(graph, input_state)
    
    return final_result

def test_translation():
    """Test the LLM translation functionality"""
    messages = [
        ("system", "You are a helpful assistant that translates English to Malayalam. Translate the user sentence."),
        ("human", "I love programming."),
    ]
    ai_msg = model.invoke(messages)
    print(f"Translation: {ai_msg.content}")

def test_query_agent():
    """Test the query creation agent"""
    test_input = "Module is Ordering, Application is Manage Central Purchase Contract, Process is GR Contract Change"
    result = parse_user_input(model, SYSTEM_PROMPT_QUERY_CREATION_AGENT, test_input)
    print(f"Parsed result: {result}")

if __name__ == "__main__":
    main()