#!/usr/bin/python3

# Function that returns a list with all values multiplied
# by a number without using any loops.

def search_replace(my_list, search, replace):
    new = []
    for n in my_list:
        if n == search:
            new.append(replace)
        else:
            new.append(n)
    return(new)
