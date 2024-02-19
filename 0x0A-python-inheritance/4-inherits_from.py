#!/usr/bin/python3

"""
<inherits Module>
Creates a function that returns true
if object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
      Return: True or False
    """
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
