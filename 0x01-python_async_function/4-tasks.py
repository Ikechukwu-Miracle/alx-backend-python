#!/usr/bin/env python3
"""
 takes in 2 int arguments (in this order): n and max_delay. You will spawn task_wait_random n times with the specified max_delay
 """
import asyncio
from typing import List
from random import uniform
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay.
    Args:
        n (int): number of times to call task_wait_random function
        max_delay (int): argument passed to wait_random

    returns:
        list - of delayed time from task_wait_random
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
