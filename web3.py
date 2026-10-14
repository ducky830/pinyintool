import streamlit as st
import subprocess
import tempfile
import os

st.title("EPUB to Pinyin")

#File Uploader
uploaded_file = st.file_uploader("Upload an EPUB file", type=["epub"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    with st.spinner("Processing file..."):
            
            #tmp file save
            with tempfile.NamedTemporaryFile(delete=False, suffix=".epub") as temp_in:
                temp_in.write(uploaded_file.getvalue())
                in_path = temp_in.name
                out_path = in_path.replace(".epub", "_processed.epub")

                from epub_pinyin import process_epub
                
                #script
                process_epub(in_path, out_path)
                
                #read
                with open(out_path, "rb") as temp_out:
                    processed_data = temp_out.read()

                st.success("Processing complete!")

                #download
                st.download_button(
                    label="Download Processed EPUB",
                    data=processed_data,
                    file_name="pinyin_" + uploaded_file.name,
                    mime="application/epub+zip"
                )

            except subprocess.CalledProcessError as e:
                st.error(f"Subprocess failed with exit code {e.returncode}")
                st.code(e.stderr)
                
            #cleanup
            finally:
                if os.path.exists(in_path):
                    os.remove(in_path)
                if os.path.exists(out_path):
                    os.remove(out_path)
