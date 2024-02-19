#!/usr/bin/python3

"""
    inherits <class> properties
"""


class MyList(list):
    """
       <subclass> for List
    """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
