#!/usr/bin/env python3
'''Module for creating asynchronous tasks.
'''

import asyncio

# Importing the wait_random coroutine from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates an asyncio.Task for the given coroutine.
    
    Args:
        max_delay: Maximum delay for wait_random.
    
    Returns:
        An asyncio.Task that can be awaited.
    '''
    # Create and return an asyncio.Task from the wait_random coroutine
    return asyncio.create_task(wait_random(max_delay))
