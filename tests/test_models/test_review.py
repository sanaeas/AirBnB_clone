#!/usr/bin/python3
"""Unittests for review.py"""

import unittest
from models.review import Review
from datetime import datetime
import models


class TestReview(unittest.TestCase):

    def test_instantiation(self):
        self.assertEqual(Review, type(Review()))

    def test_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_type(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_type(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_type(self):
        self.assertEqual(str, type(Review.text))

    def setUp(self):
        self.review = Review()

    def test_review_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_created_at(self):
        self.assertIsInstance(self.review.created_at, datetime)

    def test_review_updated_at(self):
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_str_representation(self):
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_create_review(self):
        self.review.place_id = 'abdc-1234'
        self.review.user_id = 'efgh-4321'
        self.review.text = 'Amazing'

        review_dict = self.review.to_dict()

        self.assertEqual(self.review.place_id, review_dict['place_id'])
        self.assertEqual(self.review.user_id, review_dict['user_id'])
        self.assertEqual(self.review.text, review_dict['text'])

        self.review.text = 'Beautiful'
        self.assertNotEqual(self.review.text, review_dict['text'])
        review_dict = self.review.to_dict()
        self.assertEqual(self.review.text, review_dict['text'])


if __name__ == '__main__':
    unittest.main()
