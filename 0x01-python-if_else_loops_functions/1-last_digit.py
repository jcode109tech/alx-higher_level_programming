#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

# We first convert the number to a string
number_string = str(number)

last_digit = number_string[-1]

if number < 0:
    last_digit = "-" + last_digit

print(f"Last digit of {number} is {last_digit} and", end=" ")

if int(last_digit) > 5:
    print(f"is greater than 5")
elif int(last_digit) == 0:
    print(f"is 0")
else:
    print(f"is less than 6 and not 0")
