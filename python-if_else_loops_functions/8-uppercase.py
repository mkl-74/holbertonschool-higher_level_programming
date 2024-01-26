#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 126:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
