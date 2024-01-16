#!/usr/bin/python3

def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif (i % 3 and i % 5) == 0:
            print("FizzBuzz")
        else:
            print(i)

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % (3 * 5) == 0:
            print("FizzBuzz", end=" ")
        else:
            print(f"{i}", end=" ")


print(fizzbuzz())