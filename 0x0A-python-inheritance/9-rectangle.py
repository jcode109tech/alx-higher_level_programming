#!/usr/bin/python3

"""
<subclass> validated
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle extends from BaseGeometry(parent class)
    """
    def __init__(self, width, height):
        """
        initializer
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Function to return area of a Rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns string of rectangle format
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
