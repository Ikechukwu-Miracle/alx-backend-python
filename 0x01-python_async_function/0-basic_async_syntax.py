#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay period and return it.

    Args:
        max_delay (int): The given maximum wait period

    Returns:
        float - Random wait period that does not exceed max_delay.
    """
    delay_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)

    return delay_time
