from sqlalchemy.orm import sessionmaker
from datetime import datetime
from db.models import User, Activity, Reflection
from db.db_setup import engine
from tabulate import tabulate

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()