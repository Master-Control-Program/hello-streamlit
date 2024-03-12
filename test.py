import pyodbc

# Define the connection string
conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};' \
           'SERVER=NTLPS8P11;' \
           'DATABASE=LP_CIKPROD;' \
           'Trusted_Connection=yes;' \
           'TrustServerCertificate=yes;'  # Trust the server's SSL certificate

# Establish a connection
conn = pyodbc.connect(conn_str)

# Create a cursor
cursor = conn.cursor()

# Execute a query to fetch data (selecting the first 10 rows)
cursor.execute('SELECT TOP 10 * FROM CACSE')

# Fetch and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
