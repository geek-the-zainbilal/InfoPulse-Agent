from langgraph.graph import START, END, StateGraph
from src.langgraph.LGState.state import State
from src.langgraph.LGNode.topic_input_node import get_news_topic
from src.langgraph.LGNode.llm_news_node import simple_llm_news
from src.langgraph.LGNode.tavily_search_node import latest_search_news
from src.langgraph.LGNode.output_node import show_output



graph=StateGraph(State)
#_________________________
graph.add_node("I/P",get_news_topic)
graph.add_node("LLMSEARCH",simple_llm_news)
graph.add_node("INTERNET_SEARCH",latest_search_news)
graph.add_node("O/P",show_output)
#_____________________________________________________
graph.add_edge(START,"I/P")
graph.add_edge("I/P","LLMSEARCH")
graph.add_edge("LLMSEARCH","O/P")
graph.add_edge("I/P","INTERNET_SEARCH")
graph.add_edge("INTERNET_SEARCH","O/P")
graph.add_edge("O/P",END)
#______________________________________
graph_builder=graph.compile()


