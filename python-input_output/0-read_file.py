#!/usr/bin/python3
"""Module that reads a text file and prints to stdout"""


def read_file(filename=""):
    """Method for reading a file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
