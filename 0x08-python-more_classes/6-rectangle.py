#!/usr/bin/python3

"""
   CLASS DEFINATION:
   Define Rectangle
"""


class Rectangle:
    """
        Sets <widht> and <height>
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Intilizes attribute : <Height> <Width>"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Computes area"""
        return self.height * self.width

    def perimeter(self):
        """Computes perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """
            __str__ : prints: <user friendly string>
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string

        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        """
            __repr__ : prints eval support
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ deletes rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
