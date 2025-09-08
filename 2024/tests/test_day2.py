from day2 import _parse_input
from common.input import auto_read_input


def test__parse_input():
    reports = _parse_input(auto_read_input())
    assert reports == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
