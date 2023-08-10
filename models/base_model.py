#!/usr/bin/python3
"""
Module that defines the BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that serves as the base for all other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel
        """
        if kwargs:
            tformat = '%Y-%m-%dT%H:%M:%S.%f'
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(val, tformat)
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime,
        and saves the instance to the storage system
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation
        """
        dict_repr = self.__dict__.copy()
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        dict_repr['__class__'] = self.__class__.__name__

        return dict_repr

    def __str__(self):
        """Returns a string representation of the instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
