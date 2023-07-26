#!/usr/bin/python3
""" DBStorage - Review """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """Class that defines the Review"""
    __tablename__ = "reviews"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
