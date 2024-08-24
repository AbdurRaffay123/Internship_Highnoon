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
        if connection:
            print("Connection successful!")
            return connection
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to SQL Server: {e}")
        return None

def execute_command(connection, sql_command):
    # """Execute a SQL command on the connected SQL Server database."""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_command)
        connection.commit()  # Commit the transaction if needed
        print("Command executed successfully!")
    except pyodbc.Error as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":

    server = '172.22.0.19,1433'
    database = 'rang1'  
    username = 'admin'
    password = 'passion'

    # Connect to SQL Server
    connection = connect_to_sql_server(server, database, username, password)

# SQL command to execute (e.g., creating a table)
    sql_command = """
    CREATE TABLE TestTable3 (
        ID INT PRIMARY KEY,
        Name VARCHAR(50)
    );
    """
    print(sql_command)
    # Execute the command
    if connection:
        execute_command(connection, sql_command)
        connection.close()
        print("Connection closed.")