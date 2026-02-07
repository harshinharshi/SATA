# main.py
"""
Main script for testing and running the LangGraph agent
"""
from my_agent.utils.state import State
from my_agent.utils.tools import load_environment
from my_agent.agent import graph
from IPython.display import Image, display


def display_graph_visualization():
    """Display the graph visualization"""
    try:
        display(Image(graph.get_graph().draw_mermaid_png()))
    except Exception as e:
        print(f"Could not display graph: {e}")


def execute_graph(input_state):
    """Execute the graph with given input state"""
    print("Streaming graph execution:")
    print("=" * 50)
    
    for event in graph.stream(input_state):
        print(event)
        print("-" * 50)
    
    print("\nFinal result:")
    return event


def main():
    """Main execution function"""
    # Load environment variables
    load_environment()
    
    print("LangGraph Agent Workflow")
    print("=" * 50)
    
    # Display graph visualization
    print("\nGraph Structure:")
    display_graph_visualization()
    
    # Test the graph with sample input
    print("\nExecuting graph with sample input...")
    input_state = State(
        output=["Module is Ordering, Application is Manage Central Purchase Contract, Process is GR Contract Change"]
    )
    
    final_result = execute_graph(input_state)
    
    print("\n" + "=" * 50)
    print("Execution completed!")
    
    return final_result


if __name__ == "__main__":
    main()