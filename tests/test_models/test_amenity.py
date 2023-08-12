#!/usr/bin/python3
"""Unittests for amenity.py"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
