import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import globalvar
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
import os
import credentials

st.set_page_config(page_title="Major 1" , initial_sidebar_state="collapsed" , layout="wide")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# st.write(globalvar.inputText)

os.environ['OPENAI_API_KEY'] = credentials.openai_api_key

map_prompt = """
Write a concise summary of the following in at least 250 words and at most 280 words,Strictly use words only from the given context to create the summary:
"{text}" 
CONCISE SUMMARY:
"""

map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])


combine_prompt = """
Write a concise summary of the following text delimited by triple backquotes. Consider each different summary to be a part of the same article.
Return your response in at least 500 words and at most 550 words which covers the key points of the text. Strictly use words only from the given context to create the summary.
```{text}```
SUMMARY:
"""

combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])

llm = OpenAI(temperature=0.15)

chain = load_summarize_chain(llm, chain_type="map_reduce",map_prompt=map_prompt_template,combine_prompt=combine_prompt_template)
print(globalvar.inputText)
summary = chain.run(globalvar.inputText)

st.write('Summary:')
st.write(summary)

back = st.button('Back')
if back:
        globalvar.inputText = ''
        switch_page('main_page')