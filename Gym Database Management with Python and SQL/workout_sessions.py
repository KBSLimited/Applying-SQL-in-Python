import sqlite3
from datetime import datetime

def add_workout_session(db_path, member_id, date, duration_minutes, calories_burned):
    """
    Add a new workout session to the 'WorkoutSessions' table in the gym's database.

    Parameters:
    - db_path (str): The path to the SQLite database file.
    - member_id (int): The ID of the member associated with the workout session.
    - date (str): The date of the workout session in 'YYYY-MM-DD' format.
    - duration_minutes (int): The duration of the workout session in minutes.
    - calories_burned (int): The number of calories burned during the session.

    Returns:
    - None
    """
    # Validate date format
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
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
        
        # SQL query to insert a new workout session
        sql_query = """
        INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
        VALUES (?, ?, ?, ?)
        """
        
        # Execute the query with parameters
        cursor.execute(sql_query, (member_id, date, duration_minutes, calories_burned))
        
        # Commit the transaction
        connection.commit()
        
        print("Workout session added successfully.")

    except sqlite3.Error as e:
        # Handle SQLite errors
        print(f"SQLite error: {e}")

    finally:
        # Close the database connection
        connection.close()

# Example usage
add_workout_session('gym_database.db', 1, '2024-08-11', 45, 300)
