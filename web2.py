import io
import zipfile
import streamlit as st

st.title("Pinyin Epub Annotator  ")

uploaded_file = st.file_uploader("Upload an EPUB file", type=["epub"])

if uploaded_file is not None:
  # Read the uploaded EPUB into memory
  input_buffer = io.BytesIO(uploaded_file.getbuffer())
  output_buffer = io.BytesIO()

  # Open as zip archives
  with (
      zipfile.ZipFile(input_buffer, "r") as zin,
      zipfile.ZipFile(output_buffer, "w") as zout,
  ):
    for item in zin.infolist():
      content = zin.read(item.filename)

      # Example: Modify text inside XHTML chapters
      if item.filename.endswith(".xhtml") or item.filename.endswith(".html"):
        text_content = content.decode("utf-8")

        # Perform your text edits here (e.g., replacement)
        # text_content = text_content.replace("old_word", "new_word")

        zout.writestr(item.filename, text_content.encode("utf-8"))
      else:
        # Copy other assets (images, stylesheets, xml) as-is
        zout.writestr(item, content)

  st.success("EPUB processed successfully!")

  st.download_button(
      label="Download Modified EPUB",
      data=output_buffer.getvalue(),
      file_name="modified_" + uploaded_file.name,
      mime="application/epub+zip",
  )
