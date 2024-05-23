#!/usr/bin/python3
""" Module that writes a class that inherits from list """


class MyList(list):
    """My list is a class with a public method print_sorted"""

    def print_sorted(self):
        print(sorted(self))
