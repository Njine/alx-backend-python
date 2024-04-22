#!/usr/bin/env python3
'''Module for measuring the runtime of asynchronous operations.'''

import asyncio
import time
from concurrent_coroutines import wait_n  # Importing from 1-concurrent_coroutines


def measure_time(n: int, max_delay: int) -> float:
    '''Calculates the average execution time for 'wait_n'.

    Args:
        n (int): Number of asynchronous tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: Average time taken by the tasks.
    '''
    # Start the timer
    start_time = time.time()

    # Execute the asynchronous coroutine 'wait_n'
    asyncio.run(wait_n(n, max_delay))

    # Calculate the total elapsed time and return the average
    elapsed_time = time.time() - start_time
    return elapsed_time / n
