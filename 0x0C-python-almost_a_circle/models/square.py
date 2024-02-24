#/usr/bin/python3
"""
class <Square>
<inherites <Rectangle>>
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Class Rectangle:
    Attributes:
        size
        x
        y
        id
    """
   
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)
    
    # -------------- str -----------------------
    def __str__(self):
        """String representation of Square."""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width)
    
    # --------- propert and setter -------------
    # size
    @property
    def size(self):
        """ <size> getter """
        return self.width
    
    @size.setter
    def size(self, value):
        """ <size> setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("Width must be > 0")

        self.width = value
        self.height = value

    # ------ *args & **kwargs ---------
    def update(self, *args, **kwargs):
        """ <updates>
            *args , Otherwise **kwargs
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key != "id":
                    setattr(self, key, value)


    # --------- dict -------------------
    def to_dictionary(self):
        """" Returns <dict> form <args/kwargs> """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }