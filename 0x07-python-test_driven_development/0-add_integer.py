#!/usr/bin/python3
"""
    Adds two integers.
    Prototype: def add_integer(a, b=98)
    RETURNS : (addition)
"""


def add_integer(a, b=98):
    """
    a and b must be integers or floats <Typeerror check>
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return a + b
