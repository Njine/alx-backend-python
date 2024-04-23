#!/usr/bin/env python3
"""
Measure runtime for four parallel async comprehensions
"""
import asyncio
import time
from typing import List

# Importing the async_comprehension coroutine
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous coroutine to measure the total runtime required to execute
    4 async_comprehension calls in parallel.
    """
    # Record the start time
    start_time = time.perf_counter()

    # Run four async_comprehension calls in parallel
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    # Record the end time
    end_time = time.perf_counter()

    # Calculate the total runtime
    return end_time - start_time
