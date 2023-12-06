#!/usr/bin/python3
"""Dictionary to JSON String"""
import json


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances"""
    def __init__(self):
        self.__file_path = file_path
        self.__objects = {}


    def all(self):
        """returns the dictionary of objects"""
        object_id = f"{_object.__class__.__name__}.{_object.id}"
        return object_id

    def new(self, obj):
        """sets object with key"""
        
