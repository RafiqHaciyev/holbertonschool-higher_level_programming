#!/usr/bin/python3
"""This module defines a Square class with a private size attribute"""


class Square:
    """A class that defines a square with a private size attribute"""

    def __init__(self, size):
        """Initialize a new Square with a given size

        Args:
            size: the size of the square
        """
        self.__size = size
