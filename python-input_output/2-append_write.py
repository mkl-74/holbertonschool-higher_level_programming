#!/usr/bin/python3
"""Append a string at the end of a text
file and return a number of character

"""


def append_write(filename="", text=""):
    """add a line of this text"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
