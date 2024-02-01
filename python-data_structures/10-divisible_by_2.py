#!/usr/bin/python3

#  function that finds all multiples of 2 in a list.

def divisible_by_2(my_list=[]):
    multiples_of_2 = [num % 2 == 0 for num in my_list]
    return multiples_of_2
