from member_operations import add_member, update_member_age
from workout_operations import add_workout_session, delete_workout_session

def main():
    db_path = 'gym_database.db'

    print("Gym Database Manager")
    print("1. Add Member")
    print("2. Update Member Age")
    print("3. Add Workout Session")
    print("4. Delete Workout Session")

    try:
        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter member ID: "))
            name = input("Enter member name: ")
            age = int(input("Enter member age: "))
            add_member(db_path, id, name, age)
        elif choice == '2':
            member_id = int(input("Enter member ID: "))
            new_age = int(input("Enter new age: "))
            update_member_age(db_path, member_id, new_age)
        elif choice == '3':
            member_id = int(input("Enter member ID: "))
            date = input("Enter workout date (YYYY-MM-DD): ")
            duration_minutes = int(input("Enter duration in minutes: "))
            calories_burned = int(input("Enter calories burned: "))
            add_workout_session(db_path, member_id, date, duration_minutes, calories_burned)
        elif choice == '4':
            session_id = int(input("Enter workout session ID: "))
            delete_workout_session(db_path, session_id)
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
