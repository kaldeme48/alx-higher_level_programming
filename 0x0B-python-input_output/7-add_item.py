#!/usr/bin/python3
"""Module 7-add_item.
Adds all arguments to a Python list,
and then save them to a file.
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    py_list = []
finally:
    for el in sys.argv[1:]:
        py_list.append(str(el))
    save_to_json_file(py_list, filename)
