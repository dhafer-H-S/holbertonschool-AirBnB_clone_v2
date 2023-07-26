#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review

"""DBStorage - Place"""

STORAGE = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """Class that defines a Place"""

    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="all, delete", backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
    
    @property
    def reviews(self):
        """Returns a list of 'Reviews' instances"""

        new_list = []
        for review in list(models.storage.all(Review).values()):
            if review.place_id == self.id:
                new_list.append(review)
        return new_list