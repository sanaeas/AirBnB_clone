#!/usr/bin/python3
"""Unittests for state.py"""

import unittest
from models.state import State
from datetime import datetime
import models


class TestState(unittest.TestCase):

    def test_instantiation(self):
        self.assertEqual(State, type(State()))

    def test_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_type(self):
        self.assertEqual(str, type(State.name))

    def setUp(self):
        self.state = State()

    def test_state_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_created_at(self):
        self.assertIsInstance(self.state.created_at, datetime)

    def test_state_updated_at(self):
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_str_representation(self):
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_create_state(self):
        self.state.name = 'Florida'

        state_dict = self.state.to_dict()

        self.assertEqual(self.state.name, state_dict['name'])

        self.state.name = 'Foo'
        self.assertNotEqual(self.state.name, state_dict['name'])
        state_dict = self.state.to_dict()
        self.assertEqual(self.state.name, state_dict['name'])


if __name__ == '__main__':
    unittest.main()
