from commands import session
from db.models import User
from commands import add_user, log_activity, log_reflection, view_summary

def main():
    print("Welcome to the Mental Health Activity Tracker CLI!")
    user = None  # Store active user for the session

    # Step 1: Prompt the user to add/select a user
    while not user:
        print("\n1. Add New User")
        print("2. Select Existing User")
        user_choice = input("Enter your choice (1/2): ").strip()

        if user_choice == "1":
            while True:  # Input validation for name
                name = input("Enter your name: ").strip()
                if name.replace(" ", "").isalpha():
                    add_user(name)  # Add user
                    user = session.query(User).filter_by(name=name).first()
                    print(f"\nUser '{name}' added successfully!")
                    print(f"Hello, {name}! Let's get started.\n")
                    break
                else:
                    print("Invalid name. Please use only letters.")

        elif user_choice == "2":
            name = input("Enter your name: ").strip()
            user = session.query(User).filter_by(name=name).first()
            if user:
                print(f"\nWelcome back, {user.name}!")
            else:
                print("User not found. Please try again or add a new user.")
        else:
            print("Invalid choice. Please select 1 or 2.")

    # Step 2: Main options menu (for the active user)
    while True:
        print("\nOptions:")
        print("1. Log Activity")
        print("2. Log Reflection")
        print("3. View Summary")
        print("4. Exit")

        choice = input("\nWhat would you like to do? ").strip()

        if choice == "1":
            log_activity(user)
            print(f"\nActivity logged successfully for {user.name}.")
        elif choice == "2":
            log_reflection(user)
            print(f"\nReflection logged successfully for {user.name}.")
        elif choice == "3":
            view_summary(user)
        elif choice == "4":
            print("\nThank you for using the Mental Health Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        print("\nWhat else would you like to do?")  # Follow-up prompt for next action

if __name__ == "__main__":
    main()