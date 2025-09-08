from day1 import _parse_input, calculate_distances
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    list1, list2 = _parse_input(auto_read_input())
    assert list1 == [3, 4, 2, 1, 3, 3]
    assert list2 == [4, 3, 5, 3, 9, 3]


def test_calculate_distances():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    distance = calculate_distances(list1, list2)
    assert distance == 11
