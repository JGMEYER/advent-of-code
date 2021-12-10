import os
from typing import List


def read_file(filepath: str) -> List[str]:
    """Read a file"""
    with open(filepath) as f:
        return f.read().strip().split("\n")


def input_filepath(*, day: int, test: bool = False) -> str:
    """Returns paths to both question and test inputs"""
    return (
        f"tests/test_inputs/test_day{day}.txt"
        if test
        else f"inputs/day{day}.txt"
    )


def read_input(*, day: int) -> List[str]:
    """Read the input file for a particular day"""
    filepath = os.path.abspath(input_filepath(day=day))
    return read_file(filepath)


def read_test_input(*, day: int) -> List[str]:
    """Read the test input file for a particular day"""
    filepath = os.path.abspath(input_filepath(day=day, test=True))
    return read_file(filepath)
