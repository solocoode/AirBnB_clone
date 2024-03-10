#!/usr/bin/python3
"""Module for managing file storage for the HBNB clone."""

import json


class FileStorage:
    """Class to manage storage of HBNB models in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the storage dictionary to a file."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Loads the storage dictionary from a file."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, val in serialized_objects.items():
                    class_name = val['__class__']
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            pass
