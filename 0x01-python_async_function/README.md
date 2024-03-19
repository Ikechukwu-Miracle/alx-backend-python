# 0x01. Python - Async

This project focuses on asynchronous programming, It involves managing coroutines and running concurrent programs with the help of Python's asyncio module. <br>
asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

There are a total of 5 tasks mandatory in this project: <br>
## Project Tasks
### 0. The basics of async
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

**Requirement:** Use the random module.

To accomplish this task, an asynchronous coroutine named wait_random was created. This coroutine takes an integer argument max_delay, with a default value of 10. Within the coroutine, the random module was utilized to generate a random delay between 0 and max_delay seconds (inclusive). Then the delay is waited on to complete before returning the delay value.

### 1. Let's execute multiple coroutines at the same time with async
In this task, it is required to import wait_random from the previous file and define an async routine named wait_n. This routine takes two integer arguments: n and max_delay. Within wait_n, spawn wait_random n times with the specified max_delay, and returns a list of all the delays in ascending order without using sort() due to concurrency.

### 2. Measure the runtime
For this task, it is required to measure the runtime. To achieve this, wait_n was imported into 2-measure_runtime.py. A function measure_time with integers n and max_delay as arguments was created. This function measures the total execution time for wait_n(n, max_delay) and returns total_time / n. The time module was utilized to measure an approximate elapsed time.

### 3. Tasks
In this task, a regular function syntax task_wait_random is required that takes an integer max_delay and returns a asyncio.Task.
wait_random is imported from 0-basic_async_syntax. 

### 4. Tasks
For this task, the code from wait_n is modified into a new function named task_wait_n. This function is nearly identical to wait_n, except it calls task_wait_random.
