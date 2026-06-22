import streamlit as st

st.set_page_config(
    page_title="Test App",
    layout="wide"
)

st.title("Hello World")

st.success("Streamlit is working.")

st.file_uploader(
    "Upload File",
    type=["xlsx"]
)
