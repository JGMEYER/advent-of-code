import math
import re
from collections import defaultdict
from typing import Dict

from common.input import auto_read_input


def _letter_counts_from_polymer_map(polymer_map: Dict[str, int]):
    """Convert map of character pairs to individual character counts"""
    letter_counts = defaultdict(int)
    for pair, count in polymer_map.items():
        left, right = pair
        letter_counts[left] += count
        letter_counts[right] += count
    # Use ceil here to account for first and last characters in a template.
    # These would result in odd valued counts because they do not belong to two
    # pairs. Round them up.
    return {
        pair: math.ceil(count / 2) for pair, count in letter_counts.items()
    }


def step_optimized(polymer_template, rules_map, n_steps):
    """Step template n times"""

    # Map character pairs to their counts
    polymer_map = defaultdict(int)

    # Initial setup
    for idx in range(len(polymer_template) - 1):
        pair = polymer_template[idx : idx + 2]
        polymer_map[pair] += 1

    for _ in range(n_steps):
        new_polymer_map = defaultdict(int)
        for pair in polymer_map.keys():
            left, right = pair
            # Find character to place between left and right
            chr_repl = (
                rules_map[left].get(right) if left in rules_map else None
            )
            if chr_repl:
                # Adding the new character splits the pair into two more
                new_polymer_map[left + chr_repl] += polymer_map[pair]
                new_polymer_map[chr_repl + right] += polymer_map[pair]
        polymer_map = new_polymer_map

    letter_counts = _letter_counts_from_polymer_map(polymer_map)
    return letter_counts


def _parse_input(lines):
    ## Start here
    polymer_template = lines[0]
    rules_map = defaultdict(dict)

    for line in lines[2:]:
        match = re.match(r"(\w)(\w) -> (\w)", line)
        first, second, replace_chr = match.groups()
        rules_map[first][second] = replace_chr

    return polymer_template, rules_map


def part1():
    polymer, rules_map = _parse_input(auto_read_input())
    letter_counts = step_optimized(polymer, rules_map, 10)
    return max(letter_counts.values()) - min(letter_counts.values())


def part2():
    polymer, rules_map = _parse_input(auto_read_input())
    letter_counts = step_optimized(polymer, rules_map, 40)
    return max(letter_counts.values()) - min(letter_counts.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
