import streamlit as st
import pandas as pd

# Set page config to use wide mode and dark theme
st.set_page_config(layout="wide", theme="dark")

# Dummy data for the table
dummy_data = [
    {"Product Category Code": "PC001", "Description": "Electronics", "Line of Business Name": "Consumer Goods"},
    {"Product Category Code": "PC002", "Description": "Clothing", "Line of Business Name": "Fashion"},
    {"Product Category Code": "PC003", "Description": "Food", "Line of Business Name": "Groceries"},
]

# Convert dummy data to DataFrame
df_dummy = pd.DataFrame(dummy_data)

# Function to filter data based on search criteria
def filter_data(category_code, description, line_of_business):
    filtered_data = df_dummy[
        df_dummy["Product Category Code"].str.lower().str.contains(category_code.lower()) &
        df_dummy["Description"].str.lower().str.contains(description.lower()) &
        df_dummy["Line of Business Name"].str.lower().str.contains(line_of_business.lower())
    ]
    return filtered_data

# Streamlit app layout
st.title("Product Categories")

# Search criteria section
st.header("Search Criteria")
col1, col2, col3 = st.columns(3)
with col1:
    category_code = st.text_input("Product Category Code", "")
with col2:
    description = st.text_input("Description", "")
with col3:
    line_of_business = st.text_input("Line of Business Name", "")

# Buttons for search and clear
search_clicked = st.button("Search")
clear_clicked = st.button("Clear")

# Display table based on search criteria or show the dummy data
if search_clicked:
    filtered_data = filter_data(category_code, description, line_of_business)
    st.table(filtered_data)
elif clear_clicked:
    category_code, description, line_of_business = "", "", ""
    st.table(df_dummy)
else:
    st.table(df_dummy)
