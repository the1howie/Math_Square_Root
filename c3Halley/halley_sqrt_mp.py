#!/usr/bin/env python3

"""
Halley's Method to approximate the square root.

Using the multi-precision math library https://mpmath.org/
"""

import mpmath as mpm


def halley_sqrt_mp(S, precision_dps=15, print_guesses=False, verbose=False):
    """Square Root using Halley's Method."""

    # validation
    if S < 0:
        raise ValueError("Invalid input! Expected a positive number.")

    # trivial case
    if S == 0:
        return mpm.mpf(0)

    # set precision
    mpm.mp.dps = min(15, precision_dps)

    # for printing
    significant_digits = precision_dps + len(str(S))

    # convert input S to mpf
    S = mpm.mpmathify(S)

    # set threshold
    tau = mpm.power(10, mpm.fmul(-1, precision_dps))

    # initial guess
    x = [mpm.fdiv(max(mpm.mpmathify(1), S), 2)]
    guesses = 0

    # estimate the number of iterations
    est_iter = num_iter(tau, S, x[0])

    # print out each step if verbose
    if verbose:
        progress = "iteration: {0}\tguess: {1}\tguess²: {2}"

    # do the first iteration
    if abs(mpm.fsub(mpm.power(x[-1], 2), S)) >= tau:
        if verbose:
            print(
                progress.format(
                    guesses,
                    mpm.nstr(x[-1], significant_digits),
                    mpm.nstr(mpm.power(x[-1], 2), significant_digits),
                )
            )
        guesses += 1
        # Halley: x[n+1] = x[n] * (x[n]^2 + 3*S) / (3*x[n]^2 + S)
        x.append(
            mpm.fmul(
                x[-1],
                mpm.fdiv(
                    mpm.fadd(mpm.power(x[-1], 2), mpm.fmul(3, S)),
                    mpm.fadd(mpm.fmul(3, mpm.power(x[-1], 2)), S),
                ),
            )
        )

    # do the second iteration
    if (
        abs(mpm.fsub(mpm.power(x[-1], 2), S)) >= tau
        and abs(mpm.fsub(x[-1], x[-2])) >= tau
    ):
        if verbose:
            print(
                progress.format(
                    guesses,
                    mpm.nstr(x[-1], significant_digits),
                    mpm.nstr(mpm.power(x[-1], 2), significant_digits),
                )
            )
        guesses += 1
        # Halley: x[n+1] = x[n] * (x[n]^2 + 3*S) / (3*x[n]^2 + S)
        x.append(
            mpm.fmul(
                x[-1],
                mpm.fdiv(
                    mpm.fadd(mpm.power(x[-1], 2), mpm.fmul(3, S)),
                    mpm.fadd(mpm.fmul(3, mpm.power(x[-1], 2)), S),
                ),
            )
        )

    # loop until the stopping criterion is met
    while (
        abs(mpm.fsub(mpm.power(x[-1], 2), S)) >= tau
        and abs(mpm.fsub(x[-1], x[-2])) >= tau
        and abs(mpm.fsub(x[-1], x[-3])) >= tau
        and x[-1] not in x[:-1]
    ):
        if verbose:
            print(
                progress.format(
                    guesses,
                    mpm.nstr(x[-1], significant_digits),
                    mpm.nstr(mpm.power(x[-1], 2), significant_digits),
                )
            )
        guesses += 1
        # Halley: x[n+1] = x[n] * (x[n]^2 + 3*S) / (3*x[n]^2 + S)
        x.append(
            mpm.fmul(
                x[-1],
                mpm.fdiv(
                    mpm.fadd(mpm.power(x[-1], 2), mpm.fmul(3, S)),
                    mpm.fadd(mpm.fmul(3, mpm.power(x[-1], 2)), S),
                ),
            )
        )

    if print_guesses:
        print(
            f"Number of guesses: {guesses}, Threshold: {tau}, Estimate iterations: {est_iter}."
        )

    return x[-1]


def num_iter(tau, S, x0):
    """Estimate the number of iterations."""
    d = abs(mpm.log10(tau))
    rho = mpm.fdiv(1, mpm.fmul(2, mpm.sqrt(S)))
    e0 = abs(mpm.fsub(mpm.sqrt(S), x0))
    try:
        if e0 != mpm.mpmathify(0):
            return int(
                mpm.ceil(
                    mpm.log(
                        abs(
                            mpm.fdiv(
                                mpm.log10(
                                    mpm.fmul(rho, mpm.power(10, mpm.fmul(-1, d)))
                                ),
                                mpm.log10(mpm.fmul(rho, e0)),
                            )
                        ),
                        3,
                    )
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

    prec = input("Enter precision (Default 15 d.p.): ")
    try:
        prec = int(prec)
    except Exception:
        prec = 15
    if prec < 0:
        raise ValueError("Invalid input. Input must be a positive number.")

    # significant figures for printing
    sf = prec + len(str(S))

    x = halley_sqrt_mp(S, prec, True, True)
    print(
        "\nApproximation for the square root of {0} is: {1}".format(S, mpm.nstr(x, sf))
    )

    mpm.mp.dps = min(15, prec)
    S = mpm.mpmathify(S)
    print("\nCompared to mpmath.sqrt({0}): {1}".format(S, mpm.nstr(mpm.sqrt(S), sf)))


if __name__ == "__main__":
    main()
