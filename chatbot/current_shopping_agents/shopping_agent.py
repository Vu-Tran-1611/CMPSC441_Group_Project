import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langsmith import traceable
from tools.product_tools import search_products
from tools.policy_retrieval_tools import retrieve_policies
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
load_dotenv()  


# MODEL = "qwen3:1.7b" 
# MODEL = "qwen3:8b"
# MODEL = "gpt-5.5" 
MODEL = "gpt-5.4-mini"


@traceable # This for tracing the execution of the shopping_agent function on Langsmith pretty similar to @tool
def shopping_agent(questions):
    tools = [search_products, retrieve_policies] 
    system_prompt = (
        "You are a helpful shopping assistant. Use the available tools to find "
        "products and answer questions about this ecommerce store's policies. "
        "Be polite, friendly, and concise. Use tool results to provide accurate "
        "answers. If a question is unrelated to this ecommerce store, explain "
        "that you can only help with store-related questions."
    )

    # llm = ChatOllama(temperature=0, model=MODEL) # Using local Ollama LLM
    llm = ChatOpenAI( model=MODEL, reasoning_effort="none") # Using Cloud LLM (i.e. OpenAI API)


    agent = create_agent(model=llm, tools=tools, system_prompt=system_prompt)
    result = agent.invoke({"messages": [HumanMessage(content=questions)]})
    return result["messages"][-1].content



if __name__ == "__main__":
    questions = "How to Request a Return" 
    answer = shopping_agent(questions) 
    print(answer)



