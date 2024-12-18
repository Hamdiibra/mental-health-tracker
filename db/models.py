from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, declarative_base

# Base class for our models
Base = declarative_base()

# User Table
class User(Base):
    __tablename__ = 'users'  # Corrected here
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    reflections = relationship('Reflection', back_populates='user')
    activities = relationship('Activity', back_populates='user')
