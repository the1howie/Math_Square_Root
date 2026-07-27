import json
import ijson
from utils import get_json_len  # , timer  #, profile

# from memory_profiler import profile

DATA_FILENAME = "squares.json"


# @profile
# @timer
def nearest_square_from_list(num):
    """This searches list of squares loaded in memory"""
    # load the whole file to memory
    squares = []
    with open(DATA_FILENAME, mode="r") as file:
        jdata = json.loads(file.read())
        for item in jdata:
            squares.append(item)

    # get length of list of dictionaries
    list_len = len(squares)

    # get first item
    count = 0
    next_item = squares[count]

    # search for the lower and upper bounds
    while count < list_len:
        prev_item = next_item
        if num == prev_item["square"]:
            return (prev_item, prev_item)

        count += 1
        if count < list_len:
            next_item = squares[count]
            if num > prev_item["square"] and num < next_item["square"]:
                return (prev_item, next_item)

    # if all else fails
    return (None, None)


# @profile
# @timer
def nearest_square_from_list_iter(num):
    """This searches list of squares read iteratively from RAM"""

    # ijson returns a generator which we iterate through using next(item)
    with open(DATA_FILENAME, mode="r") as file:
        # get how many dictionaries there are in the json
        file_len = get_json_len(DATA_FILENAME)

        # this creates a generator
        square_items = ijson.items(file, "item", use_float=False)

        # get first item
        count = 0
        next_item = next(square_items)

        # search for the lower and upper bounds
        while count < file_len:
            prev_item = next_item
            if num == prev_item["square"]:
                return (prev_item, prev_item)

            count += 1
            if count < file_len:
                next_item = next(square_items)
                if num > prev_item["square"] and num < next_item["square"]:
                    return (prev_item, next_item)

    # if all else fails
    return (None, None)


if __name__ == "__main__":
    num = 100
    print(f"Find nearest square(s) to {num}:\n")

    lbound, ubound = nearest_square_from_list(num)
    print(f"{lbound}, {ubound}\n")

    lbound, ubound = nearest_square_from_list_iter(num)
    print(f"{lbound}, {ubound}\n")
