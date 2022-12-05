from day1 import _parse_input, most_calories, top3_most_calories_total
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    snack_packs = _parse_input(auto_read_input())
    assert snack_packs[0] == [1000, 2000, 3000]
    assert snack_packs[1] == [4000]
    assert snack_packs[2] == [5000, 6000]
    assert snack_packs[3] == [7000, 8000, 9000]
    assert snack_packs[4] == [10000]


def test_most_calories():
    snack_packs = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    expected_calories = 24000
    assert most_calories(snack_packs) == expected_calories


def test_top3_most_calories_total():
    snack_packs = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    expected_calories = 45000
    assert top3_most_calories_total(snack_packs) == expected_calories
