from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, declarative_base

# Base class for our models
Base = declarative_base()

# User Table
class User(Base):
    __tablename__ = 'users'  
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    reflections = relationship('Reflection', back_populates='user')
    activities = relationship('Activity', back_populates='user')

    def __repr__(self):
        return f"User(name='{self.name}')"

# Activity Table
class Activity(Base):
    __tablename__ = 'activities' 
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer,ForeignKey('users.id'))
    type = Column(String, nullable=False) #e.g Sleep, Exercise
    duration = Column(Float) #Duration in hours
    date = Column(Date) # Date of activity
    user = relationship('User', back_populates='activities')

# Reflection table
class Reflection(Base):
    __tablename__ = 'reflections'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    mood = Column(String,nullable=False)
    notes = Column(String) # Optional notes
    date = Column(Date) #Date of reflection
    user = relationship('User', back_populates='reflections')