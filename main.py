import asyncio
import logging
from fibonaccier import fibonaccier
from fibo_arg_parser import get_fibo_argument_parser

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


if __name__ == '__main__':
    argument_parser = get_fibo_argument_parser()
    n: int = argument_parser.parse_args().integer

    result, task_number = asyncio.run(fibonaccier(n))

    logger.info("#%i Fibonacci number is %i. Function call number %s finished first.", n, result, task_number)
