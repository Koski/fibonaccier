from argparse import ArgumentParser, ArgumentTypeError

class InvalidFiboInput(ArgumentTypeError):
    def __init__(self):
        super().__init__("Argument should be a positive (>0) integer")

def __check_positive_integer(value) -> int:
    """
    Checks and validates that input for argument parser is a positive integer. Raises an exception if value is
    invalid.
    :param value: Input from command line
    :return: Integer value of given input
    """
    try:
        int_value = int(value)
        if int_value <= 0:
            raise InvalidFiboInput
        return int_value
    except ValueError as ex:
        raise InvalidFiboInput from ex


def get_fibo_argument_parser() -> ArgumentParser:
    """
    Creates a simple command line argument parser that takes a positive integer input
    :return: Command line parser
    """
    parser = ArgumentParser(description='Find the Nth fibonacci number based on an integer input.')
    parser.add_argument(
        'integer',
        metavar='N',
        type=__check_positive_integer,
        help='Positive integer to determine the number from a fibonacci sequence'
    )
    return parser
