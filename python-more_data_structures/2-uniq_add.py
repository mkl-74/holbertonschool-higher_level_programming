#!/usr/bin/python3

#  function that adds all unique integers in a list (only once for each integer).


def uniq_add(my_list=[]):
    new = set(my_list)
    sum = 0
    for n in new:
        sum += n
    return (sum)
