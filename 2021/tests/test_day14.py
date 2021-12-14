from re import I
from day14 import (
    _parse_input,
    step_optimized,
    _letter_counts_from_polymer_map,
)
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    polymer_template, rules_map = _parse_input(auto_read_input())
    expected_polymer_template = "NNCB"
    expected_rules_map = {
        "C": {
            "H": "B",
            "B": "H",
            "C": "N",
            "N": "C",
        },
        "H": {
            "H": "N",
            "B": "C",
            "C": "B",
            "N": "C",
        },
        "N": {
            "H": "C",
            "N": "C",
            "C": "B",
            "B": "B",
        },
        "B": {
            "H": "H",
            "N": "B",
            "B": "N",
            "C": "B",
        },
    }
    assert polymer_template == expected_polymer_template
    assert rules_map == expected_rules_map


def test_step_optimized():
    polymer_template, rules_map = _parse_input(auto_read_input())
    letter_counts = step_optimized(polymer_template, rules_map, 10)
    expected_letter_counts = {"B": 1749, "C": 298, "H": 161, "N": 865}
    assert letter_counts == expected_letter_counts

    polymer_template, rules_map = _parse_input(auto_read_input())
    letter_counts = step_optimized(polymer_template, rules_map, 40)
    assert letter_counts["B"] == 2192039569602
    assert letter_counts["H"] == 3849876073


def test__letter_counts_from_polymer_map():
    # Taken from step 2 of example
    polymer_map = {
        "NB": 2,
        "BC": 2,
        "CC": 1,
        "CN": 1,
        "BB": 2,
        "CB": 2,
        "BH": 1,
        "HC": 1,
    }
    letter_counts = _letter_counts_from_polymer_map(polymer_map)
    expected_letter_counts = {
        "N": 2,
        "B": 6,
        "C": 4,
        "H": 1,
    }
    assert letter_counts == expected_letter_counts
