from collections import defaultdict
from typing import Dict, List, Set, Tuple

from common.input import auto_read_input


class OctopusMap:
    def __init__(self, power_levels: List[List[int]]):
        self._power_levels = power_levels

    def _increment_all_by_one(self):
        flash_queue = []

        for r in range(len(self._power_levels)):
            for c in range(len(self._power_levels[r])):
                self._power_levels[r][c] += 1
                if self._power_levels[r][c] > 9:
                    flash_queue.append((r, c))

        return flash_queue

    def _get_neighbors(self, r, c):
        neighbors = []

        for direction in range(9):
            # ignore self
            if direction == 4:
                continue

            n_row = r + ((direction % 3) - 1)
            n_col = c + ((direction // 3) - 1)

            if (0 <= n_row < len(self._power_levels)) and (
                0 <= n_col < len(self._power_levels[n_row])
            ):
                neighbors.append((n_row, n_col))

        return neighbors

    def step(self):
        already_flashed = set()

        # First, the energy level of each octopus increases by 1.
        flash_queue = self._increment_all_by_one()

        # Then, any octopus with an energy level greater than 9 flashes. This
        # increases the energy level of all adjacent octopuses by 1, including
        # octopuses that are diagonally adjacent. If this causes an octopus to
        # have an energy level greater than 9, it also flashes. This process
        # continues as long as new octopuses keep having their energy level
        # increased beyond 9. (An octopus can only flash at most once per
        # step.)
        while flash_queue:
            r, c = flash_queue.pop(0)

            if (r, c) in already_flashed:
                continue

            already_flashed.add((r, c))

            neighbors = self._get_neighbors(r, c)
            for (n_r, n_c) in neighbors:
                self._power_levels[n_r][n_c] += 1
                if self._power_levels[n_r][n_c] > 9:
                    flash_queue.insert(0, (n_r, n_c))

            self._power_levels[r][c] = -9

        # Finally, any octopus that flashed during this step has its energy
        # level set to 0, as it used all of its energy to flash.
        for (r, c) in already_flashed:
            self._power_levels[r][c] = 0

        num_flashes = len(already_flashed)
        return num_flashes


def _parse_input(input_str):
    ## Start here
    power_levels = [[int(p) for p in line] for line in input_str]
    return OctopusMap(power_levels)


def part1():
    octopus_map = _parse_input(auto_read_input())

    total_flashes = 0
    for i in range(100):
        total_flashes += octopus_map.step()

    return total_flashes


def part2():
    octopus_map = _parse_input(auto_read_input())
    num_flashes = 0
    num_steps = 0

    while num_flashes != 100:
        num_flashes = octopus_map.step()
        num_steps += 1

    return num_steps


if __name__ == "__main__":
    print(part1())
    print(part2())
