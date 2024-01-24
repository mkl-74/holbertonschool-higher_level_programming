#!/usr/bin/python3


letter = ord('a')
while letter <= ord('z'):
    print("{}".format(chr(letter)), end="")
    letter += 1
print()