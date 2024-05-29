#!/usr/bin/python3
"""Module for a class Student that defines a student by public attributes"""


class Student:
    """Creating the Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
