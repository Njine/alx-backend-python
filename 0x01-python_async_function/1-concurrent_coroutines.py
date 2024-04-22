#!/usr/bin/env python3
'''Module for concurrent coroutine execution.'''

import asyncio
from typing import List
from basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns 'n' instances of 'wait_random' with 'max_delay' and returns a list of sorted delays.'''
    
    # Create a list of tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Run all tasks concurrently and wait for their completion
    wait_times = await asyncio.gather(*tasks)
    
    # Return the list of delays in ascending order
    return sorted(wait_times)
