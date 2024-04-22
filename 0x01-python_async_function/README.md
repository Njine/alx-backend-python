Asynchronous Programming in Python 3
This project focuses on learning and applying asynchronous programming techniques in Python 3, covering several tasks that explore different aspects of concurrency and asynchronous code execution.

Tasks Overview
Task 0: Basic Asynchronous Coroutine
File: 0-basic_async_syntax.py
Description: This script contains an asynchronous coroutine named wait_random. It takes an optional integer argument max_delay (defaulting to 10) and waits for a random delay between 0 and max_delay seconds before returning the delay. The random delay is generated using the random module.
Task 1: Running Multiple Coroutines Concurrently
File: 1-concurrent_coroutines.py
Description: This script defines an asynchronous coroutine wait_n that takes two integer arguments n and max_delay. The coroutine spawns wait_random n times, each with the specified max_delay. It returns a list of delay times in ascending order without using sort() to account for concurrency.
Task 2: Measuring Execution Time
File: 2-measure_runtime.py
Description: This script introduces a function measure_time that calculates the average execution time for wait_n(n, max_delay). It takes two integers n and max_delay, then measures the total time taken for wait_n(n, max_delay), returning the average time per coroutine. The time module is used for timing the execution.
Task 3: Creating an Asyncio Task
File: 3-tasks.py
Description: This script contains a function task_wait_random, which takes an integer max_delay and returns an asyncio.Task that represents the wait_random coroutine. This allows the creation of asynchronous tasks without needing to use async/await syntax.
Task 4: Task-based Concurrency
File: 4-tasks.py
Description: This script defines a new asynchronous coroutine task_wait_n, which is similar to wait_n, but uses task_wait_random to create asynchronous tasks. The function returns a list of delays in ascending order.
Additional Resources
To deepen your understanding of asynchronous programming, consider exploring these resources:

Async IO in Python: A Complete Walkthrough
asyncio - Asynchronous I/O in Python
random.uniform
With these tasks and resources, this project aims to provide a comprehensive introduction to asynchronous programming in Python, focusing on both theory and practical implementation.