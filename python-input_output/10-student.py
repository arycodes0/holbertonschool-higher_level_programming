#!/usr/bin/python3
"""Module to create a class Student that defines a student"""


class Student:
    """Creates Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            new_dict = {}
            for x in attrs:
                if str(x) == "first_name":
                    new_dict[x] = self.first_name
                elif x == "last_name":
                    new_dict[x] = self.last_name
                elif x == "age":
                    new_dict[x] = self.age
            return new_dict
        else:
            return self.__dict__
