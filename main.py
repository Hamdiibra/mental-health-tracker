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

    #Step 2: Main options menu(seamless experience)
    while True:
        print(f"\nHello, {user}! What would you like to do?")
        print("1. Log Activity")
        print("2. Log Reflection")
        print("3. View summary")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            log_activity(user)
            print(f"\nHello, {user}! What else would you like to do?")
        elif choice == "2":
            log_activity(user)
            print(f"\nHello, {user}! What else would you like to do?")
        elif choice == "3":
            view_summary(user)
            print(f"\nHello, {user}! What else would you like to do?")
        elif choice == "4":
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            

