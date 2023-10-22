import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the database connection and create tables
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.storage.close()

    def test_new_and_save(self):
        # Create a new State object, add it to the session, and save it
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        
        # Retrieve the saved object from the database
        state_from_db = self.storage.all(State).values()
        
        # Ensure that the retrieved object matches the original one
        self.assertIn(state, state_from_db)
    
    def test_delete(self):
        # Create a new User object, add it to the session, and save it
        user = User(email="test@example.com", password="password")
        self.storage.new(user)
        self.storage.save()
        
        # Retrieve the saved object from the database
        user_from_db = self.storage.all(User).values()
        
        # Ensure that the retrieved object is in the database
        self.assertIn(user, user_from_db)
        
        # Delete the object from the session and save
        self.storage.delete(user)
        self.storage.save()
        
        # Retrieve the deleted object from the database
        user_from_db = self.storage.all(User).values()
        
        # Ensure that the deleted object is no longer in the database
        self.assertNotIn(user, user_from_db)

    def test_all(self):
        # Create objects of different classes and save them
        state = State(name="New York")
        city = City(name="New York City", state_id=state.id)
        place = Place(name="Cozy Apartment", city_id=city.id)
        review = Review(text="Great place to stay", place_id=place.id)
        amenity = Amenity(name="Wi-Fi")
        
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(place)
        self.storage.new(review)
        self.storage.new(amenity)
        self.storage.save()
        
        # Retrieve objects of different classes from the database
        states = self.storage.all(State).values()
        cities = self.storage.all(City).values()
        places = self.storage.all(Place).values()
        reviews = self.storage.all(Review).values()
        amenities = self.storage.all(Amenity).values()
        
        # Check that retrieved objects match the original ones
        self.assertIn(state, states)
        self.assertIn(city, cities)
        self.assertIn(place, places)
        self.assertIn(review, reviews)
        self.assertIn(amenity, amenities)

if __name__ == '__main__':
    unittest.main()
