#!/usr/bin/env python3

"""
Babylonian Method for extracting the square root from around 1800 - 1600 BC.
x = √S ~ x + (S - x²)/(2x)

Also known as Heron's Method from the 1st century AD. 
x = √S ~ ½(x + S/x)

Heron's method is an exact simplification of the Babylonian method.
i.e., x + (S - x²)/(2x) ≡ ½(x + S/x).

For simplicity, we will use xₙ₊₁ = ½(xₙ + S/xₙ). 

This method converges quadratically i.e., |xₙ₊₁ - S| < μ|xₙ - S|² for some arbitrarily large n.

This is the most popular iterative method as it is simple and efficient. Most computers still use it.
"""
