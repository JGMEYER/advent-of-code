from day6 import _parse_input, _step_population
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    population = _parse_input(auto_read_input())
    expected_population = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 1,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    assert population == expected_population


def test__step_population():
    population = {
        0: 0,
        1: 0,
        2: 0,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    expected_population = {
        0: 0,
        1: 0,
        2: 1,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    assert _step_population(population) == expected_population
    population = expected_population
    expected_population = {
        0: 0,
        1: 1,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    assert _step_population(population) == expected_population
    population = expected_population
    expected_population = {
        0: 1,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    assert _step_population(population) == expected_population
    population = expected_population
    expected_population = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 1,
        7: 0,
        8: 1,
    }
    assert _step_population(population) == expected_population
    population = expected_population
    expected_population = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 1,
        6: 0,
        7: 1,
        8: 0,
    }
    assert _step_population(population) == expected_population

    population = _parse_input(auto_read_input())
    for day in range(18):
        _step_population(population)
    assert sum(population.values()) == 26

    population = _parse_input(auto_read_input())
    for day in range(80):
        _step_population(population)
    assert sum(population.values()) == 5934

    population = _parse_input(auto_read_input())
    for day in range(256):
        _step_population(population)
    assert sum(population.values()) == 26984457539
