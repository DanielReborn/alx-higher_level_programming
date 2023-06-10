#!/usr/bin/python3

"""
File_name: 9-max_integer.py
Created: 10th of June, 2023
Auth: Oni Ajibola Taiwo (Daniel Reborn)
Size: undefined
Project: 0x03-python-data_structures
Status: submitted.
"""


def max_integer(my_list=[]):

    """
    # Write a function that finds the biggest integer of a list.
    # Variables:
    # my_list(list): The first tuple..
    # If the list is empty, return None
    """
    if my_list:
        max = my_list[0]
        for list_number in my_list:
            if list_number >= max:
                max = list_number
        return max
    else:
        return None
