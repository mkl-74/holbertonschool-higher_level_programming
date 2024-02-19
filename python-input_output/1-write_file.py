#!/usr/bin/python3
"""function that write a string and return the number of characters"""


def write_file(filename="", text=""):
    """
    Args :
    filename = The name of the file to write
    text = the text written in to the file

    Return = the number of characters written to the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
