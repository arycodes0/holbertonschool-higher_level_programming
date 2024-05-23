#!/usr/bin/python3
"""
Module that writes a class Square
that inherits out of Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Creating the class Square that inherits
    out of Rectangle
    """

    def __init__(self, size):
        """
        Initialize a new square

        Args:
        size (int): The size of the new square>
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
