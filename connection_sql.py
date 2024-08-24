import pyodbc

def connect_to_sql_server(server, database, username, password):

# """Establish a connection to Microsoft SQL Server using pyodbc."""

    try:
        # Connection string to connect to the SQL Server
        connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
        )

    # Establish the connection
        connection = pyodbc.connect(connection_string)
        
        print("Connection successful!")
        return connection

    except pyodbc.Error as e:
        print(f"Error occurred while connecting to SQL Server: {e}")
        return None

if __name__ == "__main__":
    
# Database connection details
    
    server = '172.22.0.19,1433'  # Replace with your SQL Server address and port
    database = 'Highnoon'  # Replace with your database name
    username = 'admin'  # Replace with your username
    password = 'passion'  # Replace with your password

# Connect to SQL Server

    connection = connect_to_sql_server(server, database, username, password)

# Make sure to close the connection when done

    if connection:
        connection.close()
        print("Connection closed.")