import pyodbc
import numpy as np
import pandas as pd

# Step 1: Establish Connection using pyodbc
conn = pyodbc.connect(driver='{SQL Server}',
                      server='172.22.0.19,1433',
                      database='zeeshanfinal',
                      uid='admin',
                      pwd='passion')

cursor = conn.cursor()

# Step 2: Execute a SELECT * Query
cursor.execute("SELECT * FROM Customer")  # Replace with your table name

# Step 3: Fetch All Rows
rows = cursor.fetchall()

# Step 4: Get Column Names from Cursor Description
columns = [column[0] for column in cursor.description]

# Step 5: Convert to Dictionary
result_dict = [dict(zip(columns, row)) for row in rows]

print("Result as Dictionary: ", result_dict)


# Convert to pandas DataFrame first
result_df = pd.DataFrame(result_dict)  

# Step 6: Convert to NumPy Array
result_array = result_df.to_numpy()

print("Result as NumPy Array: ", result_df)

# Close the cursor and connection
cursor.close()
conn.close()