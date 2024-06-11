"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 5
SUPERLIST = 6
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):
    a = list_one
    b = list_two

    if len(a) == 0 and len(b) == 0:
        return EQUAL

    if len(a) == 0 or len(b) == 0:
        return UNEQUAL

    if sub(a, b):
        if len(a) == len(b):
            return EQUAL
        return SUBLIST
    elif sub(b, a):
        return SUPERLIST
    else:
        return UNEQUAL


def sub(list_a, list_b):
    matches = False
    i = 0
    for item_b in list_b:
        if item_b == list_a[i]:
            matches = True
            if i >= len(list_a) - 1:
                break
            i += 1
        else:
            matches = False
            i = 0

    return matches
