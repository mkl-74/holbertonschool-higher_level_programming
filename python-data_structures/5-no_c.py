#!/usr/bin/python3

# function that removes all characters
# c and C from a string.

def no_c(my_string):

    ch = "'c''C'"
    my_string = "".join(x for x in my_string if x not in ch)
    return(my_string)
