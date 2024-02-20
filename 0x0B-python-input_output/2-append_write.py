#!/usr/bin/python3
"""
Module to run the append
"""


def append_write(filename="", text=""):
    """
    ./appends onto a utf-8 encoded text file
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
