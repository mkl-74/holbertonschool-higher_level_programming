#!/usr/bin/python3
"""test_base"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        """Reset base"""
        Base._nb_objects = 0

    def test_base_class(self):
        # Creating objects with unique identifiers
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_spe_id(self):
        # Creating an object with a specific identifier
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_incr_id(self):
        # Automatic increment of identifier
        b5 = Base()
        self.assertEqual(b5.id, 1)

    def test_neg_id(self):
        # Negative identifier
        b6 = Base(-5)
        self.assertEqual(b6.id, -5)


if __name__ == "__main__":
        unittest.main()
