#!/usr/bin/pyhton3

def no_c(my_string):
    new_str = ""
    # loop through each character in a string
    for char in my_string:
        if char.lower() not in ['c', 'C']:
            new_str += char
    # return the modified string
    return new_str



