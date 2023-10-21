from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os

"""
#!/usr/bin/python3
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
"""

storage = DBStorage() if os.getenv(
		'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage.reload()
