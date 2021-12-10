import math
from typing import List
from collections import namedtuple

from common.input import auto_read_input

Point = namedtuple("Point", ["r", "c", "height"])


class HeightMap:
    def __init__(self, heights: List[List[int]]):
        self._heights = heights
        self._w = len(heights[0])
        self._h = len(heights)
        self._neighbors_cache = {}

    def get(self, r, c):
        return Point(r, c, self._heights[r][c])

    def neighbors(self, r, c):
        if (r, c) in self._neighbors_cache:
            return self._neighbors_cache[(r, c)]

        neighbors = [
            self.get(r - 1, c) if r > 0 else None,  # top
            self.get(r, c + 1) if c < self._w - 1 else None,  # right
            self.get(r + 1, c) if r < self._h - 1 else None,  # bottom
            self.get(r, c - 1) if c > 0 else None,  # left
        ]
        self._neighbors_cache[(r, c)] = neighbors
        return neighbors

    def is_low_point(self, r, c):
        neighbors = self.neighbors(r, c)
        return self._heights[r][c] < min(
            [p.height for p in neighbors if p is not None]
        )

    def get_all_low_points(self):
        return [
            self.get(r, c)
            for r in range(self._h)
            for c in range(self._w)
            if self.is_low_point(r, c)
        ]

    def get_all_basins(self):
        return [
            Basin(self, low_point) for low_point in self.get_all_low_points()
        ]


class Basin:
    """A basin is all locations that eventually flow downward to a single
    low point. Therefore, every low point has a basin, although some basins
    are very small. Locations of height 9 do not count as being in any
    basin, and all other locations will always be part of exactly one
    basin.

    The size of a basin is the number of locations within the basin,
    including the low point."""

    def __init__(self, heightmap: HeightMap, low_point: Point):
        visited = set()
        queue = [low_point]

        while queue:
            p = queue.pop(0)

            for neighbor in heightmap.neighbors(p.r, p.c):
                # print('\n',queue, neighbor, visited)
                if (
                    neighbor is not None
                    and neighbor not in visited
                    and neighbor.height > p.height
                    and neighbor.height < 9
                ):
                    queue.append(neighbor)
            visited.add(p)
        self._points = visited

    @property
    def size(self):
        return len(self._points)


def _parse_input(input_str):
    ## Start here
    heights = [[int(h) for h in line] for line in input_str]
    return HeightMap(heights)


def part1():
    heightmap = _parse_input(auto_read_input())
    low_points = heightmap.get_all_low_points()
    return sum([p.height for p in low_points]) + len(low_points)


def part2():
    heightmap = _parse_input(auto_read_input())
    basins = heightmap.get_all_basins()
    top3_basins = sorted(basins, key=lambda b: b.size)[-3:]
    return math.prod([b.size for b in top3_basins])


if __name__ == "__main__":
    print(part1())
    print(part2())
