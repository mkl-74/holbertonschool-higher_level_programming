#!/usr/bin/python3

for lettre in range(97, 123):
    if lettre != 101 and lettre != 113:
        print("{:c}".format(lettre), end="")
