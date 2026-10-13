import io
import zipfile
import streamlit as st
import tempfile
import os

st.title("Pinyin Epub Annotator")

uploaded_file = st.file_uploader("Upload an EPUB file", type=["epub"])

if uploaded_file is not None:
  # Create a temporary file that deletes itself after closing
  with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
    # Write the uploaded file's bytes to the temporary file
    temp_file.write(uploaded_file.getvalue())
    temp_file_path = temp_file.name
            
 # Now you can pass `temp_file_path` into any traditional script/function
st.success(f"File temporarily saved to: {temp_file_path}")
  
from epub_pinyin import process_epub

# Process an EPUB file
process_epub (uploaded_file, uploaded_file)

#Success Message + Download
st.success("EPUB processed successfully!")

st.download_button(
      label="Download Modified EPUB",
      data=output_buffer.getvalue(),
      file_name="modified_" + uploaded_file.name,
      mime="application/epub+zip",
  )
