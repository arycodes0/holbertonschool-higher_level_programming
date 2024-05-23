#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.

This module provides a base class for geometric shapes with methods for 
validating integers and calculating areas. 

Classes:
    BaseGeometry: A base class with methods to validate integers and to 
    calculate areas (not implemented).
"""


class BaseGeometry:
    """
    BaseGeometry class for geometric operations.

    Methods:
        area(self): Raises an Exception indicating that the method is not implemented.
        integer_validator(self, name, value): Validates that a value is an integer
        and greater than 0.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.

        Raises:
            Exception: Always raised with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer with the message "<name> must be an integer".
            ValueError: If value is less than or equal to 0 with the message "<name> must be greater than 0".
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
