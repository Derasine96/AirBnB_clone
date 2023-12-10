#!/usr/bin/python3
"""Define unittests for BaseModel class

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelTo_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittest for testing BaseModel instantiation"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_date_are_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_obj_unique_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_two_model_dates_are_diff(self):
        obj1 = BaseModel()
        sleep(0.1)
        obj2 = BaseModel()
        self.assertLess(obj1.created_at, obj2.created_at)
        self.assertLess(obj1.updated_at, obj2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModelSave(unittest.TestCase):
    """Test for the save method of BaseModel class"""

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
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        """Test save method"""
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_more_saves(self):
        bm = BaseModel()
        sleep(0.1)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.1)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        """Test save method with arg"""
        with self.assertRaises(TypeError):
            BaseModel().save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bm_id = f"BaseModel.{bm.id}"
        with open("file.json", "r") as f:
            self.assertIn(bm_id, f.read())

class TestBaseModelTo_dict(unittest.TestCase):
    """Test for the to_dict method of BaseModel Class"""

    def test_to_dict(self):
        """Test to_dict method"""
        bm = BaseModel()
        bm.name = "Gbenga"
        bm.my_number = 24
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)
        self.assertEqual(bm_dict["name"], "Gbenga")
        self.assertEqual(bm_dict["my_number"], 24)
        self.assertEqual(type(bm_dict["id"]), str)

    def test_to_dict_one_arg(self):
        """Test to_dict method with no args"""
        with self.assertRaises(TypeError):
            BaseModel().to_dict(None)

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_two_arg(self):
        """Test to_dict method with one more arg"""
        with self.assertRaises(TypeError):
            BaseModel().to_dict(None, None)

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Gbenga"
        bm.my_number = 24
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bm_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), bm_dict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)


if __name__ == "__main__":
    unittest.main()
