from day11 import OctopusMap, _parse_input
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    octopus_map = _parse_input(auto_read_input())

    expected_power_levels = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    assert octopus_map._power_levels == expected_power_levels


def test_OctopusMap__increment_all_by_one():
    octopus_map = OctopusMap(
        [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    flash_queue = octopus_map._increment_all_by_one()
    expected_power_levels = [
        [2, 2, 2, 2, 2],
        [2, 10, 10, 10, 2],
        [2, 10, 2, 10, 2],
        [2, 10, 10, 10, 2],
        [2, 2, 2, 2, 2],
    ]
    assert octopus_map._power_levels == expected_power_levels
    assert len(flash_queue) == 8


def test_OctopusMap_step():
    octopus_map = OctopusMap(
        [
            [1, 1, 1],
            [1, 9, 9],
            [1, 9, 1],
        ]
    )
    # step1
    octopus_map.step()
    expected_power_levels = [
        [3, 4, 4],
        [4, 0, 0],
        [4, 0, 5],
    ]
    assert octopus_map._power_levels == expected_power_levels

    octopus_map = OctopusMap(
        [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    # step1
    num_flashes = octopus_map.step()
    expected_power_levels = [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]
    assert octopus_map._power_levels == expected_power_levels
    assert num_flashes == 9
    # step2
    num_flashes = octopus_map.step()
    expected_power_levels = [
        [4, 5, 6, 5, 4],
        [5, 1, 1, 1, 5],
        [6, 1, 1, 1, 6],
        [5, 1, 1, 1, 5],
        [4, 5, 6, 5, 4],
    ]
    assert octopus_map._power_levels == expected_power_levels
    assert num_flashes == 0
