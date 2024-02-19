#!/usr/bin/python3
""" 
<object == object>
"""


def is_same_class(obj, a_class):
    """
    True <object>, Otherwise False
    """
    if (type(obj) == a_class):
        return True
    else:
        return False
