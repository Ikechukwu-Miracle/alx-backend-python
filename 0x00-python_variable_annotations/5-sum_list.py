#!/usr/bin/env python3
"""
Defines a function that takes a list as argument and
returns the sum of the list elements.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sums list of floats """
    return sum(input_list)
