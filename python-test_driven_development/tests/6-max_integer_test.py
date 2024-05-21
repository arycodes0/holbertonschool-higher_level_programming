#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_empty_list(self):
        """Tests empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Tests one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_sorted(self):
        """Tests sorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_sorted_reverse(self):
        """Tests sorted list in reverse"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_random(self):
        """Tests random list"""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negative(self):
        """Tests negative list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
