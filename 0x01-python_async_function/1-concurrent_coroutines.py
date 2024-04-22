#!/usr/bin/env python3
'''Module for creating asynchronous tasks.'''

import asyncio
from typing import List

# Importing the wait_random coroutine from the previous script
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times and returns the delays in ascending order.

    Parameters:
    n (int): The number of times to run wait_random
    max_delay (int): The maximum delay to pass to wait_random

    Returns:
    List[float]: A list of the resulting delay times in ascending order
    '''
    # List to hold coroutine results
    wait_times = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )

    # We will manually sort the list without using sort()
    # Sorting with insertion method
    for i in range(1, len(wait_times)):
        key = wait_times[i]
        j = i - 1
        # Move elements of wait_times that are > key, to one position ahead
        # of their current position
        while j >= 0 and wait_times[j] > key:
            wait_times[j + 1] = wait_times[j]
            j -= 1
        wait_times[j + 1] = key

    return wait_times
