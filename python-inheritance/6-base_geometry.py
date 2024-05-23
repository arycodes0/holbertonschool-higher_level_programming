#!/usr/bin/python3
""" Module that contains a class """


class BaseGeometry:
    """
    Public instance method that raises an Exception with a message
    """

    def area(self):
        raise Exception("area() is not implemented")
