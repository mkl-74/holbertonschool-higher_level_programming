#!/usr/bin/python3


import unittest
from models.base import Base

def test_base_class():
    # Creating objects with unique identifiers
    b1 = Base()
    b2 = Base()
    b3 = Base()
    assert b1.id == 1
    assert b2.id == 2
    assert b3.id == 3

def spe_id():
    # Creating an object with a specific identifier
    b4 = Base(12)
    assert b4.id == 12

    # Automatic increment of identifier
    b5 = Base()
    assert b5.id == 4

    # Negative identifier
    b6 = Base(-5)
    assert b6.id == -5

    # Identifier as a string
    b7 = Base("abc")
    # The identifier should remain automatic, as a string is not a valid identifier.
    assert b7.id == 5

    # Additional test : Check if __nb_objects is correctly updated
    assert Base.__nb_objects == 5

if __name__ == "__main__":
    test_base_class()
    print("All tests passed!")