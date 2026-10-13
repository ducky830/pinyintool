import io
import zipfile
import streamlit as st

st.title("Pinyin Epub Annotator")

uploaded_file = st.file_uploader("Upload an EPUB file", type=["epub"])

if uploaded_file is not None:
  # Read the uploaded EPUB into memory
  input_buffer = io.BytesIO(uploaded_file.getbuffer())
  output_buffer = io.BytesIO()
  
  from epub_pinyin import process_epub

  # Process an EPUB file
  process_epub ("item.filename", "item.filename")

#Success Message + Download
  st.success("EPUB processed successfully!")

  st.download_button(
      label="Download Modified EPUB",
      data=output_buffer.getvalue(),
      file_name="modified_" + uploaded_file.name,
      mime="application/epub+zip",
  )
