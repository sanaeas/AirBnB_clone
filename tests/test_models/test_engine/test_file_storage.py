#!/usr/bin/python3
"""Unittests for base_model.py"""

import unittest
from models.base_model import BaseModel
from models import storage
import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        self.base_model = BaseModel()
        self.base_model_id = self.base_model.id
        self.base_model_created_at = self.base_model.created_at

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_object_stored_in_storage(self):
        """Test if an object is stored in the storage dictionary"""
        key = self.base_model.__class__.__name__ + \
            '.' + str(self.base_model_id)

        self.assertIn(self.base_model, storage.all().values())
        self.assertIn(key, storage.all().keys())

        storage.save()
        storage.reload()
        self.assertNotIn(self.base_model, storage.all().values())

    def test_reloaded_object_equals_original(self):
        """Test if a reloaded object equals the original object"""
        key = self.base_model.__class__.__name__ + \
            '.' + str(self.base_model_id)

        storage.save()
        storage.reload()

        reloaded_object = storage.all()[key]
        self.assertEqual(reloaded_object.to_dict(), self.base_model.to_dict())

    def test_reloaded_object_created_at_equals_original(self):
        """Test if the reloaded object's created_at matches the original obj"""
        key = self.base_model.__class__.__name__ + \
            '.' + str(self.base_model_id)

        storage.save()
        storage.reload()

        reloaded_object = storage.all()[key]

        self.assertEqual(self.base_model_created_at,
                         reloaded_object.created_at)


if __name__ == '__main__':
    unittest.main()
