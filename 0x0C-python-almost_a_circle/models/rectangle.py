#!/usr/bin/python3
"""This module contains a class that subclasses `Base`.
"""
from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle. It is subclassed from a Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): x coordinate.
            y (int): y coordinate.
        """
        super().__init__(id)
        for inp in ["width", "height", "x", "y"]:
            if type(eval(inp)) is not int:
                raise TypeError("{} must be an integer".format(inp))
        for val in ["width", "height"]:
            if eval(val) <= 0:
                raise ValueError("{} must be > 0".format(val))
        for coord in ["x", "y"]:
            if eval(coord) < 0:
                raise ValueError("{} must be >= 0".format(coord))

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter method for the width.

        Setter method
        Args:
            value (int): New value for the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Getter method for the height.

        Setter method
        Args:
            value (int): New value for the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Getter method for the x.

        Setter method
        Args:
            value (int): New value for the x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Getter method for the y.

        Setter method
        Args:
            value (int): New value for the y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """Prints int the stdout the rectangle instance with the character #
        """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """ Custom __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attr:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns dict representation of a Rectangle.
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
