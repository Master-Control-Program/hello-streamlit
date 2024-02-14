import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Region")

# Text input boxes
description = st.text_input("Description", "")
manager_name = st.text_input("Manager Name", "")

# Search and Clear Buttons
col1, col2 = st.columns([1, 1])
if col1.button("Search"):
    # Perform search action
    pass  # Placeholder for search action
if col2.button("Clear"):
    description = ""
    manager_name = ""

# Sample table data
data = {
    "Region": ["Region A", "Region B", "Region C"],
    "Description": ["Description A", "Description B", "Description C"],
    "Manager Name": ["Manager A", "Manager B", "Manager C"]
}
df = pd.DataFrame(data)

# Filter data based on input
filtered_df = df[(df["Description"].str.contains(description, case=False)) & 
                 (df["Manager Name"].str.contains(manager_name, case=False))]

# Display table
st.table(filtered_df)
