#!/usr/bin/python3

# function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary is []:
        return None
    n =[]
    for new in a_dictionary:
        n.append(new)
    return max(n)
