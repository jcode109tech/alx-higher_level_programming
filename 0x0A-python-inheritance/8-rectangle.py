#!/usr/bin/python3

"""
<subslass>
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    <subclass> BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializer
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
