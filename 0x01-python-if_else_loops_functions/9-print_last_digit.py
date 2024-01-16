#!/usr/bin/python3

def uppercase(str):
    for char in str:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        uppercase_char = chr(ord(char) + 32) if 'A' <= char <= 'Z' else uppercase_char
        print("{}".format(uppercase_char), end="")
    print("\n")


