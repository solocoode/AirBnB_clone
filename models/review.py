#!/usr/bin/python3
"""Review module for the HBNB project.

Defines the Review class representing review information.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""
