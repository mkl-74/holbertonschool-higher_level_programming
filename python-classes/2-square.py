#!/usr/bin/python3

""" 2-square.py : Write a class Square that defines a square by:(based on 1-square.py)

"""

class Square:
    def __init__(self, size=0):
        if size is not int:
            print("size must be an integer")
        if size <= 0:
            print("size must be >= 0")
