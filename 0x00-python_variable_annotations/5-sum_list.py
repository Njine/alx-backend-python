#!/usr/bin/env python3
'''Module for computing the sum of a list of floating-point numbers.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of the input list of floating-point numbers.

    Args:
        input_list (List[float]): The list of floating-point numbers.

    Returns:
        float: The sum of the input list of numbers.
    '''
    return float(sum(input_list))
