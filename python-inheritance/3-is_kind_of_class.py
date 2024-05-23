#!/usr/bin/python3
"""
Module that returns True if obj is an instance
of, or if obj is an instance of class that inherited,
the specified class, otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Check wether an obj is the same type of another"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
