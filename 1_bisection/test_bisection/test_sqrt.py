#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__)))
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[2]))


import pytest
from sqrt import sqrt
from utils import capture_output


@capture_output
def run_sqrt_with_print(S):
    results = sqrt(S, print_guesses=True)
    return results


@pytest.mark.parametrize(
    "value, expected, printout",
    [
        (1, 0.9999999999995453, "Number of guesses: 40, Threshold: 1e-12.\n"),
        (2, 1.4142135623733338, "Number of guesses: 38, Threshold: 1e-12.\n"),
        (3, 1.732050807568612, "Number of guesses: 40, Threshold: 1e-12.\n"),
        (4, 2.0, "Number of guesses: 0, Threshold: 1e-12.\n"),
        (9, 3.0000000000000853, "Number of guesses: 44, Threshold: 1e-12.\n"),
        (10, 3.162277660168229, "Number of guesses: 42, Threshold: 1e-12.\n"),
        (25, 5.000000000000071, "Number of guesses: 45, Threshold: 1e-12.\n"),
        (37, 6.082762530298236, "Number of guesses: 47, Threshold: 1e-12.\n"),
        (49, 6.999999999999975, "Number of guesses: 47, Threshold: 1e-12.\n"),
        (73, 8.54400374531758, "Number of guesses: 48, Threshold: 1e-12.\n"),
        (81, 8.999999999999968, "Number of guesses: 47, Threshold: 1e-12.\n"),
        (100, 9.999999999999964, "Number of guesses: 48, Threshold: 1e-12.\n"),
        (121, 10.99999999999999, "Number of guesses: 49, Threshold: 1e-12.\n"),
        (1000, 31.62277660168378, "Number of guesses: 52, Threshold: 1e-12.\n"),
        (10000, 100.0, "Number of guesses: 58, Threshold: 1e-12.\n"),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
