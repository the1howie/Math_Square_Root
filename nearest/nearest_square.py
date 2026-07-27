#!/usr/bin/env python3

"""
Here we use python's algorithm for extracting the square root.
"""

from math import sqrt, pow, floor, ceil


def nearest_square(num, ubound=False):
    """
    Default ubound is set to False to return the floor of the calculation.
    If ubound is set to True then the ceiling is returned.
    """
    if not ubound:
        return int(pow(floor(sqrt(num)), 2))
    else:
        return int(pow(ceil(sqrt(num)), 2))


if __name__ == "__main__":
    print(f"Lower bound for 10 is {nearest_square(10)}")
    print(f"Upper bound for 10 is {nearest_square(10, True)}")
