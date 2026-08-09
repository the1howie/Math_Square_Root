#!/usr/bin/env python3

"""
Visit https://mpmath.org/
"""

import mpmath as mpm


def sqrt_mp(S, precision_dps=50, print_guesses=False, verbose=False):
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

    # initial guess
    x = mpm.fdiv(max(mpm.mpmathify(1), S), 2)
    guesses = 0

    # print out each step if verbose
    if verbose:
        progress = "iteration: {0}\tguess: {1}\tguess²: {2}"

    # loop until the stopping criterion is met
    while abs(mpm.fsub(mpm.power(x, 2), S)) >= tau:
        if verbose:
            print(
                progress.format(
                    str(guesses),
                    mpm.nstr(x, precision_dps),
                    mpm.nstr(mpm.power(x, 2), precision_dps),
                )
            )

        guesses += 1
        x = mpm.fdiv(mpm.fadd(x, mpm.fdiv(S, x)), 2)

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

    x = sqrt_mp(S, prec, True, True)
    print(
        "\nApproximation for the square root of {0} is: {1}".format(
            S, mpm.nstr(x, prec)
        )
    )

    mpm.mp.dps = prec + len(str(S)) + 1
    S = mpm.mpmathify(S)
    print("\nCompared to mpmath.sqrt({0}): {1}".format(S, mpm.nstr(mpm.sqrt(S), prec)))
