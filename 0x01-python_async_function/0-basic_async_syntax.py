#!/usr/bin/env python3
'''Task 0's module for defining wait_random function.'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds and returns the delay.'''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
