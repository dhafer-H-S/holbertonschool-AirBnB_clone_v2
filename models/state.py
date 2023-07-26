#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


STORAGE = getenv("HBNB_TYPE_STORAGE") == "db"


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """returns the list of city instances"""
        new_list = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                new_list.append(city)
        return new_list
