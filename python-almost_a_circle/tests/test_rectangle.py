#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):

    def setup(self):
        """Reset base"""
        Base.__nb_objects = 0
    
    def test_int_pos(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id)
        
    def 
        
    
    
    
    
    
    if __name__ == "__main__":
        unittest.main()
