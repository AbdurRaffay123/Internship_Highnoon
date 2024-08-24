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
        connection = pyodbc.connect(connection_string)
        print("Connection successful!")
        return connection
    except pyodbc.Error as e:
        print(f"Error occurred while connecting to SQL Server: {e}")
        return None

def read_sql_file_to_list(sql_file_path):
# """Read SQL file into a list of queries/commands."""
    try:
        with open(sql_file_path, 'r') as file:
            sql_queries = file.read().split(';')  # Split the file content by ';'
            sql_queries = [query.strip() for query in sql_queries if query.strip()]  # Remove any empty queries
        return sql_queries
    except FileNotFoundError as e:
        print(f"Error: SQL file not found: {e}")
        return []

def execute_queries(connection, queries):
    # """Execute a list of SQL queries on the connected SQL Server."""
    try:
        cursor = connection.cursor()
        for query in queries:
            if query:
                cursor.execute(query)
                connection.commit()  # Commit each transaction if needed
                print(f"Executed query: {query}")
        print("All queries executed successfully!")
    except pyodbc.Error as e:
        print(f"Error executing queries: {e}")

if __name__ == "__main__":
    # Database connection details
    server = '172.22.0.19,1433'  # Replace with your SQL Server address and port
    database = 'Highnoon'  # Replace with your database name
    username = 'admin'  # Replace with your username
    password = 'passion'  # Replace with your password

    # Path to the SQL file
    sql_file_path = r'C:\Users\project\Documents\Project_Sales_ML\SQL\dbproj.sql'

    # Connect to SQL Server
    connection = connect_to_sql_server(server, database, username, password)

    # Read SQL file into a list of queries
    sql_queries = read_sql_file_to_list(sql_file_path)

    # Execute each query in the list
    if connection and sql_queries:
        execute_queries(connection, sql_queries)
        connection.close()
        print("Connection closed.")