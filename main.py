from commands import session
from db.models import User
from commands import log_activity, log_reflection, view_summary
import sys

def main():
    print("Welcome to the Mental Health Activity Tracker CLI!\n")

    while True:
        print("1. Add New User")
        print("2. Select Existing User")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            add_new_user()
        elif choice == '2':
            select_existing_user()
        elif choice == '3':
            print("\nThank you for using the Mental Health Tracker. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

def add_new_user():
    while True:
        name = input("Enter your name (or type 'exit' to cancel): ").strip()
        if name.lower() == 'exit':
            print("Returning to main menu...\n")
            return
        if not all(part.isalpha() for part in name.split()):
            print("Invalid name. Please use only letters.")
        else:
            existing_user = session.query(User).filter_by(name=name).first()
            if existing_user:
                print(f"User '{name}' already exists. Please try again.")
            else:
                new_user = User(name=name)
                session.add(new_user)
                session.commit()
                print(f"User '{name}' added successfully!\n")
                user_menu(new_user)  # Pass the User object
                return

def select_existing_user():
    while True:
        name = input("Enter your name (or type 'exit' to cancel): ").strip()
        if name.lower() == 'exit':
            print("Returning to main menu...\n")
            return
        existing_user = session.query(User).filter_by(name=name).first()
        if existing_user:
            print(f"Welcome back, {name}!\n")
            user_menu(existing_user)  # Pass the User object
            return
        else:
            print("User not found. Please try again or add a new user.\n")

def user_menu(user):
    first_time = True
    while True:
        if first_time:
            print("What would you like to do?")
            first_time = False
        else:
            print("What else would you like to do?")

        print("1. Log Activity")
        print("2. Log Reflection")
        print("3. View Summary")
        print("4. Exit to Main Menu")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            log_activity(user)  
        elif choice == '2':
            log_reflection(user)  
        elif choice == '3':
            view_summary(user)  
        elif choice == '4':
            print(f"Returning to main menu...\n")
            return
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
