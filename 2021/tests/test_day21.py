from day21 import _parse_input, play_game
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    p1_pos, p2_pos = _parse_input(auto_read_input())
    assert p1_pos == 4
    assert p2_pos == 8


def test_play_game():
    p1_pos, p2_pos = _parse_input(auto_read_input())
    assert play_game(p1_pos, p2_pos) == 739785
