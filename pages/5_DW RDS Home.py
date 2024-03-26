import streamlit as st
import sqlite3
import requests

# Download the SQLite database from GitHub
def download_database(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

db_url = 'https://github.com/Master-Control-Program/hello-streamlit/blob/main/databases/temp_plancode_database.db'
db_filename = 'temp_plancode_database.db'
download_database(db_url, db_filename)

# Connect to the SQLite database
conn = sqlite3.connect(db_filename)

# Set up the Streamlit app
st.set_page_config(layout="wide")
st.sidebar.title("Home")
st.markdown("<h1 style='text-align: left; color: yellow; font-size: 75px; font-weight: bold;'>Data Warehouse Table Maintenance</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; color: white; font-size: 52px; font-weight: bold;'>Coverage</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; color: red; font-size: 36px; font-weight: bold;'>Page listing defaults to system code 1/APS ***Please enter your Search Criteria.***</h1>", unsafe_allow_html=True)

st.header("Search Criteria")
col1, col2 = st.columns(2)

with col1:
    search_coverage_plan = st.text_input("Coverage Plan (Search):")
    search_company_code = st.text_input("Company Code (Search):")
    search_system_code = st.selectbox("System Code (Search):", [None, "SHARP", "CIC", "LIFEPRO"])
    search_lob_name = st.selectbox("LOB Name (Search):", [None, "ANNUITY", "GROUP", "HEALTH", "LIFE"])

with col2:
    search_major_product_group_name = st.selectbox("Major Product Group Name (Search):", [None, "EI ANN", "EIUL", "FIXED ANN", "GRP ANN", "GRP HEALTH", "GRP LIFE"])
    search_minor_product_group_name = st.text_input("Minor Product Group Name (Search):")
    search_marketing_product_group_name = st.text_input("Marketing Product Group Name (Search):")
    search_product_code = st.text_input("Product Code (Search):")

search_button = st.button("Search")
clear_button = st.button("Clear")

# Display the contents of a table from the SQLite database
st.header("Database Table")
cur = conn.cursor()
cur.execute("SELECT * FROM coverage_table")  # Replace 'your_table_name' with the actual table name
rows = cur.fetchall()
st.table(rows)

# Close the database connection
conn.close()
