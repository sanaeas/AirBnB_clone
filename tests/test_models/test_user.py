#!/usr/bin/python3
"""Unittests for user.py"""

import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_user_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_created_at(self):
        self.assertIsInstance(self.user.created_at, datetime)

    def test_user_updated_at(self):
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_str_representation(self):
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

if __name__ == '__main__':
    unittest.main()
