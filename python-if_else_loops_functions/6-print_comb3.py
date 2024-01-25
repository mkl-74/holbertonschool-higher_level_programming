#!/usr/bin/python

for nbr1 in range(0, 9):
    for nbr2 in range(1, 10):
        if nbr1 == nbr2:
            continue
        if nbr1 < nbr2:
            if nbr1 != 8 or nbr2 != 9:
                print("{:d}{:d},".format(nbr1, nbr2), end=' ')
            else:
                print("{:d}{:d}".format(nbr1, nbr2))

#for nbr1 in range(0, 9):
#    for nbr2 in range(1, 10):
#        if nbr1 == nbr2:
#            continue
#        if nbr1 < nbr2:
#            print("{}{},".format(nbr1, nbr2), end=' ')
