#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_ints = set()  # Initializes an empty set to store unique integers

    for num in my_list:
        unique_ints.add(num)

    result = sum(unique_ints)  # Sum up all the unique integers
    return result
