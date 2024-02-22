#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """Reset base"""
        Base.__nb_objects = 0
    
    def test_without_id(self):
        """test without id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_with_id(self):
        """test with id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_area(self):
        
        
    
    
    
    
    
    if __name__ == "__main__":
        unittest.main()
