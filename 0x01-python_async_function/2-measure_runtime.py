#!/usr/bin/env python3
'''Module for measuring runtime of concurrent coroutines.
'''

import asyncio
import time
from typing import Tuple

# Importing the previously defined coroutine from '1-concurrent_coroutines'
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time of the wait_n coroutine
    and returns the average time per task.
    
    Args:
        n: Number of tasks to run.
        max_delay: Maximum delay for each task.
    
    Returns:
        A float representing the average time per task.
    '''
    start_time = time.time()  # Capture start time
    # Run the wait_n coroutine asynchronously
    asyncio.run(wait_n(n, max_delay))
    # Calculate the total elapsed time and find the average
    total_time = time.time() - start_time
    average_time = total_time / n
    return average_time
