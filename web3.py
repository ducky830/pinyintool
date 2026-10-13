import streamlit as st
import subprocess
import tempfile
import os

st.title("EPUB to Pinyin")

# 1. File Uploader widget
uploaded_file = st.file_uploader("Upload an EPUB file", type=["epub"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    # Button to trigger the processing
    if st.button("Process EPUB"):
        with st.spinner("Processing file..."):
            
            # 2. Save the uploaded file to a temporary location
            # Using suffix=".epub" helps tools that expect the correct extension
            with tempfile.NamedTemporaryFile(delete=False, suffix=".epub") as temp_in:
                temp_in.write(uploaded_file.getvalue())
                in_path = temp_in.name

            # Define a path for the output file
            out_path = in_path.replace(".epub", "_processed.epub")

            try:
                # 3. Define and run your external command
                # Replace ['your_cli_tool', ...] with your actual terminal command and arguments
                command = ["echo", "Processing", in_path, "to", out_path] 
                
                # Example of a real tool if you were converting to mobi:
                # command = ["ebook-convert", in_path, out_path]

                from epub_pinyin import process_epub

                result = subprocess.run(process_epub (in_path, out_path), 
                    command, 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                
                # For this dummy 'echo' example, we simulate creating the output file
                # Remove these 2 lines below when using a real tool that generates the file automatically
                with open(out_path, "wb") as f:
                    f.write(uploaded_file.getvalue() + b"\n# Processed")

                # 4. Read the processed file back into memory
                with open(out_path, "rb") as temp_out:
                    processed_data = temp_out.read()

                st.success("Processing complete!")

                # 5. Provide the download button
                st.download_button(
                    label="Download Processed EPUB",
                    data=processed_data,
                    file_name="processed_" + uploaded_file.name,
                    mime="application/epub+zip"
                )

            except subprocess.CalledProcessError as e:
                st.error(f"Subprocess failed with exit code {e.returncode}")
                st.code(e.stderr)
                
            finally:
                # 6. Cleanup temporary files from disk
                if os.path.exists(in_path):
                    os.remove(in_path)
                if os.path.exists(out_path):
                    os.remove(out_path)
