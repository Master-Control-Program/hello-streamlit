import sqlite3
from prettytable import PrettyTable

# Define the path to the database file
db_path = r"C:\Users\bradm\Documents\GitHub\hello-streamlit\databases\temp_plancode_database.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# Query the database and display the results
cur = conn.cursor()
cur.execute("SELECT * FROM coverage_table")  # Replace 'your_table_name' with the actual table name
rows = cur.fetchall()

# Get column headers
column_headers = [description[0] for description in cur.description]

# Create a PrettyTable instance and set the column headers
table = PrettyTable()
table.field_names = column_headers

# Add the first 5 rows to the table
for row in rows[:5]:
    table.add_row(row)

# Print the table
print(table)

# Close the database connection
conn.close()
