#!/usr/bin/python3
"""
unittest for review.py
"""
import unittest
from models.review import Review
import datetime

class test_Review(self):
    """Tests instances and methods from Review class"""

    rev = Review()


    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertEqual(str(type(self.rev)), "<calss 'models.review.Review'>")

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.rev, 'place_id'))
        self.assertTrue(hasattr(self.rev, 'user_id'))
        self.assertTrue(hasattr(self.rev, 'text'))
        self.assertTrue(hasattr(self.rev, 'id'))
        self.assertTrue(hasattr(self.rev, 'created_at'))
        self.assertTrue(hasattr(self.rev, 'updated_at'))


    def test_types(self):
        """test if attributes are of the correct type"""
        self.assertIsInstance(self.rev.place_id, str)
        self.assertIsInstance(self.rev.user_id, str)
        self.assertIsInstance(self.rev.text, str)
        self.assertIsInstance(self.rev.id, str)
        self.assertIsInstance(self.rev.created_at, datetime.datetime)
        self.assertIsInstance(self.rev.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
