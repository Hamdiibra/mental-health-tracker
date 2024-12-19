## Mental Health Activity Tracker

# Overview:

The Mental Health Activity Tracker is a command-line interface (CLI) application that helps users track their daily activities, mood reflections, and generate summaries for better mental health awareness. Built using Python and SQLAlchemy, this project emphasizes database interaction, user-friendly interfaces, and structured data handling.

# Features

- User Management: Add new users or select existing users.

- Activity Logging: Record daily activities with type, duration, and date.

- Reflection Logging: Log mood reflections with notes and dates.

- Summary View: Display a summary of activities and reflections in a tabular format.

# Technologies Used

1. Python: Core programming language for logic and functionality.
2. SQLAlchemy: ORM for managing database interactions.
3. SQLite: Lightweight database for storing user, activity, and reflection data.
4. Tabulate: Library for displaying tabular data.

# Installation

- Clone the repository:

``git clone git@github.com:Hamdiibra/mental-health-tracker.git``

- Navigate to the project directory:

``cd mental-health-tracker``

- Set up the virtual environment using Pipenv:

``pipenv install``

- Activate the Pipenv shell:

``pipenv shell``

- Install the required dependencies:

``pip install sqlalchemy ``

# Usage

- Run the application:

``python main.py``

- Main Menu Options:

1. Add New User: Create a new user profile.

2. Select Existing User: Choose an existing user profile.

3. Exit: Exit the application.

- User Menu Options:

1. Log Activity: Record a daily activity with details.

2. Log Reflection: Record a mood reflection with optional notes.

3. View Summary: View logged activities and reflections in a table.

4. Exit to Main Menu: Return to the main menu.

# Example Interaction
- Adding a New User
```bash
Enter your choice (1/2/3): 1
Enter your name (or type 'exit' to cancel): Hamdi Yusuf
User 'Hamdi Yusuf' added successfully!
```

- Logging an Activity
```bash
What would you like to do?
1. Log Activity
2. Log Reflection
3. View Summary
4. Exit to Main Menu
Enter your choice (1/2/3/4): 1
Enter activity type (e.g., Sleep, Exercise): Exercise
Enter duration in hours: 1.5
Enter date (YYYY-MM-DD): 2024-12-19
Activity 'Exercise' logged for Hamdi Yusuf.
```

- Viewing Summary
```bash
Summary for Hamdi Yusuf:

Activity         Duration (hrs)    Date
--------------  ---------------  ----------
Exercise                    1.5  2024-12-19

Reflections:
Mood         Notes       Date
----------  ----------  ----------
Happy       Feeling good 2024-12-19
```

# Project Structure
```bash
mental-health-tracker/
├── main.py          # Main entry point for the application
├── commands.py      # Contains all core functionalities (log activity, reflections, etc.)
├── db/
│   ├── db_setup.py  # Database configuration and setup
│   ├── models.py    # SQLAlchemy models for User, Activity, Reflection
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

# Learning Goals
This project demonstrates:

1. Proficiency with Python and SQLAlchemy for building CLI applications.

2. Understanding of relational databases and ORM concepts.

3. Implementation of best practices in coding, debugging, and user experience design.

# Future Enhancements:

1. Add data visualization (e.g., charts for activity and mood trends).

2. Implement a graphical user interface (GUI).

3. Add authentication for enhanced user management.

# Contributors

Hamdi Yusuf

# License

This project is licensed under the MIT License. See LICENSE for details.

