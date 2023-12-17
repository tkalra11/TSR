import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import globalvar
import os
import credentials
import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

st.set_page_config(page_title="Major 1" , initial_sidebar_state="collapsed" , layout="wide")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.write(globalvar.inputText)

os.environ['OPENAI_API_KEY'] = credentials.openai_api_key