import sqlite3

def get_connection(db_path):
    """
    Establishes a connection to the SQLite database specified by db_path.
    
    Args:
    - db_path (str): The path to the SQLite database file.
    
    Returns:
    - sqlite3.Connection: The database connection object.
    """
    return sqlite3.connect(db_path)

def execute_query(db_path, query, params=(), fetchone=False):
    """
    Executes a SQL query on the SQLite database.
    
    Args:
    - db_path (str): The path to the SQLite database file.
    - query (str): The SQL query to execute.
    - params (tuple): Parameters to pass to the SQL query.
    - fetchone (bool): Whether to fetch one result or not.
    
    Returns:
    - tuple or None: The fetched result if fetchone is True, otherwise None.
    """
    connection = get_connection(db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        if fetchone:
            return cursor.fetchone()
        connection.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        connection.close()
