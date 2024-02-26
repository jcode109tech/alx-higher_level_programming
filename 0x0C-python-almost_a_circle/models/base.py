#!/usr/bin/python3
""" CLASS <Base>
    Manages all other classes
"""


import json
import turtle

class Base:
    """ class <main> 
    Attributes:
    __nb_objects : public
    id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

    # --------- json string formart -----------
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return <JSON string> representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    # ----------- save file --------------------
    @classmethod
    def save_to_file(cls, list_objs):
        """Write <JSON string> representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    # ---------- list of json string --------
    @staticmethod
    def from_json_string(json_string): 
        """ Returns : <list of JSON string> """
        if json_string is None:
            return []

        return json.loads(json_string)
        

    # ----------- Instance with all attributes -------
    @classmethod
    def create(cls, **dictionary):
        """ Returns :  <instance>  with all attriutes """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1,1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class type")
        
        dummy.update(**dictionary)

        return dummy
    


    # ---------- Return list of instance ---------
    @classmethod
    def load_from_file(cls):
        """ Returns : <list> of instances """
        filename = "{}".format(cls.__name__) + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                instances = []
                for item in data:
                    instance = cls.to_json_string(item)
                    instances.append(instance)
                # instances = [cls.create(**instance_data) for instance_data in data]
                return instances 
        except FileNotFoundError:
            return []
        
    
    # --------- 
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """  """
        filename = cls.__name__+ ".csv"
        with open(filename, 'w', encoding='utf-8') as file:
            for obj in list_objs:
                if cls.__name__=="Rectangle":
                    line = "{},{},{},{},{}".format(obj.id, obj.width, obj.height, obj.x,obj.y)
                elif cls.__name__ == "Square":
                    line = "{},{},{},{}".format(obj.id, obj.size, obj.x,obj.y)
                file.write(line)
    
    @classmethod
    def load_from_file_csv(cls): 
        filename = cls.__name__ + ".csv"
        objects = []
        with open(filename, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                if cls.__name__ == "Rectangle":
                    obj = cls(int(fields[1]), int(fields[2]), int(fields[3]), int(fields[4]), int(fields[0]))
                elif cls.__name__ == "Square":
                    obj = cls(int(fields[1]), int(fields[2]), int(fields[3]), int(fields[0]))
                objects.append(obj)
        return objects
    
    # -------------- GUI tk ----------


    @staticmethod
    def draw(list_rectangles, list_squares):
        # Setup the turtle screen
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Drawing Rectangles and Squares")

        # Create a turtle object
        t = turtle.Turtle()
        t.speed(0)  # Set the drawing speed to the fastest

        # Draw rectangles
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.setheading(0)  # Reset the heading to face right
            t.color("blue")  # Set color to blue
            t.begin_fill()   # Start filling the rectangle
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.end_fill()     # End filling the rectangle

        # Draw squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.setheading(0)  # Reset the heading to face right
            t.color("red")   # Set color to red
            t.begin_fill()   # Start filling the square
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.end_fill()     # End filling the square

        # Hide the turtle and display the drawing
        t.hideturtle()
        turtle.done()

































    