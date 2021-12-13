import re
from typing import List, Tuple

from enum import Enum
from common.input import auto_read_input

# Takeaways: If I were to do it all over, I'd actually just go ahead and make
# Paper an object. Woulda saved some trouble.


class PaperState(str, Enum):
    EMPTY = "."
    DOT = "#"


class FoldDirection(str, Enum):
    UP = "y"
    LEFT = "x"


def print_paper(paper: List[List[int]]):
    str = ""
    for r in range(len(paper)):
        str += (
            "\n" + " ".join([paper[r][c] for c in range(len(paper[0]))]) + "\n"
        )
    print(str)


def fold(paper: List[List[int]], instructions: Tuple[FoldDirection, int]):
    fold_dir, axis = instructions
    resulting_paper = None

    if fold_dir == FoldDirection.UP:
        rows_folded = len(paper) - axis

        resulting_paper = paper[: -1 * rows_folded][:]

        # far edge of fold to fold axis
        for r in range(len(paper) - 1, len(paper) - rows_folded, -1):
            for c in range(len(paper[0])):
                target_r = axis - (r - axis)  # mirror over axis
                resulting_paper[target_r][c] = (
                    PaperState.DOT
                    if (
                        paper[r][c] == PaperState.DOT
                        or paper[target_r][c] == PaperState.DOT
                    )
                    else PaperState.EMPTY
                )

    elif fold_dir == FoldDirection.LEFT:
        cols_folded = len(paper[0]) - axis

        resulting_paper = []
        for r in range(len(paper)):
            resulting_paper.append(paper[r][: -1 * cols_folded])

        # far edge of fold to fold axis
        for c in range(len(paper[0]) - 1, len(paper[0]) - cols_folded, -1):
            for r in range(len(paper)):
                target_c = axis - (c - axis)  # mirror over axis
                resulting_paper[r][target_c] = (
                    PaperState.DOT
                    if (
                        paper[r][c] == PaperState.DOT
                        or paper[r][target_c] == PaperState.DOT
                    )
                    else PaperState.EMPTY
                )

    return resulting_paper


def num_dots(paper: List[List[int]]):
    count = 0
    for r in range(len(paper)):
        for val in paper[r]:
            if val == PaperState.DOT:
                count += 1
    return count


def _parse_input(lines):
    ## Start here
    holes = []
    instructions = []
    max_r, max_c = 0, 0

    for line in lines:
        if "," in line:
            c_str, r_str = line.split(",")
            c, r = int(c_str), int(r_str)
            holes.append((r, c))
            max_r = max(max_r, r)
            max_c = max(max_c, c)
        elif line:
            pattern = "fold along ([x|y])=(\d+)"
            match = re.match(pattern, line)
            direction_str, axis_str = match.groups()
            direction = (
                FoldDirection.UP
                if direction_str == str(FoldDirection.UP.value)
                else FoldDirection.LEFT
            )
            instructions.append((direction, int(axis_str)))

    paper = [[PaperState.EMPTY] * (max_c + 1) for r in range(max_r + 1)]

    for r, c in holes:
        paper[r][c] = PaperState.DOT

    return paper, instructions


def part1():
    paper, instructions = _parse_input(auto_read_input())
    paper = fold(paper, instructions[0])
    return num_dots(paper)


def part2():
    paper, instructions = _parse_input(auto_read_input())
    for inst in instructions:
        paper = fold(paper, inst)
    return paper


if __name__ == "__main__":
    print(part1())
    print_paper(part2())
