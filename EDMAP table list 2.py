import pyodbc

# Set up the connection string for your ODBC connection
# Replace 'your_dsn_name' with the name of your ODBC Data Source Name (DSN)
# Replace 'your_user_id' and 'your_password' with your database credentials
connection_string = 'DSN=edmap;UID=calym2;PWD=Newyear24;'

import pyodbc
from openpyxl import Workbook

# Establish the connection

conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Create a new Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Table Names"

# Retrieve and write the table names to the worksheet
row_num = 1
for row in cursor.tables():
    table_name = row.table_name
    ws.cell(row=row_num, column=1, value=table_name)
    row_num += 1

# Save the workbook
wb.save("table_names.xlsx")

# Close the connection
conn.close()
