#!/usr/bin/env python3
'''Module for executing concurrent tasks created with task_wait_random.
'''

import asyncio
from typing import List
# Import the task creation function
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawns task_wait_random n times with a given max_delay,
    and returns a list of delays.
    
    Args:
        n: Number of times to create a task with task_wait_random.
        max_delay: Maximum delay for each task.
    
    Returns:
        A list of float values representing the delays, sorted in ascending order.
    '''
    # Use asyncio.gather to run the tasks concurrently
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)  # Await the results of all tasks
    # Return the list of wait times sorted
    return sorted(wait_times)  # Uses sorting to maintain order
