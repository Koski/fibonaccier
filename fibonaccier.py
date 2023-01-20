from random import randint
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


async def __fibonacci_number(n: int, delay: float, first: int = 0, second: int = 1) -> int:
    """
    Calculates the nth Fibonacci number and delays according to given inputs.
    :param n: Denotes which Fibonacci number to calculate
    :param delay: Denotes how long the function sleeps
    :param first: Denotes first of the two previous numbers to add up
    :param second: Denotes second of the two previous numbers to add up
    :return: Nth fibonacci number
    """
    if n > 0:
        return await __fibonacci_number(n-1, delay, second, first+second)

    await asyncio.sleep(delay)
    return first


def __get_random_delay() -> float:
    """
    Generates a random delay of up to one second. The random number denotes milliseconds which are divided by 1000
    to get the delay in seconds
    :return: Delay in seconds
    """
    return randint(0, 1000) / 1000


async def fibonaccier(n) -> tuple:
    """
    Calls __fibonacci_number twice with the given input and determines which finished first.
    :param n: Which Fibonacci number to calculate
    :return: Nth Fibonacci number and call which finished first
    """
    task_1: asyncio.Task = asyncio.create_task(__fibonacci_number(n, __get_random_delay()), name='1')
    task_2: asyncio.Task = asyncio.create_task(__fibonacci_number(n, __get_random_delay()), name='2')

    finished: set
    finished, _ = await asyncio.wait([task_1, task_2], return_when=asyncio.FIRST_COMPLETED)

    finished_task = finished.pop()
    return finished_task.result(), finished_task.get_name()
