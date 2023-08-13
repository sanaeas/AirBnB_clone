#!/usr/bin/python3
"""Unittests for city.py"""

import unittest
from models.city import City
from datetime import datetime
import models


class TestCity(unittest.TestCase):

    def test_instantiation(self):
        self.assertEqual(City, type(City()))

    def test_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_type(self):
        self.assertEqual(str, type(City.name))

    def test_state_id_type(self):
        self.assertEqual(str, type(City.state_id))

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

    def test_create_city(self):
        self.city.state_id = 'sdfg-0912'
        self.city.name = 'LA'

        city_dict = self.city.to_dict()

        self.assertEqual(self.city.state_id, city_dict['state_id'])
        self.assertEqual(self.city.name, city_dict['name'])

        self.city.name = 'NY'
        self.assertNotEqual(self.city.name, city_dict['name'])
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.name, city_dict['name'])


if __name__ == '__main__':
    unittest.main()
