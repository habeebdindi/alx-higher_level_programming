#!/usr/bin/python3
"""
Module level doc
"""


class Node:
    """ Node class
    """
    def __init__(self, data, next_node=None):
        """ Initializer

        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Getter method
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter method
        """
        self.__data = value

    @property
    def next_node(self):
        """ Getter method for next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list
    """
    def __init__(self):
        """ Initialiser method
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Sorted Insert
        """
        new_node = Node(value, None)

        if self.__head is None:
            self.__head = new_node
            return

        current = self.__head
        temp = None

        while current is not None and current.data < value:
            temp = current
            current = current.next_node

        if temp is None:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node.next_node = current
            temp.next_node = new_node

    def __str__(self):
        """ __str__
        """
        result = []
        current_node = self.__head
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(result)
