#!/usr/bin/python3
"""Unittests for place.py"""

import unittest
from models.place import Place
from datetime import datetime
import models


class TestPlace(unittest.TestCase):

    def test_instantiation(self):
        self.assertEqual(Place, type(Place()))

    def test_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_type(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_type(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_type(self):
        self.assertEqual(str, type(Place.name))

    def test_description_type(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_type(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_type(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_type(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_type(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_type(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_type(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_type(self):
        self.assertEqual(list, type(Place.amenity_ids))

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
