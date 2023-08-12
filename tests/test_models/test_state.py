#!/usr/bin/python3
"""Unittests for state.py"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
