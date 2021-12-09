import os
from typing import List


def read_file(filepath: str) -> List[str]:
    """Read a file"""
    with open(filepath) as f:
        return f.read().strip().split("\n")


def read_input(*, day: int) -> List[str]:
    """Read the input file for a particular day"""
    filepath = os.path.abspath(f"inputs/day{day}.txt")
    return read_file(filepath)


def read_test_input(*, day: int) -> List[str]:
    """Read the test input file for a particular day"""
    filepath = os.path.abspath(f"tests/test_inputs/test_day{day}.txt")
    return read_file(filepath)
