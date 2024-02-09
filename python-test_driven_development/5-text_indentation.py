#!/usr/bin/python3


def text_indentation(text):
    """Print a text with two space line when meet '.' or ':' or '?'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".:?":
            print("\n" * 2, end="")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
