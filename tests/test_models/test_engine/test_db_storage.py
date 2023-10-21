#!usr/bin/python3
"""TestCases for DBStorage"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pycodestyle
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        self.storage.close()

    def test_all(self):
        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.save()

        all_objects = self.storage.all()
        self.assertIn(state, all_objects.values())
        self.assertIn(city, all_objects.values())

        state_objects = self.storage.all(State)
        self.assertIn(state, state_objects.values())
        self.assertNotIn(city, state_objects.values())

    def test_new_and_save(self):
        state = State(name="New York")
        self.storage.new(state)
        self.storage.save()

        state_objects = self.storage.all(State)
        self.assertIn(state, state_objects.values())

    def test_delete(self):
        state = State(name="Texas")
        self.storage.new(state)
        self.storage.save()

        state_objects = self.storage.all(State)
        self.assertIn(state, state_objects.values())

        self.storage.delete(state)
        state_objects = self.storage.all(State)
        self.assertNotIn(state, state_objects.values())

class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
                test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


if __name__ == '__main__':
    unittest.main()
