#!/usr/bin/python3
"""user module
"""
from sqlalchemy import column, string, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User class
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

