#!/usr/bin/env python3
'''Module for computing  sum of a list of integers and floating-point digits.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of input list of integers and floating-point digits.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the input list of numbers.
    '''
    return float(sum(mxd_lst))
