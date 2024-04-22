#!/usr/bin/env python3
'''Task 2's module for measuring runtime.'''
import asyncio
import time

# Importing wait_n from the correct module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the average time for executing wait_n.'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
