#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__)))
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[2]))


import pytest
from mpmath import mp, mpf
from c1bisection.bisect_sqrt_mp import bisect_sqrt_mp
from utils import capture_output

# Use the same threshold as in the vanilla version.
PRECISION = 12
mp.dps = PRECISION


@capture_output
def run_sqrt_with_print(S):
    return bisect_sqrt_mp(S, PRECISION, print_guesses=True)


@pytest.mark.parametrize(
    "value,  expected, printout",
    [
        (
            1,
            mpf("0.999999999999091"),
            "Number of guesses: 39, Threshold: 1e-12, Estimate iterations: 39.\n",
        ),
        (
            2,
            mpf("1.41421356237333"),
            "Number of guesses: 38, Threshold: 1e-12, Estimate iterations: 39.\n",
        ),
        (
            3,
            mpf("1.73205080756861"),
            "Number of guesses: 40, Threshold: 1e-12, Estimate iterations: 38.\n",
        ),
        (
            4,
            mpf("2.0"),
            "Number of guesses: 0, Threshold: 1e-12, Estimate iterations: 0.\n",
        ),
        (
            5,
            mpf("2.23606797749926"),
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 38.\n",
        ),
        (
            7,
            mpf("2.64575131106449"),
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 40.\n",
        ),
        (
            8,
            mpf("2.82842712474576"),
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 41.\n",
        ),
        (
            9,
            mpf("3.0"),
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 41.\n",
        ),
        (
            10,
            mpf("3.162277660168911"),
            "Number of guesses: 43, Threshold: 1e-12, Estimate iterations: 41.\n",
        ),
        (
            25,
            mpf("5.0"),
            "Number of guesses: 43, Threshold: 1e-12, Estimate iterations: 43.\n",
        ),
        (
            37,
            mpf("6.082762530298169"),
            "Number of guesses: 44, Threshold: 1e-12, Estimate iterations: 44.\n",
        ),
        (
            49,
            mpf("7.0"),
            "Number of guesses: 44, Threshold: 1e-12, Estimate iterations: 44.\n",
        ),
        (
            73,
            mpf("8.544003745317241"),
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 45.\n",
        ),
        (
            81,
            mpf("9.0"),
            "Number of guesses: 44, Threshold: 1e-12, Estimate iterations: 45.\n",
        ),
        (
            100,
            mpf("10.0"),
            "Number of guesses: 44, Threshold: 1e-12, Estimate iterations: 46.\n",
        ),
        (
            121,
            mpf("11.0"),
            "Number of guesses: 44, Threshold: 1e-12, Estimate iterations: 46.\n",
        ),
        (
            1000,
            mpf("31.622776601681835"),
            "Number of guesses: 49, Threshold: 1e-12, Estimate iterations: 49.\n",
        ),
        (
            10_000,
            mpf("100.0"),
            "Number of guesses: 48, Threshold: 1e-12, Estimate iterations: 53.\n",
        ),
        (
            100_000,
            mpf("316.22776601684745401"),
            "Number of guesses: 49, Threshold: 1e-12, Estimate iterations: 56.\n",
        ),
        (
            987_654,
            mpf("993.80782850610557944"),
            "Number of guesses: 52, Threshold: 1e-12, Estimate iterations: 59.\n",
        ),
        (
            987_543_201,
            mpf("31425.200094826519489288"),
            "Number of guesses: 59, Threshold: 1e-12, Estimate iterations: 69.\n",
        ),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
