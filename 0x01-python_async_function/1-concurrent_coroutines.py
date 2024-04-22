import asyncio
from typing import List
from random import uniform

#!/usr/bin/env python3
'''Task 1's module.

This module contains an asynchronous function that executes the `wait_random` function `n` times.
'''



async def wait_random(max_delay: int) -> float:
    '''Waits for a random delay between 0 and `max_delay` seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The actual delay in seconds.
    '''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes `wait_random` `n` times and returns the sorted list of delays.

    Args:
        n (int): The number of times to execute `wait_random`.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The sorted list of delays.
    '''
    wait_times = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(wait_times)
