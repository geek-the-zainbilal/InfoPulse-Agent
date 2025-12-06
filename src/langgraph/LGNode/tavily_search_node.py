from src.langgraph.LGState.state import State
from src.main import search_tool

def latest_search_news(state: State) -> State:
    query = state.get("topic", "")
    response2 = search_tool.search(query=query, max_results=2)
    
    # Combine results into a single string
    combined_news = ""
    for obj in response2.get("results", []):
        combined_news += f"{obj['content']}"
    
    # Save into state under 'tavily_news'
    state['tavily_news'] = combined_news.strip()
    
    return state
