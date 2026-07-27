#!/usr/bin/env python3

"""
The bisection method is linearly convergent..

We start with an interval x ∈ (a, b) for x = √S.

We halve the interval with each iteration, for example x₀ = (a + b)/2, until |xₙ - S| < ε.

This is the slowest converging method however, it is a good start for students.
"""


def square_root(x, epsilon=0.000001):
    # bisection search
    guesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    progress = "low: {0}, high: {1}, ans: {2} (ans^2: {3})"
    while abs(ans ** 2 - x) >= epsilon:
        print(progress.format(low, high, ans, ans**2))
        guesses += 1
        if ans ** 2 < x:
            # underestimate
            low = ans
        else:
            # overestimate
            high = ans
        ans = (high + low) / 2.0
    print("\nnumber of guesses: {}".format(guesses))
    return ans

if __name__ == "__main__":
    x = float(input("Enter positive number: "))
    if x < 0:
        ans = complex(0, square_root(abs(x)))
        print("approximation for the square root of {0} is: {1}".format(x, ans))
    else:
        ans = square_root(x)
        print("approximation for the square root of {0} is: {1}".format(x, ans))
        