#================ Small Note ========================== 
# This layer basically still use some functions from LangChain 
# But you may notice that I did not use create_agent function 
# Thats mean I will need to implement my own agent loop and tool call handling. 



from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage 
from langsmith import traceable
load_dotenv()
MAX_ITERATIONS = 5
MODEL = "qwen3:1.7b"  
@tool
def get_product_price(product:str) ->float: 
    """Look up the price of a product"""

    print(f" Looking up price for {product}...")
    # Simulate looking up the price of a product
    prices = {
        "laptop": 999.99,
        "smartphone": 499.99,
        "headphones": 199.99,
    }
    return prices.get(product.lower(), 0.0)

@tool
def apply_discount(price:float, discount_tier:str) ->float: 
    """Apply a discount to a price based on the discount tier
        Available discount tiers: bronze, silver, gold
    """

    print(f"Applying {discount_tier} discount to price {price}...")
    # Simulate applying a discount based on the discount tier
    discounts = {
        "bronze": 0.05,
        "silver": 0.10,
        "gold": 0.15,
    }
    discount = discounts.get(discount_tier.lower(), 0.0)
    return price * (1 - discount)


#--- Agent Loop ----- 
@traceable(name="agent_loop", project="agent_course")
def run_agent(question:str): 
    tools = [get_product_price, apply_discount]  
    tool_dict = {t.name : t for t in tools}

    llm = init_chat_model(MODEL, temperature=0)

    llm_with_tools = llm.bind_tools(tools)
    print("Starting agent loop..." )
    print(f"Question: {question}")
    print("-" * 50)

    messages = [
        SystemMessage(content="You are a helpful assistant that answers questions about product prices and applies discounts." \
        "\n\nYou have access to the following tools:" \
            "\n- get_product_price(product:str) -> float: Look up the price of a product" \
            "\n- apply_discount(price:float, discount_tier:str) -> float: Apply a discount to a price based on the discount tier" \
        ),
        HumanMessage(content=question)
    ]

    for iteration in range(MAX_ITERATIONS):
        print(f"Iteration {iteration + 1}...")
        
        ai_message = llm_with_tools.invoke(messages)
        tool_calls = ai_message.tool_calls 

        # If no tool calls, we assume the model is done and returns the final answer
        if not tool_calls:
            print("No tool calls, final answer:")
            print(ai_message.content)
            return ai_message.content
        
        # Process each tool call
        tool_call = tool_calls[0]  # For simplicity, we only handle one tool call per iteration
        tool_name = tool_call.get("name")
        tool_args = tool_call.get("args", {})
        tool_call_id = tool_call.get("id")

        print(f"[Tool Selected] {tool_name} with args {tool_args} and id {tool_call_id}")

        tool_to_use = tool_dict.get(tool_name)
        if not tool_to_use:
            print(f"Tool {tool_name} not found. Skipping tool call.")
            continue
        observation = tool_to_use.invoke(tool_args)
        print(f"[Observation] {observation}") 
        messages.append(ai_message)  # Add the AI message with the tool call to the conversation
        messages.append(
            ToolMessage(
                content=str(observation),
                tool_call_id=tool_call_id
            )
        )
    print("Max iterations reached, final answer:")
    print(ai_message.content)
    return ai_message.content

if __name__ == "__main__":
    print("Hello Agent Loop")
    question = "What is the price of a laptop with a silver discount?"
    result = run_agent(question) 
    # print(f"Final Result: {result}")