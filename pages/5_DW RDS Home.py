

import streamlit as st
import os
from docx import Document

# Set page title
st.set_page_config(page_title="DW RDS Home",layout="wide")

st.write("This page/section was linked to a word document that is listed below.")




# Path to the .doc file
file_path = r'C:\Users\bradm\Documents\GitHub\hello-streamlit\.documents\RDS_TMApp_User_Manual.doc'

# Load the document
doc = Document(file_path)

# Extract text from the document
text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Display the text using Streamlit
st.text(text)


