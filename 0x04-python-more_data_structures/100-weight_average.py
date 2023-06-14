#!/usr/bin/python3

"""
File_name: 100-weight_average.py
Created: 14th of June, 2023
Auth: Oni Ajibola Taiwo (Daniel Reborn)
Size: undefined
Project: 0x04-python-more_data_structures
Status: submitted.
"""


def weight_average(my_list=[]):

    """
    # Write a function that returns the weighted average
    # of all integers tuple (<score>, <weight>)
    # VARIABLE(" "):
    # weight_average(list): Weighted average!
    # Returns: 0 if the list is empty
    """

    if not my_list:
        return 0

    total_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    return total_sum / total_weight
