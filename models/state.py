#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
"""
#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
		name = 
		"""
		""" State class """
		__tablename__ = 'states'
		name = Column(
				String(128), nullable=False
		) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
		if os.getenv('HBNB_TYPE_STORAGE') == 'db':
				cities = relationship(
						'City',
						cascade='all, delete, delete-orphan',
						backref='state'
				)
		else:
				@property
				def cities(self):
						"""Returns the cities in this State"""
						from models import storage
						st_city = []
						for value in storage.all(City).values():
								if value.state_id == self.id:
										st_city.append(value)
						return st_city
