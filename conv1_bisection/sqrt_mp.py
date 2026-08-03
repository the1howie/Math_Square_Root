#!/usr/bin/env python3

"""
Visit https://mpmath.org/
"""

import mpmath as mpm


def sqrt_mp(S, precision_dps=50, print_guesses=False):
    """Square Root using Bisection Search Method."""

    # validation
    if S < 0:
        raise ValueError("Invalid input! Expected a positive number.")

    # set precision
    mpm.mp.dps = precision_dps + len(str(S)) + 1

    # convert input S to mpf
    S = mpm.mpmathify(S)

    # set threshold
    tau = mpm.power(10, mpm.fmul(-1, precision_dps))

    # initial interval
    low = mpm.mpmathify(0)
    high = max(mpm.mpmathify(1), S)

    # # initial guess
    x = mpm.fdiv(mpm.fadd(low, high), 2)
    guesses = 0

    # # loop until the stopping criterion is met
    while abs(x**2 - S) >= tau:
        guesses += 1
        if mpm.power(x, 2) < S:
            # guess is too low
            low = x
        else:
            # guess is too high
            high = x
        x = mpm.fdiv(mpm.fadd(low, high), 2)

    if print_guesses:
        print(
            f"Number of guesses: {mpm.nstr(guesses, precision_dps)}, Threshold: {mpm.nstr(tau, precision_dps)}."
        )

    return x


if __name__ == "__main__":
    S = float(input("Enter positive number: "))
    prec = int(input("Enter dps (precision): "))
    if prec < 0:
        raise ValueError("Invalid input. It must be a positive integer.")

    if S < 0:
        raise ValueError("Invalid input. It must be a positive number.")

    x = sqrt_mp(S, prec, True)
    print(
        "\napproximation for the square root of {0} is: {1}".format(
            S, mpm.nstr(x, prec)
        )
    )

    mpm.mp.dps = prec + len(str(S)) + 1
    S = mpm.mpmathify(S)
    print("\ncompared to mpmath.sqrt({0}): {1}".format(S, mpm.nstr(mpm.sqrt(S), prec)))
