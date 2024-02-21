import streamlit as st
import os
from docx import Document
from docx.opc.exceptions import PackageNotFoundError

# Path to the .docx file
file_path = r'C:\Users\bradm\Documents\GitHub\hello-streamlit\.documents\RDS_TMApp_User_Manual.docx'

# Check if the file exists
if not os.path.exists(file_path):
    st.error("File not found.")
else:
    try:
        # Load the document
        doc = Document(file_path)

        # Extract text from the document
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

        # Display the text using Streamlit
        st.text(text)
    except PackageNotFoundError:
        st.error("Invalid .docx file format.")



