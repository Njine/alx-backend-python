#!/usr/bin/env python3
'''Module for executing concurrent coroutines with a custom order.
'''

import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawns wait_random n times with a given max_delay and returns a list of delays.
    
    Args:
        n: Number of times to execute wait_random.
        max_delay: Maximum delay in seconds for wait_random.
    
    Returns:
        A list of delays in ascending order.
    '''
    # Use asyncio.gather to run multiple coroutines concurrently
    delays = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )

    # Manual sorting: Find the minimum delay repeatedly until the list is empty
    sorted_delays = []
    while delays:
        min_delay = min(delays)  # Find the minimum delay
        sorted_delays.append(min_delay)  # Add to the sorted list
        delays.remove(min_delay)  # Remove the minimum from the original list

    return sorted_delays
