#!/usr/bin/python3
"""Module that creates an Object form a JSON file"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file”"""
    with open(filename, "r", encoding="utf-8") as f:
        import json

        return json.load(f)
