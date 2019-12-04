import math

from common.input import read_input


def fuel_required(mass: int) -> int:
    return math.floor(mass / 3) - 2


def main() -> None:
    total_fuel = 0
    for line in read_input(1):
        mass = int(line)
        total_fuel += fuel_required(mass)
    print(total_fuel)


if __name__ == "__main__":
    main()
