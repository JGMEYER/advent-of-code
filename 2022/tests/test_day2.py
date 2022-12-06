from day2 import _parse_input, score, determine_move
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    moves = _parse_input(auto_read_input())
    assert moves == [
        [0, 1],
        [1, 0],
        [2, 2],
    ]


def test_score():
    assert score(0, 1) == 8
    assert score(1, 0) == 1
    assert score(2, 2) == 6


def test_determine_move():
    assert determine_move(0, 1) == 0
    assert determine_move(1, 0) == 0
    assert determine_move(2, 2) == 0
