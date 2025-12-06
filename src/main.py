import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tavily import TavilyClient

load_dotenv()
groqapikey=os.getenv("GROQ_API_KEY")
tavilyapikey=os.getenv("TAVILY_API_KEY")

llm=ChatGroq(model="llama-3.1-8b-instant",api_key=groqapikey)
search_tool = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))