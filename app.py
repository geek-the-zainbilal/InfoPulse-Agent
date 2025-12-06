import streamlit as st
from src.langgraph.LGGraph.graph import graph_builder
st.set_page_config(page_title="AI-Powered_News",page_icon="📰")
st.header("Get Latest Technology Related News with just one click and text :)")


user_prompt=st.text_input(label="What kind of news you want ?")


#-creating columns 
col1, col2 = st.columns(2)
with col1:
    button=st.button("Get AI News")
with col2:
    search_news_button=st.button("Get News with Google")
output_container = st.container()



if user_prompt and button:
        result=graph_builder.invoke({"topic":user_prompt})
        st.write(result['llm_news'])
if user_prompt and search_news_button:
        srch_rslt=graph_builder.invoke({"topic":user_prompt})
        st.write(srch_rslt['tavily_news'])

clr_otpt=st.button("Clear Screen")

if clr_otpt:
      st.write("")