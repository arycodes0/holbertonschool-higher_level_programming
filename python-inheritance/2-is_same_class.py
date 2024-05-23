#!/usr/bin/python3
"""
Module that returns True if he obj is exactly an instance
of the specified class, False ortherwise
"""


def is_same_class(obj, a_class):
    """
    Checks class if same type of object
    args:
        obj: object import
        a_class: class type
    Return:
        True or False
    """

    if type(obj) is a_class:
        return True
    else:
        return False
