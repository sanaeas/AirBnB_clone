#!/usr/bin/python3
"""Unittests for city.py"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_city_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_created_at(self):
        self.assertIsInstance(self.city.created_at, datetime)

    def test_city_updated_at(self):
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_str_representation(self):
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()
