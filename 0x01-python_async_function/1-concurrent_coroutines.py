#!/usr/bin/env python3
'''Task 1's module for defining wait_n function.'''
import asyncio
from typing import List

# Importing the wait_random function
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times and returns a sorted list of delays.'''
    wait_times = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    # Using insertion sort to order the results
    for i in range(1, len(wait_times)):
        key = wait_times[i]
        j = i - 1
        while j >= 0 and wait_times[j] > key:
            wait_times[j + 1] = wait_times[j]
            j -= 1
        wait_times[j + 1] = key
    return wait_times
