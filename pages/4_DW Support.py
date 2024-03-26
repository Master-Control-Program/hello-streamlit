import streamlit as st
import sqlite3
import requests

# Set page config to use wide mode
st.set_page_config(layout="wide")

# URL of the SQLite database file in the GitHub repository
db_url = "https://github.com/Master-Control-Program/hello-streamlit/blob/main/databases/temp_plancode_database.db"

# Path to save the downloaded database file
db_path = "temp_plancode_database.db"

# Download the database file
response = requests.get(db_url)
with open(db_path, "wb") as file:
    file.write(response.content)

# Connect to the downloaded database
conn = sqlite3.connect(db_path)

# Query the database and display the results
cur = conn.cursor()
cur.execute("SELECT * FROM coverage_table LIMIT 5")  # Retrieve the first 5 rows
rows = cur.fetchall()

# Get column headers
column_headers = [description[0] for description in cur.description]

# Display the table with column headers
st.table([column_headers] + rows)

# Close the database connection
conn.close()
