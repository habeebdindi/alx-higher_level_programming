#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and number % 10 != 0:
    print(f"Last digit of {number:d} is -{abs(number) % 10:d} and is less than\
 6 and not 0")
else:
    if number % 10 < 6 and number % 10 > 0:
        print(f"Last digit of {number:d} is {abs(number) % 10:d} and is less\
 than 6 and not 0")
    elif number % 10 == 0:
        print(f"Last digit of {number:d} is {abs(number) % 10:d} and is 0")
    else:
        print(f"Last digit of {number:d} is {abs(number) % 10:d} and is\
 greater than 5")
