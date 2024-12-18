from commands import add_user, log_activity, log_reflection, view_summary
def main():
    print("Welcome to the Mental Health Activity Tracker CLI!")
    user = None # store active user for the session

    # Step1: Propt the user to add or select a user
    while not user:
        print("\nLet's get started!")
        print("1. Add New User")
        print("2. Select Existing User")

        user_choice = input("Enter your choice (1/2): ").strip()
        if user_choice == "1":
            user = add_user() # adds new user and stores in memory
        elif user_choice == "2":
            user = input("Enter your name: ").strip()
            print(f"Welcome back, {user}!")
        else:
            print("Invalid choice. Please choose 1 or 2.")

    
