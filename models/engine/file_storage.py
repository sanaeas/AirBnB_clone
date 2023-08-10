#!/usr/bin/python3
"""
Defines the FileStorage class responsible for serializing instances to JSON
and deserializing instances from JSON
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    A class that manages serialization and deserialization of instances to JSON
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary containing all instances"""
        return self.__objects

    def new(self, obj):
        """Adds a new instance to the dictionary of objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes instances to JSON and saves to a file"""
        obj_dict = dict(self.__objects)
        for key, val in obj_dict.items():
            obj_dict[key] = val.to_dict()

        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes instances from JSON and populates the dictionary of objects"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    obj = eval(class_name)(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
