#!/usr/bin/python3
"""
<class> : geometry
"""


class BaseGeometry:
    """
    BaseGeometry
    Methods:
        Area
        integer_validator
    """
    def area(self):
        """
        <raise excption>
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        <checks input values
        """
        if (type(value) != int):
            raise TypeError(name +" must be an integer")

        if (value <= 0):
            raise ValueError(name +" must be greater than 0")
