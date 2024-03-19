#!/usr/bin/env python3
""" Measures the runtime"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total time to execute wait_n function.

    Args:
        n (int): first argument passed to wait_n
        max_delay (int): second argument passed to wait_n

    Returns:
        float - total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
