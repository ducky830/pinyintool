import pandas as pd
import streamlit as st

st.title("Pinyin Epub Annotator")

    #File upload
uploaded_files = st.file_uploader(
    "Upload EPUB", type= "epub",
    accept_multiple_files=False,
    disabled=False, 
    label_visibility="visible",
    width="stretch"
)

for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)

from epub_pinyin import process_epub

# Process an EPUB file
process_epub("uploaded_file", "annotatedbook.epub")
    
    # Create a dropdown menu for selecting file type
# filetype = st.selectbox("Select Export Type", ['EPUB', 'PDF'])

#if filetype = ['EPUB']

