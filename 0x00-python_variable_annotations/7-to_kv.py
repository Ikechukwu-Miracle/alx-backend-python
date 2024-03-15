#!/usr/bin/env python3
"""
Defines a function that takes a string and either an int or float and
returns a tuple containing the string and the square of the number.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes in string and a number (flat or int) and returns a tuple"""
    return (k, v ** 2)
