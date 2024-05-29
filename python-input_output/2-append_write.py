#!/usr/bin/python3
"""Module to append to a file"""


def append_write(filename="", text=""):
    """Method for appending to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
