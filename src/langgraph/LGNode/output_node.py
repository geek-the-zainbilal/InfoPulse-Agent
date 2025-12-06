from src.langgraph.LGState.state import State

def show_output(state: State) -> State:
    # Check if LLM news exists
    if 'llm_news' in state:
        output = state['llm_news']
        print("AI News:")
    elif 'tavily_news' in state:
        output = state['tavily_news']
        print("Tavily News:")
    else:
        output = "No news available"
        print("Nothing found:")
    
    print(output)
    return {"last_output": output}
    