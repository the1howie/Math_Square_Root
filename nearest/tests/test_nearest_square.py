#!/usr/bin/env python3

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pytest
from nearest_square import nearest_square


@pytest.mark.parametrize(
    "number, ubound_flag, expected",
    [
        (5, False, 4),
        (5, True, 9),
        (10, False, 9),
        (10, True, 16),
        (25, False, 25),
        (25, True, 25),
    ],
)
def test_nearest_square(number, ubound_flag, expected):
    assert nearest_square(number, ubound_flag) == expected
