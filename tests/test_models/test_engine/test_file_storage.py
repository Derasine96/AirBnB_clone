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


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class"""

    def test_no_args_instantiates(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_path_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


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

    def test_all_returns_dict(self):
        self.assertEqual(dict, type(FileStorage().all()))

    def test_all_returns_objects(self):
        self.assertIs(FileStorage().all(), FileStorage._FileStorage__objects)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn(bm, models.storage.all().values())
        self.assertIn(f"BaseModel.{bm.id}", models.storage.all().keys())

    def test_new_with_args(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        with open("file.json", "r") as f:
            self.assertIn(bm.id, f.read())

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        self.assertIn(f"BaseModel.{bm.id}", models.storage.all().keys())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_file_does_not_exist(self):
        self.assertIsNone(models.storage.reload())

    def test_reload_from_nonexistent_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        self.assertIsNone(models.storage.reload())


if __name__ == "__main__":
    unittest.main()
