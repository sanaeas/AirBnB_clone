#!/usr/bin/python3
"""Unittests for amenity.py"""

import unittest
from models.amenity import Amenity
from datetime import datetime
import models


class TestAmenity(unittest.TestCase):

    def test_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_type(self):
        self.assertEqual(str, type(Amenity.name))

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_created_at(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_amenity_updated_at(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_str_representation(self):
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_create_amenity(self):
        self.amenity.name = 'WiFi'

        amenity_dict = self.amenity.to_dict()

        self.assertEqual(self.amenity.name, amenity_dict['name'])

        self.amenity.name = 'swimming pool'
        self.assertNotEqual(self.amenity.name, amenity_dict['name'])
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(self.amenity.name, amenity_dict['name'])


if __name__ == '__main__':
    unittest.main()
