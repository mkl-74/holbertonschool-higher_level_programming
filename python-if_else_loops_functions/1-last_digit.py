#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    lastnbr = number % 10
else:
    lastnbr = abs(number) % 10 * -1


if lastnbr > 5:
    print(f"Last digit of {number} is {lastnbr} and is greater than 5")
elif lastnbr == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    print(f"Last digit of {number} is {lastnbr} and is less than 6 and not 0")
