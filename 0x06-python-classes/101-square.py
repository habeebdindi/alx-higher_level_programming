#!/usr/bin/python3
class Square:
    """ A class that defines a square

    Attributes:
    size (obj: 'int'): size of the square
    area (obj: 'int'): area of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        """ Set private attribute of square size to var size
        Set private attribute of position to var position
        """

    @property
    def size(self):
        """ Defines size of square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Defines size of square object to change to value

        Args:
        size (obj:'int') size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """ Only positive integers allowed for attribute size

        """
        self.__size = value

    @property
    def position(self):
        """ Defines position of square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position of value if its a tupe of 2 pos ints
        
        """
        if type(value) is not tuple or len(value) != 2 or\
            type(value[0]) is not int or value[0] < 0 or\
            value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """ Defines area of square object

        """
        return self.__size ** 2

    def __str__(self):
        new_str = ""
        if self.__size is 0:
            return ""
        else:
            new_str += '\n' * self.__position[1]
            for i in range(self.__size):
                new_str += ' ' * self.position[0]
                new_str += '#' * self.__size
                new_str += '\n'
        return new_str[:-1]

    def my_print(self):
        """ Prints a square of hashes

        """
        if self.size is 0:
            print()
            return ""
        for i in range(0, self.position[1]):
            print()
        for i in range(0, self.size):
            print((" " * self.position[0]) + ("#" * self.size))
        return ""
