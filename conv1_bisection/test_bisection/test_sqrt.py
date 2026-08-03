#!/usr/bin/env python3

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import pytest
from sqrt import sqrt

# test number of guesses? get from stream io
