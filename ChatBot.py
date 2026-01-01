from langgraph.graph import StateGraph,START,END    
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated
from dotenv import load_dotenv
from typing import List
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

chatllm=ChatOpenAI()

class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage],add_messages]

def chatnode(state:ChatState):
    response=chatllm.invoke(state["messages"])
    return {"messages":[response]}

checkpointer=MemorySaver()

graph=StateGraph(ChatState)

graph.add_node("chat",chatnode)

graph.add_edge(START,"chat")
graph.add_edge("chat",END)

workflow=graph.compile(checkpointer=checkpointer)

thread_id='1'

while True:
    user_input=input("User:")
    if user_input.strip().lower()in ["exit","quit","bye"]:
        break
    config= {'configurable' :{'thread_id':thread_id}}
    
    response = workflow.invoke({"messages":[HumanMessage(content=user_input)]},config=config)

    print("Bot:",response["messages"][-1].content) 


