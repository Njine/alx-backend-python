#!/usr/bin/env python3
'''Module for creating a multiplier function.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function that multiplies a float.

    Args:
        multiplier (float): The multiplier to be used in the function.

    Returns:
        Callable[[float], float]: A function that takes a float as input.
        '''
    return lambda x: x * multiplier
