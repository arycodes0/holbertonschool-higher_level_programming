#!/usr/bin/python3
"""Module returning the JSON representation of an object"""


def to_json_string(my_obj):
    """Returns JSON representation of a string"""
    import json

    return json.dumps(my_obj)
