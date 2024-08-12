# Applying-SQL-in-Python
 Module 5: Assignment 3

# Gym Database Manager

This Python application manages a gym's database. It allows you to add members, update member information, and manage workout sessions.

## Project Structure

- `database.py`: Handles database connections and query execution.
- `member_operations.py`: Contains functions to add and update member information.
- `workout_operations.py`: Contains functions to add and delete workout sessions.
- `main.py`: Entry point of the application, providing a CLI for user interaction.
- `schema.sql`: SQL schema for creating the database tables.

## Setup

1. **Create the Database and Tables:**
   Run the following command to initialize the database:
   ```sh
   sqlite3 gym_database.db < schema.sql
