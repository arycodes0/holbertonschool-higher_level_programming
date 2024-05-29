#!/usr/bin/python3
"""Module that adds all args to a Python list, then saves them to a file"""


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []
for x in sys.argv[1:]:
    my_list.append(x)
    save_to_json_file(my_list, "add_item.json")
