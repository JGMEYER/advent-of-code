from day1 import _parse_input, calculate_distances, get_frequency_map, calculate_similarity_score
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


def test_get_frequency_map():
    list2 = [4, 3, 5, 3, 9, 3]
    assert get_frequency_map(list2) == {
        3: 3,
        4: 1,
        5: 1,
        9: 1,
    }


def test_calculate_similarity_score():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    score = calculate_similarity_score(list1, list2)
    assert score == 31
