#!/usr/bin/python3

class Square:
   """ 
       Intialization of size : square
       size -> private
   """

   def __init__(self, size=0):
      """
         Hanbles type error and value error
      """
      if type(size)  != int:
         raise TypeError("size must be an integer")
      if size < 0:
         raise ValueError("size must be >= 0")
      else:
         self.__size = size 


   def area(self):
      """
         Finds area
      """
      return self.__size * self.__size
