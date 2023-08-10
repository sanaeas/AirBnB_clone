#!/usr/bin/python3
"""Defines the Review class, which inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing a review in the AirBnB clone project"""
    place_id = ''
    user_id = ''
    text = ''
