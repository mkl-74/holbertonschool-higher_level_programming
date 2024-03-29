#!/usr/bin/python3




def add_integer(a, b=98):
    """Write a function that adds 2 integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")
