#!/usr/bin/env python3
"""
Async generator example
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields a random float between 0 and 10
    every second, 10 times in total.
    """
    for _ in range(10):
        # Wait for 1 second asynchronously
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.uniform(0, 10)
