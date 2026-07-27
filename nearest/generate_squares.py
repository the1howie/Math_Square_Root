#!/usr/bin/env python3

import json

from utils import get_json_len
from math import pow

DATA_FILENAME = "squares.json"
# UPPER_LIMIT = 1_000_001 is too large for GitHub! (50 MB limit)
UPPER_LIMIT = 1001


def generate_squares(start=0, upper_limit=UPPER_LIMIT):
    if start >= upper_limit:
        raise ValueError("Invalid inputs.")

    squares = []
    for num in range(start, upper_limit):
        squares.append({"number": num, "square": int(pow(num, 2))})
    return sorted(squares, key=lambda x: (x["number"]))


def write_squares_to_json(squares_list, mode="w"):
    with open(DATA_FILENAME, mode=mode) as file:
        json.dump(squares_list, file, indent=4)


def overwrite_squares_json():
    squares = generate_squares()
    write_squares_to_json(squares)


if __name__ == "__main__":
    overwrite_squares_json()
