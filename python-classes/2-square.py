#!/usr/bin/python3
"""This module defines a Square class with size validation"""


class Square:
    """A class that defines a square with size validation"""

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
