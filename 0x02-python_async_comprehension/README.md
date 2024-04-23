
Here is a reworded summary of the provided content:

Project: Python - Async Comprehension
Resources
To understand this project, you should read or watch:

PEP 530 – Asynchronous Comprehensions
"What's New in Python": sections on asynchronous comprehensions and generators
Guidance on type hints for generators
Learning Goals
By the end of this project, you should know:

How to write an asynchronous generator in Python
How to use asynchronous comprehensions
How to add type annotations to generators and coroutines
Requirements
General guidelines for this project:

Editors you can use: vi, vim, emacs
The code will be compiled/interpreted on Ubuntu 18.04 LTS with Python 3.7
Ensure all files end with a new line
The first line of each Python file must be #!/usr/bin/env python3
Include a README.md file in the root directory
Follow the pycodestyle conventions (version 2.5.x)
Each file's length will be verified with wc
Each module must have a descriptive docstring
Each function and coroutine must have a docstring
Ensure type annotations for all functions and coroutines
Tasks
Async Generator
Write an asynchronous generator called async_generator that does not take any arguments.
This coroutine should loop 10 times, pausing asynchronously for 1 second each time, then yield a random number between 0 and 10.
To test, use a script that asynchronously collects the generated values and prints them.
The expected output would be a list of 10 random numbers.
Files:
GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 0-async_generator.py
Async Comprehensions
Write a coroutine called async_comprehension that imports async_generator from the previous step.
This coroutine collects 10 random numbers using asynchronous comprehension over async_generator, then returns these numbers as a list.
Test with a script that runs this coroutine and prints the results.
Files:
GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 1-async_comprehension.py
Run Time for Four Parallel Comprehensions
Write a coroutine called measure_runtime that executes async_comprehension four times in parallel using asyncio.gather.
This coroutine should measure the total runtime required to run four parallel instances of async_comprehension and return it.
The expected runtime is roughly 10 seconds because the operations happen asynchronously, but they run concurrently.
Files:
GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 2-measure_runtime.py