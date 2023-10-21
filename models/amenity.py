#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import column, string
from model.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity class defination"""
    __tablename__ = "amenities"
    name = column(string(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
