from database import execute_query
from datetime import datetime

def add_workout_session(db_path, member_id, date, duration_minutes, calories_burned):
    """
    Adds a new workout session to the 'WorkoutSessions' table.
    
    Args:
    - db_path (str): The path to the SQLite database file.
    - member_id (int): The ID of the member associated with the workout session.
    - date (str): The date of the workout session in 'YYYY-MM-DD' format.
    - duration_minutes (int): The duration of the workout session in minutes.
    - calories_burned (int): The number of calories burned during the session.
    """
    if duration_minutes <= 0 or calories_burned < 0:
        print("Invalid duration or calories. Must be positive integers.")
        return

    # Validate date format
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return

    # Check if member_id exists
    query = "SELECT 1 FROM Members WHERE id = ?"
    if execute_query(db_path, query, (member_id,), fetchone=True) is None:
        print(f"Member ID {member_id} does not exist.")
        return

    query = """
    INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
    VALUES (?, ?, ?, ?)
    """
    execute_query(db_path, query, (member_id, date, duration_minutes, calories_burned))

def delete_workout_session(db_path, session_id):
    """
    Deletes a workout session from the 'WorkoutSessions' table.
    
    Args:
    - db_path (str): The path to the SQLite database file.
    - session_id (int): The ID of the workout session to be deleted.
    """
    # Check if session_id exists
    query = "SELECT 1 FROM WorkoutSessions WHERE session_id = ?"
    if execute_query(db_path, query, (session_id,), fetchone=True) is None:
        print(f"Session ID {session_id} does not exist.")
        return

    query = "DELETE FROM WorkoutSessions WHERE session_id = ?"
    execute_query(db_path, query, (session_id,))
