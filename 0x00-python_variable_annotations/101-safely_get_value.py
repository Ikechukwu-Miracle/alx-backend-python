#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations
to the function
"""
from typing import Union, Any, TypeVar, Mapping
T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Gets value safely"""
    if key in dct:
        return dct[key]
    else:
        return default
