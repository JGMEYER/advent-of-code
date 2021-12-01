from typing import List

from common.input import read_input


def _num_depth_increases(depths: List[int]) -> int:
    num_depth_increases = 0
    for idx in range(len(depths) - 1):
        if depths[idx] < depths[idx + 1]:
            num_depth_increases += 1
    return num_depth_increases


def _num_depth_increases_sliding_window(depths: List[int]) -> int:
    num_depth_increases = 0
    for idx in range(len(depths) - 3):
        if sum(depths[idx : idx + 3]) < sum(depths[idx + 1 : idx + 4]):
            num_depth_increases += 1
    return num_depth_increases


def part1():
    depths = [int(line) for line in read_input(day=1)]
    return _num_depth_increases(depths)


def part2():
    depths = [int(line) for line in read_input(day=1)]
    return _num_depth_increases_sliding_window(depths)


if __name__ == "__main__":
    print(part1())
    print(part2())
