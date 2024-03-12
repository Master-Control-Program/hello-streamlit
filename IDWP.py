import pyodbc

# Define the connection string
conn_str = 'DRIVER={edmap};' \
           'SERVER=edmap-pkg.conseco.com;' \
           'PORT=1521;' \
           'DATABASE=edmap;' \
           'UID=calym2;' \
           'PWD=your_password;'

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
