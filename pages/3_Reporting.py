import streamlit as st
import pandas as pd

# Title of the page
st.title("Plan Codes by Product")

# Note on the page
st.write("This previously was 'reporting' but the reports were outdated and most likely not being used. Thinking about pivoting to Plan Codes by Product search page.")

# Search Criteria Section
st.sidebar.title("Search Criteria")

# Dropdown for Line of Business (LOB)
lob_options = ["Option 1", "Option 2", "Option 3"]
selected_lob = st.sidebar.selectbox("Select Line of Business (LOB):", lob_options)

# Dropdown for Product
product_options = ["Product 1", "Product 2", "Product 3"]
selected_product = st.sidebar.selectbox("Select Product:", product_options)

# Text box for inputting Plan Code
plan_code = st.sidebar.text_input("Enter Plan Code:")

# Dummy data for the table
data = {
    "Plan Code": ["Plan1", "Plan2", "Plan3"],
    "Product": ["Product 1", "Product 2", "Product 3"],
    "LOB": ["Option 1", "Option 2", "Option 3"],
}
df = pd.DataFrame(data)

# Filter data based on search criteria
filtered_df = df[(df["LOB"] == selected_lob) & (df["Product"] == selected_product) & (df["Plan Code"].str.contains(plan_code, case=False))]

# Display the filtered table
st.write("Search Results:")
st.table(filtered_df)
