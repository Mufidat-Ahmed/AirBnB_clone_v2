#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
import models
from models.city import City
import os
import shlex

class State(BaseModel, Base):
    """State class defintion"""
    __tablename__ = 'states'
    name = Column(
            String(128), nullable=False)
    cities = relationship('City',
            cascade='all, delete, delete-orphan', backref='state')
    @property			
    def cities(self):
        """Returns the cities in this State"""
        var = models.storage.all()
        lists = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lists.append(var[key])
        for elem in lists:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
