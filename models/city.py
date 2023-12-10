#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """User class definition

    Inherits the BaseModel class

    Attributes:
        state_id (str): The id of the city
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
