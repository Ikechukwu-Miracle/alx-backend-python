#!/usr/bin/env python3
"""
 takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay
 """
import asyncio
from typing import List
from random import uniform


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay.
    Args:
        n (int): number of times to call wait_random function
        max_delay (int): argument passed to wait_random

    returns:
        list - of delayed time from wait_random
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
