import math
from collections import defaultdict

from common.input import auto_read_input


def _parse_input(lines):
    ## Start here
    return [int(pos_str) for pos_str in lines[0].split(",")]


def brute_force_minimal_fuel(crab_arr):
    distances_to_idx = defaultdict(int)

    max_idx = max(crab_arr)
    for idx in range(max_idx):
        for pos in crab_arr:
            distances_to_idx[idx] += abs(idx - pos)

    min_fuel = min(distances_to_idx.values())
    return min_fuel


def brute_force_minimal_fuel_series(crab_arr):
    distances_to_idx = defaultdict(int)

    # Cache our calculations
    dist_values = {0: 0, 1: 1}
    max_dist_calculated = 1

    max_idx = max(crab_arr)
    for idx in range(max_idx):
        for pos in crab_arr:
            dist = abs(idx - pos)

            # If not in cache, calculate onwards from largest computed dist
            if dist not in dist_values:
                for d in range(max_dist_calculated, dist + 1):
                    dist_values[d] = d + dist_values[d - 1]
                max_dist_calculated = dist

            distances_to_idx[idx] += dist_values[dist]

    min_fuel = min(distances_to_idx.values())
    return min_fuel


def part1():
    crab_arr = _parse_input(auto_read_input())
    return brute_force_minimal_fuel(crab_arr)


def part2():
    crab_arr = _parse_input(auto_read_input())
    return brute_force_minimal_fuel_series(crab_arr)


if __name__ == "__main__":
    print(part1())
    print(part2())
