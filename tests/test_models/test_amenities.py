#!/usr/bin/python3
"""
unittest for amenities.
"""

import unittest
from models.amenity import Amenity
import datetime

class TestAmenity(unittest.TestCase):
    """
    For testing amenity class methods and instances
    """
    am = Amenity()
    
    def test_cls_exist(self):
        """class existance tester"""
        e = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.am)), e)

    def test_user_inheritance(self):
        """test if BaseModel is Amenitys parent class"""
        self.assertIsInstance(self.am, Amenity)

    def test_attributes(self):
        """test attributes existance"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_kind(self):
        """Tests attributes"""
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime.datetime)
        self.assertIsInstance(self.am.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
