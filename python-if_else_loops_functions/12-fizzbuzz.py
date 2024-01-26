#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0:
            if number % 5 == 0:
                print("FizzBuzz", end=" ")
            else:
                print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(number), end=" ")