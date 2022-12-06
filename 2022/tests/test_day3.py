from day3 import _parse_input, get_priority
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    rucksacks = _parse_input(auto_read_input())
    assert rucksacks == [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]

def test_get_priority():
    assert get_priority('p') == 16
    assert get_priority('L') == 38
    assert get_priority('P') == 42
    assert get_priority('v') == 22
    assert get_priority('t') == 20
    assert get_priority('s') == 19
