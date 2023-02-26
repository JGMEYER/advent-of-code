from day8 import _parse_input, TreeSurveyor
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    tree_map = _parse_input(auto_read_input())
    assert tree_map == [[3, 0, 3, 7, 3],
                        [2, 5, 5, 1, 2],
                        [6, 5, 3, 3, 2],
                        [3, 3, 5, 4, 9],
                        [3, 5, 3, 9, 0]]


def test_TreeSurveyor_count_visible():
    tree_map = [[3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]]
    ts = TreeSurveyor()
    ts.load(tree_map)
    assert ts.count_visible() == 21
