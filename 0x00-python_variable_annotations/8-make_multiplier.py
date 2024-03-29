#!/usr/bin/env python3
"""
Defines a function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float and returns a float"""
    return lambda x: multiplier * x
