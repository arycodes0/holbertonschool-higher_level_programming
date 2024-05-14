#!/usr/bin/python3
def no_c(my_string):
    # Empty string to store the result
    result = ""
    for char in my_string:
        if char != "c" and char != "C":
            # Append the char to the result string
           result += char
    return result
