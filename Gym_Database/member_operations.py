from database import execute_query

def add_member(db_path, id, name, age):
    """
    Adds a new member to the 'Members' table.
    
    Args:
    - db_path (str): The path to the SQLite database file.
    - id (int): The unique ID for the new member.
    - name (str): The name of the member.
    - age (int): The age of the member.
    """
    if age <= 0:
        print("Invalid age. Age must be a positive integer.")
        return

    query = "INSERT INTO Members (id, name, age) VALUES (?, ?, ?)"
    execute_query(db_path, query, (id, name, age))

def update_member_age(db_path, member_id, new_age):
    """
    Updates the age of a member in the 'Members' table.
    
    Args:
    - db_path (str): The path to the SQLite database file.
    - member_id (int): The ID of the member whose age needs to be updated.
    - new_age (int): The new age to set for the member.
    """
    if new_age <= 0:
        print("Invalid age. Age must be a positive integer.")
        return

    # Check if member_id exists
    query = "SELECT 1 FROM Members WHERE id = ?"
    if execute_query(db_path, query, (member_id,), fetchone=True) is None:
        print(f"Member ID {member_id} does not exist.")
        return

    query = "UPDATE Members SET age = ? WHERE id = ?"
    execute_query(db_path, query, (new_age, member_id))
