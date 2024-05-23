#!/usr/bin/python3
"""
Module that writes a class Rectangle
that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Creating a class Rectangle"""

    def __init__(self, width, height):
        """
        Create an instance of the class with
        specified width and height private attributes
        """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """
        The area method is implemented
        """
        return self.__width * self.__height

    def __str__(self):
        """
        The str method returns the Rectangle description,
        it's width, and height
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
