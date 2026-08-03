#!/usr/bin/env python3

"""
Runtime Complexity of Algorithm
(not to be confused with Convergence)

I.e. how much time it takes the algorithm to run.

"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import big_o
from sqrt import sqrt

# # define generator for a List of numbers
# positive_int_gen = lambda n: big_o.datagen.integers(n, min_=0, max_=100000)

# generate a single number at a time
number_generator = big_o.datagen.n_

best, others = big_o.big_o(sqrt, number_generator, n_repeats=5, min_n=1, max_n=2000)

print(best)
# print(others)
