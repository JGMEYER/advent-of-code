import re
from collections import defaultdict

from common.input import auto_read_input


def insert_rules(polymer_template, rules_map):
    result_polymer = ""
    letter_counts = defaultdict(int)

    for idx in range(len(polymer_template)):
        result_polymer += polymer_template[idx]
        letter_counts[polymer_template[idx]] += 1

        if idx < len(polymer_template) - 1:
            left, right = polymer_template[idx : idx + 2]
            chr_repl = rules_map[left].get(right) if left in rules_map else ""
            result_polymer += chr_repl
            letter_counts[chr_repl] += 1

    return result_polymer, letter_counts


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

    for _ in range(10):
        polymer, letter_counts = insert_rules(polymer, rules_map)

    return max(letter_counts.values()) - min(letter_counts.values())


def part2():
    polymer, rules_map = _parse_input(auto_read_input())

    for day_idx in range(40):
        print(day_idx)
        polymer, letter_counts = insert_rules(polymer, rules_map)

    return max(letter_counts.values()) - min(letter_counts.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
