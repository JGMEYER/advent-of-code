from collections import namedtuple
from typing import Callable, List, Set, Tuple

from common.input import read_input


Point = namedtuple('Point', 'x y')

DIRECTIONS = {  # (x, y)
    'U': Point(0, 1),
    'D': Point(0, -1),
    'R': Point(1, 0),
    'L': Point(-1, 0),
}


def manhattan_distance(point1: Point, point2: Point) -> int:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def iterate_coords(wire: List[str], point_func: Callable) -> None:
    """Iterates through all coordinates in the wire and invokes `point_func` on
    each one, excluding the origin.
    """
    cur_x, cur_y = (0, 0)
    for path_step in wire:
        print(path_step)
        dir, paces = path_step[0], int(path_step[1:])
        dir_step = DIRECTIONS[dir]
        for i in range(paces):
            cur_x, cur_y = (cur_x + dir_step.x), (cur_y + dir_step.y)
            point_func(Point(cur_x, cur_y))


def intersections(wire1: List[str], wire2: List[str]) -> Set[Point]:
    """Returns a set of `Point`s where the two wires intersect."""
    wire1_coords = set([Point(0, 0)])
    inters = set()

    def _add_wire1_coord(point: Point):
        wire1_coords.add(point)

    def _add_if_intersection(point: Point):
        if point in wire1_coords:
            inters.add(point)

    iterate_coords(wire1, _add_wire1_coord)
    iterate_coords(wire2, _add_if_intersection)
    return inters


def intersections_with_combined_steps(wire1: List[str], wire2: List[str]
                                      ) -> List[Tuple[Point, int]]:
    """Returns a set of `Point`s where the two wires intersect, along with the
    total distanced traveled by both wires to reach the `Point`.
    """
    pass


def fewest_steps_to_intersection(wire1: List[str], wire2: List[str]
                                 ) -> Set[Point]:
    """Returns the fewest combined steps each wire needs to make to reach an
    intersection.
    """
    wire1_coords: Dict[Point, int] = {}  # {coord: dist_from_wire1}

    def _add_wire1_coord(point: Point):
        wire1_coords.add(point)

    pass


def part1() -> int:
    wire1_str, wire2_str = read_input(day=3)
    wire1 = wire1_str.split(',')
    wire2 = wire2_str.split(',')
    inters = intersections(wire1, wire2)
    min_distance = float("inf")

    for inter in inters:
        min_distance = min(min_distance,
                           manhattan_distance(Point(0, 0), inter))
    return min_distance


def part2() -> int:
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
