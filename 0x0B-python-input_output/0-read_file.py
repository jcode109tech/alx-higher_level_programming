#!/usr/bin/python3
"""
read <Json>
"""


def read_file(filename=""):
    """
    reads file <utf-8>
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
