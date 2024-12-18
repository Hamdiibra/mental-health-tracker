from sqlalchemy import create_engine
from db.models import Base

# Create SQlite database
engine = create_engine('sqlite:///mental_health.db')
Base.metadata.create_all(engine)
print("Database initialized successfully!")