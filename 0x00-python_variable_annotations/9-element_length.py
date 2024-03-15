#!/usr/bin/env python3
"""
An anotation of a given function below using Duck typing
"""
from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """The annotated function"""
    return [(i, len(i)) for i in lst]
