#!/usr/bin/python3

import unittest
import os
from models.basemodel import BaseModel

"""
BaseModel Unittest
"""

class TestBaseModelll(unittest.TestCase):
    """
    Tests for the base model
    """
    modelll = BaseModel()

    def test_id(self):
        base1, base2 = modelll, modelll
        self.assertNotEqual(base1.id, base2.id)
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base1.id, BaseModel)
        self.assertIsInstance(base2.id, str)
        self.assertIsInstance(base2.id, BaseModel)

if __name__ == '__main__':
        unittest.main()
