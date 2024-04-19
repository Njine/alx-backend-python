#!/usr/bin/env python3
'''Module for creating a multiplier function.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the function.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns the result
        of multiplying that float by the multiplier.
    '''
    return lambda x: x * multiplier
