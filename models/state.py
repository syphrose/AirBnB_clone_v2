#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                         cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """lists of city instances"""
        from models import storage
        my_cities = []
        cities = storage.all(City)
        for c in cities.values():
            if c.state_if == self.id:
                my_cities.append(c)
        return my_cities
