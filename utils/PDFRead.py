import streamlit as st
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter


class PDFReader:
    def __init__(self) -> None:
        self.uploaded_file = st.file_uploader("Choose a file", type=["pdf"])

    def get_content(self):
        if self.uploaded_file is not None:
            doc = ""
            pdf_file = PyPDF2.PdfReader(self.uploaded_file)
            number_of_pages = len(pdf_file.pages)
            for page_num in range(number_of_pages):
                page = pdf_file.pages[page_num]
                doc += page.extract_text()
            
            text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n" , '\n'], chunk_size=2000, chunk_overlap=500)
            doc_content = text_splitter.create_documents([doc])
            return doc_content