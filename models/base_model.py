#!/usr/bin/python3

import uuid
from datetime import datetime
from models
"""defines the BaseModel class and its attr and methods"""


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, val)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        returns string representation of the object instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update instance attribute"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all
         keys/values of __dict__ of the instance
        """
        res_dict = self.__dict__.copy()
        res_dict["__class__"] = self.__class__.__name__
        res_dict["created_at"] = self.created_at.isoformat()
        res_dict["updated_at"] = self.updated_at.isoformat()
        return res_dict
