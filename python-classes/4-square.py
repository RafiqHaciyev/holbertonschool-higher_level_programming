#!/usr/bin/python3
"""This module defines a Square class with getter and setter"""


class Square:
    """A class that defines a square with getter and setter for size"""

    def __init__(self, size=0):
        """Initialize a new Square with a given size

        Args:
            size (int): the size of the square, defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square

        Returns:
            The current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation

        Args:
            value (int): the new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size ** 2
