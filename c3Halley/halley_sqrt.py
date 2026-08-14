#!/usr/bin/env python3

"""
Halley's method for extracting the square root has cubic convergence.

Edmond Halley's (yes, the same guy that has a commet name after him)
method is an improvement on Newton's method using the second derivative.

x[n+1] = x[n] - (2*f(x[n])*f'(x[n])) / (2*f'(x[n])^2 - f(x[n])*f''(x[n]))

Substitute: f(x) = x^2 - S, f'(x) = 2*x, f''(x) = 2

To obtain: x[n+1] = x[n] * (x[n]^2 + 3*S) / (3*x[n]^2 + S)

Since it converges cubically, it is faster than the Babylonian method.
"""

import math
from utils import write_data_to_file

# from utils import trace_locals


# Use this decorator when you want all the local variables printed.
# @trace_locals
def halley_sqrt(S, precision_dps=15, print_guesses=False, verbose=False, file_path=None):
    """Square Root using Halley's Method."""

    # validation
    if S < 0:
        raise ValueError("Invalid input! Expected a positive number.")

    # trivial
    if S == 0:
        return 0

    # initial guess
    x = [max(1, S) / 2]
    guesses = 0

    # set threshold
    tau = 10 ** (-1 * precision_dps)

    # estimate the number of iterations
    est_iter = num_iter(tau, S, x[0])

    # print out each step if verbose
    if verbose:
        progress = "iteration: {0}\tguess: {1}\tguess²: {2}"

    # do the first iteration
    if abs(x[-1] ** 2 - S) >= tau:
        if verbose:
            print(progress.format(guesses, x[-1], x[-1] ** 2))
        guesses += 1
        # Halley's approximation
        x.append(x[-1] * (x[-1] ** 2 + 3 * S) / (3 * x[-1] ** 2 + S))

    # do the second iteration
    if abs(x[-1] ** 2 - S) >= tau and abs(x[-1] - x[-2]) >= tau:
        if verbose:
            print(progress.format(guesses, x[-1], x[-1] ** 2))
        guesses += 1
        # Halley's approximation
        x.append(x[-1] * (x[-1] ** 2 + 3 * S) / (3 * x[-1] ** 2 + S))

    # loop until the stopping criterion is met after the 2nd iteration onwards
    while (
        abs(x[-1] ** 2 - S) >= tau
        and abs(x[-1] - x[-2]) >= tau
        and abs(x[-1] - x[-3]) >= tau
    ):
        if verbose:
            print(progress.format(guesses, x[-1], x[-1] ** 2))
        guesses += 1
        # Halley's approximation
        x.append(x[-1] * (x[-1] ** 2 + 3 * S) / (3 * x[-1] ** 2 + S))

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
    rho = 1 / (2 * math.sqrt(S))
    e0 = abs(math.sqrt(S) - x0)
    try:
        if e0 != 0:
            return math.ceil(
                math.log(
                    abs(math.log10(rho * math.pow(10, -d)) / math.log10(rho * e0)), 3
                )
            )
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

    x = halley_sqrt(S, precision_dps=prec, print_guesses=True, verbose=True)
    print("\nApproximation for the square root of {0} is: {1}".format(S, x))
    print("\nCompared to math.sqrt({0}): {1}".format(S, math.sqrt(S)))


if __name__ == "__main__":
    main()
