from day2 import _parse_input, RPSType, score
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    moves = _parse_input(auto_read_input())
    assert moves == [
        [RPSType.ROCK, RPSType.PAPER],
        [RPSType.PAPER, RPSType.ROCK],
        [RPSType.SCISSORS, RPSType.SCISSORS],
    ]


def test_score():
    assert score(RPSType.ROCK, RPSType.PAPER) == 8
    assert score(RPSType.PAPER, RPSType.ROCK) == 1
    assert score(RPSType.SCISSORS, RPSType.SCISSORS) == 6
