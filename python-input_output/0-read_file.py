#!/usr/bin/python3
"""function that read a text file"""


def read_file(filename=""):
    """
    Read the files "my_file_0
    """
    with open(filename, 'r', encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end="")
