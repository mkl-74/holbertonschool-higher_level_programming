#!/usr/bin/python3
"""function that write a string and return the number of characters"""


def write_file(filename="", text=""):
    with open('filename', 'w', encoding='utf-8') as f:
        f.write(text)
        print(text, end='')
        return len(text)
