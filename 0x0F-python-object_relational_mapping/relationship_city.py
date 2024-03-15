#!/usr/bin/python3
""" Defines City class """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from model_state import Base


class City(Base):
    """ Represents a city with SQLalchemy
    Attr:
        id (sqlalchemy.Column): The city's id
        name (sqlalchemy.Column): The city's name
        state_id (sqlalchemy.Column): The city's state id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
