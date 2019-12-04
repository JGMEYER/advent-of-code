import os
from typing import List


def read_file(filepath: str) -> List[str]:
    """Read a file"""
    with open(filepath) as f:
        return f.read().strip().split()


def read_input(day_num: int) -> List[str]:
    """Read the input file for a particular day"""
    filepath = os.path.abspath(f"inputs/day{day_num}.txt")
    return read_file(filepath)
