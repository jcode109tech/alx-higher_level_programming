#!/usr/bin/python3

"""
   CLASS DEFINATION:
   Define Rectangle
"""

class Rectangle:
   """
      Sets <widht> and <height
   """

   def __init__(self, width=0, height=0):
      """ Intilizes attribute : <Height> <Width>"""
      self.width = width
      self.height = height

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
