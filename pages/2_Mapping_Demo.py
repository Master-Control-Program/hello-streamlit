import streamlit as st
import pandas as pd

# Dummy data for the table
dummy_data = [
    {"Product Category Code": "PC001", "Description": "Electronics", "Line of Business Name": "Consumer Goods"},
    {"Product Category Code": "PC002", "Description": "Clothing", "Line of Business Name": "Fashion"},
    {"Product Category Code": "PC003", "Description": "Food", "Line of Business Name": "Groceries"},
]

# Function to filter data based on search criteria
def filter_data(category_code, description, line_of_business):
    filtered_data = []
    for row in dummy_data:
        if (category_code.lower() in row["Product Category Code"].lower() and
            description.lower() in row["Description"].lower() and
            line_of_business.lower() in row["Line of Business Name"].lower()):
            filtered_data.append(row)
    return filtered_data

# Streamlit app layout
st.title("Product Categories")

# Search criteria section
st.header("Search Criteria")
col1, col2, col3 = st.columns(3)
with col1:
    category_code = st.text_input("Product Category Code")
with col2:
    description = st.text_input("Description")
with col3:
    line_of_business = st.text_input("Line of Business Name")

# Buttons for search and clear
search_clicked = st.button("Search")
clear_clicked = st.button("Clear")

# Display table based on search criteria
if search_clicked:
    filtered_data = filter_data(category_code, description, line_of_business)
    if filtered_data:
        df = pd.DataFrame(filtered_data)
        st.table(df)
    else:
        st.write("No matching records found.")
elif clear_clicked:
    st.table([])  # Clear the table
