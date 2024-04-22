#!/usr/bin/env python3
'''Module for measuring the runtime of asynchronous tasks.'''

import asyncio
import time

# Importing the wait_n coroutine
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n with given parameters.

    Parameters:
    n (int): The number of times to run wait_n.
    max_delay (int): The maximum delay for each wait_random coroutine.

    Returns:
    float: The average runtime for wait_n(n, max_delay).
    '''
    # Get the start time
    start_time = time.time()
    # Run the asynchronous function
    asyncio.run(wait_n(n, max_delay))
    # Calculate the elapsed time and return the average
    return (time.time() - start_time) / n
