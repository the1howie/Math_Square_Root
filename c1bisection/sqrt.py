#!/usr/bin/env python3

"""
The bisection method is linearly convergent..

We start with an interval x ∈ (a, b) for x = √S.

We halve the interval with each iteration, for example x₀ = (a + b)/2, until |xₙ - S| < τ.

This is the slowest converging method however, it is a good start for students.
"""

# from utils import trace_locals


# Use this decorator when you want all the local variables printed.
# @trace_locals
def sqrt(S, tau=10 ** (-12), print_guesses=False, verbose=False):
    """Square Root using Bisection Search Method."""

    # validation
    if S < 0:
        raise ValueError("Invalid input! Expected a positive number.")

    # initial interval
    low = 0
    high = max(1, S)

    # initial guess
    x = (low + high) / 2
    guesses = 0

    # print out each step if verbose
    if verbose:
        progress = "low: {0}\thigh: {1}\tguess: {2}\tguess²: {3}"

    # loop until the stopping criterion is met
    while abs(x**2 - S) >= tau:
        if verbose:
            print(progress.format(low, high, x, x**2))

        guesses += 1
        if x**2 < S:
            # guess is too low
            low = x
        else:
            # guess is too high
            high = x
        x = (low + high) / 2

    if print_guesses:
        print(f"Number of guesses: {guesses}, Threshold: {tau}.")

    return x


if __name__ == "__main__":
    S = float(input("Enter positive number: "))

    if S < 0:
        raise ValueError("Invalid input. Input must be a positive number.")

    x = sqrt(S, print_guesses=True, verbose=True)
    print("\nApproximation for the square root of {0} is: {1}".format(S, x))
    import math

    print("\nCompared to math.sqrt({0}): {1}".format(S, math.sqrt(S)))
