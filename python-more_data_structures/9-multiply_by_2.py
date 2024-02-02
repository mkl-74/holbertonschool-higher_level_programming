#!/usr/bin/python3

# function that returns a new dictionary with all
# values multiplied by 2

def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key_value in new:
        new[key_value] *= 2
    return new
