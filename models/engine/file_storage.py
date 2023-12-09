#!/usr/bin/python3
"""Dictionary to JSON String"""
import json


class FileStorage:
    """Represents a storage engine

    Attributes:
        __file_path: string - path to the JSON file
        __objects: store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets object with key"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data_dict = FileStorage.__objects
        objs = {obj: data_dict[obj].to_dict() for obj in data_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objs, f)

    def reload(self):
        """deserializes the JSON file to __objects, if it exits"""
        try:
            with open(FileStorage.__file_path) as f:
                objs = json.load(f)
                for obj in objs.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
