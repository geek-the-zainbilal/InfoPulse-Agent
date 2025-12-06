from src.langgraph.LGState.state import State

def get_news_topic(state:State)->State:
    return {"topic":state["topic"]}