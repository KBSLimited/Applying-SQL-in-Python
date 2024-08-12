import sqlite3

def update_member_age(db_path, member_id, new_age):
    """
    Update the age of a member in the 'Members' table in the gym's database.

    Parameters:
    - db_path (str): The path to the SQLite database file.
    - member_id (int): The ID of the member whose age needs to be updated.
    - new_age (int): The new age to set for the member.

    Returns:
    - None
    """
    # Validate new_age
    if new_age <= 0:
        print("Invalid age. Age must be a positive integer.")
        return

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Check if member_id exists in Members table
        cursor.execute("SELECT 1 FROM Members WHERE id = ?", (member_id,))
        if cursor.fetchone() is None:
            print(f"Member ID {member_id} does not exist.")
            return

        # SQL query to update member age
        sql_query = "UPDATE Members SET age = ? WHERE id = ?"

        # Execute the query with parameters
        cursor.execute(sql_query, (new_age, member_id))

        # Check if the update was successful
        if cursor.rowcount == 0:
            print(f"No updates were made. Member ID {member_id} might not have an age change.")
        else:
            # Commit the transaction
            connection.commit()
            print("Member age updated successfully.")

    except sqlite3.Error as e:
        # Handle SQLite errors
        print(f"SQLite error: {e}")

    finally:
        # Close the database connection
        connection.close()

# Example usage
update_member_age('gym_database.db', 1, 30)
