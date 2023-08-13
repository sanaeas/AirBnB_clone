#!/usr/bin/python3
"""Unittests for user.py"""

import unittest
from models.user import User
from datetime import datetime
import models


class TestUser(unittest.TestCase):

    def test_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_type(self):
        self.assertEqual(str, type(User.email))

    def test_password_type(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_type(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_type(self):
        self.assertEqual(str, type(User.last_name))

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
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_create_user(self):
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john@email.com"
        self.user.password = "Abcd123"

        user_dict = self.user.to_dict()

        self.assertEqual(self.user.first_name, user_dict['first_name'])
        self.assertEqual(self.user.last_name, user_dict['last_name'])
        self.assertEqual(self.user.email, user_dict['email'])
        self.assertEqual(self.user.password, user_dict['password'])

        self.user.first_name = "Foo"
        self.assertNotEqual(self.user.first_name, user_dict['first_name'])
        user_dict = self.user.to_dict()
        self.assertEqual(self.user.first_name, user_dict['first_name'])


if __name__ == '__main__':
    unittest.main()
