#!/usr/bin/python3
"""
Defines the City class, which inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class representing a city in the AirBnB clone project"""
    state_id = ''
    name = ''
