#!/usr/bin/python3
"""Module for instantiating a FileStorage object."""

from models.engine.file_storage import FileStorage

# Instantiate a FileStorage object
storage = FileStorage()

# Reload objects from storage
storage.reload()
