#!/usr/bin/python3
"""Unittests for place.py"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_place_attributes(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_place_created_at(self):
        self.assertIsInstance(self.place.created_at, datetime)

    def test_place_updated_at(self):
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_place_str_representation(self):
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_create_place(self):
        self.place.city_id = 'abdd-0987'
        self.place.name = '221B'
        self.place.number_rooms = 1
        self.place.max_guest = 2

        place_dict = self.place.to_dict()

        self.assertEqual(self.place.city_id, place_dict['city_id'])
        self.assertEqual(self.place.name, place_dict['name'])
        self.assertEqual(self.place.number_rooms, place_dict['number_rooms'])
        self.assertEqual(self.place.max_guest, place_dict['max_guest'])

        self.place.name = 'SH'
        self.assertNotEqual(self.place.name, place_dict['name'])
        place_dict = self.place.to_dict()
        self.assertEqual(self.place.name, place_dict['name'])


if __name__ == '__main__':
    unittest.main()
