#!/usr/bin/python3
"""Unittests for base_model.py"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    @patch('models.storage')
    def test_save_updates_updated_at(self, mock_storage):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    @patch('models.storage')
    def test_to_dict_returns_dict(self, mock_storage):
        dict_repr = self.base_model.to_dict()
        self.assertIsInstance(dict_repr, dict)

    def test_to_dict_has_expected_keys(self):
        dict_repr = self.base_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(dict_repr.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        dict_repr = self.base_model.to_dict()
        datetime_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.assertEqual(
            dict_repr['created_at'], self.base_model.created_at.strftime(datetime_format))
        self.assertEqual(
            dict_repr['updated_at'], self.base_model.updated_at.strftime(datetime_format))

    def test_to_dict_attributes_are_correct(self):
        self.base_model_dict = self.base_model.to_dict()
        self.assertEqual(self.base_model_dict['id'], self.base_model.id)
        self.assertEqual(self.base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(self.base_model_dict['updated_at'], self.base_model.updated_at.isoformat())
        self.assertEqual(self.base_model_dict['__class__'], 'BaseModel')

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
