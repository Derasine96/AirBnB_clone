#!/usr/bin/python3

import uuid
from datetime import datetime
"""defines the BaseModel class and its attr and methods"""


class BaseModel:
    """Base class for AirBnb"""
    def __init__(self, *args, **kwargs):
        """constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        returns string representation of the object instance
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
         returns a dictionary containing all
         keys/values of __dict__ of the instance
        """
        res_dict = self.__dict__.copy()
        res_dict["__class__"] = type(self).__name__
        res_dict["created_at"] = self.created_at.isoformat()
        res_dict["updated_at"] = self.updated_at.isoformat()
        return res_dict
