from typing_extensions import TypedDict,Optional

class State(TypedDict):
    topic:Optional[str]
    llm_news:Optional[str]
    tavily_news:Optional[str]
    last_output:str
