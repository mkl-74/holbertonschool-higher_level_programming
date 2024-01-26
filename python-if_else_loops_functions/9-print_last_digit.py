#!/usr/bin/python3

def print_last_digit(number):
    lastdigit = abs(number) % 10
    print("{}".format(lastdigit), end="")
    return lastdigit
