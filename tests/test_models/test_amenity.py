#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
import unittest


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

class TestAmenity_setup(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        self.session.close()

    def test_amenity_creation(self):
        amenity = Amenity(name="Swimming Pool")
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_name(self):
        amenity = Amenity(name="Fitness Center")
        self.assertEqual(amenity.name, "Fitness Center")

    def test_amenity_relationship(self):
        place = Place(name="Cozy Cabin")
        self.session.add(place)

        amenity = Amenity(name="Hot Tub")
        amenity.place_amenities.append(place)
        self.session.add(amenity)
        self.session.commit()

        self.assertEqual(place.amenities, [amenity])

if __name__ == '__main__':
    unittest.main()
