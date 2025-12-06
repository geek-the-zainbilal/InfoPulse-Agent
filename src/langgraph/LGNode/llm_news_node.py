from src.langgraph.LGState.state import State
from src.main import llm

def simple_llm_news(state:State)->State:
    req=state['topic']
    prompt = f"""
            Okay you are an expert AI News Researcher 
            Fetches latest information & news regarding the user request
            User Request : {req}    """
    response=llm.invoke(prompt)
    return {"llm_news":response.content}

