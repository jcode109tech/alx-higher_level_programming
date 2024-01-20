#!/usr/bin/pyhton3

def no_c(my_string):
    new_str = ""
    for char in my_string:
        if ord(char.lower()) not in (ord('c'), ord('C')):
            new_str += char
    return new_str




