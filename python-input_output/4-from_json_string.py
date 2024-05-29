#!/usr/bin/python3
"""Module that returns an object represented by a JSON string"""


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON str"""
    import json

    return json.loads(my_str)
