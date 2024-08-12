import sqlite3

def add_member(db_path, id, name, age):
    """
    Add a new member to the 'Members' table in the gym's database.

    Parameters:
    - db_path (str): The path to the SQLite database file.
    - id (int): The unique identifier for the member.
    - name (str): The name of the member.
    - age (int): The age of the member.

    Returns:
    - None
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        
        # SQL query to insert a new member
        sql_query = "INSERT INTO Members (id, name, age) VALUES (?, ?, ?)"
        
        # Execute the query with parameters
        cursor.execute(sql_query, (id, name, age))
        
        # Commit the transaction
        connection.commit()
        
        print("Member added successfully.")
    
    except sqlite3.IntegrityError as e:
        # Handle integrity errors (e.g., duplicate ID)
        print(f"Error adding member: {e}")
    
    except sqlite3.Error as e:
        # Handle other SQLite errors
        print(f"SQLite error: {e}")
    
    finally:
        # Close the database connection
        connection.close()

# Example usage
add_member('gym_database.db', 1, 'John Doe', 25)
