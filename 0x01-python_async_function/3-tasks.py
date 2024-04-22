#!/usr/bin/env python3
'''Module for creating asynchronous tasks.'''

import asyncio

# Import the wait_random coroutine from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Creates an asyncio.Task for the given coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: An asynchronous task that can be awaited.
    '''
    # Create and return an asyncio.Task from the wait_random coroutine
    return asyncio.create_task(wait_random(max_delay))
