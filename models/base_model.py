#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
from models import storage
from datetime import datetime
import os
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    """parameters added: id, created at and updated_at"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            """Parameters seetup created_at and updated_at"""
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.now())


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        """base dict: bs_dict. | handle _sa_instance_state"""
        bs_dict = dict(self.__dict__)
        bs_dict["__class__"] = str(type(self).__name__)
        bs_dict["created_at"] = self.created_at.isoformat()
        bs_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in bs_dict.keys():
            del bs_dict['_sa_instance_state']
        return bs_dict
    def delete(self):
        """the delete module"""
        models.storage.delete(self)
