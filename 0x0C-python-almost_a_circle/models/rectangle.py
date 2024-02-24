#!/usr/bin/python3
"""
class <Rectangle>
<inherites <Base>>
"""


from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle:
    Attributes:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ---------------------- @widht --------------
    @property
    def width(self):
        """ <width> getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ <width> setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("Width must be > 0")

        self.__width = value

    # ------------------------ @height ----------
    @property
    def height(self):
        """ <height> getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ <height> setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value


    # -------------- @x ----------------------------
    @property
    def x(self):
        """ <x> getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ <x> Setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")

        self.__x = value

    # --------------- @y ---------------------------
    @property
    def y(self):
        """ <y> getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ <y> setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")

        self.__y = value

    # ------- __str__ overide -------------------
    def __str__(self) -> str:
        """ custom : overright <__str__>"""
        custom_str = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                                    self.id,
                                                                    self.x,
                                                                    self.y,
                                                                    self.width,
                                                                    self.height)
        return custom_str

    
    # -------------- area of rectangle ----------
    def area(self):
        """ calc area(<height> * <width>) """
        return self.height * self.width
    
    def display(self):
        """ dislay : #
            handleS : <x> <y>
        """
        for _ in range(self.y):
            print()   
        for _ in range(self.height):
            print(" " * self.x  + "#" * self.width)
        
    
    # -------- update class attriutes by args ----
    def update(self, *args, **kwargs):
        """<Update : attributes> with provided <arguments>."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    # ---- set to dictionary ------------
    def to_dictionary(self):
        """Return : <dict> rep of Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    
