#!/usr/bin/python

for nbr1 in range(0, 9):
    for nbr2 in range(1, 10):
        if nbr1 == nbr2:
            continue
        if nbr1 < nbr2:
            print(f"{nbr1}{nbr2},", end=' ')
