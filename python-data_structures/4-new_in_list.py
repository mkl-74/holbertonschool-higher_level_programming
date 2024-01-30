#!/usr/bin/python3

# replaces an element in a list at
# a specific position without modifying the original list.

def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
