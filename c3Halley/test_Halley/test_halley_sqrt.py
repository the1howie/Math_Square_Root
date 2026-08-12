#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__)))
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[2]))


import pytest
from c3Halley.halley_sqrt import halley_sqrt
from utils import capture_output


@capture_output
def run_sqrt_with_print(S):
    return halley_sqrt(S, print_guesses=True)


@pytest.mark.parametrize(
    "value, expected, printout",
    [
        (
            1,
            0.9999999999997379,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            2,
            1.414213562373095,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            3,
            1.7320508075688772,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (4, 2.0, "Number of guesses: 0, Threshold: 1e-12, Estimate iterations: 0.\n"),
        (
            5,
            2.2360679774997902,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            7,
            2.6457513110645903,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            8,
            2.82842712474619,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            9,
            3.0,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            10,
            3.162277660168379,
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            25,
            5.0,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            37,
            6.082762530298221,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 7.\n",
        ),
        (
            49,
            7.0,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            73,
            8.54400374531753,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            81,
            9.000000000000002,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            100,
            10.0,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            121,
            11.0,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            1000,
            31.622776601683793,
            "Number of guesses: 6, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            10_000,
            99.99999999999997,
            "Number of guesses: 8, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            100_000,
            316.2277660168379,
            "Number of guesses: 9, Threshold: 1e-12, Estimate iterations: 2.\n",
        ),
        (
            987_654,
            993.807828506095,
            "Number of guesses: 10, Threshold: 1e-12, Estimate iterations: 2.\n",
        ),
        (
            987_543_201,
            31425.200094828353,
            "Number of guesses: 15, Threshold: 1e-12, Estimate iterations: 2.\n",
        ),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
