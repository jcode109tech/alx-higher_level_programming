#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

# Check conditions based on the last digit
if last_digit > 5:
    print("The last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("The last digit and is 0")
elif last_digit < 6 and last_digit == 0:
    print("and is less than 6 and not 0")
else:
    print("The last digit is less than 5")
