import math
import re
from typing import NamedTuple
from common.input import auto_read_input

# NOTE: Least favorite one so far. Had to hack this together.


def _parse_input(lines):
    ## Start here
    input_pattern = (
        r"target area\: x=(\-?\d+)\.\.(\-?\d+), y=(\-?\d+)\.\.(\-?\d+)"
    )
    match = re.match(input_pattern, lines[0])
    x_min, x_max, y_min, y_max = match.groups()
    return int(x_min), int(x_max), int(y_min), int(y_max)


PossibleXVelData = NamedTuple(
    "PossibleXVelData",
    [("x_v0", int), ("x_stays_infinite", bool), ("t", int)],
)
PossibleYVelData = NamedTuple(
    "PossibleYVelData",
    [("y_v0", int), ("t", int)],
)
PossibleXYVelData = NamedTuple(
    "PossibleXYVelData",
    [("x_v0", int), ("y_v0", int), ("t", int)],
)


def _possible_x_v0(x_min, x_max):
    x_v0 = 1
    possible_x_v0 = []
    while x_v0 <= x_max:
        x, t, x_vt = 0, 0, x_v0
        # Only handle positive x for now
        while x <= x_max and x_vt >= 0:
            x += x_vt
            t += 1

            if x_min <= x <= x_max:
                # x remains infinitely in the range starting at this t
                x_stays_infinite = x_vt == 0
                possible_x_v0.append(
                    PossibleXVelData(x_v0, x_stays_infinite, t)
                )

            x_vt -= 1
        x_v0 += 1
    return possible_x_v0


def _possible_y_v0(y_min, y_max):
    y_v0, t = 0, 1
    possible_y_v0 = []

    # HACK: Brute force large window cuz I'm tired
    for y_v0 in range(-1000, 1000):
        y, y_v = 0, y_v0
        for t in range(1, 1001):
            y += y_v
            if y_min <= y <= y_max:
                possible_y_v0.append(PossibleYVelData(y_v0, t))
            if y < y_min:
                break
            y_v -= 1

    return possible_y_v0


def _possible_x_v0_and_y_v0(possible_x_v0, possible_y_v0):
    possible_x_v0_and_y_v0 = set()
    for y_v0, t in possible_y_v0:
        for x_data in possible_x_v0:
            if x_data.t == t or (x_data.x_stays_infinite and t >= x_data.t):
                possible_x_v0_and_y_v0.add(
                    PossibleXYVelData(x_data.x_v0, y_v0, t)
                )
    return possible_x_v0_and_y_v0


def _max_height(y_v0, t_final):
    y_v = y_v0
    max_height = 0
    for t in range(1, t_final + 1):
        height = max_height + y_v
        if height > max_height:
            max_height = height
        else:
            break
        y_v -= 1
    return max_height


def _valid_v0_with_highest_peak(possible_x_v0_and_y_v0):
    highest_pair = None
    highest_peak = -math.inf

    for x_v0, y_v0, t_final in possible_x_v0_and_y_v0:
        max_height = _max_height(y_v0, t_final)
        if max_height > highest_peak:
            highest_pair = (x_v0, y_v0)
            highest_peak = max_height

    return highest_pair, highest_peak


def part1():
    x_min, x_max, y_min, y_max = _parse_input(auto_read_input())
    possible_x_v0 = _possible_x_v0(x_min, x_max)
    possible_y_v0 = _possible_y_v0(y_min, y_max)
    possible_x_v0_and_y_v0 = _possible_x_v0_and_y_v0(
        possible_x_v0, possible_y_v0
    )
    v0_pair, max_height = _valid_v0_with_highest_peak(possible_x_v0_and_y_v0)
    return v0_pair, max_height


def part2():
    x_min, x_max, y_min, y_max = _parse_input(auto_read_input())
    possible_x_v0 = _possible_x_v0(x_min, x_max)
    possible_y_v0 = _possible_y_v0(y_min, y_max)
    possible_x_v0_and_y_v0 = _possible_x_v0_and_y_v0(
        possible_x_v0, possible_y_v0
    )
    return len(
        {(v0_data.x_v0, v0_data.y_v0) for v0_data in possible_x_v0_and_y_v0}
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
