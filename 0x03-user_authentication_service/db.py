#!/usr/bin/python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import User, Base


class DB:
    """DB class
    """
    
    def __init__(self):
        """Constructor
        """
        self.__engine = create_engine('sqlite:///a.db', echo=False)
        Base.metadata.drop_all(self.__engine)