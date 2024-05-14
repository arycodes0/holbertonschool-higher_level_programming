#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Initialize an empty set to store common elements
    common_set_of_elements = set()

    for element in set_1:
        if element in set_2:
            common_set_of_elements.add(element)

    return common_set_of_elements
