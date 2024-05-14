#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = [my_list[len(my_list) - i] for i in range(1, len(my_list) + 1)]
    for num in reversed_list:
        print("{:d}".format(num))
