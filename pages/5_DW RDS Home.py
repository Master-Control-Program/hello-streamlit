

import streamlit as st
import os

# Set page title
st.set_page_config(page_title="DW RDS Home",layout="wide")

st.write("This page/section was linked to a word document that is listed below.")

# Upload the file
uploaded_file = st.sidebar.file_uploader("Upload a Word document", type=["doc"])

# If a file was uploaded
if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Create a download link for the file
    download_link = f'<a href="tempDir/{uploaded_file.name}" download>Click here to download</a>'
    st.markdown(download_link, unsafe_allow_html=True)

