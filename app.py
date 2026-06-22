import streamlit as st

st.set_page_config(
    page_title="IGR Property Parser",
    layout="wide"
)

st.title("🏢 IGR Property Description Parser")

st.success("Application loaded successfully.")

uploaded = st.file_uploader(
    "Upload Excel File",
    type=["xlsx", "xls", "csv"]
)

if uploaded:
    st.success(f"File uploaded: {uploaded.name}")
