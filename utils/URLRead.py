import streamlit as st
import validators


class URLReader:
    def __init__(self) -> None:
        self.url_string = st.text_area(
            label="Enter a link :", placeholder="Enter a link", max_chars=200
        )
        self.check_url()

    def check_url(self):
        result = validators.url(self.url_string.strip())
        if isinstance(result, validators.ValidationError):
            st.write("Enter a valid url")
        else:
            st.write(f"Fetching data from {self.url_string}")