# llm_setup.py
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


def initialize_llm(model_name="openai/gpt-oss-120b", temperature=0, max_retries=2):
    """Initialize the LLM model"""
    return ChatGroq(
        model=model_name,
        temperature=temperature,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=max_retries
    )


# Create a shared model instance
model = initialize_llm()
llm = initialize_llm()