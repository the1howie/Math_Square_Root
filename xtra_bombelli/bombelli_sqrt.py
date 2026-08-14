"""
Square root approximation as a simple continued fraction.

https://en.wikipedia.org/wiki/Rafael_Bombelli#:~:text=%5B6%5D-,Bombelli%27s%20method%20of%20calculating%20square%20roots,-edit
"""

import math
from fractions import Fraction


def validate_positive_int(n):
    # check if n is an integer
    try:
        n = int(n)
    except Exception as e:
        raise Exception(e)

    # check if S is positive
    if n < 0:
        raise Exception("Invalid input. Enter a positive integer.")

    # finally return the integer value
    return n


def bombelli_sqrt(S, depth=5):
    """iterative method to compute the simple continuted fraction,
    √S ≈ a + r where r = |S - a²| / (2a + r)"""

    # validation
    S = validate_positive_int(S)
    depth = validate_positive_int(depth)

    # lower boundary such that a² ≤ S
    a = math.floor(math.sqrt(S))

    # trivial cases and perfect squares
    if a * a == S:
        return a

    # trivial case of no continued fractions
    if depth == 0:
        return a

    # simple continued fractions
    r = 0
    while depth > 0:
        r = Fraction(S - a**2, 2 * a + r)
        depth -= 1

    return a + r


def frac_to_mixed(frac: Fraction):
    return (
        frac.numerator // frac.denominator,
        Fraction(frac.numerator % frac.denominator, frac.denominator),
    )


def frac_to_float(frac: Fraction):
    m = frac_to_mixed(frac)
    return float(m[0] + m[1])


def main():
    S = validate_positive_int(input("Enter a positive integer: "))

    depth = input("Enter the depth (default is 5): ")
    if depth.strip() == "":
        depth = 5
    else:
        depth = validate_positive_int(depth)

    # list of approximations
    x = []

    print(f"depth: \tfraction \t = mixed number \t = float")

    for i in range(depth + 1):
        x.append(bombelli_sqrt(S, depth=i))
        print(f"{i:03}: \t{x[i]} \t = {frac_to_mixed(x[i])} \t = {frac_to_float(x[i])}")

    print(f"\nmath.sqrt({S}) = {math.sqrt(S)}")


if __name__ == "__main__":
    main()
