#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):

    def setup(self):
        """Reset base"""
        Base.__nb_objects = 0
    
    def test_nbr_id(self):
        """test nbr_id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        
        
    
    
    
    
    
    if __name__ == "__main__":
        unittest.main()
