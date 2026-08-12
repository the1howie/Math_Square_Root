#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__)))
sys.path.append(str(Path(__file__).parents[1]))
sys.path.append(str(Path(__file__).parents[2]))


import pytest
from c1bisection.bisect_sqrt import bisect_sqrt
from utils import capture_output


@capture_output
def run_sqrt_with_print(S):
    return bisect_sqrt(S, print_guesses=True)


@pytest.mark.parametrize(
    "value, expected, printout",
    [
        (
            1,
            0.9999999999990905,
            "Number of guesses: 39, Threshold: 1e-12, Estimate iterations: 39.\n",
        ),
        (
            2,
            1.4142135623733338,
            "Number of guesses: 38, Threshold: 1e-12, Estimate iterations: 39.\n",
        ),
        (
            3,
            1.732050807568612,
            "Number of guesses: 40, Threshold: 1e-12, Estimate iterations: 38.\n",
        ),
        (4, 2.0, "Number of guesses: 0, Threshold: 1e-12, Estimate iterations: 0.\n"),
        (
            5,
            2.2360679774999426,
            "Number of guesses: 41, Threshold: 1e-12, Estimate iterations: 38.\n",
        ),
        (
            7,
            2.6457513110646005,
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 40.\n",
        ),
        (
            8,
            2.828427124745758,
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 41.\n",
        ),
        (
            9,
            2.9999999999998295,
            "Number of guesses: 43, Threshold: 1e-12, Estimate iterations: 41.\n",
        ),
        (
            10,
            3.162277660168229,
            "Number of guesses: 42, Threshold: 1e-12, Estimate iterations: 41.\n",
        ),
        (
            25,
            5.000000000000426,
            "Number of guesses: 44, Threshold: 1e-12, Estimate iterations: 43.\n",
        ),
        (
            37,
            6.082762530297842,
            "Number of guesses: 45, Threshold: 1e-12, Estimate iterations: 44.\n",
        ),
        (
            49,
            7.000000000000497,
            "Number of guesses: 45, Threshold: 1e-12, Estimate iterations: 44.\n",
        ),
        (
            73,
            8.544003745317191,
            "Number of guesses: 46, Threshold: 1e-12, Estimate iterations: 45.\n",
        ),
        (
            81,
            8.99999999999968,
            "Number of guesses: 46, Threshold: 1e-12, Estimate iterations: 45.\n",
        ),
        (
            100,
            10.000000000000142,
            "Number of guesses: 46, Threshold: 1e-12, Estimate iterations: 46.\n",
        ),
        (
            121,
            10.999999999999453,
            "Number of guesses: 46, Threshold: 1e-12, Estimate iterations: 46.\n",
        ),
        (
            1000,
            31.62277660168389,
            "Number of guesses: 49, Threshold: 1e-12, Estimate iterations: 49.\n",
        ),
        (
            10_000,
            99.99999999999953,
            "Number of guesses: 53, Threshold: 1e-12, Estimate iterations: 53.\n",
        ),
        (
            100_000,
            316.22776601683756,
            "Number of guesses: 56, Threshold: 1e-12, Estimate iterations: 56.\n",
        ),
        (
            987_654,
            993.8078285060951,
            "Number of guesses: 59, Threshold: 1e-12, Estimate iterations: 59.\n",
        ),
        (
            987_543_201,
            31425.200094828353,
            "Number of guesses: 69, Threshold: 1e-12, Estimate iterations: 69.\n",
        ),
        (
            673_003_460_632_639_326_586_069_439_443,
            820367881278051.5,
            "Number of guesses: 103, Threshold: 1e-12, Estimate iterations: 138.\n",
        ),
        (
            1_000_000_000_000_000_000_000_000_000_000,
            1000000000000000.0,
            "Number of guesses: 101, Threshold: 1e-12, Estimate iterations: 139.\n",
        ),
        (
            1_367_999_732_000_000_000_000_000_000_071,
            1169615206809487.5,
            "Number of guesses: 103, Threshold: 1e-12, Estimate iterations: 139.\n",
        ),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
