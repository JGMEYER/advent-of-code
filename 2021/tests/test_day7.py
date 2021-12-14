from day7 import (
    _parse_input,
    brute_force_minimal_fuel,
    brute_force_minimal_fuel_series,
)
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    crab_arr = _parse_input(auto_read_input())
    expected_crab_arr = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert crab_arr == expected_crab_arr


def test_brute_force_minimal_fuel():
    crab_arr = _parse_input(auto_read_input())
    min_fuel = brute_force_minimal_fuel(crab_arr)
    expected_min_fuel = 37
    assert min_fuel == expected_min_fuel


def test_brute_force_minimal_fuel_series():
    crab_arr = _parse_input(auto_read_input())
    min_fuel = brute_force_minimal_fuel_series(crab_arr)
    expected_min_fuel = 168
    assert min_fuel == expected_min_fuel
