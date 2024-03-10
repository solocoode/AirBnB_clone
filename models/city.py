#!/usr/bin/python3
""" City Module for HBNB project

Defines the City class representing cities in HBNB.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class containing state id and name"""
    state_id = ""
    name = ""
