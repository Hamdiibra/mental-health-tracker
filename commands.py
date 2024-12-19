from sqlalchemy.orm import sessionmaker
from datetime import datetime
from db.models import User, Activity, Reflection
from db.db_setup import engine
from tabulate import tabulate

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()

# 1. Add User
def add_user(name):
    if session.query(User).filter_by(name=name).first():
        print("User already exists.")
    else:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User '{name}' added successfully.")

# 2. Log Activity
def log_activity(user):
    activity_type = input("Enter activity type (e.g., Sleep, Exercise): ").strip()
    duration = float(input("Enter duration in hours: "))
    date = input("Enter date (YYYY-MM-DD): ").strip()
    activity_date = datetime.strptime(date, '%Y-%m-%d')

    activity = Activity(user_id=user.id, type=activity_type, duration=duration, date=activity_date)
    session.add(activity)
    session.commit()
    print(f"Activity '{activity_type}' logged for {user.name}.")

# 3. Log Reflection
def log_reflection(user):
    mood = input("Enter your mood today (e.g., Happy, Stressed): ").strip()
    notes = input("Enter additional notes (optional): ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    reflection_date = datetime.strptime(date, '%Y-%m-%d')

    reflection = Reflection(user_id=user.id, mood=mood, notes=notes, date=reflection_date)
    session.add(reflection)
    session.commit()
    print(f"Reflection logged for {user.name}.")

# 4. View Summary
def view_summary(user):
    print(f"\nSummary for {user.name}:\n")

    # Display Activities
    activities = session.query(Activity).filter_by(user_id=user.id).all()
    if activities:
        activity_data = [(a.type, a.duration, a.date) for a in activities]
        print(tabulate(activity_data, headers=["Activity", "Duration (hrs)", "Date"]))
    else:
        print("No activities logged.")

    # Display Reflections
    reflections = session.query(Reflection).filter_by(user_id=user.id).all()
    if reflections:
        reflection_data = [(r.mood, r.notes, r.date) for r in reflections]
        print("\nReflections:")
        print(tabulate(reflection_data, headers=["Mood", "Notes", "Date"]))
    else:
        print("No reflections logged.")

# 4. View Summary
def view_summary(user):
    print(f"\nSummary for {user.name}:\n")

    # Display Activities
    activities = session.query(Activity).filter_by(user_id=user.id).all()
    if activities:
        activity_data = [(a.type, a.duration, a.date) for a in activities]
        print(tabulate(activity_data, headers=["Activity", "Duration (hrs)", "Date"]))
    else:
        print("No activities logged.")

    # Display Reflections
    reflections = session.query(Reflection).filter_by(user_id=user.id).all()  # Ensure correct column name
    if reflections:
        reflection_data = [(r.mood, r.notes, r.date) for r in reflections]
        print("\nReflections:")
        print(tabulate(reflection_data, headers=["Mood", "Notes", "Date"]))
    else:
        print("No reflections logged.")
