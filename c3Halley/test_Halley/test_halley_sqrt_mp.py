#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__)))
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[2]))


import pytest
from mpmath import mp, mpf
from c3Halley.halley_sqrt_mp import halley_sqrt_mp
from utils import capture_output

# Use the same threshold as in the vanilla version.
PRECISION = 12
mp.dps = PRECISION


@capture_output
def run_sqrt_with_print(S):
    return halley_sqrt_mp(S, PRECISION, print_guesses=True)


@pytest.mark.parametrize(
    "value,  expected, printout",
    [
        (
            1,
            mpf("0.999999999999659"),
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            2,
            mpf("1.41421356237288"),
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            3,
            mpf("1.73205080756884"),
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            4,
            mpf("2.0"),
            "Number of guesses: 0, Threshold: 1e-12, Estimate iterations: 0.\n",
        ),
        (
            5,
            mpf("2.23606797749972"),
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            7,
            mpf("2.64575131106449"),
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            8,
            mpf("2.82842712474621"),
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            9,
            mpf("3.0"),
            "Number of guesses: 3, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            10,
            mpf("3.162277660168002"),
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            25,
            mpf("5.0"),
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            37,
            mpf("6.082762530298169"),
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 7.\n",
        ),
        (
            49,
            mpf("7.0"),
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 5.\n",
        ),
        (
            73,
            mpf("8.544003745317241"),
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            81,
            mpf("9.0"),
            "Number of guesses: 4, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            100,
            mpf("10.0"),
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            121,
            mpf("11.0"),
            "Number of guesses: 5, Threshold: 1e-12, Estimate iterations: 4.\n",
        ),
        (
            1000,
            mpf("31.622776601685473"),
            "Number of guesses: 8, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            10_000,
            mpf("100.0"),
            "Number of guesses: 9, Threshold: 1e-12, Estimate iterations: 3.\n",
        ),
        (
            100_000,
            mpf("316.22776601684745401"),
            "Number of guesses: 8, Threshold: 1e-12, Estimate iterations: 2.\n",
        ),
        (
            987_654,
            mpf("993.80782850622199476"),
            "Number of guesses: 11, Threshold: 1e-12, Estimate iterations: 2.\n",
        ),
        (
            987_543_201,
            mpf("31425.200094826519489288"),
            "Number of guesses: 15, Threshold: 1e-12, Estimate iterations: 2.\n",
        ),
        (
            673_003_460_632_639_326_586_069_439_443,
            mpf("820367881277952.0"),
            "Number of guesses: 38, Threshold: 1e-12, Estimate iterations: 1.\n",
        ),
        (
            1_000_000_000_000_000_000_000_000_000_000,
            mpf("999999999999872.0"),
            "Number of guesses: 35, Threshold: 1e-12, Estimate iterations: 1.\n",
        ),
        (
            1_367_999_732_000_000_000_000_000_000_071,
            mpf("1169615206809344.0"),
            "Number of guesses: 36, Threshold: 1e-12, Estimate iterations: 1.\n",
        ),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
