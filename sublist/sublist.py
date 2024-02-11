"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from functools import reduce

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = object()
SUPERLIST = object()
EQUAL = object()
UNEQUAL = object()


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if list_one and not list_two:
        return SUPERLIST

    if not list_one and list_two:
        return SUBLIST

    if len(list_one) > len(list_two):
        try:
            for start in range(len(list_one) - len(list_two)):
                start = list_one.index(list_two[0], start)
                end = start + len(list_two)
                if list_two == list_one[start:end]:
                    return SUPERLIST
        except Exception:
            pass

    if len(list_one) < len(list_two):
        try:
            for start in range(len(list_two) - len(list_one)):
                start = list_two.index(list_one[0], start)
                end = start + len(list_one)
                if list_one == list_two[start:end]:
                    return SUBLIST
        except Exception:
            pass

    return UNEQUAL
