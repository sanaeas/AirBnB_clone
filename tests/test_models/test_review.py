#!/usr/bin/python3
"""Unittests for review.py"""

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
