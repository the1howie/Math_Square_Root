#!/usr/bin/env python3

"""
The bisection method is linearly convergent..

We start with an interval x ∈ (a, b) for x = √S.

We halve the interval with each iteration, for example x₀ = (a + b)/2, until |xₙ - S| < τ.

This is the slowest converging method however, it is a good start for students.
"""

import math
from utils import write_data_to_file

# from utils import trace_locals


# Use this decorator when you want all the local variables printed.
# @trace_locals
def bisect_sqrt(
    S, precision_dps=15, print_guesses=False, verbose=False, file_path=None
):
    """Square Root using Bisection Search Method."""

    # validation
    if S < 0:
        raise ValueError("Invalid input! Expected a positive number.")

    # trivial case
    if S == 0:
        return 0

    # set threshold
    tau = 10 ** (-1 * precision_dps)

    # initial interval
    low = 0
    high = max(1, S)

    # initial guess
    x = [(low + high) / 2]
    guesses = 0

    # estimate the number of iterations
    est_iter = num_iter(tau, S, x[0])

    # print out each step if verbose
    if verbose:
        progress = "iteration: {0}\tlow: {1}\thigh: {2}\tguess: {3}\tguess²: {4}"

    # do the first iteration
    if abs(x[-1] ** 2 - S) >= tau:
        if verbose:
            print(progress.format(guesses, low, high, x[-1], x[-1] ** 2))
        guesses += 1
        if x[-1] ** 2 < S:
            # guess is too low
            low = x[-1]
        else:
            # guess is too high
            high = x[-1]
        x.append((low + high) / 2)

    # loop until the stopping criterion is met after the first iteration onwards
    while abs(x[-1] ** 2 - S) >= tau and abs(x[-1] - x[-2]) >= tau:
        if verbose:
            print(progress.format(guesses, low, high, x[-1], x[-1] ** 2))
        guesses += 1
        if x[-1] ** 2 < S:
            # guess is too low
            low = x[-1]
        else:
            # guess is too high
            high = x[-1]
        x.append((low + high) / 2)

    if print_guesses:
        print(
            f"Number of guesses: {guesses}, Threshold: {tau}, Estimate iterations: {est_iter}."
        )

    # write guesses to file
    if file_path is not None:
        write_data_to_file(x, file_path)

    # return the final guess
    return x[-1]


def num_iter(tau, S, x0):
    """Estimate the number of iterations."""
    d = abs(math.log10(tau))
    mu = 1 / 2
    e0 = abs(x0 - math.sqrt(S))
    try:
        if e0 != 0:
            return math.ceil(abs(-1 * (d + math.log10(e0)) / math.log10(mu)))
        else:
            return 0
    except Exception as e:
        raise Exception(e)


def main():
    S = input("Enter positive number: ")
    try:
        S = float(S)
    except Exception as e:
        raise Exception(e)
    if S < 0:
        raise ValueError("Invalid input. Input must be a positive number.")

    prec = input("Enter precision between 0 and 15 (Default 15 d.p.): ")
    try:
        prec = int(prec)
    except Exception:
        prec = 15
    if prec < 0:
        raise ValueError("Invalid input. Input must be a positive number.")
    if prec > 15:
        raise ValueError("Invalid input. Input must be between 0 and 15.")

    x = bisect_sqrt(S, precision_dps=prec, print_guesses=True, verbose=True)
    print("\nApproximation for the square root of {0} is: {1}".format(S, x))
    print("\nCompared to math.sqrt({0}): {1}".format(S, math.sqrt(S)))


if __name__ == "__main__":
    main()
