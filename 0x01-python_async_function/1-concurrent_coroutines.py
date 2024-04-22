#!/usr/bin/env python3
'''Task 1's module for running concurrent asynchronous coroutines.'''

import asyncio
from typing import List
from basic_async_syntax import wait_random

def create_tasks(n: int, max_delay: int) -> List[asyncio.Task]:
    '''Creates a list of asyncio tasks for given n and max_delay.'''
    return [wait_random(max_delay) for _ in range(n)]

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs 'wait_random' 'n' times concurrently and returns the list of delays in ascending order.'''
    
    # Create the tasks
    tasks = create_tasks(n, max_delay)
    
    # Wait for all tasks to complete
    wait_times = await asyncio.gather(*tasks)
    
    # Return the results in ascending order
    return sorted(wait_times)
