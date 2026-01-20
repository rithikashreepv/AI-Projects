from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a:float,b: float):
    print("works1")
    return f" The sum of {a} + {b} is {a + b}"
@tool
def greeting(name:str):
    print("works")
    return f" hello { name} nice to see you"
    
   

def main():
    model = ChatOpenAI(temperature =0)
    tools =[calculator,greeting]
    agent_excecutor = create_react_agent(model,tools)
    print("Hi!!!! Im Your AI assistant.To exit type 'quit'")
    print("Tell me what are you feeling")

    while True:
        user_input= input("\n You:").strip()
        if user_input == "quit":
            break

        print("\nAssistant:", end ="")
        for chunk in agent_excecutor.stream( {"messages":[HumanMessage(content = user_input)]}):
            if "agent" in chunk and  "messages" in chunk["agent"]: 
                for message in chunk["agent"]["messages"]:
                    print(message.content, end ="")
        print()
if __name__ == "__main__":
    main()





