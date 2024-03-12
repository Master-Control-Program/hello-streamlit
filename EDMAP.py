import pyodbc

# Define the connection string
conn_str = 'DRIVER={idwp 12_1 System};' \
           'SERVER=edmap-pkg.conseco.com;' \
           'PORT=1521;' \
           'DATABASE=edmap;' \
           'Trusted_Connection=yes;' \
           'TrustServerCertificate=yes;'  # Trust the server's SSL certificate

# Establish a connection
conn = pyodbc.connect(conn_str)

# Create a cursor
cursor = conn.cursor()

# Execute a query to fetch data from an EDMAP table
cursor.execute('SELECT TOP 10 * FROM ENTPRS_COVRG_PLAN_VW')

# Fetch and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
