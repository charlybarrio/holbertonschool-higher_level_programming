#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

items = []
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

for item in sys.argv[1:]:
    items.append(item)

save_to_json_file(items, "add_item.json")
