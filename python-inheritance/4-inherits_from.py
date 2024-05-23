#!/usr/bin/python3
"""
Module that returns True if the obj is an instance
of a class that inherited from the specified class, otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if obj is an inherited instance of a_class or not"""

    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
