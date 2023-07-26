#!/usr/bin/python3
"""this module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiates a new databese"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary all cls in db or all obj in database"""
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                objects[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            classes = [State, Place, User, City, Review, Amenity]
            for every_class in classes:
                for ob in self.__session.query(every_class).all():
                    objects[ob.to_dict()['__class__'] + '.' + ob.id] = ob
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        the_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(the_session)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
