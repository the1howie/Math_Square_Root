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
        (2, 1.4142135623733338, "Number of guesses: 38, Threshold: 1e-12.\n"),
        (10, 3.162277660168229, "Number of guesses: 42, Threshold: 1e-12.\n"),
        (25, 5.000000000000071, "Number of guesses: 45, Threshold: 1e-12.\n"),
    ],
)
def test_sqrt(value, expected, printout):
    results = run_sqrt_with_print(value)
    assert results["value"] == expected
    assert results["printout"] == printout
