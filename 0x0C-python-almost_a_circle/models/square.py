#!/usr/bin/python3
"""This module contains a square class that subclasses a rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square

    Args:
        size (int): size of the square.
        x (int): x coordinate.
        y (int): y coordinate.
        id (int): id of the class created
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialiser
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Custom implementation of __str__.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ Getter method
        """
        return super().width

    @size.setter
    def size(self, new_value):
        """Setter method
        """
        Rectangle.width.__set__(self, new_value)
        Rectangle.height.__set__(self, new_value)

    def update(self, *args, **kwargs):
        """Assigns attributes
        """
        attr = ['id', 'width', 'x', 'y']
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k != 'height':
                    setattr(self, k, v)
            self.height = self.width

    def to_dictionary(self):
        """Returns dict representation of a Rectangle.
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
