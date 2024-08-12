import sqlite3

def delete_workout_session(db_path, session_id):
    """
    Delete a workout session from the 'WorkoutSessions' table in the gym's database.

    Parameters:
    - db_path (str): The path to the SQLite database file.
    - session_id (int): The ID of the workout session to be deleted.

    Returns:
    - None
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Check if session_id exists in WorkoutSessions table
        cursor.execute("SELECT 1 FROM WorkoutSessions WHERE session_id = ?", (session_id,))
        if cursor.fetchone() is None:
            print(f"Session ID {session_id} does not exist.")
            return

        # SQL query to delete the workout session
        sql_query = "DELETE FROM WorkoutSessions WHERE session_id = ?"

        # Execute the query with the session_id
        cursor.execute(sql_query, (session_id,))

        # Check if the deletion was successful
        if cursor.rowcount == 0:
            print(f"No sessions were deleted. Session ID {session_id} might not exist.")
        else:
            # Commit the transaction
            connection.commit()
            print("Workout session deleted successfully.")

    except sqlite3.Error as e:
        # Handle SQLite errors
        print(f"SQLite error: {e}")

    finally:
        # Close the database connection
        connection.close()

# Example usage
delete_workout_session('gym_database.db', 1)
