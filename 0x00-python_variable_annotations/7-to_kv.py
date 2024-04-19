#!/usr/bin/env python3
'''Module for converting a key-value pair to a tuple with the value squared.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its value.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value as an integer or float.

    Returns:
        Tuple[str, float]: A tuple containing key and square of its value.
    '''
    return (k, float(v ** 2))
