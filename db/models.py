from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, declarative_base

# Base class for our models
Base = declarative_base()
