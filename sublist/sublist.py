from typing import List

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 3
EQUAL = 1
UNEQUAL = 4


def sublist(list_a: List[int], list_b: List[int]) -> int:
    """
    Given two lists: list_a, list_b determine if
    - the first list is contained within the second list, (or if) => list_one is SUBLIST
    - the second list is contained within the first list, (or if) => list_one is SUPERLIST
    - both lists are contained within each other or if            => EQUAL
    - none of these are true.                                     => UNEQUAL

    to be a sublist or a superlist, consider contiguous 'sequences'
    """

    if len(list_a) == 0 and len(list_b) == 0:
        return EQUAL
    elif len(list_a) == 0:
        return SUBLIST       # [] is a sublist of any non empty list_b
    elif len(list_b) == 0:
        return SUPERLIST     # list_a non empty is superlist of []

    # from here we have 2 non empty list
    if len(list_a) <= len(list_b):
       return classify_sublist(list_a, list_b)

    else:
        # len(list_a) > len(list_b)
        return classify_sublist(list_b, list_a, from_a=False)


def classify_sublist(list_a: List[int], list_b: List[int], from_a:bool=True) -> int:
    """
    classify list_a as
    - a sublist (or superlist), or
    - an equal or
    - an unequal list

    of list_b

    from_a == True means if list_a is contained in list_b, then SUBLIST result will be returned
    otherwise (if list_a contains list_b) and from_A == False => SUPERLIST
    """
    list_class = SUBLIST if from_a else SUPERLIST

    ixes = index_of(list_a[0], list_b)  # lookup for alignment from 1st element of list_a

    if len(ixes) == 0:
        return UNEQUAL

    # len(ixes) > 1
    for ix in ixes:
        jx = 1
        while jx < len(list_a) and ix + jx < len(list_b) and list_a[jx] == list_b[ix + jx]:
            jx += 1

        if jx >= len(list_a):
            # no mismatch found
            return EQUAL if len(list_a) == len(list_b) else list_class
        else:
            # mismatch
            continue

    # exhaust all possibilities
    return UNEQUAL

def index_of(elem: int, lst: List[int]) -> List[int]:
    """
    return all indexes of elem within lst (if elem in lst)
    [] otherwise
    """
    return [
        ix for ix, e in enumerate(lst) if e == elem
    ]
