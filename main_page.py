import streamlit as st
import utils.TextRead as TextRead
import utils.URLRead as URLRead
import utils.PDFRead as PDFRead
import globalvar
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.switch_page_button import switch_page

globalvar.init()

st.set_page_config(page_title="Major 1" , initial_sidebar_state="collapsed" , layout="wide")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.write("Welcome to Text Summarization and Insightful Response(TSR)")

with st.container():
    option = selectbox(
        "Select option to upload text : ",
        ("Enter text", "Upload pdf", ),
        no_selection_label="---",
    )
    
    input_text = None
    if option == "Enter text":
        text = TextRead.TextReader()
        input_text = text.get_text()

    elif option == "Upload link":
        url = URLRead.URLReader()
        input_text = url

    elif option == "Upload pdf":
        pdf = PDFRead.PDFReader()
        input_text = pdf.get_content()
    
    globalvar.inputText = input_text    
    
    summarize_button = st.button('Summarize')
    if summarize_button:
        if input_text is not None:
            switch_page('summarized')
        else:
            st.warning('Select a source before submitting')
            
    query_button = st.button('Query over context')
    if query_button:
        if input_text is not None:
            switch_page('query')
        else:
            st.warning('Select a source before submitting')