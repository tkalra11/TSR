import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextReader:

    def __init__(self) -> None:
        self.text = st.text_area(
            label="Enter input text :",
            placeholder="Enter text here",
            max_chars=100000
        )
    
    def get_text(self):
        self.text = self.text.replace(' ','\n')
        text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n" , '\n'], chunk_size=2500, chunk_overlap=500)
        doc_content = text_splitter.create_documents([self.text])
        return doc_content
        