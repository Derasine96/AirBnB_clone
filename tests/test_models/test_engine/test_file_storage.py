#!/usr/bin/python3
"""
Defines unittests for FileStorage module

Unittest cases:
    TestFileStorageInstantiation
    TestFileStorageMethods
"""
import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class"""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(bm)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn(f"BaseModel.{bm.id}", models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn(f"User.{user.id}", models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn(f"State.{state.id}", models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn(f"Place.{place.id}", models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn(f"City.{city.id}", models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn(f"Amenity.{amenity.id}", models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn(f"Review.{review.id}", models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(bm)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        text = ""
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn(f"BaseModel.{bm.id}", text)
            self.assertIn(f"User.{user.id}", text)
            self.assertIn(f"State.{state.id}", text)
            self.assertIn(f"Place.{place.id}", text)
            self.assertIn(f"City.{city.id}", text)
            self.assertIn(f"Amenity.{amenity.id}", text)
            self.assertIn(f"Review.{review.id}", text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(bm)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn(f"User.{user.id}", objs)
        self.assertIn(f"State.{state.id}", objs)
        self.assertIn(f"Place.{place.id}", objs)
        self.assertIn(f"City.{city.id}", objs)
        self.assertIn(f"Amenity.{amenity.id}", objs)
        self.assertIn(f"Review.{review.id}", objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
