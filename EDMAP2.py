import pyodbc


# Define the connection string
conn_str = 'DSN=EDMAP;' \
           'UID=calym2;' \
           'PWD=Newyear24;'

# Establish a connection
conn = pyodbc.connect(conn_str)

# Create a cursor
cursor = conn.cursor()

# Specify the table name
table_name = 'ENTERPRISE_COVERAGE_MASTER'

# Execute a query to select all rows from the specified table
cursor.execute(f'SELECT * FROM "{table_name}" FETCH FIRST 10 ROWS ONLY')  # Assuming the table name is case-sensitive and requires quotes

for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()