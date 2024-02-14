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

    print(a)
    print(b)
    if a == b:
        return EQUAL

    if contains_list(a, b):
        return SUBLIST

    if contains_list(b, a):
        return SUPERLIST

    return UNEQUAL


def contains_list(list_a, list_b):
    i = 0
    matching = False
    for item in list_a:
        if len(list_b) == 0:
            matching = True
            break
        if item == list_b[i]:
            matching = True
            if i < len(list_b) - 1:
                i += 1
        else:
            matching = False
            i = 0

    if matching and i == len(list_b):
        return True

    return False


