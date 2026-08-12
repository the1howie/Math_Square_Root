#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__)))
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[2]))


import pytest
from c2Babylon.babylon_sqrt import babylon_sqrt
from utils import capture_output


@capture_output
def run_sqrt_with_print(S):
    return babylon_sqrt(S, print_guesses=True)


@pytest.mark.parametrize(
    "value, expected, printout",
    [
        (
            1,
            1.000000000000001,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            2,
            1.414213562373095,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            3,
            1.7320508075688772,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (4, 2.0, "Number of guesses: 0, Threshold: 1e-12, Estimate iterations: 0.\n"),
        (
            5,
            2.23606797749979,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            7,
            2.6457513110646933,
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            8,
            2.82842712474619,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            9,
            3.0,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            10,
            3.162277660168379,
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            25,
            5.0,
            "Number of guesses: 6, Threshold: 1e-12, Estimate iterations: 7.\n",
        ),
        (
            37,
            6.08276253029822,
            "Number of guesses: 6, Threshold: 1e-12, Estimate iterations: 11.\n",
        ),
        (
            49,
            7.0,
            "Number of guesses: 6, Threshold: 1e-12, Estimate iterations: 8.\n",
        ),
        (
            73,
            8.544003745317532,
            "Number of guesses: 7, Threshold: 1e-12, Estimate iterations: 6.\n",
        ),
        (
            81,
            9.0,
            "Number of guesses: 7, Threshold: 1e-12, Estimate iterations: 6.\n",
        ),
        (
            100,
            10.0,
            "Number of guesses: 7, Threshold: 1e-12, Estimate iterations: 6.\n",
        ),
        (
            121,
            11.0,
            "Number of guesses: 7, Threshold: 1e-12, Estimate iterations: 6.\n",
        ),
        (
            1000,
            31.622776601683793,
            "Number of guesses: 9, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            10_000,
            100.0,
            "Number of guesses: 10, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            100_000,
            316.2277660168379,
            "Number of guesses: 13, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            987_654,
            993.8078285060951,
            "Number of guesses: 15, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            987_543_201,
            31425.200094828353,
            "Number of guesses: 20, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            673_003_460_632_639_326_586_069_439_443,
            820367881278051.5,
            "Number of guesses: 54, Threshold: 1e-12, Estimate iterations: 1.\n",
        ),
        (
            1_000_000_000_000_000_000_000_000_000_000,
            1000000000000000.0,
            "Number of guesses: 54, Threshold: 1e-12, Estimate iterations: 1.\n",
        ),
        (
            1_367_999_732_000_000_000_000_000_000_071,
            1169615206809487.5,
            "Number of guesses: 55, Threshold: 1e-12, Estimate iterations: 1.\n",
        ),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
