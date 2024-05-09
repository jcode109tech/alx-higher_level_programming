#!/usr/bin/python3

"""
Finds a peak in a list of integers
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of integers
    """
    if list(list_of_integers):
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None

