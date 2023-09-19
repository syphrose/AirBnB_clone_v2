#!/usr/bin/python3
"""New engine """


from models.base_model import Base
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


class DBStorage():
    """
    New engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """public instance method"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      user, password, host, database),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        querries the the current database session
        """
        names = (User, State, City, Amenity, Place, Review)
        new_dict = {}
        if cls is None:
            for i in names:
                get_querry = self.__session.query(i)
                for x in get_querry.all():
                    dict_keys = "{}.{}".format(x.__class__.name__, x.id)
                    new_dict[dict_keys] = x
        else:
            get_querry = self.__session.query(cls)
            for x in get_querry.all():
                dict_keys = "{}.{}".format(x.__class__.__name__, x.id)
                new_dict[dict_keys] = x
        return new_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits all changes to the database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(
                               bind=self.__engine, expire_on_commit=False)
        get_session = scoped_session(session)
        self.__session = get_session()

    def close(self):
        """
        close the current database session
        """
        self.__session.close()
