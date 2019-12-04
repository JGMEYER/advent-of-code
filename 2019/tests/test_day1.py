from day1 import (
    _calculate_total_fuel,
    _fuel_required,
    _recursive_fuel_required,
)


def test__fuel_required():
    assert _fuel_required(12) == 2
    assert _fuel_required(14) == 2
    assert _fuel_required(1969) == 654
    assert _fuel_required(100756) == 33583


def test__recursive_fuel_required():
    assert _recursive_fuel_required(14) == 2
    assert _recursive_fuel_required(1969) == 966
    assert _recursive_fuel_required(100756) == 50346


def test__calculate_total_fuel():
    masses1 = [12, 14, 1969, 100756]
    expected1 = 2 + 2 + 654 + 33583
    assert _calculate_total_fuel(_fuel_required, masses1) == expected1

    masses2 = [14, 1969, 100756]
    expected2 = 2 + 966 + 50346
    assert (
        _calculate_total_fuel(_recursive_fuel_required, masses2) == expected2
    )
