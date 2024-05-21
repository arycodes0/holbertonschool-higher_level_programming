#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number, defaults to 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
