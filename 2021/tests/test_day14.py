from re import I
from day14 import _parse_input, insert_rules
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


def test_insert_rules():
    polymer_template, rules_map = _parse_input(auto_read_input())

    polymer, _ = insert_rules(polymer_template, rules_map)
    expected_polymer = "NCNBCHB"
    assert polymer == expected_polymer

    polymer, _ = insert_rules(polymer, rules_map)
    expected_polymer = "NBCCNBBBCBHCB"
    assert polymer == expected_polymer

    polymer, _ = insert_rules(polymer, rules_map)
    expected_polymer = "NBBBCNCCNBBNBNBBCHBHHBCHB"
    assert polymer == expected_polymer

    polymer, _ = insert_rules(polymer, rules_map)
    expected_polymer = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    assert polymer == expected_polymer

    polymer, _ = insert_rules(polymer, rules_map)
    assert len(polymer) == 97

    polymer, _ = insert_rules(polymer, rules_map)
    polymer, _ = insert_rules(polymer, rules_map)
    polymer, _ = insert_rules(polymer, rules_map)
    polymer, _ = insert_rules(polymer, rules_map)
    polymer, letter_counts = insert_rules(polymer, rules_map)

    expected_letter_counts = {"B": 1749, "C": 298, "H": 161, "N": 865}
    assert len(polymer) == 3073
    assert letter_counts == expected_letter_counts
