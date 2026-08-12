#!/usr/bin/env python3

"""
The Bisection Brute-Force Search Method to calculate the square root.

Using the multi-precision math library https://mpmath.org/
"""

import mpmath as mpm


def bisect_sqrt_mp(S, precision_dps=15, print_guesses=False, verbose=False):
    """Square Root using Bisection Search Method."""

    # validation
    if S < 0:
        raise ValueError("Invalid input! Expected a positive number.")

    # set precision
    mpm.mp.dps = min(15, precision_dps)

    # for printing
    significant_digits = precision_dps + len(str(S))

    # convert input S to mpf
    S = mpm.mpmathify(S)

    # set threshold
    tau = mpm.power(10, mpm.fmul(-1, precision_dps))

    # initial interval
    low = mpm.mpmathify(0)
    high = max(mpm.mpmathify(1), S)

    # initial guess
    x = [mpm.fdiv(mpm.fadd(low, high), 2)]
    guesses = 0

    # estimate the number of iterations
    est_iter = num_iter(tau, S, x[0])

    # print out each step if verbose
    if verbose:
        progress = "iteration: {0}\tlow: {1}\thigh: {2}\tguess: {3}\tguess²: {4}"

    # do the first iteration
    if abs(mpm.fsub(mpm.power(x[-1], 2), S)) >= tau:
        if verbose:
            print(
                progress.format(
                    guesses,
                    mpm.nstr(low, significant_digits),
                    mpm.nstr(high, significant_digits),
                    mpm.nstr(x[-1], significant_digits),
                    mpm.nstr(mpm.power(x[-1], 2), significant_digits),
                )
            )
        guesses += 1
        if mpm.power(x[-1], 2) < S:
            # guess is too low
            low = x[-1]
        else:
            # guess is too high
            high = x[-1]
        x.append(mpm.fdiv(mpm.fadd(low, high), 2))

    # # loop until the stopping criterion is met
    while (
        abs(mpm.fsub(mpm.power(x[-1], 2), S)) >= tau
        and abs(mpm.fsub(x[-1], x[-2])) >= tau
    ):
        if verbose:
            print(
                progress.format(
                    guesses,
                    mpm.nstr(low, significant_digits),
                    mpm.nstr(high, significant_digits),
                    mpm.nstr(x[-1], significant_digits),
                    mpm.nstr(mpm.power(x[-1], 2), significant_digits),
                )
            )
        guesses += 1
        if mpm.power(x[-1], 2) < S:
            # guess is too low
            low = x[-1]
        else:
            # guess is too high
            high = x[-1]
        x.append(mpm.fdiv(mpm.fadd(low, high), 2))

    if print_guesses:
        print(
            f"Number of guesses: {guesses}, Threshold: {tau}, Estimate iterations: {est_iter}."
        )

    return x[-1]


def num_iter(tau, S, x0):
    """Estimate the number of iterations."""
    d = abs(mpm.log10(tau))
    mu = mpm.fdiv(1, 2)
    e0 = abs(mpm.fsub(x0, mpm.sqrt(S)))
    try:
        if e0 != mpm.mpmathify(0):
            return int(
                mpm.ceil(
                    abs(
                        mpm.fdiv(
                            mpm.fmul(-1, mpm.fadd(d, mpm.log10(e0))), mpm.log10(mu)
                        )
                    )
                )
            )
        else:
            return 0
    except Exception as e:
        raise Exception(e)


if __name__ == "__main__":
    S = float(input("Enter positive number: "))
    prec = int(input("Enter dps (precision): "))
    if prec < 0:
        raise ValueError("Invalid input. It must be a positive integer.")

    if S < 0:
        raise ValueError("Invalid input. It must be a positive number.")

    # significant figures for printing
    sf = prec + len(str(S))

    x = bisect_sqrt_mp(S, prec, True, True)
    print(
        "\nApproximation for the square root of {0} is: {1}".format(S, mpm.nstr(x, sf))
    )

    mpm.mp.dps = min(15, prec)
    S = mpm.mpmathify(S)
    print("\nCompared to mpmath.sqrt({0}): {1}".format(S, mpm.nstr(mpm.sqrt(S), sf)))
