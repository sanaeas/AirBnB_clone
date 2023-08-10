#!/usr/bin/python3
"""
Defines the User class, which inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class representing a user in the AirBnB clone project"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
