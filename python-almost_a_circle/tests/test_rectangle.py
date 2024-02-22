#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    
    def test_int_pos(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id)
        
    
    
    
    
    
    if __name__ == "__main__":
        unittest.main()
