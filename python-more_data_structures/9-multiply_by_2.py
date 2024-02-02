#!/usr/bin/python3

# function that returns a new dictionary with all
# values multiplied by 2

def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for ne in new:
        new[ne] *= 2
    return new
