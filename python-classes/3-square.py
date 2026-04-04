#!/usr/bin/python3
"""This module defines a Square class with area method"""


class Square:
    """A class that defines a square with size validation and area method"""

    def __init__(self, size=0):
        """Initialize a new Square with a given size

        Args:
            size (int): the size of the square, defaults to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size * size)
        """
        return self.__size ** 2
