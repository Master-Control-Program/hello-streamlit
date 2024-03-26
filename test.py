import streamlit as st
import sqlite3

# Set page config to use wide mode and dark theme
st.set_page_config(layout="wide")

# Define the path to the database file
db_path = r"C:\Users\bradm\Documents\GitHub\hello-streamlit\databases\temp_plancode_database.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# Query the database and display the results
cur = conn.cursor()
cur.execute("SELECT * FROM coverage_table")  # Replace 'your_table_name' with the actual table name
rows = cur.fetchall()
st.table(rows)

# Close the database connection
conn.close()
