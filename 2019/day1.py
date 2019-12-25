import math
from typing import Callable, List

from common.input import read_input


def _fuel_required(mass: int) -> int:
    """Calculates required fuel based on mass"""
    return math.floor(mass / 3) - 2


def _recursive_fuel_required(mass: int) -> int:
    """Determine the total recursive amount of fuel needed for a give mass.

    An object of a provided mass requires fuel, that fuel then requires
    fuel, which requires fuel, and so on. Fuel's fuel requirement is 0 if our
    calculation requires no fuel, or negative fuel.
    """
    total_fuel_required = last_fuel = _fuel_required(mass)
    while last_fuel > 0:
        last_fuel = _fuel_required(last_fuel)
        if last_fuel > 0:
            total_fuel_required += last_fuel
    return total_fuel_required


def _calculate_total_fuel(fuel_func: Callable, masses: List[int]) -> int:
    """Calculate total fuel requirements for list of masses."""
    total_fuel = 0
    for mass in masses:
        total_fuel += fuel_func(mass)
    return total_fuel


def part1() -> int:
    masses = [int(line) for line in read_input(day=1)]
    return _calculate_total_fuel(_fuel_required, masses)


def part2() -> int:
    masses = [int(line) for line in read_input(day=1)]
    return _calculate_total_fuel(_recursive_fuel_required, masses)


if __name__ == "__main__":
    print(part1())
    print(part2())
