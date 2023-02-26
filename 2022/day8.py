from common.input import auto_read_input

"""
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.
"""


class TreeSurveyor:
    def __init__(self):
        self._tree_map = None
        self._rows = -1
        self._cols = -1
        self._top_map = None
        self._left_map = None
        self._bottom_map = None
        self._right_map = None

    def load(self, tree_map):
        rows, cols = len(tree_map), len(tree_map[0])
        assert rows >= 3
        assert cols >= 3

        self._rows, self._cols = rows, cols
        self._tree_map = tree_map
        self._top_map, self._left_map = self._map_top_left(tree_map)
        self._bottom_map, self._right_map = self._map_bottom_right(tree_map)

    def count_visible(self):
        num_visible = 0

        for r in range(self._rows):
            for c in range(self._cols):
                max_top = self._top_map[r][c]
                max_left = self._left_map[r][c]
                max_bottom = self._bottom_map[r][c]
                max_right = self._right_map[r][c]

                min_neighbor = min(max_top, max_left, max_bottom, max_right)
                if min_neighbor < self._tree_map[r][c]:
                    num_visible += 1

        return num_visible

    def _map_top_left(self, tree_map):
        """Use dynamic programming to track the largest tree to top and left of any given cell"""
        self._rows, cols = len(tree_map), len(tree_map[0])
        top_map = [[-1 for c in range(self._cols)] for r in range(self._rows)]
        left_map = [[-1 for c in range(self._cols)] for r in range(self._rows)]

        for r in range(1, self._rows - 1):
            for c in range(1, self._cols - 1):
                max_top = top_map[r - 1][c]
                last_top = tree_map[r - 1][c]
                top_map[r][c] = max(max_top, last_top)

                max_left = left_map[r][c - 1]
                last_left = tree_map[r][c - 1]
                left_map[r][c] = max(max_left, last_left)

        return top_map, left_map

    def _map_bottom_right(self, tree_map):
        """Use dynamic programming to track the largest tree to bottom and right of any given cell"""
        self.rows, self.cols = len(tree_map), len(tree_map[0])
        bottom_map = [[-1 for c in range(self.cols)] for r in range(self.rows)]
        right_map = [[-1 for c in range(self.cols)] for r in range(self.rows)]

        for r in range(self.rows - 2, 0, -1):
            for c in range(self.cols - 2, 0, -1):
                max_bottom = bottom_map[r + 1][c]
                last_bottom = tree_map[r + 1][c]
                bottom_map[r][c] = max(max_bottom, last_bottom)

                max_right = right_map[r][c + 1]
                last_right = tree_map[r][c + 1]
                right_map[r][c] = max(max_right, last_right)

        return bottom_map, right_map


def _parse_input(lines):
    ## Start here
    tree_map = []
    for line in lines:
        row = [int(ch) for ch in line]
        tree_map.append(row)
    return tree_map


def part1():
    tree_map = _parse_input(auto_read_input())
    ts = TreeSurveyor()
    ts.load(tree_map)
    return ts.count_visible()


def part2():
    _ = _parse_input(auto_read_input())
    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
