#!/usr/bin/python3

"""
File_name: 11-delete_at.py
Created: 10th of June, 2023
Auth: Oni Ajibola Taiwo (Daniel Reborn)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def delete_at(my_list=[], idx=0):
    if my_list:
        if 0 <= idx < len(my_list):
            del my_list[idx]
    return my_list
