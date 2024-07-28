"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
SUBLIST = 5
SUPERLIST = 6
EQUAL = 1
UNEQUAL = 0


def sublist(list_one, list_two):
    a = list_one
    b = list_two

    if equal(a, b):
        return EQUAL
    elif is_sublist(a, b):
        return SUBLIST
    elif is_superlist(a, b):
        return SUPERLIST
    else:
        return UNEQUAL


def equal(a, b):
    return a == b


def is_sublist(a, b):
    if len(a) > len(b):
        return False
    for i in range(len(b) - len(a) + 1):
        if b[i:i+len(a)] == a:
            return True
    return False


def is_superlist(a, b):
    return is_sublist(b, a)
