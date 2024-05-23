#!/usr/bin/python3
"""
Module that writes a class Rectangle
that inherits  BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """
        Create an instance of the class with
        specified width and height attributes
        """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

        self.__width = width
        self.__height = height
