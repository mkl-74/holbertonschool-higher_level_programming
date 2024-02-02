#!/usr/bin/python3

# prints a dictionary by ordered keys.


def print_sorted_dictionary(a_dictionary):
    for key, values in sorted(a_dictionary.items()):
        print("{}: {}".format(key, values))
