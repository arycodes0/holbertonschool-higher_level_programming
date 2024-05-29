#!/usr/bin/python3
"""Module that returns the dictionary 4 JSON serialization of an object"""


import json


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
